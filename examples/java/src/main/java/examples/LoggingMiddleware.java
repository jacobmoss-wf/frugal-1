package examples;

import com.workiva.frugal.exception.FRateLimitException;
import com.workiva.frugal.middleware.InvocationHandler;
import com.workiva.frugal.middleware.ServiceMiddleware;

import java.lang.reflect.Method;

public class LoggingMiddleware implements ServiceMiddleware {

    @Override
    public <T> InvocationHandler<T> apply(T next) {
        return new InvocationHandler<T>(next) {
            @Override
            public Object invoke(Method method, Object receiver, Object[] args) throws Throwable {
                System.out.printf("==== CALLING %s.%s ====\n", method.getDeclaringClass().getName(), method.getName());
                if(method.getName() == "buyAlbum"){
                    throw new FRateLimitException("rate limit exceeded");
                }
                Object ret = method.invoke(receiver, args);
                System.out.printf("==== CALLED  %s.%s ====\n", method.getDeclaringClass().getName(), method.getName());
                return ret;
            }
        };
    }
}