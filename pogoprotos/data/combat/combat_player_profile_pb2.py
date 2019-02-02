# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/combat_player_profile.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import player_public_profile_pb2 as pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2
from pogoprotos.data import location_pb2 as pogoprotos_dot_data_dot_location__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/combat/combat_player_profile.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_pb=_b('\n2pogoprotos/data/combat/combat_player_profile.proto\x12\x16pogoprotos.data.combat\x1a\x32pogoprotos/data/player/player_public_profile.proto\x1a\x1epogoprotos/data/location.proto\"\xd7\x01\n\x13\x43ombatPlayerProfile\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x43\n\x0epublic_profile\x18\x02 \x01(\x0b\x32+.pogoprotos.data.player.PlayerPublicProfile\x12!\n\x19\x63ombat_league_template_id\x18\x03 \x03(\t\x12\x18\n\x10\x62uddy_pokemon_id\x18\x04 \x01(\x06\x12+\n\x08location\x18\x05 \x01(\x0b\x32\x19.pogoprotos.data.Locationb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_location__pb2.DESCRIPTOR,])




_COMBATPLAYERPROFILE = _descriptor.Descriptor(
  name='CombatPlayerProfile',
  full_name='pogoprotos.data.combat.CombatPlayerProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.data.combat.CombatPlayerProfile.player_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='public_profile', full_name='pogoprotos.data.combat.CombatPlayerProfile.public_profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_league_template_id', full_name='pogoprotos.data.combat.CombatPlayerProfile.combat_league_template_id', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buddy_pokemon_id', full_name='pogoprotos.data.combat.CombatPlayerProfile.buddy_pokemon_id', index=3,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='pogoprotos.data.combat.CombatPlayerProfile.location', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=163,
  serialized_end=378,
)

_COMBATPLAYERPROFILE.fields_by_name['public_profile'].message_type = pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2._PLAYERPUBLICPROFILE
_COMBATPLAYERPROFILE.fields_by_name['location'].message_type = pogoprotos_dot_data_dot_location__pb2._LOCATION
DESCRIPTOR.message_types_by_name['CombatPlayerProfile'] = _COMBATPLAYERPROFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatPlayerProfile = _reflection.GeneratedProtocolMessageType('CombatPlayerProfile', (_message.Message,), dict(
  DESCRIPTOR = _COMBATPLAYERPROFILE,
  __module__ = 'pogoprotos.data.combat.combat_player_profile_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.CombatPlayerProfile)
  ))
_sym_db.RegisterMessage(CombatPlayerProfile)


# @@protoc_insertion_point(module_scope)