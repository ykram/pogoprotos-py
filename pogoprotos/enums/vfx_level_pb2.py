# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/vfx_level.proto

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
  name='pogoprotos/enums/vfx_level.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n pogoprotos/enums/vfx_level.proto\x12\x10pogoprotos.enums*M\n\x08VfxLevel\x12\x12\n\x0eNONE_VFX_LEVEL\x10\x00\x12\t\n\x05START\x10\x01\x12\x08\n\x04NICE\x10\x02\x12\t\n\x05GREAT\x10\x03\x12\r\n\tEXCELLENT\x10\x04\x62\x06proto3')
)

_VFXLEVEL = _descriptor.EnumDescriptor(
  name='VfxLevel',
  full_name='pogoprotos.enums.VfxLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_VFX_LEVEL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NICE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREAT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCELLENT', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=54,
  serialized_end=131,
)
_sym_db.RegisterEnumDescriptor(_VFXLEVEL)

VfxLevel = enum_type_wrapper.EnumTypeWrapper(_VFXLEVEL)
NONE_VFX_LEVEL = 0
START = 1
NICE = 2
GREAT = 3
EXCELLENT = 4


DESCRIPTOR.enum_types_by_name['VfxLevel'] = _VFXLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
