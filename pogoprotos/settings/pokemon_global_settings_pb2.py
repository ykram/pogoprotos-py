# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/pokemon_global_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/pokemon_global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n1pogoprotos/settings/pokemon_global_settings.proto\x12\x13pogoprotos.settings\"3\n\x15PokemonGlobalSettings\x12\x1a\n\x12\x65nable_camo_shader\x18\x01 \x01(\x08\x62\x06proto3')
)




_POKEMONGLOBALSETTINGS = _descriptor.Descriptor(
  name='PokemonGlobalSettings',
  full_name='pogoprotos.settings.PokemonGlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_camo_shader', full_name='pogoprotos.settings.PokemonGlobalSettings.enable_camo_shader', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  ],
  serialized_start=74,
  serialized_end=125,
)

DESCRIPTOR.message_types_by_name['PokemonGlobalSettings'] = _POKEMONGLOBALSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokemonGlobalSettings = _reflection.GeneratedProtocolMessageType('PokemonGlobalSettings', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONGLOBALSETTINGS,
  __module__ = 'pogoprotos.settings.pokemon_global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.PokemonGlobalSettings)
  ))
_sym_db.RegisterMessage(PokemonGlobalSettings)


# @@protoc_insertion_point(module_scope)
