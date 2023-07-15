#! /usr/bin/env python3

import cgi
import os
import sys
import io

class CL:

    @classmethod
    def top(cls):
        print("Content-Type: text/html;charset=utf8")
        print("")
        print("<form method=post>")
        print("<input text name=v1 value=\"ABC\">")
        print("<input type=submit>")
        print("</form>")

    @classmethod
    def view(cls):
        print("Content-Type: text/html;charset=utf8")
        print("")
        print('[' + GLOBAL_CGI_PARAMS['v1'].value + ']')

    @classmethod
    def env(cls):
        print('<hr>');
        iii = 0
        for name in os.environ:
            print('[' + name + '][' + os.environ[name] + ']',end='<br>')
            iii += 1 ;

    @classmethod
    def entry(self):
        if 'v1' in GLOBAL_CGI_PARAMS:
            self.view()
            self.env()
        else:
            self.top()
            self.env()

    @classmethod
    def aaa(x):
        print("Content-Type: text/html;charset=utf8")
        print("")
        print('TEST') ;


GLOBAL_CGI_PARAMS = cgi.FieldStorage()

cl = CL()
cl.entry()







