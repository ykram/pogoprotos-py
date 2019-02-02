# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/quest/daily_quest_settings.proto

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
  name='pogoprotos/settings/master/quest/daily_quest_settings.proto',
  package='pogoprotos.settings.master.quest',
  syntax='proto3',
  serialized_pb=_b('\n;pogoprotos/settings/master/quest/daily_quest_settings.proto\x12 pogoprotos.settings.master.quest\"\x7f\n\x12\x44\x61ilyQuestSettings\x12\x17\n\x0f\x62uckets_per_day\x18\x01 \x01(\x05\x12\x15\n\rstreak_length\x18\x02 \x01(\x05\x12\x18\n\x10\x62onus_multiplier\x18\x03 \x01(\x02\x12\x1f\n\x17streak_bonus_multiplier\x18\x04 \x01(\x02\x62\x06proto3')
)




_DAILYQUESTSETTINGS = _descriptor.Descriptor(
  name='DailyQuestSettings',
  full_name='pogoprotos.settings.master.quest.DailyQuestSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buckets_per_day', full_name='pogoprotos.settings.master.quest.DailyQuestSettings.buckets_per_day', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='streak_length', full_name='pogoprotos.settings.master.quest.DailyQuestSettings.streak_length', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bonus_multiplier', full_name='pogoprotos.settings.master.quest.DailyQuestSettings.bonus_multiplier', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='streak_bonus_multiplier', full_name='pogoprotos.settings.master.quest.DailyQuestSettings.streak_bonus_multiplier', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=97,
  serialized_end=224,
)

DESCRIPTOR.message_types_by_name['DailyQuestSettings'] = _DAILYQUESTSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyQuestSettings = _reflection.GeneratedProtocolMessageType('DailyQuestSettings', (_message.Message,), dict(
  DESCRIPTOR = _DAILYQUESTSETTINGS,
  __module__ = 'pogoprotos.settings.master.quest.daily_quest_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.quest.DailyQuestSettings)
  ))
_sym_db.RegisterMessage(DailyQuestSettings)


# @@protoc_insertion_point(module_scope)
