# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/token/sfida_auth_token.proto

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
  name='pogoprotos/data/token/sfida_auth_token.proto',
  package='pogoprotos.data.token',
  syntax='proto3',
  serialized_pb=_b('\n,pogoprotos/data/token/sfida_auth_token.proto\x12\x15pogoprotos.data.token\":\n\x0eSfidaAuthToken\x12\x16\n\x0eresponse_token\x18\x01 \x01(\x0c\x12\x10\n\x08sfida_id\x18\x02 \x01(\tb\x06proto3')
)




_SFIDAAUTHTOKEN = _descriptor.Descriptor(
  name='SfidaAuthToken',
  full_name='pogoprotos.data.token.SfidaAuthToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_token', full_name='pogoprotos.data.token.SfidaAuthToken.response_token', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sfida_id', full_name='pogoprotos.data.token.SfidaAuthToken.sfida_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=71,
  serialized_end=129,
)

DESCRIPTOR.message_types_by_name['SfidaAuthToken'] = _SFIDAAUTHTOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SfidaAuthToken = _reflection.GeneratedProtocolMessageType('SfidaAuthToken', (_message.Message,), dict(
  DESCRIPTOR = _SFIDAAUTHTOKEN,
  __module__ = 'pogoprotos.data.token.sfida_auth_token_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.token.SfidaAuthToken)
  ))
_sym_db.RegisterMessage(SfidaAuthToken)


# @@protoc_insertion_point(module_scope)
