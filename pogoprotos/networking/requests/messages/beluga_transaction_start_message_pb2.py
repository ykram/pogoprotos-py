# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/beluga_transaction_start_message.proto

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
  name='pogoprotos/networking/requests/messages/beluga_transaction_start_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nNpogoprotos/networking/requests/messages/beluga_transaction_start_message.proto\x12\'pogoprotos.networking.requests.messages\"U\n\x1d\x42\x65lugaTransactionStartMessage\x12\x12\n\npokemon_id\x18\x01 \x03(\x03\x12\r\n\x05nonce\x18\x02 \x01(\t\x12\x11\n\tbeluga_id\x18\x03 \x01(\tb\x06proto3')
)




_BELUGATRANSACTIONSTARTMESSAGE = _descriptor.Descriptor(
  name='BelugaTransactionStartMessage',
  full_name='pogoprotos.networking.requests.messages.BelugaTransactionStartMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.networking.requests.messages.BelugaTransactionStartMessage.pokemon_id', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='pogoprotos.networking.requests.messages.BelugaTransactionStartMessage.nonce', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beluga_id', full_name='pogoprotos.networking.requests.messages.BelugaTransactionStartMessage.beluga_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=123,
  serialized_end=208,
)

DESCRIPTOR.message_types_by_name['BelugaTransactionStartMessage'] = _BELUGATRANSACTIONSTARTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BelugaTransactionStartMessage = _reflection.GeneratedProtocolMessageType('BelugaTransactionStartMessage', (_message.Message,), dict(
  DESCRIPTOR = _BELUGATRANSACTIONSTARTMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.beluga_transaction_start_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.BelugaTransactionStartMessage)
  ))
_sym_db.RegisterMessage(BelugaTransactionStartMessage)


# @@protoc_insertion_point(module_scope)
