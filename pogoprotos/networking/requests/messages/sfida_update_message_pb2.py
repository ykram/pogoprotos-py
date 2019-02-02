# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/sfida_update_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.sfida import sfida_metrics_update_pb2 as pogoprotos_dot_data_dot_sfida_dot_sfida__metrics__update__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/sfida_update_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nBpogoprotos/networking/requests/messages/sfida_update_message.proto\x12\'pogoprotos.networking.requests.messages\x1a\x30pogoprotos/data/sfida/sfida_metrics_update.proto\"\x7f\n\x12SfidaUpdateMessage\x12\x12\n\nplayer_lat\x18\x01 \x01(\x01\x12\x12\n\nplayer_lng\x18\x02 \x01(\x01\x12\x41\n\x0emetrics_update\x18\x03 \x01(\x0b\x32).pogoprotos.data.sfida.SfidaMetricsUpdateb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_sfida_dot_sfida__metrics__update__pb2.DESCRIPTOR,])




_SFIDAUPDATEMESSAGE = _descriptor.Descriptor(
  name='SfidaUpdateMessage',
  full_name='pogoprotos.networking.requests.messages.SfidaUpdateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_lat', full_name='pogoprotos.networking.requests.messages.SfidaUpdateMessage.player_lat', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_lng', full_name='pogoprotos.networking.requests.messages.SfidaUpdateMessage.player_lng', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metrics_update', full_name='pogoprotos.networking.requests.messages.SfidaUpdateMessage.metrics_update', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=161,
  serialized_end=288,
)

_SFIDAUPDATEMESSAGE.fields_by_name['metrics_update'].message_type = pogoprotos_dot_data_dot_sfida_dot_sfida__metrics__update__pb2._SFIDAMETRICSUPDATE
DESCRIPTOR.message_types_by_name['SfidaUpdateMessage'] = _SFIDAUPDATEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SfidaUpdateMessage = _reflection.GeneratedProtocolMessageType('SfidaUpdateMessage', (_message.Message,), dict(
  DESCRIPTOR = _SFIDAUPDATEMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.sfida_update_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.SfidaUpdateMessage)
  ))
_sym_db.RegisterMessage(SfidaUpdateMessage)


# @@protoc_insertion_point(module_scope)
