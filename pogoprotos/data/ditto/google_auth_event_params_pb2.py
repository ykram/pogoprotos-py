# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/ditto/google_auth_event_params.proto

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
  name='pogoprotos/data/ditto/google_auth_event_params.proto',
  package='pogoprotos.data.ditto',
  syntax='proto3',
  serialized_pb=_b('\n4pogoprotos/data/ditto/google_auth_event_params.proto\x12\x15pogoprotos.data.ditto\">\n\x15GoogleAuthEventParams\x12\x0f\n\x07payload\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x02 \x01(\tb\x06proto3')
)




_GOOGLEAUTHEVENTPARAMS = _descriptor.Descriptor(
  name='GoogleAuthEventParams',
  full_name='pogoprotos.data.ditto.GoogleAuthEventParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='pogoprotos.data.ditto.GoogleAuthEventParams.payload', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_name', full_name='pogoprotos.data.ditto.GoogleAuthEventParams.account_name', index=1,
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
  serialized_start=79,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['GoogleAuthEventParams'] = _GOOGLEAUTHEVENTPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GoogleAuthEventParams = _reflection.GeneratedProtocolMessageType('GoogleAuthEventParams', (_message.Message,), dict(
  DESCRIPTOR = _GOOGLEAUTHEVENTPARAMS,
  __module__ = 'pogoprotos.data.ditto.google_auth_event_params_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.ditto.GoogleAuthEventParams)
  ))
_sym_db.RegisterMessage(GoogleAuthEventParams)


# @@protoc_insertion_point(module_scope)
