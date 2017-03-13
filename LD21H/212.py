import random
print "<html>"
print "<pre>"
color = ["red","green", "blue"]
a = random.randrange(0,len(color))
x = color [a]
for i in range (0,11):
    b = i*i
    print ("<p><font size+\"3\" color=\"%s\">"%(x))
    print ("%d %d")% (i, b)
print "</pre>"
print "</html>"
