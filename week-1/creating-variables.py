print 'Hello World!'

#int
i = 4
print type(i)
print i

#float
f = 4.23
print type(f)
print f

#bool
b = True
print type(b)
print b

#str
s = "This is a string."
print type(s)
print s

#list
lst = [3, 2, 1]
print type(lst)
print lst

#dict
d = {'foo':1, 'bar':2.3, 's':'my first dictionary'}
print type(d)
print d
print d['foo']

#None - same as null in Java
n = None
print type(n)
print n

#printing variables in strings
print "Our float value is %s, and our int value is %s." % (f, i)
