# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/pokemon_go_plus_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_go_plus_ids_pb2 as pogoprotos_dot_enums_dot_pokemon__go__plus__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/pokemon_go_plus_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_pb=_b('\n9pogoprotos/data/telemetry/pokemon_go_plus_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a*pogoprotos/enums/pokemon_go_plus_ids.proto\"s\n\x16PokemonGoPlusTelemetry\x12\x39\n\rpgp_event_ids\x18\x01 \x01(\x0e\x32\".pogoprotos.enums.PokemonGoPlusIds\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x0f\n\x07version\x18\x03 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__go__plus__ids__pb2.DESCRIPTOR,])




_POKEMONGOPLUSTELEMETRY = _descriptor.Descriptor(
  name='PokemonGoPlusTelemetry',
  full_name='pogoprotos.data.telemetry.PokemonGoPlusTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pgp_event_ids', full_name='pogoprotos.data.telemetry.PokemonGoPlusTelemetry.pgp_event_ids', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='pogoprotos.data.telemetry.PokemonGoPlusTelemetry.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='pogoprotos.data.telemetry.PokemonGoPlusTelemetry.version', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=132,
  serialized_end=247,
)

_POKEMONGOPLUSTELEMETRY.fields_by_name['pgp_event_ids'].enum_type = pogoprotos_dot_enums_dot_pokemon__go__plus__ids__pb2._POKEMONGOPLUSIDS
DESCRIPTOR.message_types_by_name['PokemonGoPlusTelemetry'] = _POKEMONGOPLUSTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokemonGoPlusTelemetry = _reflection.GeneratedProtocolMessageType('PokemonGoPlusTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONGOPLUSTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.pokemon_go_plus_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.PokemonGoPlusTelemetry)
  ))
_sym_db.RegisterMessage(PokemonGoPlusTelemetry)


# @@protoc_insertion_point(module_scope)
