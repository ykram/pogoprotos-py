# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/combat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.combat import combat_player_pb2 as pogoprotos_dot_data_dot_combat_dot_combat__player__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/combat/combat.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_pb=_b('\n#pogoprotos/data/combat/combat.proto\x12\x16pogoprotos.data.combat\x1a*pogoprotos/data/combat/combat_player.proto\"\xed\x04\n\x06\x43ombat\x12@\n\x0c\x63ombat_state\x18\x01 \x01(\x0e\x32*.pogoprotos.data.combat.Combat.CombatState\x12\x11\n\tcombat_id\x18\x02 \x01(\t\x12\x34\n\x06player\x18\x03 \x01(\x0b\x32$.pogoprotos.data.combat.CombatPlayer\x12\x36\n\x08opponent\x18\x04 \x01(\x0b\x32$.pogoprotos.data.combat.CombatPlayer\x12\x17\n\x0f\x63ombat_start_ms\x18\x05 \x01(\x03\x12\x15\n\rcombat_end_ms\x18\x06 \x01(\x03\x12\x11\n\tserver_ms\x18\x07 \x01(\x03\x12\x14\n\x0c\x63urrent_turn\x18\x08 \x01(\x05\x12\x15\n\rturn_start_ms\x18\t \x01(\x03\x12\x17\n\x0fminigame_end_ms\x18\n \x01(\x03\x12$\n\x1cminigame_submit_score_end_ms\x18\x0b \x01(\x03\x12\x1d\n\x15\x63hange_pokemon_end_ms\x18\x0c \x01(\x03\x12\'\n\x1fquick_swap_cooldown_duration_ms\x18\r \x01(\x03\"\xa8\x01\n\x0b\x43ombatState\x12\t\n\x05UNSET\x10\x00\x12\x17\n\x13WAITING_FOR_PLAYERS\x10\x01\x12\t\n\x05READY\x10\x02\x12\n\n\x06\x41\x43TIVE\x10\x03\x12\x12\n\x0eSPECIAL_ATTACK\x10\x04\x12\x1e\n\x1aWAITING_FOR_CHANGE_POKEMON\x10\x05\x12\x0c\n\x08\x46INISHED\x10\x06\x12\x0f\n\x0bPLAYER_QUIT\x10\x07\x12\x0b\n\x07TIMEOUT\x10\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_combat_dot_combat__player__pb2.DESCRIPTOR,])



_COMBAT_COMBATSTATE = _descriptor.EnumDescriptor(
  name='CombatState',
  full_name='pogoprotos.data.combat.Combat.CombatState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAITING_FOR_PLAYERS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPECIAL_ATTACK', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAITING_FOR_CHANGE_POKEMON', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINISHED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_QUIT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=561,
  serialized_end=729,
)
_sym_db.RegisterEnumDescriptor(_COMBAT_COMBATSTATE)


_COMBAT = _descriptor.Descriptor(
  name='Combat',
  full_name='pogoprotos.data.combat.Combat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='combat_state', full_name='pogoprotos.data.combat.Combat.combat_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_id', full_name='pogoprotos.data.combat.Combat.combat_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player', full_name='pogoprotos.data.combat.Combat.player', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opponent', full_name='pogoprotos.data.combat.Combat.opponent', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_start_ms', full_name='pogoprotos.data.combat.Combat.combat_start_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_end_ms', full_name='pogoprotos.data.combat.Combat.combat_end_ms', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_ms', full_name='pogoprotos.data.combat.Combat.server_ms', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_turn', full_name='pogoprotos.data.combat.Combat.current_turn', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='turn_start_ms', full_name='pogoprotos.data.combat.Combat.turn_start_ms', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minigame_end_ms', full_name='pogoprotos.data.combat.Combat.minigame_end_ms', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minigame_submit_score_end_ms', full_name='pogoprotos.data.combat.Combat.minigame_submit_score_end_ms', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='change_pokemon_end_ms', full_name='pogoprotos.data.combat.Combat.change_pokemon_end_ms', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quick_swap_cooldown_duration_ms', full_name='pogoprotos.data.combat.Combat.quick_swap_cooldown_duration_ms', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMBAT_COMBATSTATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=729,
)

_COMBAT.fields_by_name['combat_state'].enum_type = _COMBAT_COMBATSTATE
_COMBAT.fields_by_name['player'].message_type = pogoprotos_dot_data_dot_combat_dot_combat__player__pb2._COMBATPLAYER
_COMBAT.fields_by_name['opponent'].message_type = pogoprotos_dot_data_dot_combat_dot_combat__player__pb2._COMBATPLAYER
_COMBAT_COMBATSTATE.containing_type = _COMBAT
DESCRIPTOR.message_types_by_name['Combat'] = _COMBAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Combat = _reflection.GeneratedProtocolMessageType('Combat', (_message.Message,), dict(
  DESCRIPTOR = _COMBAT,
  __module__ = 'pogoprotos.data.combat.combat_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.Combat)
  ))
_sym_db.RegisterMessage(Combat)


# @@protoc_insertion_point(module_scope)
