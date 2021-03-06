# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ipython.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ipython.proto',
  package='ipython',
  syntax='proto3',
  serialized_pb=_b('\n\ripython.proto\x12\x07ipython\"\x1e\n\x0e\x45xecuteRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"l\n\x0f\x45xecuteResponse\x12&\n\x06status\x18\x01 \x01(\x0e\x32\x16.ipython.ExecuteStatus\x12!\n\x04type\x18\x02 \x01(\x0e\x32\x13.ipython.OutputType\x12\x0e\n\x06output\x18\x03 \x01(\t\"\x0f\n\rCancelRequest\"\x10\n\x0e\x43\x61ncelResponse\"1\n\x11\x43ompletionRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0e\n\x06\x63ursor\x18\x02 \x01(\x05\"%\n\x12\x43ompletionResponse\x12\x0f\n\x07matches\x18\x01 \x03(\t\"\x0f\n\rStatusRequest\"8\n\x0eStatusResponse\x12&\n\x06status\x18\x01 \x01(\x0e\x32\x16.ipython.IPythonStatus\"\r\n\x0bStopRequest\"\x0e\n\x0cStopResponse*\'\n\rExecuteStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01**\n\rIPythonStatus\x12\x0c\n\x08STARTING\x10\x00\x12\x0b\n\x07RUNNING\x10\x01*!\n\nOutputType\x12\x08\n\x04TEXT\x10\x00\x12\t\n\x05IMAGE\x10\x01\x32\xc3\x02\n\x07IPython\x12@\n\x07\x65xecute\x12\x17.ipython.ExecuteRequest\x1a\x18.ipython.ExecuteResponse\"\x00\x30\x01\x12\x45\n\x08\x63omplete\x12\x1a.ipython.CompletionRequest\x1a\x1b.ipython.CompletionResponse\"\x00\x12;\n\x06\x63\x61ncel\x12\x16.ipython.CancelRequest\x1a\x17.ipython.CancelResponse\"\x00\x12;\n\x06status\x12\x16.ipython.StatusRequest\x1a\x17.ipython.StatusResponse\"\x00\x12\x35\n\x04stop\x12\x14.ipython.StopRequest\x1a\x15.ipython.StopResponse\"\x00\x42<\n org.apache.zeppelin.python.protoB\x0cIPythonProtoP\x01\xa2\x02\x07IPythonb\x06proto3')
)

_EXECUTESTATUS = _descriptor.EnumDescriptor(
  name='ExecuteStatus',
  full_name='ipython.ExecuteStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=399,
  serialized_end=438,
)
_sym_db.RegisterEnumDescriptor(_EXECUTESTATUS)

ExecuteStatus = enum_type_wrapper.EnumTypeWrapper(_EXECUTESTATUS)
_IPYTHONSTATUS = _descriptor.EnumDescriptor(
  name='IPythonStatus',
  full_name='ipython.IPythonStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STARTING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=440,
  serialized_end=482,
)
_sym_db.RegisterEnumDescriptor(_IPYTHONSTATUS)

IPythonStatus = enum_type_wrapper.EnumTypeWrapper(_IPYTHONSTATUS)
_OUTPUTTYPE = _descriptor.EnumDescriptor(
  name='OutputType',
  full_name='ipython.OutputType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=484,
  serialized_end=517,
)
_sym_db.RegisterEnumDescriptor(_OUTPUTTYPE)

OutputType = enum_type_wrapper.EnumTypeWrapper(_OUTPUTTYPE)
SUCCESS = 0
ERROR = 1
STARTING = 0
RUNNING = 1
TEXT = 0
IMAGE = 1



_EXECUTEREQUEST = _descriptor.Descriptor(
  name='ExecuteRequest',
  full_name='ipython.ExecuteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='ipython.ExecuteRequest.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=26,
  serialized_end=56,
)


_EXECUTERESPONSE = _descriptor.Descriptor(
  name='ExecuteResponse',
  full_name='ipython.ExecuteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ipython.ExecuteResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='ipython.ExecuteResponse.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output', full_name='ipython.ExecuteResponse.output', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=58,
  serialized_end=166,
)


_CANCELREQUEST = _descriptor.Descriptor(
  name='CancelRequest',
  full_name='ipython.CancelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=168,
  serialized_end=183,
)


_CANCELRESPONSE = _descriptor.Descriptor(
  name='CancelResponse',
  full_name='ipython.CancelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=185,
  serialized_end=201,
)


_COMPLETIONREQUEST = _descriptor.Descriptor(
  name='CompletionRequest',
  full_name='ipython.CompletionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='ipython.CompletionRequest.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='ipython.CompletionRequest.cursor', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=203,
  serialized_end=252,
)


_COMPLETIONRESPONSE = _descriptor.Descriptor(
  name='CompletionResponse',
  full_name='ipython.CompletionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='matches', full_name='ipython.CompletionResponse.matches', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=254,
  serialized_end=291,
)


_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='ipython.StatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=293,
  serialized_end=308,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='ipython.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ipython.StatusResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=310,
  serialized_end=366,
)


