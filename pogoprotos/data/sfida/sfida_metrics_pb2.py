# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/sfida/sfida_metrics.proto

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
  name='pogoprotos/data/sfida/sfida_metrics.proto',
  package='pogoprotos.data.sfida',
  syntax='proto3',
  serialized_pb=_b('\n)pogoprotos/data/sfida/sfida_metrics.proto\x12\x15pogoprotos.data.sfida\"q\n\x0cSfidaMetrics\x12\x1a\n\x12\x64istance_walked_km\x18\x01 \x01(\x01\x12\x12\n\nstep_count\x18\x02 \x01(\x05\x12\x17\n\x0f\x63\x61lories_burned\x18\x03 \x01(\x01\x12\x18\n\x10\x65xercise_time_ms\x18\x04 \x01(\x03\x62\x06proto3')
)




_SFIDAMETRICS = _descriptor.Descriptor(
  name='SfidaMetrics',
  full_name='pogoprotos.data.sfida.SfidaMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='distance_walked_km', full_name='pogoprotos.data.sfida.SfidaMetrics.distance_walked_km', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_count', full_name='pogoprotos.data.sfida.SfidaMetrics.step_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calories_burned', full_name='pogoprotos.data.sfida.SfidaMetrics.calories_burned', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exercise_time_ms', full_name='pogoprotos.data.sfida.SfidaMetrics.exercise_time_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=68,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['SfidaMetrics'] = _SFIDAMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SfidaMetrics = _reflection.GeneratedProtocolMessageType('SfidaMetrics', (_message.Message,), dict(
  DESCRIPTOR = _SFIDAMETRICS,
  __module__ = 'pogoprotos.data.sfida.sfida_metrics_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.sfida.SfidaMetrics)
  ))
_sym_db.RegisterMessage(SfidaMetrics)


# @@protoc_insertion_point(module_scope)
