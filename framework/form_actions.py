import logging
from typing import List, Optional, Sequence

from playwright.sync_api import Locator

logger = logging.getLogger(__name__)


# Author: Aathira Shaji
# Description: Selects a radio button by its value and verifies the selection.
def select_radio_button(radio_group: Locator, value: str) -> str:
    """Select the radio button with the given value and return that value."""
    radio_group.first.wait_for(state="attached")

    matching_radio = None
    for radio in radio_group.all():
        if radio.get_attribute("value") == value:
            if matching_radio is not None:
                raise ValueError(
                    f"Multiple radio buttons in the group have value {value!r}."
                )
            matching_radio = radio

    if matching_radio is None:
        raise ValueError(f"No radio button in the group has value {value!r}.")

    matching_radio.check()
    if not matching_radio.is_checked():
        raise RuntimeError(f"Radio button {value!r} was not selected.")

    logger.info("Selected radio button '%s'", value)
    return value


# Author: Aathira Shaji
# Description: Selects and verifies multiple options in native or searchable dropdowns.
def select_multiple_dropdown_options(
    dropdown: Locator,
    values: Sequence[str],
    listbox: Optional[Locator] = None,
    search_box: Optional[Locator] = None,
) -> List[str]:
    """Select and verify multiple options in a native or custom dropdown."""
    if not values:
        raise ValueError("At least one dropdown option must be provided.")

    dropdown.wait_for(state="visible")
    if dropdown.evaluate("(element) => element.tagName.toLowerCase()") == "select":
        if dropdown.get_attribute("multiple") is None:
            raise ValueError("The native <select> must have the multiple attribute.")
        selected = dropdown.select_option(value=list(values))
        if set(selected) != set(values):
            raise RuntimeError(f"Could not select all requested options: {list(values)}")
        return selected

    if listbox is None:
        raise ValueError("Pass the listbox locator for a custom dropdown.")

    selected = []
    for value in values:
        if not listbox.is_visible():
            dropdown.click()
        listbox.wait_for(state="visible")

        if search_box is not None:
            search_box.fill(value)

        option = listbox.get_by_role("option", name=value, exact=True)
        if option.get_attribute("aria-selected") != "true":
            option.click()
        if option.get_attribute("aria-selected") != "true":
            raise RuntimeError(f"Dropdown option {value!r} was not selected.")
        selected.append(value)

    return selected