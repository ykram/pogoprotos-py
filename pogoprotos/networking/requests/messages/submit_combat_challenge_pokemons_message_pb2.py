# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/submit_combat_challenge_pokemons_message.proto

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
  name='pogoprotos/networking/requests/messages/submit_combat_challenge_pokemons_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nVpogoprotos/networking/requests/messages/submit_combat_challenge_pokemons_message.proto\x12\'pogoprotos.networking.requests.messages\"Z\n$SubmitCombatChallengePokemonsMessage\x12\x14\n\x0c\x63hallenge_id\x18\x01 \x01(\t\x12\x1c\n\x14\x61ttacking_pokemon_id\x18\x02 \x03(\x06\x62\x06proto3')
)




_SUBMITCOMBATCHALLENGEPOKEMONSMESSAGE = _descriptor.Descriptor(
  name='SubmitCombatChallengePokemonsMessage',
  full_name='pogoprotos.networking.requests.messages.SubmitCombatChallengePokemonsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge_id', full_name='pogoprotos.networking.requests.messages.SubmitCombatChallengePokemonsMessage.challenge_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attacking_pokemon_id', full_name='pogoprotos.networking.requests.messages.SubmitCombatChallengePokemonsMessage.attacking_pokemon_id', index=1,
      number=2, type=6, cpp_type=4, label=3,
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
  serialized_start=131,
  serialized_end=221,
)

DESCRIPTOR.message_types_by_name['SubmitCombatChallengePokemonsMessage'] = _SUBMITCOMBATCHALLENGEPOKEMONSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitCombatChallengePokemonsMessage = _reflection.GeneratedProtocolMessageType('SubmitCombatChallengePokemonsMessage', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITCOMBATCHALLENGEPOKEMONSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.submit_combat_challenge_pokemons_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.SubmitCombatChallengePokemonsMessage)
  ))
_sym_db.RegisterMessage(SubmitCombatChallengePokemonsMessage)


# @@protoc_insertion_point(module_scope)
