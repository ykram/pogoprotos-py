# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/combat_stat_stage_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/combat_stat_stage_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n;pogoprotos/settings/master/combat_stat_stage_settings.proto\x12\x1apogoprotos.settings.master\"\x92\x01\n\x17\x43ombatStatStageSettings\x12\x1a\n\x12minimum_stat_stage\x18\x01 \x01(\x05\x12\x1a\n\x12maximum_stat_stage\x18\x02 \x01(\x05\x12\x1e\n\x16\x61ttack_buff_multiplier\x18\x03 \x03(\x02\x12\x1f\n\x17\x64\x65\x66\x65nse_buff_multiplier\x18\x04 \x03(\x02\x62\x06proto3')
)




_COMBATSTATSTAGESETTINGS = _descriptor.Descriptor(
  name='CombatStatStageSettings',
  full_name='pogoprotos.settings.master.CombatStatStageSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minimum_stat_stage', full_name='pogoprotos.settings.master.CombatStatStageSettings.minimum_stat_stage', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum_stat_stage', full_name='pogoprotos.settings.master.CombatStatStageSettings.maximum_stat_stage', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attack_buff_multiplier', full_name='pogoprotos.settings.master.CombatStatStageSettings.attack_buff_multiplier', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defense_buff_multiplier', full_name='pogoprotos.settings.master.CombatStatStageSettings.defense_buff_multiplier', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=92,
  serialized_end=238,
)

DESCRIPTOR.message_types_by_name['CombatStatStageSettings'] = _COMBATSTATSTAGESETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatStatStageSettings = _reflection.GeneratedProtocolMessageType('CombatStatStageSettings', (_message.Message,), dict(
  DESCRIPTOR = _COMBATSTATSTAGESETTINGS,
  __module__ = 'pogoprotos.settings.master.combat_stat_stage_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.CombatStatStageSettings)
  ))
_sym_db.RegisterMessage(CombatStatStageSettings)


# @@protoc_insertion_point(module_scope)
