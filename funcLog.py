#!/usr/bin/env python

from time import time

def logged(when):
    def log(func, *args, **kargs):
        print """Called:
function: %s
args: %r
kargs: %r""" % (func, args, kargs)

    def pre_logged(f):
        def wrapper(*args, **kargs):
            print "---------pre----------->"
            log(f, *args, **kargs)
            try:
                return f(*args, **kargs)
            finally:
                print "<========pre========="
        return wrapper

    def post_logged(f):
        def wrapper(*args, **kargs):
            print "---------post----------->"
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                log(f, *args, **kargs)
                print "    time delta: %s" % (time()-now)
                print "<========post========="
        return wrapper
    def pre2(f):
        print ">>>>>>>pre2>>>>>>>>"
        log(f, *args, **kargs)
        return f(*args, **kargs)
    try:
        return {"pre": pre_logged,
		"post": post_logged}[when]
    except KeyError, e:
        raise ValueError(e), 'must be "pre" or "post"'

@logged("pre")
def hello(name):
    print "   in hello(): Hello,", name

hello("World!")
