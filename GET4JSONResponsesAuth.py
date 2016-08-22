#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    The MIT License (MIT)

    Copyright (c) 2016 sinfonier-project

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""


import basesinfonierbolt
import urllib2
import requests
import json
import ssl

class GET4JSONResponsesAuth (basesinfonierbolt.BaseSinfonierBolt):
      
    def __init__(self):
        basesinfonierbolt.BaseSinfonierBolt().__init__()
    
    def userprepare(self):
        # Load the URL to be requested
        self.url = self.getParam("url")
        # And the user / pass if entered
        self.user = self.getParam("username")
        self.password = self.getParam("password")
    
    def userprocess(self):
        try:
          if self.user:
            r = requests.get (self.url, verify=False, auth=HTTPBasicAuth(self.user, self.password) )
          else:
            r = requests.get (self.url, verify=False)
          
          data = json.loads(r.text)
          self.addField("json_response", data)
        
        except Exception, e:
          self.addField("error", "Error processing the request: " + str(e))
        
        self.emit()
    
    def userclose(self):
        pass


GET4JSONResponsesAuth().run()
