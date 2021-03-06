# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/unlock_condition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import condition_type_pb2 as pogoprotos_dot_enums_dot_condition__type__pb2
from pogoprotos.data.combat import with_player_level_pb2 as pogoprotos_dot_data_dot_combat_dot_with__player__level__pb2
from pogoprotos.data.combat import with_pokemon_cp_limit_pb2 as pogoprotos_dot_data_dot_combat_dot_with__pokemon__cp__limit__pb2
from pogoprotos.data.combat import with_pokemon_type_pb2 as pogoprotos_dot_data_dot_combat_dot_with__pokemon__type__pb2
from pogoprotos.data.combat import with_pokemon_category_pb2 as pogoprotos_dot_data_dot_combat_dot_with__pokemon__category__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/combat/unlock_condition.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_pb=_b('\n-pogoprotos/data/combat/unlock_condition.proto\x12\x16pogoprotos.data.combat\x1a%pogoprotos/enums/condition_type.proto\x1a.pogoprotos/data/combat/with_player_level.proto\x1a\x32pogoprotos/data/combat/with_pokemon_cp_limit.proto\x1a.pogoprotos/data/combat/with_pokemon_type.proto\x1a\x32pogoprotos/data/combat/with_pokemon_category.proto\"\xfa\x02\n\x0fUnlockCondition\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.pogoprotos.enums.ConditionType\x12\x19\n\x11min_pokemon_count\x18\x02 \x01(\x05\x12\x42\n\x11with_player_level\x18\x03 \x01(\x0b\x32\'.pogoprotos.data.combat.WithPlayerLevel\x12I\n\x15with_pokemon_cp_limit\x18\x04 \x01(\x0b\x32*.pogoprotos.data.combat.WithPokemonCpLimit\x12\x42\n\x11with_pokemon_type\x18\x05 \x01(\x0b\x32\'.pogoprotos.data.combat.WithPokemonType\x12J\n\x15with_pokemon_category\x18\x06 \x01(\x0b\x32+.pogoprotos.data.combat.WithPokemonCategoryb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_condition__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_with__player__level__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_with__pokemon__cp__limit__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_with__pokemon__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_with__pokemon__category__pb2.DESCRIPTOR,])




_UNLOCKCONDITION = _descriptor.Descriptor(
  name='UnlockCondition',
  full_name='pogoprotos.data.combat.UnlockCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.data.combat.UnlockCondition.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_pokemon_count', full_name='pogoprotos.data.combat.UnlockCondition.min_pokemon_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='with_player_level', full_name='pogoprotos.data.combat.UnlockCondition.with_player_level', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='with_pokemon_cp_limit', full_name='pogoprotos.data.combat.UnlockCondition.with_pokemon_cp_limit', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='with_pokemon_type', full_name='pogoprotos.data.combat.UnlockCondition.with_pokemon_type', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='with_pokemon_category', full_name='pogoprotos.data.combat.UnlockCondition.with_pokemon_category', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=313,
  serialized_end=691,
)

_UNLOCKCONDITION.fields_by_name['type'].enum_type = pogoprotos_dot_enums_dot_condition__type__pb2._CONDITIONTYPE
_UNLOCKCONDITION.fields_by_name['with_player_level'].message_type = pogoprotos_dot_data_dot_combat_dot_with__player__level__pb2._WITHPLAYERLEVEL
_UNLOCKCONDITION.fields_by_name['with_pokemon_cp_limit'].message_type = pogoprotos_dot_data_dot_combat_dot_with__pokemon__cp__limit__pb2._WITHPOKEMONCPLIMIT
_UNLOCKCONDITION.fields_by_name['with_pokemon_type'].message_type = pogoprotos_dot_data_dot_combat_dot_with__pokemon__type__pb2._WITHPOKEMONTYPE
_UNLOCKCONDITION.fields_by_name['with_pokemon_category'].message_type = pogoprotos_dot_data_dot_combat_dot_with__pokemon__category__pb2._WITHPOKEMONCATEGORY
DESCRIPTOR.message_types_by_name['UnlockCondition'] = _UNLOCKCONDITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnlockCondition = _reflection.GeneratedProtocolMessageType('UnlockCondition', (_message.Message,), dict(
  DESCRIPTOR = _UNLOCKCONDITION,
  __module__ = 'pogoprotos.data.combat.unlock_condition_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.UnlockCondition)
  ))
_sym_db.RegisterMessage(UnlockCondition)


# @@protoc_insertion_point(module_scope)
