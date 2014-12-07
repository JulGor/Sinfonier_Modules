#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    The MIT License (MIT)

    Copyright (c) 2014 sinfonier-project

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

class CrackItWithAbusix(basesinfonierbolt.BaseSinfonierBolt):


    def __init__(self):
        basesinfonierbolt.BaseSinfonierBolt().__init__()

    def userprepare(self):
        pass

    def userprocess(self):
        hhash = self.getField("hash")
        self.removeField("hash")
        url = "http://api.leakdb.abusix.com/?j=%s" % (hhash)
        response = urllib2.urlopen(url)
        html = response.read()
        js= json.loads(html)
        
        if js["type"] == "plaintext":
            self.addField("error","The hash could not be cracked.")
        else:
            self.addField("value",js["hashes"][0]["plaintext"])

        self.emit()
               
CrackItWithAbusix().run()
