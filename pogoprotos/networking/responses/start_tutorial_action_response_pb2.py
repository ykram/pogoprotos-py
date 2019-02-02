# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/start_tutorial_action_response.proto

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
  name='pogoprotos/networking/responses/start_tutorial_action_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nDpogoprotos/networking/responses/start_tutorial_action_response.proto\x12\x1fpogoprotos.networking.responses\"\xda\x01\n\x1bStartTutorialActionResponse\x12S\n\x06result\x18\x01 \x01(\x0e\x32\x43.pogoprotos.networking.responses.StartTutorialActionResponse.Result\"f\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12)\n%ERROR_PLAYER_ALREADY_STARTED_TUTORIAL\x10\x02\x12\x19\n\x15\x45RROR_FAILED_TO_START\x10\x03\x62\x06proto3')
)



_STARTTUTORIALACTIONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.StartTutorialActionResponse.Result',
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
      name='ERROR_PLAYER_ALREADY_STARTED_TUTORIAL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FAILED_TO_START', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=222,
  serialized_end=324,
)
_sym_db.RegisterEnumDescriptor(_STARTTUTORIALACTIONRESPONSE_RESULT)


_STARTTUTORIALACTIONRESPONSE = _descriptor.Descriptor(
  name='StartTutorialActionResponse',
  full_name='pogoprotos.networking.responses.StartTutorialActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.StartTutorialActionResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STARTTUTORIALACTIONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=324,
)

_STARTTUTORIALACTIONRESPONSE.fields_by_name['result'].enum_type = _STARTTUTORIALACTIONRESPONSE_RESULT
_STARTTUTORIALACTIONRESPONSE_RESULT.containing_type = _STARTTUTORIALACTIONRESPONSE
DESCRIPTOR.message_types_by_name['StartTutorialActionResponse'] = _STARTTUTORIALACTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartTutorialActionResponse = _reflection.GeneratedProtocolMessageType('StartTutorialActionResponse', (_message.Message,), dict(
  DESCRIPTOR = _STARTTUTORIALACTIONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.start_tutorial_action_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.StartTutorialActionResponse)
  ))
_sym_db.RegisterMessage(StartTutorialActionResponse)


# @@protoc_insertion_point(module_scope)
