# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/notification_type.proto

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
  name='pogoprotos/enums/notification_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n(pogoprotos/enums/notification_type.proto\x12\x10pogoprotos.enums*v\n\x10NotificationType\x12\x14\n\x10NO_NOTIFICATIONS\x10\x00\x12\x19\n\x15POKEMON_NOTIFICATIONS\x10\x01\x12\x1a\n\x16POKESTOP_NOTIFICATIONS\x10\x02\x12\x15\n\x11\x41LL_NOTIFICATIONS\x10\x03\x62\x06proto3')
)

_NOTIFICATIONTYPE = _descriptor.EnumDescriptor(
  name='NotificationType',
  full_name='pogoprotos.enums.NotificationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_NOTIFICATIONS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_NOTIFICATIONS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKESTOP_NOTIFICATIONS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALL_NOTIFICATIONS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=62,
  serialized_end=180,
)
_sym_db.RegisterEnumDescriptor(_NOTIFICATIONTYPE)

NotificationType = enum_type_wrapper.EnumTypeWrapper(_NOTIFICATIONTYPE)
NO_NOTIFICATIONS = 0
POKEMON_NOTIFICATIONS = 1
POKESTOP_NOTIFICATIONS = 2
ALL_NOTIFICATIONS = 3


DESCRIPTOR.enum_types_by_name['NotificationType'] = _NOTIFICATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
