# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x13\x66unction_as_service\"-\n\x0f\x46unctionRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\"\"\n\x10\x46unctionResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2q\n\x0f\x46unctionService\x12^\n\x0f\x45xecuteFunction\x12$.function_as_service.FunctionRequest\x1a%.function_as_service.FunctionResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_FUNCTIONREQUEST']._serialized_start=38
  _globals['_FUNCTIONREQUEST']._serialized_end=83
  _globals['_FUNCTIONRESPONSE']._serialized_start=85
  _globals['_FUNCTIONRESPONSE']._serialized_end=119
  _globals['_FUNCTIONSERVICE']._serialized_start=121
  _globals['_FUNCTIONSERVICE']._serialized_end=234
# @@protoc_insertion_point(module_scope)
