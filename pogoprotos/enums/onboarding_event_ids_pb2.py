# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/onboarding_event_ids.proto

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
  name='pogoprotos/enums/onboarding_event_ids.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n+pogoprotos/enums/onboarding_event_ids.proto\x12\x10pogoprotos.enums*\xbd\x05\n\x12OnboardingEventIds\x12\x10\n\x0cTOS_ACCEPTED\x10\x00\x12\x14\n\x10PRIVACY_ACCEPTED\x10\x01\x12\x10\n\x0c\x43ONVERSATION\x10\x02\x12\x13\n\x0f\x45NCOUNTER_ENTER\x10\x03\x12\x13\n\x0f\x45NCOUNTER_LEAVE\x10\x04\x12\x1f\n\x1b\x41VATAR_SELECTION_ONBOARDING\x10\x05\x12\x11\n\rAVATAR_GENDER\x10\x06\x12\x18\n\x14\x41VATAR_GENDER_CHOSEN\x10\x07\x12\x16\n\x12\x41VATAR_HEAD_CHOSEN\x10\x08\x12\x16\n\x12\x41VATAR_BODY_CHOSEN\x10\t\x12\x14\n\x10\x41VATAR_TRY_AGAIN\x10\n\x12\x13\n\x0f\x41VATAR_ACCEPTED\x10\x0b\x12\x0e\n\nNAME_ENTRY\x10\x0c\x12\x14\n\x10NAME_UNAVAILABLE\x10\r\x12\x11\n\rNAME_ACCEPTED\x10\x0e\x12\x1c\n\x18POKEDEX_TUTORIAL_STARTED\x10\x0f\x12,\n(POKEDEX_TUTORIAL_INFO_PANEL_EXIT_PRESSED\x10\x10\x12\x18\n\x14POKEDEX_EXIT_PRESSED\x10\x11\x12\x18\n\x14\x45GG_TUTORIAL_STARTED\x10\x12\x12\x16\n\x12\x45GG_TUTORIAL_PRESS\x10\x13\x12\x19\n\x15\x45GG_TUTORIAL_FINISHED\x10\x14\x12\x13\n\x0fPOKESTOP_LETSGO\x10\x15\x12\"\n\x1eWILD_POKEMON_ENCOUNTER_ENTERED\x10\x16\x12\x17\n\x13WILD_POKEMON_CAUGHT\x10\x17\x12\x17\n\x13\x41R_STANDARD_ENABLED\x10\x18\x12\x18\n\x14\x41R_STANDARD_REJECTED\x10\x19\x12\x13\n\x0f\x41R_PLUS_ENABLED\x10\x1a\x12\x14\n\x10\x41R_PLUS_REJECTED\x10\x1b*#\n\x11OnboardingPathIds\x12\x06\n\x02V1\x10\x00\x12\x06\n\x02V2\x10\x01\x62\x06proto3')
)

_ONBOARDINGEVENTIDS = _descriptor.EnumDescriptor(
  name='OnboardingEventIds',
  full_name='pogoprotos.enums.OnboardingEventIds',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TOS_ACCEPTED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIVACY_ACCEPTED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONVERSATION', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_ENTER', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_LEAVE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVATAR_SELECTION_ONBOARDING', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVATAR_GENDER', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVATAR_GENDER_CHOSEN', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVATAR_HEAD_CHOSEN', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVATAR_BODY_CHOSEN', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVATAR_TRY_AGAIN', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVATAR_ACCEPTED', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAME_ENTRY', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAME_UNAVAILABLE', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAME_ACCEPTED', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEDEX_TUTORIAL_STARTED', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEDEX_TUTORIAL_INFO_PANEL_EXIT_PRESSED', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEDEX_EXIT_PRESSED', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGG_TUTORIAL_STARTED', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGG_TUTORIAL_PRESS', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGG_TUTORIAL_FINISHED', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKESTOP_LETSGO', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WILD_POKEMON_ENCOUNTER_ENTERED', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WILD_POKEMON_CAUGHT', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AR_STANDARD_ENABLED', index=24, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AR_STANDARD_REJECTED', index=25, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AR_PLUS_ENABLED', index=26, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AR_PLUS_REJECTED', index=27, number=27,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=66,
  serialized_end=767,
)
_sym_db.RegisterEnumDescriptor(_ONBOARDINGEVENTIDS)

OnboardingEventIds = enum_type_wrapper.EnumTypeWrapper(_ONBOARDINGEVENTIDS)
_ONBOARDINGPATHIDS = _descriptor.EnumDescriptor(
  name='OnboardingPathIds',
  full_name='pogoprotos.enums.OnboardingPathIds',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='V1', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=769,
  serialized_end=804,
)
_sym_db.RegisterEnumDescriptor(_ONBOARDINGPATHIDS)

OnboardingPathIds = enum_type_wrapper.EnumTypeWrapper(_ONBOARDINGPATHIDS)
TOS_ACCEPTED = 0
PRIVACY_ACCEPTED = 1
CONVERSATION = 2
ENCOUNTER_ENTER = 3
ENCOUNTER_LEAVE = 4
AVATAR_SELECTION_ONBOARDING = 5
AVATAR_GENDER = 6
AVATAR_GENDER_CHOSEN = 7
AVATAR_HEAD_CHOSEN = 8
AVATAR_BODY_CHOSEN = 9
AVATAR_TRY_AGAIN = 10
AVATAR_ACCEPTED = 11
NAME_ENTRY = 12
NAME_UNAVAILABLE = 13
NAME_ACCEPTED = 14
POKEDEX_TUTORIAL_STARTED = 15
POKEDEX_TUTORIAL_INFO_PANEL_EXIT_PRESSED = 16
POKEDEX_EXIT_PRESSED = 17
EGG_TUTORIAL_STARTED = 18
EGG_TUTORIAL_PRESS = 19
EGG_TUTORIAL_FINISHED = 20
POKESTOP_LETSGO = 21
WILD_POKEMON_ENCOUNTER_ENTERED = 22
WILD_POKEMON_CAUGHT = 23
AR_STANDARD_ENABLED = 24
AR_STANDARD_REJECTED = 25
AR_PLUS_ENABLED = 26
AR_PLUS_REJECTED = 27
V1 = 0
V2 = 1


DESCRIPTOR.enum_types_by_name['OnboardingEventIds'] = _ONBOARDINGEVENTIDS
DESCRIPTOR.enum_types_by_name['OnboardingPathIds'] = _ONBOARDINGPATHIDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)