# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionSet, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from ..Items import item_name_groups
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class WinCount(Range):
    """
    How many weapons you must have before being able to claim the victory location.
    Mining picks and the default melee weapon do not count towards this total.
    """
    display_name = "Win Requirement"
    range_start = 10
    range_end = 35
    default = 30

class KillCount(Range):
    """How many kills each location requires"""
    display_name = "Location Kill Requirement"
    range_start = 5
    range_end = 30
    default = 10

class KitCount(Range):
    """
    How many random loadouts will be generated as location
    0 will use the minimum number of locations
    """
    display_name = "Randomized Kit Locations"
    range_start = 0
    range_end = 50
    default = 15

class EnabledClasses(OptionSet):
    """Classes that will be randomized into the pool"""
    display_name = "Enabled Classes"
    keys = item_name_groups["Classes"]
    default = frozenset(keys)

class RandomTools(Toggle):
    """Randomizes mining pick, first aid kit, and melee"""
    display_name = "Randomized Tools"

class RandomClassTools(Toggle):
    """Randomizes class specific items (e.g. ammo pouch, bulwark shield, hunting kit)"""
    display_name = "Randomized Perk Equipment"

class StartingGuns(Range):
    """
    Number of guns you starts with.
    Chooses from primaries, secondaries, and mods (if enabled)
    """
    display_name = "Starting Gun Count"
    range_start = 1
    range_end = 4

class FillerName(Choice):
    """Pick a side for filler item names"""
    display_name = "Filler Name"
    option_royal_nation = 0
    option_golden_empire = 1

class Hope(Toggle):
    """
    Enable to add Hope as an unlock.
    ***IF YOU DO NOT HAVE HOPE DO NOT TURN THIS ON***
    or i guess do if you want like a free location
    """
    display_name = "Hope Unlock"

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["win_count"] = WinCount
    options["location_kills"] = KillCount
    options["rando_kit_count"] = KitCount
    options["enabled_classes"] = EnabledClasses
    options["random_tool"] = RandomTools
    options["random_class_tool"] = RandomClassTools
    options["filler_name"] = FillerName
    options["hope_item"] = Hope
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
