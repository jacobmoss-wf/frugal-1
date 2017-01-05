#
# Autogenerated by Frugal Compiler (2.0.0-RC5)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#



from threading import Lock

from frugal.middleware import Method
from frugal.exceptions import FApplicationException, FMessageSizeException
from frugal.processor import FBaseProcessor
from frugal.processor import FProcessorFunction
from thrift.Thrift import TApplicationException
from thrift.Thrift import TMessageType

from .ttypes import *


class Iface(object):
    """
    Services are the API for client and server interaction.
    Users can buy an album or enter a giveaway for a free album.
    """

    def buyAlbum(self, ctx, ASIN, acct):
        """
        Args:
            ctx: FContext
            ASIN: string
            acct: string
        """
        pass

    def enterAlbumGiveaway(self, ctx, email, name):
        """
        Args:
            ctx: FContext
            email: string
            name: string
        """
        pass


class Client(Iface):

    def __init__(self, provider, middleware=None):
        """
        Create a new Client with an FServiceProvider containing a transport
        and protocol factory.

        Args:
            provider: FServiceProvider with FSynchronousTransport
            middleware: ServiceMiddleware or list of ServiceMiddleware
        """
        middleware = middleware or []
        if middleware and not isinstance(middleware, list):
            middleware = [middleware]
        self._transport = provider.get_transport()
        self._protocol_factory = provider.get_protocol_factory()
        self._oprot = self._protocol_factory.get_protocol(self._transport)
        self._iprot = self._protocol_factory.get_protocol(self._transport)
        self._write_lock = Lock()
        middleware += provider.get_middleware()
        self._methods = {
            'buyAlbum': Method(self._buyAlbum, middleware),
            'enterAlbumGiveaway': Method(self._enterAlbumGiveaway, middleware),
        }

    def buyAlbum(self, ctx, ASIN, acct):
        """
        Args:
            ctx: FContext
            ASIN: string
            acct: string
        """
        return self._methods['buyAlbum']([ctx, ASIN, acct])

    def _buyAlbum(self, ctx, ASIN, acct):
        self._send_buyAlbum(ctx, ASIN, acct)
        return self._recv_buyAlbum(ctx)

    def _send_buyAlbum(self, ctx, ASIN, acct):
        oprot = self._oprot
        with self._write_lock:
            oprot.get_transport().set_timeout(ctx.timeout)
            oprot.write_request_headers(ctx)
            oprot.writeMessageBegin('buyAlbum', TMessageType.CALL, 0)
            args = buyAlbum_args()
            args.ASIN = ASIN
            args.acct = acct
            args.write(oprot)
            oprot.writeMessageEnd()
            oprot.get_transport().flush()

    def _recv_buyAlbum(self, ctx):
        self._iprot.read_response_headers(ctx)
        _, mtype, _ = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            if x.type == FApplicationException.RESPONSE_TOO_LARGE:
                raise FMessageSizeException.response(x.message)
            raise x
        result = buyAlbum_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.error is not None:
            raise result.error
        if result.success is not None:
            return result.success
        x = TApplicationException(TApplicationException.MISSING_RESULT, "buyAlbum failed: unknown result")
        raise x

    def enterAlbumGiveaway(self, ctx, email, name):
        """
        Args:
            ctx: FContext
            email: string
            name: string
        """
        return self._methods['enterAlbumGiveaway']([ctx, email, name])

    def _enterAlbumGiveaway(self, ctx, email, name):
        self._send_enterAlbumGiveaway(ctx, email, name)
        return self._recv_enterAlbumGiveaway(ctx)

    def _send_enterAlbumGiveaway(self, ctx, email, name):
        oprot = self._oprot
        with self._write_lock:
            oprot.get_transport().set_timeout(ctx.timeout)
            oprot.write_request_headers(ctx)
            oprot.writeMessageBegin('enterAlbumGiveaway', TMessageType.CALL, 0)
            args = enterAlbumGiveaway_args()
            args.email = email
            args.name = name
            args.write(oprot)
            oprot.writeMessageEnd()
            oprot.get_transport().flush()

    def _recv_enterAlbumGiveaway(self, ctx):
        self._iprot.read_response_headers(ctx)
        _, mtype, _ = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            if x.type == FApplicationException.RESPONSE_TOO_LARGE:
                raise FMessageSizeException.response(x.message)
            raise x
        result = enterAlbumGiveaway_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        x = TApplicationException(TApplicationException.MISSING_RESULT, "enterAlbumGiveaway failed: unknown result")
        raise x

class Processor(FBaseProcessor):

    def __init__(self, handler, middleware=None):
        """
        Create a new Processor.

        Args:
            handler: Iface
        """
        if middleware and not isinstance(middleware, list):
            middleware = [middleware]

        super(Processor, self).__init__()
        self.add_to_processor_map('buyAlbum', _buyAlbum(Method(handler.buyAlbum, middleware), self.get_write_lock()))
        self.add_to_annotations_map('buyAlbum', {'auth': 'false'})
        self.add_to_processor_map('enterAlbumGiveaway', _enterAlbumGiveaway(Method(handler.enterAlbumGiveaway, middleware), self.get_write_lock()))
        self.add_to_annotations_map('enterAlbumGiveaway', {'foo': 'bar'})


