# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/invitation_type.proto

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
  name='pogoprotos/enums/invitation_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n&pogoprotos/enums/invitation_type.proto\x12\x10pogoprotos.enums*\x87\x01\n\x0eInvitationType\x12\x19\n\x15INVITATION_TYPE_UNSET\x10\x00\x12\x18\n\x14INVITATION_TYPE_CODE\x10\x01\x12\x1c\n\x18INVITATION_TYPE_FACEBOOK\x10\x02\x12\"\n\x1eINVITATION_TYPE_SERVER_REQUEST\x10\x03\x62\x06proto3')
)

_INVITATIONTYPE = _descriptor.EnumDescriptor(
  name='InvitationType',
  full_name='pogoprotos.enums.InvitationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVITATION_TYPE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVITATION_TYPE_CODE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVITATION_TYPE_FACEBOOK', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVITATION_TYPE_SERVER_REQUEST', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=61,
  serialized_end=196,
)
_sym_db.RegisterEnumDescriptor(_INVITATIONTYPE)

InvitationType = enum_type_wrapper.EnumTypeWrapper(_INVITATIONTYPE)
INVITATION_TYPE_UNSET = 0
INVITATION_TYPE_CODE = 1
INVITATION_TYPE_FACEBOOK = 2
INVITATION_TYPE_SERVER_REQUEST = 3


DESCRIPTOR.enum_types_by_name['InvitationType'] = _INVITATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
