# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/sfida/sfida_nearby_pokemon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_display_pb2 as pogoprotos_dot_data_dot_pokemon__display__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/sfida/sfida_nearby_pokemon.proto',
  package='pogoprotos.data.sfida',
  syntax='proto3',
  serialized_pb=_b('\n0pogoprotos/data/sfida/sfida_nearby_pokemon.proto\x12\x15pogoprotos.data.sfida\x1a%pogoprotos/data/pokemon_display.proto\"x\n\x12SfidaNearbyPokemon\x12\x16\n\x0epokedex_number\x18\x01 \x01(\x05\x12\x10\n\x08uncaught\x18\x02 \x01(\x08\x12\x38\n\x0fpokemon_display\x18\x03 \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplayb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__display__pb2.DESCRIPTOR,])




_SFIDANEARBYPOKEMON = _descriptor.Descriptor(
  name='SfidaNearbyPokemon',
  full_name='pogoprotos.data.sfida.SfidaNearbyPokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokedex_number', full_name='pogoprotos.data.sfida.SfidaNearbyPokemon.pokedex_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uncaught', full_name='pogoprotos.data.sfida.SfidaNearbyPokemon.uncaught', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_display', full_name='pogoprotos.data.sfida.SfidaNearbyPokemon.pokemon_display', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=114,
  serialized_end=234,
)

_SFIDANEARBYPOKEMON.fields_by_name['pokemon_display'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
DESCRIPTOR.message_types_by_name['SfidaNearbyPokemon'] = _SFIDANEARBYPOKEMON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SfidaNearbyPokemon = _reflection.GeneratedProtocolMessageType('SfidaNearbyPokemon', (_message.Message,), dict(
  DESCRIPTOR = _SFIDANEARBYPOKEMON,
  __module__ = 'pogoprotos.data.sfida.sfida_nearby_pokemon_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.sfida.SfidaNearbyPokemon)
  ))
_sym_db.RegisterMessage(SfidaNearbyPokemon)


# @@protoc_insertion_point(module_scope)
