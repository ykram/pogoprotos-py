# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/fitness/fitness_record.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.fitness import fitness_sample_pb2 as pogoprotos_dot_data_dot_fitness_dot_fitness__sample__pb2
from pogoprotos.data.fitness import fitness_stats_pb2 as pogoprotos_dot_data_dot_fitness_dot_fitness__stats__pb2
from pogoprotos.data.fitness import fitness_metrics_report_history_pb2 as pogoprotos_dot_data_dot_fitness_dot_fitness__metrics__report__history__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/fitness/fitness_record.proto',
  package='pogoprotos.data.fitness',
  syntax='proto3',
  serialized_pb=_b('\n,pogoprotos/data/fitness/fitness_record.proto\x12\x17pogoprotos.data.fitness\x1a,pogoprotos/data/fitness/fitness_sample.proto\x1a+pogoprotos/data/fitness/fitness_stats.proto\x1a<pogoprotos/data/fitness/fitness_metrics_report_history.proto\"\xff\x01\n\rFitnessRecord\x12;\n\x0braw_samples\x18\x02 \x03(\x0b\x32&.pogoprotos.data.fitness.FitnessSample\x12%\n\x1dlast_aggregation_timestamp_ms\x18\x03 \x01(\x03\x12<\n\rfitness_stats\x18\x04 \x01(\x0b\x32%.pogoprotos.data.fitness.FitnessStats\x12L\n\x0ereport_history\x18\x05 \x01(\x0b\x32\x34.pogoprotos.data.fitness.FitnessMetricsReportHistoryb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_fitness_dot_fitness__sample__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_fitness_dot_fitness__stats__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_fitness_dot_fitness__metrics__report__history__pb2.DESCRIPTOR,])




_FITNESSRECORD = _descriptor.Descriptor(
  name='FitnessRecord',
  full_name='pogoprotos.data.fitness.FitnessRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_samples', full_name='pogoprotos.data.fitness.FitnessRecord.raw_samples', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_aggregation_timestamp_ms', full_name='pogoprotos.data.fitness.FitnessRecord.last_aggregation_timestamp_ms', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fitness_stats', full_name='pogoprotos.data.fitness.FitnessRecord.fitness_stats', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='report_history', full_name='pogoprotos.data.fitness.FitnessRecord.report_history', index=3,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=227,
  serialized_end=482,
)

_FITNESSRECORD.fields_by_name['raw_samples'].message_type = pogoprotos_dot_data_dot_fitness_dot_fitness__sample__pb2._FITNESSSAMPLE
_FITNESSRECORD.fields_by_name['fitness_stats'].message_type = pogoprotos_dot_data_dot_fitness_dot_fitness__stats__pb2._FITNESSSTATS
_FITNESSRECORD.fields_by_name['report_history'].message_type = pogoprotos_dot_data_dot_fitness_dot_fitness__metrics__report__history__pb2._FITNESSMETRICSREPORTHISTORY
DESCRIPTOR.message_types_by_name['FitnessRecord'] = _FITNESSRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FitnessRecord = _reflection.GeneratedProtocolMessageType('FitnessRecord', (_message.Message,), dict(
  DESCRIPTOR = _FITNESSRECORD,
  __module__ = 'pogoprotos.data.fitness.fitness_record_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.fitness.FitnessRecord)
  ))
_sym_db.RegisterMessage(FitnessRecord)


# @@protoc_insertion_point(module_scope)
