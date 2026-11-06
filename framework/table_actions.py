from typing import Optional

from playwright.sync_api import Locator


# Author: Aathira Shaji
# Description: Navigates through table pages or clicks a specified page number.
def check_table_pagination(
    table: Locator,
    next_button: Locator,
    previous_button: Locator,
    page_button: Optional[Locator] = None,
    max_pages: int = 100,
) -> int:
    """Navigate through pages and return their count, or click a specific page."""
    table.wait_for(state="visible")
    next_button.wait_for(state="visible")
    previous_button.wait_for(state="visible") 

    if page_button is not None:
        page_button.wait_for(state="visible")
        page_number = page_button.inner_text().strip()
        if not page_number.isdigit():
            raise ValueError(f"Page button text must be a number, got {page_number!r}.")
        page_button.click()
        return int(page_number)

    pages_visited = 1

    while next_button.is_enabled():
        if pages_visited >= max_pages:
            raise RuntimeError(f"Pagination exceeded the limit of {max_pages} pages.")

        next_button.click()
        pages_visited += 1

    return pages_visited