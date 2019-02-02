# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_inbox_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.inbox import client_inbox_pb2 as pogoprotos_dot_data_dot_inbox_dot_client__inbox__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_inbox_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n8pogoprotos/networking/responses/get_inbox_response.proto\x12\x1fpogoprotos.networking.responses\x1a(pogoprotos/data/inbox/client_inbox.proto\"\xcd\x01\n\x10GetInboxResponse\x12H\n\x06result\x18\x01 \x01(\x0e\x32\x38.pogoprotos.networking.responses.GetInboxResponse.Result\x12\x31\n\x05inbox\x18\x02 \x01(\x0b\x32\".pogoprotos.data.inbox.ClientInbox\"<\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x12\r\n\tTIMED_OUT\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_inbox_dot_client__inbox__pb2.DESCRIPTOR,])



_GETINBOXRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GetInboxResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMED_OUT', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=281,
  serialized_end=341,
)
_sym_db.RegisterEnumDescriptor(_GETINBOXRESPONSE_RESULT)


_GETINBOXRESPONSE = _descriptor.Descriptor(
  name='GetInboxResponse',
  full_name='pogoprotos.networking.responses.GetInboxResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GetInboxResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inbox', full_name='pogoprotos.networking.responses.GetInboxResponse.inbox', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETINBOXRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=341,
)

_GETINBOXRESPONSE.fields_by_name['result'].enum_type = _GETINBOXRESPONSE_RESULT
_GETINBOXRESPONSE.fields_by_name['inbox'].message_type = pogoprotos_dot_data_dot_inbox_dot_client__inbox__pb2._CLIENTINBOX
_GETINBOXRESPONSE_RESULT.containing_type = _GETINBOXRESPONSE
DESCRIPTOR.message_types_by_name['GetInboxResponse'] = _GETINBOXRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetInboxResponse = _reflection.GeneratedProtocolMessageType('GetInboxResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETINBOXRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_inbox_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetInboxResponse)
  ))
_sym_db.RegisterMessage(GetInboxResponse)


# @@protoc_insertion_point(module_scope)