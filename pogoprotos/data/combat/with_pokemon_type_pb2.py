# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/with_pokemon_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_type_pb2 as pogoprotos_dot_enums_dot_pokemon__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/combat/with_pokemon_type.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_pb=_b('\n.pogoprotos/data/combat/with_pokemon_type.proto\x12\x16pogoprotos.data.combat\x1a#pogoprotos/enums/pokemon_type.proto\"F\n\x0fWithPokemonType\x12\x33\n\x0cpokemon_type\x18\x01 \x03(\x0e\x32\x1d.pogoprotos.enums.PokemonTypeb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__type__pb2.DESCRIPTOR,])




_WITHPOKEMONTYPE = _descriptor.Descriptor(
  name='WithPokemonType',
  full_name='pogoprotos.data.combat.WithPokemonType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_type', full_name='pogoprotos.data.combat.WithPokemonType.pokemon_type', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=111,
  serialized_end=181,
)

_WITHPOKEMONTYPE.fields_by_name['pokemon_type'].enum_type = pogoprotos_dot_enums_dot_pokemon__type__pb2._POKEMONTYPE
DESCRIPTOR.message_types_by_name['WithPokemonType'] = _WITHPOKEMONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WithPokemonType = _reflection.GeneratedProtocolMessageType('WithPokemonType', (_message.Message,), dict(
  DESCRIPTOR = _WITHPOKEMONTYPE,
  __module__ = 'pogoprotos.data.combat.with_pokemon_type_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.WithPokemonType)
  ))
_sym_db.RegisterMessage(WithPokemonType)


# @@protoc_insertion_point(module_scope)
