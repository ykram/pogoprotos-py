# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/combat_type.proto

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
  name='pogoprotos/enums/combat_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n\"pogoprotos/enums/combat_type.proto\x12\x10pogoprotos.enums*Z\n\nCombatType\x12\x15\n\x11\x43OMBAT_TYPE_UNSET\x10\x00\x12\x08\n\x04SOLO\x10\x01\x12\x0b\n\x07QR_CODE\x10\x02\x12\x0b\n\x07\x46RIENDS\x10\x03\x12\x11\n\rNEARBY_COMBAT\x10\x04\x62\x06proto3')
)

_COMBATTYPE = _descriptor.EnumDescriptor(
  name='CombatType',
  full_name='pogoprotos.enums.CombatType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMBAT_TYPE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOLO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QR_CODE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIENDS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEARBY_COMBAT', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=56,
  serialized_end=146,
)
_sym_db.RegisterEnumDescriptor(_COMBATTYPE)

CombatType = enum_type_wrapper.EnumTypeWrapper(_COMBATTYPE)
COMBAT_TYPE_UNSET = 0
SOLO = 1
QR_CODE = 2
FRIENDS = 3
NEARBY_COMBAT = 4


DESCRIPTOR.enum_types_by_name['CombatType'] = _COMBATTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
