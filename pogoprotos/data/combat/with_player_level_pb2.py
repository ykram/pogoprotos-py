# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/with_player_level.proto

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
  name='pogoprotos/data/combat/with_player_level.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_pb=_b('\n.pogoprotos/data/combat/with_player_level.proto\x12\x16pogoprotos.data.combat\" \n\x0fWithPlayerLevel\x12\r\n\x05level\x18\x01 \x01(\x05\x62\x06proto3')
)




_WITHPLAYERLEVEL = _descriptor.Descriptor(
  name='WithPlayerLevel',
  full_name='pogoprotos.data.combat.WithPlayerLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='pogoprotos.data.combat.WithPlayerLevel.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=74,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['WithPlayerLevel'] = _WITHPLAYERLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WithPlayerLevel = _reflection.GeneratedProtocolMessageType('WithPlayerLevel', (_message.Message,), dict(
  DESCRIPTOR = _WITHPLAYERLEVEL,
  __module__ = 'pogoprotos.data.combat.with_player_level_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.WithPlayerLevel)
  ))
_sym_db.RegisterMessage(WithPlayerLevel)


# @@protoc_insertion_point(module_scope)
