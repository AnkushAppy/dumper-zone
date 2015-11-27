import time

print 'Set-Cookie: lastvisit=' + str(time.time())
print 'Content-Type: text/html\n'
print '<html><body>'
print'Server time is',time.asctime(time.localtime())
print '</body></html>'

