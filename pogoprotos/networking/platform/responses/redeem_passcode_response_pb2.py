# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/responses/redeem_passcode_response.proto

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
  name='pogoprotos/networking/platform/responses/redeem_passcode_response.proto',
  package='pogoprotos.networking.platform.responses',
  syntax='proto3',
  serialized_pb=_b('\nGpogoprotos/networking/platform/responses/redeem_passcode_response.proto\x12(pogoprotos.networking.platform.responses\"\xb4\x01\n\x16RedeemPasscodeResponse\x12W\n\x06status\x18\x01 \x01(\x0e\x32G.pogoprotos.networking.platform.responses.RedeemPasscodeResponse.Status\x12\x0e\n\x06qrcode\x18\x04 \x01(\t\"1\n\x06Status\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07INVALID\x10\x02\x62\x06proto3')
)



_REDEEMPASSCODERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.platform.responses.RedeemPasscodeResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=249,
  serialized_end=298,
)
_sym_db.RegisterEnumDescriptor(_REDEEMPASSCODERESPONSE_STATUS)


_REDEEMPASSCODERESPONSE = _descriptor.Descriptor(
  name='RedeemPasscodeResponse',
  full_name='pogoprotos.networking.platform.responses.RedeemPasscodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.platform.responses.RedeemPasscodeResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qrcode', full_name='pogoprotos.networking.platform.responses.RedeemPasscodeResponse.qrcode', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REDEEMPASSCODERESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=298,
)

_REDEEMPASSCODERESPONSE.fields_by_name['status'].enum_type = _REDEEMPASSCODERESPONSE_STATUS
_REDEEMPASSCODERESPONSE_STATUS.containing_type = _REDEEMPASSCODERESPONSE
DESCRIPTOR.message_types_by_name['RedeemPasscodeResponse'] = _REDEEMPASSCODERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedeemPasscodeResponse = _reflection.GeneratedProtocolMessageType('RedeemPasscodeResponse', (_message.Message,), dict(
  DESCRIPTOR = _REDEEMPASSCODERESPONSE,
  __module__ = 'pogoprotos.networking.platform.responses.redeem_passcode_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.RedeemPasscodeResponse)
  ))
_sym_db.RegisterMessage(RedeemPasscodeResponse)


# @@protoc_insertion_point(module_scope)
