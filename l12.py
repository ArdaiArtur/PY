#!/usr/bin/python
import cgi

form = cgi.FieldStorage()
name = form.getvalue("name")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Script</title>")
print("</head>")
print("<body>")
print("<h2>Hello, %s!</h2>" % name)
print("</body>")
print("</html>")