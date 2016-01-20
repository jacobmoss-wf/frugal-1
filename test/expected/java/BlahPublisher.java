/**
 * Autogenerated by Frugal Compiler (0.0.1)
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

package foo;

import com.workiva.frugal.FContext;
import com.workiva.frugal.FScopeProvider;
import com.workiva.frugal.FSubscription;
import com.workiva.frugal.FProtocol;
import com.workiva.frugal.transport.FScopeTransport;
import org.apache.thrift.TException;
import org.apache.thrift.TApplicationException;
import org.apache.thrift.transport.TTransportException;
import org.apache.thrift.protocol.*;

import javax.annotation.Generated;
import java.util.logging.Logger;




@Generated(value = "Autogenerated by Frugal Compiler (0.0.1)", date = "2015-11-24")
public class BlahPublisher {

	private static final String DELIMITER = ".";

	private final FScopeProvider provider;
	private FScopeTransport transport;
	private FProtocol protocol;

	public BlahPublisher(FScopeProvider provider) {
		this.provider = provider;
	}

	public void open() throws TException {
		FScopeProvider.Client client = provider.build();
		transport = client.getTransport();
		protocol = client.getProtocol();
		transport.open();
	}

	public void close() throws TException {
		transport.close();
	}

	public void publishDoStuff(FContext ctx, Thing req) throws TException {
		String op = "DoStuff";
		String prefix = "";
		String topic = String.format("%sBlah%s%s", prefix, DELIMITER, op);
		transport.lockTopic(topic);
		try {
			protocol.writeRequestHeader(ctx);
			protocol.writeMessageBegin(new TMessage(op, TMessageType.CALL, 0));
			req.write(protocol);
			protocol.writeMessageEnd();
			transport.flush();
		} catch (TException e) {
			close();
			throw e;
		} finally {
			transport.unlockTopic();
		}
	}
}
