/**
 * Autogenerated by Frugal Compiler (0.0.1)
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */



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




/**
 * This docstring gets added to the generated code because it has
 * the @ sign.
 */
@Generated(value = "Autogenerated by Frugal Compiler (0.0.1)", date = "2016-1-19")
public class EventsSubscriber {

	private static final String DELIMITER = ".";
	private static Logger LOGGER = Logger.getLogger(EventsSubscriber.class.getName());

	private final FScopeProvider provider;

	public EventsSubscriber(FScopeProvider provider) {
		this.provider = provider;
	}

	public interface EventCreatedHandler {
		void onEventCreated(FContext ctx, Event req);
	}

	/**
	 * This is a docstring.
	 */
	public FSubscription subscribeEventCreated(String user, final EventCreatedHandler handler) throws TException {
		final String op = "EventCreated";
		String prefix = String.format("foo.%s.", user);
		String topic = String.format("%sEvents%s%s", prefix, DELIMITER, op);
		final FScopeProvider.Client client = provider.build();
		FScopeTransport transport = client.getTransport();
		transport.subscribe(topic);

		final FSubscription sub = new FSubscription(topic, transport);
		new Thread(new Runnable() {
			public void run() {
				while (true) {
					try {
						FContext ctx = client.getProtocol().readRequestHeader();
						Event received = recvEventCreated(op, client.getProtocol());
						handler.onEventCreated(ctx, received);
					} catch (TException e) {
						if (e instanceof TTransportException) {
							TTransportException transportException = (TTransportException) e;
							if (transportException.getType() == TTransportException.END_OF_FILE) {
								return;
							}
						}
						LOGGER.severe("Subscriber recvEventCreated error " + e.getMessage());
						sub.signal(e);
						sub.unsubscribe();
						return;
					}
				}
			}
		}).start();

		return sub;
	}

	private Event recvEventCreated(String op, FProtocol iprot) throws TException {
		TMessage msg = iprot.readMessageBegin();
		if (!msg.name.equals(op)) {
			TProtocolUtil.skip(iprot, TType.STRUCT);
			iprot.readMessageEnd();
			throw new TApplicationException(TApplicationException.UNKNOWN_METHOD);
		}
		Event req = new Event();
		req.read(iprot);
		iprot.readMessageEnd();
		return req;
	}


}
