#! -*- coding: utf-8 -*-

"""
A simple script to
login with requests and do otehr stuff


"""

import requests

session = requests.Session()
r = session.post('https://siamcenter.pathintelligence.com/accounts/login/'
                 , {  'username': 'noone'
                    , 'password': 'urhowmEic1'}
                )
print 'headers', r.headers
print 'cookies', requests.utils.dict_from_cookiejar(session.cookies)


testurl = 'https://siamcenter.pathintelligence.com/pdf_archive_list/'
testurl = 'https://siamcenter.pathintelligence.com/admin/'
r2 = session.get(testurl)
print r2.status_code