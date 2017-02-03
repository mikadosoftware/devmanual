#!/usr/bin/env python
#! -*- coding: utf-8 -*-

###
# Copyright (c) Rice University 2012-13
# This software is subject to
# the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
###


from splinter.browser import Browser
browser = Browser()
browser.visit('http://www.office.mikadosoftware.com')
browser.click_link_by_href('/login')
openidbox = browser.find_by_xpath('''id('column2')/form/p/input[1]''').first
openidbox.fill('https://www.google.com/accounts/o8/id')
browser.find_by_value('Sign in').first.click()
#id="Email"
#id="Passwd"
browser.find_by_id("Email").first.fill('paul@mikadosoftware.com') 
browser.find_by_id("Passwd").first.fill('empathy1') 
browser.find_by_value('Sign in').first.click()

browser.uncheck('remember_choices')
browser.find_by_value('Allow').first.click()
print browser.title
print 

for z in browser.cookies.driver.get_cookies():
    if z['domain'] == u'www.office.mikadosoftware.com' and z['name'] == u'session': 
        print z['value']

