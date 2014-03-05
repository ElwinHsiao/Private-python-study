##from random import randint
##allNums = range(9)
##for eachNum in range(9): 
##    allNums.append(eachNum)
##print allNums
##print filter(lambda n: n%2, allNums)
##print [n for n in range(9) if n%2]

##print range(9)
##print map((lambda x: x+2), range(9))

##def foo(m):
##    print m,
##    def bar(n): 
##        print m + n 
##    return bar
##    return lambda n: m + n
##
##print foo(3)(4)
##
##b=foo(3)
##b(1);

##def counter(start_at=0):
##    count = start_at
##    def incr():
##        x = count
##        x += 1
##        return x
##    
##    return incr 
##
##print counter(1)()

##def foo(i, m=0):
##    x = m
##    print type(x),x, type(m)
##    def bar(n): 
##        y=1+x
##        return y;
##    return bar
##b=foo(3)
##b(1);


###!/usr/bin/env python
##
##output = '<int %r id=%#0x value=%d>'
##w = x = y = z = 1
##
##def f1():
##    x = y = z = 2
##
##    def f2():
##        y = z = 3
##
##        def f3():
##            z = 4
##            print output % ('w', id(w), w)
##            print output % ('x', id(x), x)
##            print output % ('y', id(y), y)
##            print output % ('z', id(z), z)
##
##        clo = f3.func_closure
##        if clo:
##            print "f3 closure vars:", [str(c) for c in clo]
##        else:
##            print "no f3 closure vars"
##        f3()
##
##    clo = f2.func_closure
##    if clo:
##        print "f2 closure vars:", [str(c) for c in clo]
##    else:
##        print "no f2 closure vars"
##    f2()
##
##clo = f1.func_closure
##if clo:
##    print "f1 closure vars:", [str(c) for c in clo]
##else:
##    print "no f1 closure vars"
##    
##f1()

###!/usr/bin/env python
##
##from time import time
##
##def logged(when):
##    def log(f, *args, **kargs):
##        print """Called:
##function: %s
##args: %r
##kargs: %r""" % (f, args, kargs)
##
##    def pre_logged(f):
##        def wrapper(*args, **kargs):
##            log(f, *args, **kargs)
##            return f(*args, **kargs)
##        return wrapper
##
##    def post_logged(f):
##        def wrapper(*args, **kargs):
##            now = time()
##            try:
##                return f(*args, **kargs)
##            finally:
##                log(f, *args, **kargs)
##                print "    time delta: %s" % (time()-now)
##        return wrapper
##
##    try:
##        return {"pre": pre_logged,
##		"post": post_logged}[when]
##    except KeyError, e:
##        raise ValueError(e), 'must be "pre" or "post"'
##
##@logged("post")
##def hello(name):
##    print "Hello,", name
##
##hello("World!")

##def bar(x):
##    if x==1:
##        return 1
##    else:
##        return 'a'
##def bar():
##    return ('abc', [4-2j, 'python'], "Guido")

#!/usr/bin/env python

from operator import add, sub, mul, div
from random import randint, choice

##ops = {'+': add, '-': sub, '*': mul, '/': div}
##MAXTRIES = 2
##
##def doprob():
####    op = choice('+-*/')
##    op = '-'
##    nums = [ randint(1,9) for i in range(2) ]
##    nums.sort(reverse=False)
##    nums[0] += 10;
##    ans = ops[op](*nums)
##    pr = '%d %s %s = ' % (nums[0], op, nums[1])
##    oops = 0
##    while True:
##        try:
##            if int(raw_input(pr)) == ans:
##                print 'correct'
##                break
##            if oops == MAXTRIES:
##                print 'sorry... the answer is\n%s%d' % (pr, ans)
##                break
##            else:
##                print 'incorrect... try again'
##                oops += 1
##        except (ValueError):
##            print 'invalid input... try again'
##
##def main():
##    while True:
##        try:
##            opt = raw_input('Again? [y] ').lower()
##            if opt and opt[0] == 'n':
##                break
##        except (KeyboardInterrupt, EOFError):
##            break
##        doprob()
##        try:
##            opt = raw_input('Again? [y] ').lower()
##            if opt and opt[0] == 'n':
##                break
##        except (KeyboardInterrupt, EOFError):
##            break

##if __name__ == '__main__':
##    main()

##def getlist():
##    for x in range(1,10):
##            for y in range(x+1,10):
##                    print x+10,y


##def wrapper(msg, msg2):
##    print 'in wrapper:', msg, msg2
##    def gener(f):
##        def outter(*args, **kargs):
##            "doc: outter"
##            print "in outter:", args, kargs
##            f(*args, **kargs);
##        return outter
##    return gener;
##
##@wrapper("ok", "2")
##def hello(msg, msg2, *args, **kargs):
##    "doc: outter"
##    print "in hello:", msg, msg2, args, kargs
##
##hello("World", "2", "3", key="value")

##def simpleGen():
##    yield 1
##    yield '2 --> punch!'

##def counter(start_at=0):
##    count = start_at
##    while True:
##        print 'before yield'
##        val = (yield count)
##        print 'after yield: count=', count, 'val=', val
##        if val is not None:
##            count = val
##        else:
##            count += 1

import sys
##print 'you entered', len(sys.argv), 'arguments...'
##print 'they were:', sys.argv
##print type(sys.argv)
try:
    f = open('blah', 'r')
except Exception, e:
    print e.filename, e.__str__()
##print sys.exc_info()
