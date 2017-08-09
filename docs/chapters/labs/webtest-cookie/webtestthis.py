from webtest import TestApp

def header_from_cookiejar(cj):
    """
    ignoring domains etc for now
    """
    cookies = []
    
    for ck in cj:
        cookies.append("%s=%s" % (ck.name, ck.value))
        
    ident_header = {'COOKIE':';'.join(cookies)}
    return ident_header
        
        

from simpleapp import methodapp
fakeuuid = "00000000-0000-0000-0000-000000000000"

app = TestApp(methodapp, use_unicode=True)
ident_header = {'COOKIE':'cnxsessionid=%s' % fakeuuid}
app.cookies.update(ident_header)
#CookieJar.add_cookie_header
r = app.get("/")
print r

### get a new cookie header
cj = app.cookiejar
r = app.get("/", headers=header_from_cookiejar(cj))
print r


### get a new cookie header
cj = app.cookiejar
r = app.get("/", headers=header_from_cookiejar(cj))
print r


### get a new cookie header
cj = app.cookiejar
r = app.get("/", headers=header_from_cookiejar(cj))
print r


### get a new cookie header
cj = app.cookiejar
r = app.get("/", headers=header_from_cookiejar(cj))
print r






