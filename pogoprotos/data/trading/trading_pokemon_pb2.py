# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/trading/trading_pokemon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_display_pb2 as pogoprotos_dot_data_dot_pokemon__display__pb2
from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.inventory.item import item_data_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__data__pb2
from pogoprotos.enums import pokemon_move_pb2 as pogoprotos_dot_enums_dot_pokemon__move__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/trading/trading_pokemon.proto',
  package='pogoprotos.data.trading',
  syntax='proto3',
  serialized_pb=_b('\n-pogoprotos/data/trading/trading_pokemon.proto\x12\x17pogoprotos.data.trading\x1a%pogoprotos/data/pokemon_display.proto\x1a\"pogoprotos/data/pokemon_data.proto\x1a)pogoprotos/inventory/item/item_data.proto\x1a#pogoprotos/enums/pokemon_move.proto\"\xd8\x05\n\x0eTradingPokemon\x12\x12\n\npokemon_id\x18\x01 \x01(\x06\x12\x1c\n\x14pokedex_entry_number\x18\x02 \x01(\x05\x12\x13\n\x0boriginal_cp\x18\x03 \x01(\x05\x12\x17\n\x0f\x61\x64justed_cp_min\x18\x04 \x01(\x05\x12\x17\n\x0f\x61\x64justed_cp_max\x18\x05 \x01(\x05\x12\x18\n\x10original_stamina\x18\x06 \x01(\x05\x12\x1c\n\x14\x61\x64justed_stamina_min\x18\x07 \x01(\x05\x12\x1c\n\x14\x61\x64justed_stamina_max\x18\x08 \x01(\x05\x12\x18\n\x10\x66riend_level_cap\x18\t \x01(\x08\x12,\n\x05move1\x18\n \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12,\n\x05move2\x18\x0b \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12\x38\n\x0fpokemon_display\x18\x0c \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplay\x12\x1b\n\x13\x63\x61ptured_s2_cell_id\x18\r \x01(\x03\x12\x34\n\x0etraded_pokemon\x18\x0e \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12\x35\n\x08pokeball\x18\x0f \x01(\x0b\x32#.pogoprotos.inventory.item.ItemData\x12\x19\n\x11individual_attack\x18\x10 \x01(\x05\x12\x1a\n\x12individual_defense\x18\x11 \x01(\x05\x12\x1a\n\x12individual_stamina\x18\x12 \x01(\x05\x12\x10\n\x08nickname\x18\x13 \x01(\t\x12\x10\n\x08\x66\x61vorite\x18\x14 \x01(\x08\x12,\n\x05move3\x18\x15 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12\x18\n\x10\x63reation_time_ms\x18\x16 \x01(\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__display__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__data__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__move__pb2.DESCRIPTOR,])




_TRADINGPOKEMON = _descriptor.Descriptor(
  name='TradingPokemon',
  full_name='pogoprotos.data.trading.TradingPokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.trading.TradingPokemon.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokedex_entry_number', full_name='pogoprotos.data.trading.TradingPokemon.pokedex_entry_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='original_cp', full_name='pogoprotos.data.trading.TradingPokemon.original_cp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adjusted_cp_min', full_name='pogoprotos.data.trading.TradingPokemon.adjusted_cp_min', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adjusted_cp_max', full_name='pogoprotos.data.trading.TradingPokemon.adjusted_cp_max', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='original_stamina', full_name='pogoprotos.data.trading.TradingPokemon.original_stamina', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adjusted_stamina_min', full_name='pogoprotos.data.trading.TradingPokemon.adjusted_stamina_min', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adjusted_stamina_max', full_name='pogoprotos.data.trading.TradingPokemon.adjusted_stamina_max', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend_level_cap', full_name='pogoprotos.data.trading.TradingPokemon.friend_level_cap', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move1', full_name='pogoprotos.data.trading.TradingPokemon.move1', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move2', full_name='pogoprotos.data.trading.TradingPokemon.move2', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_display', full_name='pogoprotos.data.trading.TradingPokemon.pokemon_display', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='captured_s2_cell_id', full_name='pogoprotos.data.trading.TradingPokemon.captured_s2_cell_id', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traded_pokemon', full_name='pogoprotos.data.trading.TradingPokemon.traded_pokemon', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokeball', full_name='pogoprotos.data.trading.TradingPokemon.pokeball', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_attack', full_name='pogoprotos.data.trading.TradingPokemon.individual_attack', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_defense', full_name='pogoprotos.data.trading.TradingPokemon.individual_defense', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_stamina', full_name='pogoprotos.data.trading.TradingPokemon.individual_stamina', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='pogoprotos.data.trading.TradingPokemon.nickname', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='favorite', full_name='pogoprotos.data.trading.TradingPokemon.favorite', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move3', full_name='pogoprotos.data.trading.TradingPokemon.move3', index=20,
      number=21, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_time_ms', full_name='pogoprotos.data.trading.TradingPokemon.creation_time_ms', index=21,
      number=22, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=958,
)

_TRADINGPOKEMON.fields_by_name['move1'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_TRADINGPOKEMON.fields_by_name['move2'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_TRADINGPOKEMON.fields_by_name['pokemon_display'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
_TRADINGPOKEMON.fields_by_name['traded_pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_TRADINGPOKEMON.fields_by_name['pokeball'].message_type = pogoprotos_dot_inventory_dot_item_dot_item__data__pb2._ITEMDATA
_TRADINGPOKEMON.fields_by_name['move3'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
DESCRIPTOR.message_types_by_name['TradingPokemon'] = _TRADINGPOKEMON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TradingPokemon = _reflection.GeneratedProtocolMessageType('TradingPokemon', (_message.Message,), dict(
  DESCRIPTOR = _TRADINGPOKEMON,
  __module__ = 'pogoprotos.data.trading.trading_pokemon_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.trading.TradingPokemon)
  ))
_sym_db.RegisterMessage(TradingPokemon)


# @@protoc_insertion_point(module_scope)