_STOPREQUEST = _descriptor.Descriptor(
  name='StopRequest',
  full_name='ipython.StopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=368,
  serialized_end=381,
)


_STOPRESPONSE = _descriptor.Descriptor(
  name='StopResponse',
  full_name='ipython.StopResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=383,
  serialized_end=397,
)

_EXECUTERESPONSE.fields_by_name['status'].enum_type = _EXECUTESTATUS
_EXECUTERESPONSE.fields_by_name['type'].enum_type = _OUTPUTTYPE
_STATUSRESPONSE.fields_by_name['status'].enum_type = _IPYTHONSTATUS
DESCRIPTOR.message_types_by_name['ExecuteRequest'] = _EXECUTEREQUEST
DESCRIPTOR.message_types_by_name['ExecuteResponse'] = _EXECUTERESPONSE
DESCRIPTOR.message_types_by_name['CancelRequest'] = _CANCELREQUEST
DESCRIPTOR.message_types_by_name['CancelResponse'] = _CANCELRESPONSE
DESCRIPTOR.message_types_by_name['CompletionRequest'] = _COMPLETIONREQUEST
DESCRIPTOR.message_types_by_name['CompletionResponse'] = _COMPLETIONRESPONSE
DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.message_types_by_name['StopRequest'] = _STOPREQUEST
DESCRIPTOR.message_types_by_name['StopResponse'] = _STOPRESPONSE
DESCRIPTOR.enum_types_by_name['ExecuteStatus'] = _EXECUTESTATUS
DESCRIPTOR.enum_types_by_name['IPythonStatus'] = _IPYTHONSTATUS
DESCRIPTOR.enum_types_by_name['OutputType'] = _OUTPUTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecuteRequest = _reflection.GeneratedProtocolMessageType('ExecuteRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTEREQUEST,
  __module__ = 'ipython_pb2'
  # @@protoc_insertion_point(class_scope:ipython.ExecuteRequest)
  ))
_sym_db.RegisterMessage(ExecuteRequest)

ExecuteResponse = _reflection.GeneratedProtocolMessageType('ExecuteResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTERESPONSE,
  __module__ = 'ipython_pb2'
  # @@protoc_insertion_point(class_scope:ipython.ExecuteResponse)
  ))
_sym_db.RegisterMessage(ExecuteResponse)

CancelRequest = _reflection.GeneratedProtocolMessageType('CancelRequest', (_message.Message,), dict(
  DESCRIPTOR = _CANCELREQUEST,
  __module__ = 'ipython_pb2'
  # @@protoc_insertion_point(class_scope:ipython.CancelRequest)
  ))
_sym_db.RegisterMessage(CancelRequest)

CancelResponse = _reflection.GeneratedProtocolMessageType('CancelResponse', (_message.Message,), dict(
  DESCRIPTOR = _CANCELRESPONSE,
  __module__ = 'ipython_pb2'
  # @@protoc_insertion_point(class_scope:ipython.CancelResponse)
  ))
_sym_db.RegisterMessage(CancelResponse)

CompletionRequest = _reflection.GeneratedProtocolMessageType('CompletionRequest', (_message.Message,), dict(
  DESCRIPTOR = _COMPLETIONREQUEST,
  __module__ = 'ipython_pb2'
  # @@protoc_insertion_point(class_scope:ipython.CompletionRequest)
  ))
_sym_db.RegisterMessage(CompletionRequest)

CompletionResponse = _reflection.GeneratedProtocolMessageType('CompletionResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMPLETIONRESPONSE,
  __module__ = 'ipython_pb2'
  # @@protoc_insertion_point(class_scope:ipython.CompletionResponse)
  ))
_sym_db.RegisterMessage(CompletionResponse)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _STATUSREQUEST,
  __module__ = 'ipython_pb2'
  # @@protoc_insertion_point(class_scope:ipython.StatusRequest)
  ))
_sym_db.RegisterMessage(StatusRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _STATUSRESPONSE,
  __module__ = 'ipython_pb2'
  # @@protoc_insertion_point(class_scope:ipython.StatusResponse)
  ))
_sym_db.RegisterMessage(StatusResponse)

StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), dict(
  DESCRIPTOR = _STOPREQUEST,
  __module__ = 'ipython_pb2'
  # @@protoc_insertion_point(class_scope:ipython.StopRequest)
  ))
_sym_db.RegisterMessage(StopRequest)

StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), dict(
  DESCRIPTOR = _STOPRESPONSE,
  __module__ = 'ipython_pb2'
  # @@protoc_insertion_point(class_scope:ipython.StopResponse)
  ))
