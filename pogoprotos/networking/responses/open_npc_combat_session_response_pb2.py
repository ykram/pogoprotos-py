# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/open_npc_combat_session_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.combat import combat_pb2 as pogoprotos_dot_data_dot_combat_dot_combat__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/open_npc_combat_session_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nFpogoprotos/networking/responses/open_npc_combat_session_response.proto\x12\x1fpogoprotos.networking.responses\x1a#pogoprotos/data/combat/combat.proto\"\xb6\x02\n\x1cOpenNpcCombatSessionResponse\x12T\n\x06result\x18\x01 \x01(\x0e\x32\x44.pogoprotos.networking.responses.OpenNpcCombatSessionResponse.Result\x12.\n\x06\x63ombat\x18\x02 \x01(\x0b\x32\x1e.pogoprotos.data.combat.Combat\"\x8f\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12$\n ERROR_PLAYER_BELOW_MINIMUM_LEVEL\x10\x02\x12.\n*ERROR_POKEMON_LINEUP_INELIGIBLE_FOR_LEAGUE\x10\x03\x12\x17\n\x13\x45RROR_ACCESS_DENIED\x10\x04\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_combat_dot_combat__pb2.DESCRIPTOR,])



_OPENNPCCOMBATSESSIONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.OpenNpcCombatSessionResponse.Result',
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
      name='ERROR_PLAYER_BELOW_MINIMUM_LEVEL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_LINEUP_INELIGIBLE_FOR_LEAGUE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ACCESS_DENIED', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=312,
  serialized_end=455,
)
_sym_db.RegisterEnumDescriptor(_OPENNPCCOMBATSESSIONRESPONSE_RESULT)


_OPENNPCCOMBATSESSIONRESPONSE = _descriptor.Descriptor(
  name='OpenNpcCombatSessionResponse',
  full_name='pogoprotos.networking.responses.OpenNpcCombatSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.OpenNpcCombatSessionResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat', full_name='pogoprotos.networking.responses.OpenNpcCombatSessionResponse.combat', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OPENNPCCOMBATSESSIONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=455,
)

_OPENNPCCOMBATSESSIONRESPONSE.fields_by_name['result'].enum_type = _OPENNPCCOMBATSESSIONRESPONSE_RESULT
_OPENNPCCOMBATSESSIONRESPONSE.fields_by_name['combat'].message_type = pogoprotos_dot_data_dot_combat_dot_combat__pb2._COMBAT
_OPENNPCCOMBATSESSIONRESPONSE_RESULT.containing_type = _OPENNPCCOMBATSESSIONRESPONSE
DESCRIPTOR.message_types_by_name['OpenNpcCombatSessionResponse'] = _OPENNPCCOMBATSESSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OpenNpcCombatSessionResponse = _reflection.GeneratedProtocolMessageType('OpenNpcCombatSessionResponse', (_message.Message,), dict(
  DESCRIPTOR = _OPENNPCCOMBATSESSIONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.open_npc_combat_session_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.OpenNpcCombatSessionResponse)
  ))
_sym_db.RegisterMessage(OpenNpcCombatSessionResponse)


# @@protoc_insertion_point(module_scope)
