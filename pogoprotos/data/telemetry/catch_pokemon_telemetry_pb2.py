# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/catch_pokemon_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.telemetry import encounter_pokemon_telemetry_pb2 as pogoprotos_dot_data_dot_telemetry_dot_encounter__pokemon__telemetry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/catch_pokemon_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_pb=_b('\n7pogoprotos/data/telemetry/catch_pokemon_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a;pogoprotos/data/telemetry/encounter_pokemon_telemetry.proto\"\xd1\x01\n\x15\x43\x61tchPokemonTelemetry\x12\x0e\n\x06status\x18\x01 \x01(\t\x12Y\n\x1b\x65ncounter_pokemon_telemetry\x18\x02 \x01(\x0b\x32\x34.pogoprotos.data.telemetry.EncounterPokemonTelemetry\x12\x10\n\x08\x62\x61lltype\x18\x03 \x01(\x05\x12\x11\n\thit_grade\x18\x04 \x01(\x05\x12\x12\n\ncurve_ball\x18\x05 \x01(\x08\x12\x14\n\x0cmiss_percent\x18\x06 \x01(\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_telemetry_dot_encounter__pokemon__telemetry__pb2.DESCRIPTOR,])




_CATCHPOKEMONTELEMETRY = _descriptor.Descriptor(
  name='CatchPokemonTelemetry',
  full_name='pogoprotos.data.telemetry.CatchPokemonTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.data.telemetry.CatchPokemonTelemetry.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter_pokemon_telemetry', full_name='pogoprotos.data.telemetry.CatchPokemonTelemetry.encounter_pokemon_telemetry', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='balltype', full_name='pogoprotos.data.telemetry.CatchPokemonTelemetry.balltype', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hit_grade', full_name='pogoprotos.data.telemetry.CatchPokemonTelemetry.hit_grade', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='curve_ball', full_name='pogoprotos.data.telemetry.CatchPokemonTelemetry.curve_ball', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='miss_percent', full_name='pogoprotos.data.telemetry.CatchPokemonTelemetry.miss_percent', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=148,
  serialized_end=357,
)

_CATCHPOKEMONTELEMETRY.fields_by_name['encounter_pokemon_telemetry'].message_type = pogoprotos_dot_data_dot_telemetry_dot_encounter__pokemon__telemetry__pb2._ENCOUNTERPOKEMONTELEMETRY
DESCRIPTOR.message_types_by_name['CatchPokemonTelemetry'] = _CATCHPOKEMONTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CatchPokemonTelemetry = _reflection.GeneratedProtocolMessageType('CatchPokemonTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _CATCHPOKEMONTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.catch_pokemon_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.CatchPokemonTelemetry)
  ))
_sym_db.RegisterMessage(CatchPokemonTelemetry)


# @@protoc_insertion_point(module_scope)
