# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/inventory_key.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import quest_type_pb2 as pogoprotos_dot_enums_dot_quest__type__pb2
from pogoprotos.enums import pokemon_family_id_pb2 as pogoprotos_dot_enums_dot_pokemon__family__id__pb2
from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/inventory_key.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_pb=_b('\n(pogoprotos/inventory/inventory_key.proto\x12\x14pogoprotos.inventory\x1a!pogoprotos/enums/quest_type.proto\x1a(pogoprotos/enums/pokemon_family_id.proto\x1a\'pogoprotos/inventory/item/item_id.proto\"\x87\x04\n\x0cInventoryKey\x12\x14\n\npokemon_id\x18\x01 \x01(\x06H\x00\x12\x31\n\x04item\x18\x02 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemIdH\x00\x12\x1a\n\x10pokedex_entry_id\x18\x03 \x01(\x05H\x00\x12\x16\n\x0cplayer_stats\x18\x04 \x01(\x08H\x00\x12\x19\n\x0fplayer_currency\x18\x05 \x01(\x08H\x00\x12\x17\n\rplayer_camera\x18\x06 \x01(\x08H\x00\x12\x1c\n\x12inventory_upgrades\x18\x07 \x01(\x08H\x00\x12\x17\n\rapplied_items\x18\x08 \x01(\x08H\x00\x12\x18\n\x0e\x65gg_incubators\x18\t \x01(\x08H\x00\x12>\n\x11pokemon_family_id\x18\n \x01(\x0e\x32!.pogoprotos.enums.PokemonFamilyIdH\x00\x12\x31\n\nquest_type\x18\x0b \x01(\x0e\x32\x1b.pogoprotos.enums.QuestTypeH\x00\x12\x1c\n\x12\x61vatar_template_id\x18\x0c \x01(\tH\x00\x12\x16\n\x0craid_tickets\x18\r \x01(\x08H\x00\x12\x10\n\x06quests\x18\x0e \x01(\x08H\x00\x12\x14\n\ngift_boxes\x18\x0f \x01(\x08H\x00\x12\x1c\n\x12\x62\x65luga_incense_box\x18\x10 \x01(\x08H\x00\x42\x06\n\x04Typeb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_quest__type__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__family__id__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,])




_INVENTORYKEY = _descriptor.Descriptor(
  name='InventoryKey',
  full_name='pogoprotos.inventory.InventoryKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.inventory.InventoryKey.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='pogoprotos.inventory.InventoryKey.item', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokedex_entry_id', full_name='pogoprotos.inventory.InventoryKey.pokedex_entry_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_stats', full_name='pogoprotos.inventory.InventoryKey.player_stats', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_currency', full_name='pogoprotos.inventory.InventoryKey.player_currency', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_camera', full_name='pogoprotos.inventory.InventoryKey.player_camera', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_upgrades', full_name='pogoprotos.inventory.InventoryKey.inventory_upgrades', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applied_items', full_name='pogoprotos.inventory.InventoryKey.applied_items', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_incubators', full_name='pogoprotos.inventory.InventoryKey.egg_incubators', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_family_id', full_name='pogoprotos.inventory.InventoryKey.pokemon_family_id', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_type', full_name='pogoprotos.inventory.InventoryKey.quest_type', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_template_id', full_name='pogoprotos.inventory.InventoryKey.avatar_template_id', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_tickets', full_name='pogoprotos.inventory.InventoryKey.raid_tickets', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quests', full_name='pogoprotos.inventory.InventoryKey.quests', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift_boxes', full_name='pogoprotos.inventory.InventoryKey.gift_boxes', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beluga_incense_box', full_name='pogoprotos.inventory.InventoryKey.beluga_incense_box', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
      name='Type', full_name='pogoprotos.inventory.InventoryKey.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=185,
  serialized_end=704,
)

_INVENTORYKEY.fields_by_name['item'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_INVENTORYKEY.fields_by_name['pokemon_family_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__family__id__pb2._POKEMONFAMILYID
_INVENTORYKEY.fields_by_name['quest_type'].enum_type = pogoprotos_dot_enums_dot_quest__type__pb2._QUESTTYPE
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['pokemon_id'])
_INVENTORYKEY.fields_by_name['pokemon_id'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['item'])
_INVENTORYKEY.fields_by_name['item'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['pokedex_entry_id'])
_INVENTORYKEY.fields_by_name['pokedex_entry_id'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['player_stats'])
_INVENTORYKEY.fields_by_name['player_stats'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['player_currency'])
_INVENTORYKEY.fields_by_name['player_currency'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['player_camera'])
_INVENTORYKEY.fields_by_name['player_camera'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['inventory_upgrades'])
_INVENTORYKEY.fields_by_name['inventory_upgrades'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['applied_items'])
_INVENTORYKEY.fields_by_name['applied_items'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['egg_incubators'])
_INVENTORYKEY.fields_by_name['egg_incubators'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['pokemon_family_id'])
_INVENTORYKEY.fields_by_name['pokemon_family_id'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['quest_type'])
_INVENTORYKEY.fields_by_name['quest_type'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['avatar_template_id'])
_INVENTORYKEY.fields_by_name['avatar_template_id'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['raid_tickets'])
_INVENTORYKEY.fields_by_name['raid_tickets'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['quests'])
_INVENTORYKEY.fields_by_name['quests'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['gift_boxes'])
_INVENTORYKEY.fields_by_name['gift_boxes'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
_INVENTORYKEY.oneofs_by_name['Type'].fields.append(
  _INVENTORYKEY.fields_by_name['beluga_incense_box'])
_INVENTORYKEY.fields_by_name['beluga_incense_box'].containing_oneof = _INVENTORYKEY.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['InventoryKey'] = _INVENTORYKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InventoryKey = _reflection.GeneratedProtocolMessageType('InventoryKey', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYKEY,
  __module__ = 'pogoprotos.inventory.inventory_key_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.InventoryKey)
  ))
_sym_db.RegisterMessage(InventoryKey)


# @@protoc_insertion_point(module_scope)
