# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/responses/redeem_google_receipt_response.proto

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
  name='pogoprotos/networking/platform/responses/redeem_google_receipt_response.proto',
  package='pogoprotos.networking.platform.responses',
  syntax='proto3',
  serialized_pb=_b('\nMpogoprotos/networking/platform/responses/redeem_google_receipt_response.proto\x12(pogoprotos.networking.platform.responses\"\xc5\x01\n\x1bRedeemGoogleReceiptResponse\x12\\\n\x06result\x18\x01 \x01(\x0e\x32L.pogoprotos.networking.platform.responses.RedeemGoogleReceiptResponse.Status\x12\x19\n\x11transaction_token\x18\x02 \x01(\t\"-\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x62\x06proto3')
)



_REDEEMGOOGLERECEIPTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.platform.responses.RedeemGoogleReceiptResponse.Status',
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
  ],
  containing_type=None,
  options=None,
  serialized_start=276,
  serialized_end=321,
)
_sym_db.RegisterEnumDescriptor(_REDEEMGOOGLERECEIPTRESPONSE_STATUS)


_REDEEMGOOGLERECEIPTRESPONSE = _descriptor.Descriptor(
  name='RedeemGoogleReceiptResponse',
  full_name='pogoprotos.networking.platform.responses.RedeemGoogleReceiptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.platform.responses.RedeemGoogleReceiptResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_token', full_name='pogoprotos.networking.platform.responses.RedeemGoogleReceiptResponse.transaction_token', index=1,
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
    _REDEEMGOOGLERECEIPTRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=321,
)

_REDEEMGOOGLERECEIPTRESPONSE.fields_by_name['result'].enum_type = _REDEEMGOOGLERECEIPTRESPONSE_STATUS
_REDEEMGOOGLERECEIPTRESPONSE_STATUS.containing_type = _REDEEMGOOGLERECEIPTRESPONSE
DESCRIPTOR.message_types_by_name['RedeemGoogleReceiptResponse'] = _REDEEMGOOGLERECEIPTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedeemGoogleReceiptResponse = _reflection.GeneratedProtocolMessageType('RedeemGoogleReceiptResponse', (_message.Message,), dict(
  DESCRIPTOR = _REDEEMGOOGLERECEIPTRESPONSE,
  __module__ = 'pogoprotos.networking.platform.responses.redeem_google_receipt_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.RedeemGoogleReceiptResponse)
  ))
_sym_db.RegisterMessage(RedeemGoogleReceiptResponse)


# @@protoc_insertion_point(module_scope)
