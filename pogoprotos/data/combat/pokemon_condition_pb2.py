# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/pokemon_condition.proto

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
from pogoprotos.data.combat import with_pokemon_cp_limit_pb2 as pogoprotos_dot_data_dot_combat_dot_with__pokemon__cp__limit__pb2
from pogoprotos.data.combat import with_pokemon_type_pb2 as pogoprotos_dot_data_dot_combat_dot_with__pokemon__type__pb2
from pogoprotos.data.combat import with_pokemon_category_pb2 as pogoprotos_dot_data_dot_combat_dot_with__pokemon__category__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/combat/pokemon_condition.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_pb=_b('\n.pogoprotos/data/combat/pokemon_condition.proto\x12\x16pogoprotos.data.combat\x1a%pogoprotos/enums/condition_type.proto\x1a\x32pogoprotos/data/combat/with_pokemon_cp_limit.proto\x1a.pogoprotos/data/combat/with_pokemon_type.proto\x1a\x32pogoprotos/data/combat/with_pokemon_category.proto\"\x9c\x02\n\x10PokemonCondition\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.pogoprotos.enums.ConditionType\x12I\n\x15with_pokemon_cp_limit\x18\x02 \x01(\x0b\x32*.pogoprotos.data.combat.WithPokemonCpLimit\x12\x42\n\x11with_pokemon_type\x18\x03 \x01(\x0b\x32\'.pogoprotos.data.combat.WithPokemonType\x12J\n\x15with_pokemon_category\x18\x04 \x01(\x0b\x32+.pogoprotos.data.combat.WithPokemonCategoryb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_condition__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_with__pokemon__cp__limit__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_with__pokemon__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_with__pokemon__category__pb2.DESCRIPTOR,])




_POKEMONCONDITION = _descriptor.Descriptor(
  name='PokemonCondition',
  full_name='pogoprotos.data.combat.PokemonCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.data.combat.PokemonCondition.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='with_pokemon_cp_limit', full_name='pogoprotos.data.combat.PokemonCondition.with_pokemon_cp_limit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='with_pokemon_type', full_name='pogoprotos.data.combat.PokemonCondition.with_pokemon_type', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='with_pokemon_category', full_name='pogoprotos.data.combat.PokemonCondition.with_pokemon_category', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=266,
  serialized_end=550,
)

_POKEMONCONDITION.fields_by_name['type'].enum_type = pogoprotos_dot_enums_dot_condition__type__pb2._CONDITIONTYPE
_POKEMONCONDITION.fields_by_name['with_pokemon_cp_limit'].message_type = pogoprotos_dot_data_dot_combat_dot_with__pokemon__cp__limit__pb2._WITHPOKEMONCPLIMIT
_POKEMONCONDITION.fields_by_name['with_pokemon_type'].message_type = pogoprotos_dot_data_dot_combat_dot_with__pokemon__type__pb2._WITHPOKEMONTYPE
_POKEMONCONDITION.fields_by_name['with_pokemon_category'].message_type = pogoprotos_dot_data_dot_combat_dot_with__pokemon__category__pb2._WITHPOKEMONCATEGORY
DESCRIPTOR.message_types_by_name['PokemonCondition'] = _POKEMONCONDITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokemonCondition = _reflection.GeneratedProtocolMessageType('PokemonCondition', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONCONDITION,
  __module__ = 'pogoprotos.data.combat.pokemon_condition_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.PokemonCondition)
  ))
_sym_db.RegisterMessage(PokemonCondition)


# @@protoc_insertion_point(module_scope)