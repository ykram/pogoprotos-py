# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/social/list_incoming_friend_invites_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.friends import incoming_friend_invite_display_pb2 as pogoprotos_dot_data_dot_friends_dot_incoming__friend__invite__display__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/social/list_incoming_friend_invites_response.proto',
  package='pogoprotos.networking.responses.social',
  syntax='proto3',
  serialized_pb=_b('\nRpogoprotos/networking/responses/social/list_incoming_friend_invites_response.proto\x12&pogoprotos.networking.responses.social\x1a<pogoprotos/data/friends/incoming_friend_invite_display.proto\"\x81\x02\n!ListIncomingFriendInvitesResponse\x12`\n\x06result\x18\x01 \x01(\x0e\x32P.pogoprotos.networking.responses.social.ListIncomingFriendInvitesResponse.Result\x12\x45\n\x07invites\x18\x02 \x03(\x0b\x32\x34.pogoprotos.data.friends.IncomingFriendInviteDisplay\"3\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_friends_dot_incoming__friend__invite__display__pb2.DESCRIPTOR,])



_LISTINCOMINGFRIENDINVITESRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.social.ListIncomingFriendInvitesResponse.Result',
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
      name='ERROR_UNKNOWN', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=395,
  serialized_end=446,
)
_sym_db.RegisterEnumDescriptor(_LISTINCOMINGFRIENDINVITESRESPONSE_RESULT)


_LISTINCOMINGFRIENDINVITESRESPONSE = _descriptor.Descriptor(
  name='ListIncomingFriendInvitesResponse',
  full_name='pogoprotos.networking.responses.social.ListIncomingFriendInvitesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.social.ListIncomingFriendInvitesResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invites', full_name='pogoprotos.networking.responses.social.ListIncomingFriendInvitesResponse.invites', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LISTINCOMINGFRIENDINVITESRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=446,
)

_LISTINCOMINGFRIENDINVITESRESPONSE.fields_by_name['result'].enum_type = _LISTINCOMINGFRIENDINVITESRESPONSE_RESULT
_LISTINCOMINGFRIENDINVITESRESPONSE.fields_by_name['invites'].message_type = pogoprotos_dot_data_dot_friends_dot_incoming__friend__invite__display__pb2._INCOMINGFRIENDINVITEDISPLAY
_LISTINCOMINGFRIENDINVITESRESPONSE_RESULT.containing_type = _LISTINCOMINGFRIENDINVITESRESPONSE
DESCRIPTOR.message_types_by_name['ListIncomingFriendInvitesResponse'] = _LISTINCOMINGFRIENDINVITESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListIncomingFriendInvitesResponse = _reflection.GeneratedProtocolMessageType('ListIncomingFriendInvitesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTINCOMINGFRIENDINVITESRESPONSE,
  __module__ = 'pogoprotos.networking.responses.social.list_incoming_friend_invites_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.ListIncomingFriendInvitesResponse)
  ))
_sym_db.RegisterMessage(ListIncomingFriendInvitesResponse)


# @@protoc_insertion_point(module_scope)
