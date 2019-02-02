# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/player_public_profile.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import player_avatar_pb2 as pogoprotos_dot_data_dot_player_dot_player__avatar__pb2
from pogoprotos.data.player import player_badge_pb2 as pogoprotos_dot_data_dot_player_dot_player__badge__pb2
from pogoprotos.enums import team_color_pb2 as pogoprotos_dot_enums_dot_team__color__pb2
from pogoprotos.enums import gym_badge_type_pb2 as pogoprotos_dot_enums_dot_gym__badge__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/player/player_public_profile.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_pb=_b('\n2pogoprotos/data/player/player_public_profile.proto\x12\x16pogoprotos.data.player\x1a*pogoprotos/data/player/player_avatar.proto\x1a)pogoprotos/data/player/player_badge.proto\x1a!pogoprotos/enums/team_color.proto\x1a%pogoprotos/enums/gym_badge_type.proto\"\xf6\x02\n\x13PlayerPublicProfile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05level\x18\x02 \x01(\x05\x12\x34\n\x06\x61vatar\x18\x03 \x01(\x0b\x32$.pogoprotos.data.player.PlayerAvatar\x12/\n\nteam_color\x18\x04 \x01(\x0e\x32\x1b.pogoprotos.enums.TeamColor\x12\x13\n\x0b\x62\x61ttles_won\x18\x05 \x01(\x05\x12\x11\n\tkm_walked\x18\x06 \x01(\x02\x12\x16\n\x0e\x63\x61ught_pokemon\x18\x07 \x01(\x05\x12\x36\n\x0egym_badge_type\x18\x08 \x01(\x0e\x32\x1e.pogoprotos.enums.GymBadgeType\x12\x33\n\x06\x62\x61\x64ges\x18\t \x03(\x0b\x32#.pogoprotos.data.player.PlayerBadge\x12\x12\n\nexperience\x18\n \x01(\x03\x12\x1a\n\x12has_shared_ex_pass\x18\x0b \x01(\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_player__avatar__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_player__badge__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_team__color__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_gym__badge__type__pb2.DESCRIPTOR,])




_PLAYERPUBLICPROFILE = _descriptor.Descriptor(
  name='PlayerPublicProfile',
  full_name='pogoprotos.data.player.PlayerPublicProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pogoprotos.data.player.PlayerPublicProfile.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='pogoprotos.data.player.PlayerPublicProfile.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='pogoprotos.data.player.PlayerPublicProfile.avatar', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team_color', full_name='pogoprotos.data.player.PlayerPublicProfile.team_color', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battles_won', full_name='pogoprotos.data.player.PlayerPublicProfile.battles_won', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='km_walked', full_name='pogoprotos.data.player.PlayerPublicProfile.km_walked', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caught_pokemon', full_name='pogoprotos.data.player.PlayerPublicProfile.caught_pokemon', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gym_badge_type', full_name='pogoprotos.data.player.PlayerPublicProfile.gym_badge_type', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='badges', full_name='pogoprotos.data.player.PlayerPublicProfile.badges', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experience', full_name='pogoprotos.data.player.PlayerPublicProfile.experience', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_shared_ex_pass', full_name='pogoprotos.data.player.PlayerPublicProfile.has_shared_ex_pass', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=240,
  serialized_end=614,
)

_PLAYERPUBLICPROFILE.fields_by_name['avatar'].message_type = pogoprotos_dot_data_dot_player_dot_player__avatar__pb2._PLAYERAVATAR
_PLAYERPUBLICPROFILE.fields_by_name['team_color'].enum_type = pogoprotos_dot_enums_dot_team__color__pb2._TEAMCOLOR
_PLAYERPUBLICPROFILE.fields_by_name['gym_badge_type'].enum_type = pogoprotos_dot_enums_dot_gym__badge__type__pb2._GYMBADGETYPE
_PLAYERPUBLICPROFILE.fields_by_name['badges'].message_type = pogoprotos_dot_data_dot_player_dot_player__badge__pb2._PLAYERBADGE
DESCRIPTOR.message_types_by_name['PlayerPublicProfile'] = _PLAYERPUBLICPROFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerPublicProfile = _reflection.GeneratedProtocolMessageType('PlayerPublicProfile', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERPUBLICPROFILE,
  __module__ = 'pogoprotos.data.player.player_public_profile_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.player.PlayerPublicProfile)
  ))
_sym_db.RegisterMessage(PlayerPublicProfile)


# @@protoc_insertion_point(module_scope)
