from utils import *

ITEM_FIELD_RARITY = "rarity"
ITEM_FIELD_NAME = "name"
ITEM_FIELD_PRICE = "price"
ITEM_FIELD_ATTUNEMENT = "attunement"
ITEM_FIELD_RARITY_LEVEL = "rarity_level"
ITEM_FIELD_DESCRIPTION = "description"
ITEM_FIELD_OFFICIAL = "official"
ITEM_FIELD_BANNED = "banned"


def get_unsold_item_row_string(
        index: int,
        magic_item: dict,
        field_key_quantity: str
) -> str:
    magic_item_string = f'{index}) **{magic_item[ITEM_FIELD_NAME]}** - quantity: '
    item_quantity = magic_item[field_key_quantity]
    quantity_string = str(item_quantity) if item_quantity != infinite_quantity else '*infinite*'
    magic_item_string += quantity_string
    magic_item_string += f' - {tokens_per_rarity(magic_item[ITEM_FIELD_RARITY], magic_item[ITEM_FIELD_RARITY_LEVEL])}\n'
    return magic_item_string


def get_sold_item_row_string(
        index: int,
        magic_item: dict,
        field_key_quantity: str
) -> str:
    magic_item_string = f'~~{index}) {magic_item[ITEM_FIELD_NAME]} - quantity: '
    item_quantity = magic_item[field_key_quantity]
    quantity_string = str(item_quantity) if item_quantity != infinite_quantity else '*infinite*'
    magic_item_string += quantity_string
    magic_item_string += f' - {tokens_per_rarity(magic_item[ITEM_FIELD_RARITY], magic_item[ITEM_FIELD_RARITY_LEVEL])}~~\n'
    return magic_item_string
