import string
import random
import uuid
import selenium

rand = uuid.uuid1()
link = 'fyii.de/trashmail/?.html'
email = '?@fyii.de'
ident = ('e'+str(rand))
emailadr = (email.replace("?", (ident))
print '(emailadr)'
emaillnk = (link.replace("?", (ident))
print '(emaillnk)'
