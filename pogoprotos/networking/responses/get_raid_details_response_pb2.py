# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_raid_details_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.raid import lobby_pb2 as pogoprotos_dot_data_dot_raid_dot_lobby__pb2
from pogoprotos.data.battle import battle_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__pb2
from pogoprotos.data.raid import raid_info_pb2 as pogoprotos_dot_data_dot_raid_dot_raid__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_raid_details_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n?pogoprotos/networking/responses/get_raid_details_response.proto\x12\x1fpogoprotos.networking.responses\x1a pogoprotos/data/raid/lobby.proto\x1a#pogoprotos/data/battle/battle.proto\x1a$pogoprotos/data/raid/raid_info.proto\"\x80\x05\n\x16GetRaidDetailsResponse\x12*\n\x05lobby\x18\x01 \x01(\x0b\x32\x1b.pogoprotos.data.raid.Lobby\x12\x33\n\x0braid_battle\x18\x02 \x01(\x0b\x32\x1e.pogoprotos.data.battle.Battle\x12\x1d\n\x15player_can_join_lobby\x18\x03 \x01(\x08\x12N\n\x06result\x18\x04 \x01(\x0e\x32>.pogoprotos.networking.responses.GetRaidDetailsResponse.Result\x12\x31\n\traid_info\x18\x05 \x01(\x0b\x32\x1e.pogoprotos.data.raid.RaidInfo\x12\x13\n\x0bticket_used\x18\x06 \x01(\x08\x12\x1d\n\x15\x66ree_ticket_available\x18\x07 \x01(\x08\x12\x18\n\x10throws_remaining\x18\x08 \x01(\x05\x12\x18\n\x10received_rewards\x18\t \x01(\x08\x12\x1c\n\x14num_players_in_lobby\x18\n \x01(\x05\x12\x11\n\tserver_ms\x18\x0b \x01(\x03\x12\x17\n\x0fserver_instance\x18\x0c \x01(\x05\"\xb0\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x02\x12\x18\n\x14\x45RROR_RAID_COMPLETED\x10\x03\x12\x1a\n\x16\x45RROR_RAID_UNAVAILABLE\x10\x04\x12$\n ERROR_PLAYER_BELOW_MINIMUM_LEVEL\x10\x05\x12\x1a\n\x16\x45RROR_POI_INACCESSIBLE\x10\x06\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_raid_dot_lobby__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_battle_dot_battle__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_raid_dot_raid__info__pb2.DESCRIPTOR,])



_GETRAIDDETAILSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.Result',
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
      name='ERROR_NOT_IN_RANGE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RAID_COMPLETED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RAID_UNAVAILABLE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_BELOW_MINIMUM_LEVEL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POI_INACCESSIBLE', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=674,
  serialized_end=850,
)
_sym_db.RegisterEnumDescriptor(_GETRAIDDETAILSRESPONSE_RESULT)


_GETRAIDDETAILSRESPONSE = _descriptor.Descriptor(
  name='GetRaidDetailsResponse',
  full_name='pogoprotos.networking.responses.GetRaidDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lobby', full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.lobby', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_battle', full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.raid_battle', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_can_join_lobby', full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.player_can_join_lobby', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.result', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_info', full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.raid_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ticket_used', full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.ticket_used', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='free_ticket_available', full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.free_ticket_available', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='throws_remaining', full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.throws_remaining', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='received_rewards', full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.received_rewards', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_players_in_lobby', full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.num_players_in_lobby', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_ms', full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.server_ms', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_instance', full_name='pogoprotos.networking.responses.GetRaidDetailsResponse.server_instance', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETRAIDDETAILSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=850,
)

_GETRAIDDETAILSRESPONSE.fields_by_name['lobby'].message_type = pogoprotos_dot_data_dot_raid_dot_lobby__pb2._LOBBY
_GETRAIDDETAILSRESPONSE.fields_by_name['raid_battle'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__pb2._BATTLE
_GETRAIDDETAILSRESPONSE.fields_by_name['result'].enum_type = _GETRAIDDETAILSRESPONSE_RESULT
_GETRAIDDETAILSRESPONSE.fields_by_name['raid_info'].message_type = pogoprotos_dot_data_dot_raid_dot_raid__info__pb2._RAIDINFO
_GETRAIDDETAILSRESPONSE_RESULT.containing_type = _GETRAIDDETAILSRESPONSE
DESCRIPTOR.message_types_by_name['GetRaidDetailsResponse'] = _GETRAIDDETAILSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRaidDetailsResponse = _reflection.GeneratedProtocolMessageType('GetRaidDetailsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETRAIDDETAILSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_raid_details_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetRaidDetailsResponse)
  ))
_sym_db.RegisterMessage(GetRaidDetailsResponse)


# @@protoc_insertion_point(module_scope)
