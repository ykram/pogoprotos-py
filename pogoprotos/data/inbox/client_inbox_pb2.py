# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/inbox/client_inbox.proto

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
  name='pogoprotos/data/inbox/client_inbox.proto',
  package='pogoprotos.data.inbox',
  syntax='proto3',
  serialized_pb=_b('\n(pogoprotos/data/inbox/client_inbox.proto\x12\x15pogoprotos.data.inbox\"\xe0\x04\n\x0b\x43lientInbox\x12\x46\n\rnotifications\x18\x01 \x03(\x0b\x32/.pogoprotos.data.inbox.ClientInbox.Notification\x12N\n\x11\x62uiltin_variables\x18\x02 \x03(\x0b\x32\x33.pogoprotos.data.inbox.ClientInbox.TemplateVariable\x1a\xce\x02\n\x0cNotification\x12\x17\n\x0fnotification_id\x18\x01 \x01(\t\x12\x11\n\ttitle_key\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x1b\n\x13\x63reate_timestamp_ms\x18\x04 \x01(\x03\x12\x46\n\tvariables\x18\x05 \x03(\x0b\x32\x33.pogoprotos.data.inbox.ClientInbox.TemplateVariable\x12\x45\n\x06labels\x18\x06 \x03(\x0e\x32\x35.pogoprotos.data.inbox.ClientInbox.Notification.Label\x12\x16\n\x0e\x65xpire_time_ms\x18\x07 \x01(\x03\"<\n\x05Label\x12\x0f\n\x0bUNSET_LABEL\x10\x00\x12\n\n\x06UNREAD\x10\x01\x12\x07\n\x03NEW\x10\x02\x12\r\n\tIMMEDIATE\x10\x03\x1ah\n\x10TemplateVariable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07literal\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x14\n\x0clookup_table\x18\x04 \x01(\t\x12\x12\n\nbyte_value\x18\x05 \x01(\x0c\x62\x06proto3')
)



_CLIENTINBOX_NOTIFICATION_LABEL = _descriptor.EnumDescriptor(
  name='Label',
  full_name='pogoprotos.data.inbox.ClientInbox.Notification.Label',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_LABEL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREAD', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMMEDIATE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=510,
  serialized_end=570,
)
_sym_db.RegisterEnumDescriptor(_CLIENTINBOX_NOTIFICATION_LABEL)


_CLIENTINBOX_NOTIFICATION = _descriptor.Descriptor(
  name='Notification',
  full_name='pogoprotos.data.inbox.ClientInbox.Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification_id', full_name='pogoprotos.data.inbox.ClientInbox.Notification.notification_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title_key', full_name='pogoprotos.data.inbox.ClientInbox.Notification.title_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='pogoprotos.data.inbox.ClientInbox.Notification.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_timestamp_ms', full_name='pogoprotos.data.inbox.ClientInbox.Notification.create_timestamp_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variables', full_name='pogoprotos.data.inbox.ClientInbox.Notification.variables', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labels', full_name='pogoprotos.data.inbox.ClientInbox.Notification.labels', index=5,
      number=6, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expire_time_ms', full_name='pogoprotos.data.inbox.ClientInbox.Notification.expire_time_ms', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTINBOX_NOTIFICATION_LABEL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=570,
)

_CLIENTINBOX_TEMPLATEVARIABLE = _descriptor.Descriptor(
  name='TemplateVariable',
  full_name='pogoprotos.data.inbox.ClientInbox.TemplateVariable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pogoprotos.data.inbox.ClientInbox.TemplateVariable.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='literal', full_name='pogoprotos.data.inbox.ClientInbox.TemplateVariable.literal', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='pogoprotos.data.inbox.ClientInbox.TemplateVariable.key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lookup_table', full_name='pogoprotos.data.inbox.ClientInbox.TemplateVariable.lookup_table', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='byte_value', full_name='pogoprotos.data.inbox.ClientInbox.TemplateVariable.byte_value', index=4,
      number=5, type=12, cpp_type=9, label=1,
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
  serialized_start=572,
  serialized_end=676,
)

_CLIENTINBOX = _descriptor.Descriptor(
  name='ClientInbox',
  full_name='pogoprotos.data.inbox.ClientInbox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notifications', full_name='pogoprotos.data.inbox.ClientInbox.notifications', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='builtin_variables', full_name='pogoprotos.data.inbox.ClientInbox.builtin_variables', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CLIENTINBOX_NOTIFICATION, _CLIENTINBOX_TEMPLATEVARIABLE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=676,
)

_CLIENTINBOX_NOTIFICATION.fields_by_name['variables'].message_type = _CLIENTINBOX_TEMPLATEVARIABLE
_CLIENTINBOX_NOTIFICATION.fields_by_name['labels'].enum_type = _CLIENTINBOX_NOTIFICATION_LABEL
_CLIENTINBOX_NOTIFICATION.containing_type = _CLIENTINBOX
_CLIENTINBOX_NOTIFICATION_LABEL.containing_type = _CLIENTINBOX_NOTIFICATION
_CLIENTINBOX_TEMPLATEVARIABLE.containing_type = _CLIENTINBOX
_CLIENTINBOX.fields_by_name['notifications'].message_type = _CLIENTINBOX_NOTIFICATION
_CLIENTINBOX.fields_by_name['builtin_variables'].message_type = _CLIENTINBOX_TEMPLATEVARIABLE
DESCRIPTOR.message_types_by_name['ClientInbox'] = _CLIENTINBOX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientInbox = _reflection.GeneratedProtocolMessageType('ClientInbox', (_message.Message,), dict(

  Notification = _reflection.GeneratedProtocolMessageType('Notification', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTINBOX_NOTIFICATION,
    __module__ = 'pogoprotos.data.inbox.client_inbox_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.inbox.ClientInbox.Notification)
    ))
  ,

  TemplateVariable = _reflection.GeneratedProtocolMessageType('TemplateVariable', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTINBOX_TEMPLATEVARIABLE,
    __module__ = 'pogoprotos.data.inbox.client_inbox_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.inbox.ClientInbox.TemplateVariable)
    ))
  ,
  DESCRIPTOR = _CLIENTINBOX,
  __module__ = 'pogoprotos.data.inbox.client_inbox_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.inbox.ClientInbox)
  ))
_sym_db.RegisterMessage(ClientInbox)
_sym_db.RegisterMessage(ClientInbox.Notification)
_sym_db.RegisterMessage(ClientInbox.TemplateVariable)


# @@protoc_insertion_point(module_scope)
