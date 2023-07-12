#! /usr/bin/env python3

import cgi
import os
import sys
import io

form = cgi.FieldStorage()

if 'v1' in form:
    print("Content-Type: text/html;charset=utf8")
    print("")
    print(form['v1'].value)
else:
    print("Content-Type: text/html;charset=utf8")
    print("")
    print("<form method=post>")
    print("<input text name=v1 value=\"ABC\">")
    print("<input type=submit>")
    print("</form>")
