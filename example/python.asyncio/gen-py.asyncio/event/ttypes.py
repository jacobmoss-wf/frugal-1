#
# Autogenerated by Frugal Compiler (1.16.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import base.ttypes

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol


class Event:
    """
    This docstring gets added to the generated code because it has
    the @ sign.
    
    Attributes:
     - ID: ID is a unique identifier for an event.
     - Message: Message contains the event payload.
    """
    _DEFAULT_ID_MARKER = -1
    def __init__(self, ID=_DEFAULT_ID_MARKER, Message=None):
        self.ID = ID
        self.Message = Message

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.ID = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.Message = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('Event')
        if self.ID is not None:
            oprot.writeFieldBegin('ID', TType.I64, 1)
            oprot.writeI64(self.ID)
            oprot.writeFieldEnd()
        if self.Message is not None:
            oprot.writeFieldBegin('Message', TType.STRING, 2)
            oprot.writeString(self.Message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.ID)
        value = (value * 31) ^ hash(self.Message)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class AwesomeException(TException):
    """
    Attributes:
     - ID: ID is a unique identifier for an awesome exception.
     - Reason: Reason contains the error message.
    """
    def __init__(self, ID=None, Reason=None):
        self.ID = ID
        self.Reason = Reason

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.ID = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.Reason = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('AwesomeException')
        if self.ID is not None:
            oprot.writeFieldBegin('ID', TType.I64, 1)
            oprot.writeI64(self.ID)
            oprot.writeFieldEnd()
        if self.Reason is not None:
            oprot.writeFieldBegin('Reason', TType.STRING, 2)
            oprot.writeString(self.Reason)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.ID)
        value = (value * 31) ^ hash(self.Reason)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

