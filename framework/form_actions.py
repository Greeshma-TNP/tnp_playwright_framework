import logging
from typing import List, Sequence

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
# Description: Selects and verifies multiple values in a native HTML multi-select.
def select_multiple_dropdown_options(
    dropdown: Locator,
    values: Sequence[str],
) -> List[str]:
    """Select multiple values in a native <select multiple> element."""
    if not values:
        raise ValueError("At least one dropdown option must be provided.")

    dropdown.wait_for(state="visible")
    if dropdown.evaluate("(element) => element.tagName.toLowerCase()") != "select":
        raise ValueError("This method only supports native HTML <select> elements.")
    if dropdown.get_attribute("multiple") is None:
        raise ValueError("The native <select> must have the multiple attribute.")

    selected = dropdown.select_option(value=list(values))
    if set(selected) != set(values):
        raise RuntimeError(f"Could not select all requested options: {list(values)}")
    return selected
