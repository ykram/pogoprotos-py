# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/rpc_socket_response_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.telemetry import rpc_socket_response_time_pb2 as pogoprotos_dot_data_dot_telemetry_dot_rpc__socket__response__time__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/rpc_socket_response_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_pb=_b('\n=pogoprotos/data/telemetry/rpc_socket_response_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a\x38pogoprotos/data/telemetry/rpc_socket_response_time.proto\"\x81\x01\n\x1aRpcSocketResponseTelemetry\x12\x17\n\x0fwindow_duration\x18\x01 \x01(\x02\x12J\n\x10response_timings\x18\x02 \x03(\x0b\x32\x30.pogoprotos.data.telemetry.RpcSocketResponseTimeb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_telemetry_dot_rpc__socket__response__time__pb2.DESCRIPTOR,])




_RPCSOCKETRESPONSETELEMETRY = _descriptor.Descriptor(
  name='RpcSocketResponseTelemetry',
  full_name='pogoprotos.data.telemetry.RpcSocketResponseTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='window_duration', full_name='pogoprotos.data.telemetry.RpcSocketResponseTelemetry.window_duration', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response_timings', full_name='pogoprotos.data.telemetry.RpcSocketResponseTelemetry.response_timings', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=151,
  serialized_end=280,
)

_RPCSOCKETRESPONSETELEMETRY.fields_by_name['response_timings'].message_type = pogoprotos_dot_data_dot_telemetry_dot_rpc__socket__response__time__pb2._RPCSOCKETRESPONSETIME
DESCRIPTOR.message_types_by_name['RpcSocketResponseTelemetry'] = _RPCSOCKETRESPONSETELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RpcSocketResponseTelemetry = _reflection.GeneratedProtocolMessageType('RpcSocketResponseTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _RPCSOCKETRESPONSETELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.rpc_socket_response_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.RpcSocketResponseTelemetry)
  ))
_sym_db.RegisterMessage(RpcSocketResponseTelemetry)


# @@protoc_insertion_point(module_scope)
