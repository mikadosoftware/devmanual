import datetime
import webtest
import Cookie

class classapp(object):
    """
    Stolen from PEP333
    NB - same applies here - we are returning an instance of a class that
    is an iterable - we do not return the class)

    This is not middleware -> this is not - it is an app that expects to be
    backend
    
    """
    def __init__(self):
        print "init class"

    def __call__(self, environ, start_response):
        print "called call"
        if environ.get('repoze.who.identity') is None:
            start_response("401 ", [])
            return ''
        else:
            usr = environ.get("REMOTE_USER")
            s = "You are %s" % usr
            s += "<br/>".join(["%s:%s" % (k, environ.get(k))
                               for k in sorted(environ)])
            start_response("200 OK", [('Content-type', 'text/html')])
            return s
        # pi = environ.get("PATH_INFO")
        # if pi.startswith("/login"):
        #     start_response("200 OK", [('Content-type', 'text/plain')])
        #     return ['This is a form to login']
        # else:
        #     status = "200 OK"
        #     response_headers = [('Content-type', 'text/plain'),
        #                         ('X-paul','pbrian')]
        #     start_response(status, response_headers)
        #     return [":Hello:"]
        


CNXSESSIONID = "cnxsessionid"
            
def capture_session(env):
    """
    >>> env = {"HTTP_COOKIE": "cnxsessionid=00000000",}
    >>> capture_session(env)
    '00000000'

    >>> env = {"HTTP_COOKIE": "name=value",}
    >>> capture_session(env) is None
    True
    
    >>> env = {"foobar": "wibble",}
    >>> capture_session(env) is None
    True

    """
    
    if "HTTP_COOKIE" in env:
        cookiestr = env.get("HTTP_COOKIE")        
    else:
        return None

    cookieset = Cookie.BaseCookie(cookiestr)
    
    if CNXSESSIONID in cookieset.keys():
        sessid = cookieset[CNXSESSIONID].value
    else:
        return None

    return sessid

def lookup_session(sessid):
    """
    We would expect this to be redis-style cache in production
    """
    onehour = datetime.timedelta(hours=1)
    developercache = {"00000000-0000-0000-0000-000000000000":
                       {'name': 'Paul',
                        'useruri':'/users/00000000-0000-0000-0000-000000000000',
                        'starttimeUTC': datetime.datetime.utcnow(),
                        'starttimeUTC': datetime.datetime.utcnow()+onehour}
                      }
    try:
        return developercache[sessid]
    except:
        return None
        #in reality here we might want to try the redis chace or contact user server
        
    
def methodapp(environ, start_response):
    sessid = capture_session(environ)
    userd = lookup_session(sessid)
    if userd:
        userstr = "You are user %s" % userd['name']
    else:
        userstr = "Dont know user"
        
    s = userstr + "</br>".join(["%s::%s" % (k,v) for k, v in environ.items()])
    status = "200 OK"
    respstr =  s

    import random
    i = random.randint(0,9)
    response_headers = [('Content-type', 'text/html'),
                        ('Content-length', str(len(respstr))),
                        ('Set-Cookie', "cnxsessionid=00000000-0000-0000-0000-00000000000%s" % i)
                         ]

    start_response(status, response_headers)
    return (str(respstr),)


    


if __name__ == '__main__':
    import doctest
    doctest.testmod()