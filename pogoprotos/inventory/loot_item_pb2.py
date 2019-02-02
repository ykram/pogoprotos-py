# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/loot_item.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/loot_item.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_pb=_b('\n$pogoprotos/inventory/loot_item.proto\x12\x14pogoprotos.inventory\x1a\'pogoprotos/inventory/item/item_id.proto\x1a!pogoprotos/enums/pokemon_id.proto\x1a\"pogoprotos/data/pokemon_data.proto\"\xff\x01\n\x08LootItem\x12\x31\n\x04item\x18\x01 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemIdH\x00\x12\x12\n\x08stardust\x18\x02 \x01(\x08H\x00\x12\x12\n\x08pokecoin\x18\x03 \x01(\x08H\x00\x12\x34\n\rpokemon_candy\x18\x04 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonIdH\x00\x12\x0f\n\x05\x63ount\x18\x05 \x01(\x05H\x00\x12\x14\n\nexperience\x18\x06 \x01(\x08H\x00\x12\x33\n\x0bpokemon_egg\x18\x07 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonDataH\x00\x42\x06\n\x04Typeb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,])




_LOOTITEM = _descriptor.Descriptor(
  name='LootItem',
  full_name='pogoprotos.inventory.LootItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='pogoprotos.inventory.LootItem.item', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stardust', full_name='pogoprotos.inventory.LootItem.stardust', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokecoin', full_name='pogoprotos.inventory.LootItem.pokecoin', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_candy', full_name='pogoprotos.inventory.LootItem.pokemon_candy', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='pogoprotos.inventory.LootItem.count', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experience', full_name='pogoprotos.inventory.LootItem.experience', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_egg', full_name='pogoprotos.inventory.LootItem.pokemon_egg', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='Type', full_name='pogoprotos.inventory.LootItem.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=175,
  serialized_end=430,
)

_LOOTITEM.fields_by_name['item'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_LOOTITEM.fields_by_name['pokemon_candy'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_LOOTITEM.fields_by_name['pokemon_egg'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_LOOTITEM.oneofs_by_name['Type'].fields.append(
  _LOOTITEM.fields_by_name['item'])
_LOOTITEM.fields_by_name['item'].containing_oneof = _LOOTITEM.oneofs_by_name['Type']
_LOOTITEM.oneofs_by_name['Type'].fields.append(
  _LOOTITEM.fields_by_name['stardust'])
_LOOTITEM.fields_by_name['stardust'].containing_oneof = _LOOTITEM.oneofs_by_name['Type']
_LOOTITEM.oneofs_by_name['Type'].fields.append(
  _LOOTITEM.fields_by_name['pokecoin'])
_LOOTITEM.fields_by_name['pokecoin'].containing_oneof = _LOOTITEM.oneofs_by_name['Type']
_LOOTITEM.oneofs_by_name['Type'].fields.append(
  _LOOTITEM.fields_by_name['pokemon_candy'])
_LOOTITEM.fields_by_name['pokemon_candy'].containing_oneof = _LOOTITEM.oneofs_by_name['Type']
_LOOTITEM.oneofs_by_name['Type'].fields.append(
  _LOOTITEM.fields_by_name['count'])
_LOOTITEM.fields_by_name['count'].containing_oneof = _LOOTITEM.oneofs_by_name['Type']
_LOOTITEM.oneofs_by_name['Type'].fields.append(
  _LOOTITEM.fields_by_name['experience'])
_LOOTITEM.fields_by_name['experience'].containing_oneof = _LOOTITEM.oneofs_by_name['Type']
_LOOTITEM.oneofs_by_name['Type'].fields.append(
  _LOOTITEM.fields_by_name['pokemon_egg'])
_LOOTITEM.fields_by_name['pokemon_egg'].containing_oneof = _LOOTITEM.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['LootItem'] = _LOOTITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LootItem = _reflection.GeneratedProtocolMessageType('LootItem', (_message.Message,), dict(
  DESCRIPTOR = _LOOTITEM,
  __module__ = 'pogoprotos.inventory.loot_item_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.LootItem)
  ))
_sym_db.RegisterMessage(LootItem)


# @@protoc_insertion_point(module_scope)
