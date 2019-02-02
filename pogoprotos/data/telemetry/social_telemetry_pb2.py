# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/social_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/social_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_pb=_b('\n0pogoprotos/data/telemetry/social_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"x\n\x0fSocialTelemetry\x12=\n\x0fsocial_click_id\x18\x01 \x01(\x0e\x32$.pogoprotos.enums.SocialTelemetryIds\x12&\n\x1epages_scrolled_in_friends_list\x18\x02 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])




_SOCIALTELEMETRY = _descriptor.Descriptor(
  name='SocialTelemetry',
  full_name='pogoprotos.data.telemetry.SocialTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='social_click_id', full_name='pogoprotos.data.telemetry.SocialTelemetry.social_click_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pages_scrolled_in_friends_list', full_name='pogoprotos.data.telemetry.SocialTelemetry.pages_scrolled_in_friends_list', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=117,
  serialized_end=237,
)

_SOCIALTELEMETRY.fields_by_name['social_click_id'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._SOCIALTELEMETRYIDS
DESCRIPTOR.message_types_by_name['SocialTelemetry'] = _SOCIALTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SocialTelemetry = _reflection.GeneratedProtocolMessageType('SocialTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _SOCIALTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.social_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.SocialTelemetry)
  ))
_sym_db.RegisterMessage(SocialTelemetry)


# @@protoc_insertion_point(module_scope)