class _buyAlbum(FProcessorFunction):

    def __init__(self, handler, lock):
        super(_buyAlbum, self).__init__(handler, lock)

    def process(self, ctx, iprot, oprot):
        args = buyAlbum_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = buyAlbum_result()
        try:
            result.success = self._handler([ctx, args.ASIN, args.acct])
        except PurchasingError as error:
            result.error = error
        except TApplicationException as ex:
            with self._lock:
                _write_application_exception(ctx, oprot, "buyAlbum", exception=ex)
                return
        except Exception as e:
            with self._lock:
                e = _write_application_exception(ctx, oprot, "buyAlbum", ex_code=TApplicationException.UNKNOWN, message=e.message)
            raise e
        with self._lock:
            try:
                oprot.write_response_headers(ctx)
                oprot.writeMessageBegin('buyAlbum', TMessageType.REPLY, 0)
                result.write(oprot)
                oprot.writeMessageEnd()
                oprot.get_transport().flush()
            except FMessageSizeException as e:
                raise _write_application_exception(ctx, oprot, "buyAlbum", ex_code=FApplicationException.RESPONSE_TOO_LARGE, message=e.args[0])


class _enterAlbumGiveaway(FProcessorFunction):

    def __init__(self, handler, lock):
        super(_enterAlbumGiveaway, self).__init__(handler, lock)

    def process(self, ctx, iprot, oprot):
        args = enterAlbumGiveaway_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = enterAlbumGiveaway_result()
        try:
            result.success = self._handler([ctx, args.email, args.name])
        except TApplicationException as ex:
            with self._lock:
                _write_application_exception(ctx, oprot, "enterAlbumGiveaway", exception=ex)
                return
        except Exception as e:
            with self._lock:
                e = _write_application_exception(ctx, oprot, "enterAlbumGiveaway", ex_code=TApplicationException.UNKNOWN, message=e.message)
            raise e
        with self._lock:
            try:
                oprot.write_response_headers(ctx)
                oprot.writeMessageBegin('enterAlbumGiveaway', TMessageType.REPLY, 0)
                result.write(oprot)
                oprot.writeMessageEnd()
                oprot.get_transport().flush()
            except FMessageSizeException as e:
                raise _write_application_exception(ctx, oprot, "enterAlbumGiveaway", ex_code=FApplicationException.RESPONSE_TOO_LARGE, message=e.args[0])


def _write_application_exception(ctx, oprot, method, ex_code=None, message=None, exception=None):
    if exception is not None:
        x = exception
    else:
        x = TApplicationException(type=ex_code, message=message)
    oprot.write_response_headers(ctx)
    oprot.writeMessageBegin(method, TMessageType.EXCEPTION, 0)
    x.write(oprot)
    oprot.writeMessageEnd()
    oprot.get_transport().flush()
    return x

class buyAlbum_args(object):
    """
    Attributes:
     - ASIN
     - acct
    """
    def __init__(self, ASIN=None, acct=None):
        self.ASIN = ASIN
        self.acct = acct

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.ASIN = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.acct = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('buyAlbum_args')
        if self.ASIN is not None:
            oprot.writeFieldBegin('ASIN', TType.STRING, 1)
            oprot.writeString(self.ASIN)
            oprot.writeFieldEnd()
        if self.acct is not None:
            oprot.writeFieldBegin('acct', TType.STRING, 2)
            oprot.writeString(self.acct)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.ASIN)
        value = (value * 31) ^ hash(self.acct)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class buyAlbum_result(object):
    """
    Attributes:
     - success
     - error
    """
    def __init__(self, success=None, error=None):
        self.success = success
        self.error = error

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Album()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.error = PurchasingError()
                    self.error.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('buyAlbum_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.error is not None:
            oprot.writeFieldBegin('error', TType.STRUCT, 1)
            self.error.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.success)
        value = (value * 31) ^ hash(self.error)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class enterAlbumGiveaway_args(object):
    """
    Attributes:
     - email
     - name
    """
    def __init__(self, email=None, name=None):
        self.email = email
        self.name = name

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.email = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('enterAlbumGiveaway_args')
        if self.email is not None:
            oprot.writeFieldBegin('email', TType.STRING, 1)
            oprot.writeString(self.email)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.email)
        value = (value * 31) ^ hash(self.name)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class enterAlbumGiveaway_result(object):
    """
    Attributes:
     - success
    """
    def __init__(self, success=None):
        self.success = success

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.BOOL:
                    self.success = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('enterAlbumGiveaway_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.BOOL, 0)
            oprot.writeBool(self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.success)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