_sym_db.RegisterMessage(StopResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n org.apache.zeppelin.python.protoB\014IPythonProtoP\001\242\002\007IPython'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class IPythonStub(object):
    """The IPython service definition.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.execute = channel.unary_stream(
          '/ipython.IPython/execute',
          request_serializer=ExecuteRequest.SerializeToString,
          response_deserializer=ExecuteResponse.FromString,
          )
      self.complete = channel.unary_unary(
          '/ipython.IPython/complete',
          request_serializer=CompletionRequest.SerializeToString,
          response_deserializer=CompletionResponse.FromString,
          )
      self.cancel = channel.unary_unary(
          '/ipython.IPython/cancel',
          request_serializer=CancelRequest.SerializeToString,
          response_deserializer=CancelResponse.FromString,
          )
      self.status = channel.unary_unary(
          '/ipython.IPython/status',
          request_serializer=StatusRequest.SerializeToString,
          response_deserializer=StatusResponse.FromString,
          )
      self.stop = channel.unary_unary(
          '/ipython.IPython/stop',
          request_serializer=StopRequest.SerializeToString,
          response_deserializer=StopResponse.FromString,
          )


  class IPythonServicer(object):
    """The IPython service definition.
    """

    def execute(self, request, context):
      """Sends code
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def complete(self, request, context):
      """Get completion
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def cancel(self, request, context):
      """Cancel the running statement
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def status(self, request, context):
      """Get ipython kernel status
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def stop(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_IPythonServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'execute': grpc.unary_stream_rpc_method_handler(
            servicer.execute,
            request_deserializer=ExecuteRequest.FromString,
            response_serializer=ExecuteResponse.SerializeToString,
        ),
        'complete': grpc.unary_unary_rpc_method_handler(
            servicer.complete,
            request_deserializer=CompletionRequest.FromString,
            response_serializer=CompletionResponse.SerializeToString,
        ),
        'cancel': grpc.unary_unary_rpc_method_handler(
            servicer.cancel,
            request_deserializer=CancelRequest.FromString,
            response_serializer=CancelResponse.SerializeToString,
        ),
        'status': grpc.unary_unary_rpc_method_handler(
            servicer.status,
            request_deserializer=StatusRequest.FromString,
            response_serializer=StatusResponse.SerializeToString,
        ),
        'stop': grpc.unary_unary_rpc_method_handler(
            servicer.stop,
            request_deserializer=StopRequest.FromString,
            response_serializer=StopResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ipython.IPython', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaIPythonServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """The IPython service definition.
    """
    def execute(self, request, context):
      """Sends code
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def complete(self, request, context):
      """Get completion
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def cancel(self, request, context):
      """Cancel the running statement
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def status(self, request, context):
      """Get ipython kernel status
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def stop(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaIPythonStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """The IPython service definition.
    """
    def execute(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Sends code
      """
      raise NotImplementedError()
    def complete(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Get completion
      """
      raise NotImplementedError()
    complete.future = None
    def cancel(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Cancel the running statement
      """
      raise NotImplementedError()
    cancel.future = None
    def status(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Get ipython kernel status
      """
      raise NotImplementedError()
    status.future = None
    def stop(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    stop.future = None


  def beta_create_IPython_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('ipython.IPython', 'cancel'): CancelRequest.FromString,
      ('ipython.IPython', 'complete'): CompletionRequest.FromString,
      ('ipython.IPython', 'execute'): ExecuteRequest.FromString,
      ('ipython.IPython', 'status'): StatusRequest.FromString,
      ('ipython.IPython', 'stop'): StopRequest.FromString,
    }
    response_serializers = {
      ('ipython.IPython', 'cancel'): CancelResponse.SerializeToString,
      ('ipython.IPython', 'complete'): CompletionResponse.SerializeToString,
      ('ipython.IPython', 'execute'): ExecuteResponse.SerializeToString,
      ('ipython.IPython', 'status'): StatusResponse.SerializeToString,
      ('ipython.IPython', 'stop'): StopResponse.SerializeToString,
    }
    method_implementations = {
      ('ipython.IPython', 'cancel'): face_utilities.unary_unary_inline(servicer.cancel),
      ('ipython.IPython', 'complete'): face_utilities.unary_unary_inline(servicer.complete),
      ('ipython.IPython', 'execute'): face_utilities.unary_stream_inline(servicer.execute),
      ('ipython.IPython', 'status'): face_utilities.unary_unary_inline(servicer.status),
      ('ipython.IPython', 'stop'): face_utilities.unary_unary_inline(servicer.stop),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_IPython_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('ipython.IPython', 'cancel'): CancelRequest.SerializeToString,
      ('ipython.IPython', 'complete'): CompletionRequest.SerializeToString,
      ('ipython.IPython', 'execute'): ExecuteRequest.SerializeToString,
      ('ipython.IPython', 'status'): StatusRequest.SerializeToString,
      ('ipython.IPython', 'stop'): StopRequest.SerializeToString,
    }
    response_deserializers = {
      ('ipython.IPython', 'cancel'): CancelResponse.FromString,
      ('ipython.IPython', 'complete'): CompletionResponse.FromString,
      ('ipython.IPython', 'execute'): ExecuteResponse.FromString,
      ('ipython.IPython', 'status'): StatusResponse.FromString,
      ('ipython.IPython', 'stop'): StopResponse.FromString,
    }
    cardinalities = {
      'cancel': cardinality.Cardinality.UNARY_UNARY,
      'complete': cardinality.Cardinality.UNARY_UNARY,
      'execute': cardinality.Cardinality.UNARY_STREAM,
      'status': cardinality.Cardinality.UNARY_UNARY,
      'stop': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'ipython.IPython', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
