# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/poi_submission_tutorial_page.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/poi_submission_tutorial_page.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n3pogoprotos/enums/poi_submission_tutorial_page.proto\x12\x10pogoprotos.enums*\x7f\n\x19PoiSubmissionTutorialPage\x12\x14\n\x10WHAT_IS_POKESTOP\x10\x00\x12\x15\n\x11SUBMIT_FOR_REVIEW\x10\x01\x12\x1c\n\x18HOW_TO_CHOOSE_A_LOCATION\x10\x02\x12\x17\n\x13\x44\x45SCRIBE_A_LOCATION\x10\x03\x62\x06proto3')
)

_POISUBMISSIONTUTORIALPAGE = _descriptor.EnumDescriptor(
  name='PoiSubmissionTutorialPage',
  full_name='pogoprotos.enums.PoiSubmissionTutorialPage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WHAT_IS_POKESTOP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_FOR_REVIEW', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOW_TO_CHOOSE_A_LOCATION', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCRIBE_A_LOCATION', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=73,
  serialized_end=200,
)
_sym_db.RegisterEnumDescriptor(_POISUBMISSIONTUTORIALPAGE)

PoiSubmissionTutorialPage = enum_type_wrapper.EnumTypeWrapper(_POISUBMISSIONTUTORIALPAGE)
WHAT_IS_POKESTOP = 0
SUBMIT_FOR_REVIEW = 1
HOW_TO_CHOOSE_A_LOCATION = 2
DESCRIBE_A_LOCATION = 3


DESCRIPTOR.enum_types_by_name['PoiSubmissionTutorialPage'] = _POISUBMISSIONTUTORIALPAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
