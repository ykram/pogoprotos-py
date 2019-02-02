# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/requests/add_login_action_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import identity_provider_pb2 as pogoprotos_dot_enums_dot_identity__provider__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/requests/add_login_action_message.proto',
  package='pogoprotos.networking.platform.requests',
  syntax='proto3',
  serialized_pb=_b('\nFpogoprotos/networking/platform/requests/add_login_action_message.proto\x12\'pogoprotos.networking.platform.requests\x1a(pogoprotos/enums/identity_provider.proto\"m\n\x15\x41\x64\x64LoginActionMessage\x12=\n\x11identity_provider\x18\x01 \x01(\x0e\x32\".pogoprotos.enums.IdentityProvider\x12\x15\n\rinner_message\x18\x02 \x01(\x0c\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_identity__provider__pb2.DESCRIPTOR,])




_ADDLOGINACTIONMESSAGE = _descriptor.Descriptor(
  name='AddLoginActionMessage',
  full_name='pogoprotos.networking.platform.requests.AddLoginActionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity_provider', full_name='pogoprotos.networking.platform.requests.AddLoginActionMessage.identity_provider', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inner_message', full_name='pogoprotos.networking.platform.requests.AddLoginActionMessage.inner_message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=157,
  serialized_end=266,
)

_ADDLOGINACTIONMESSAGE.fields_by_name['identity_provider'].enum_type = pogoprotos_dot_enums_dot_identity__provider__pb2._IDENTITYPROVIDER
DESCRIPTOR.message_types_by_name['AddLoginActionMessage'] = _ADDLOGINACTIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddLoginActionMessage = _reflection.GeneratedProtocolMessageType('AddLoginActionMessage', (_message.Message,), dict(
  DESCRIPTOR = _ADDLOGINACTIONMESSAGE,
  __module__ = 'pogoprotos.networking.platform.requests.add_login_action_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.requests.AddLoginActionMessage)
  ))
_sym_db.RegisterMessage(AddLoginActionMessage)


# @@protoc_insertion_point(module_scope)
