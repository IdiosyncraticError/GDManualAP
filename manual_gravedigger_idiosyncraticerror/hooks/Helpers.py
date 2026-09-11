from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Helpers import get_option_value
    classes = get_option_value(multiworld, player, "enabled_classes")

    if category_name.endswith("C"):
        enabled_classes = []
        for c in classes:
            enabled_classes.append(c + "C")
        return category_name in enabled_classes

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    from ..Helpers import get_option_value
    classes = get_option_value(multiworld, player, "enabled_classes")
    if "Classes" in item["category"]:
        return item["name"] in classes

    mods = get_option_value(multiworld, player, "mods_list")
    if "Mods" in item["category"]:
        return item["name"] in mods

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
