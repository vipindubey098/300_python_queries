import urllib.request

site = urllib.request.urlopen("https://www.google.co.in")
code = site.getcode()
print(code)