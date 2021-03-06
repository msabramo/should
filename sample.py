#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should import it


class RangeError(Exception):
    pass

def fib(n):
    if not isinstance(n, int):
        raise ValueError(str(n) + ' is not int')
    if n < 0 or n > 40:
        raise RangeError(str(n) + 'out of range: 0~40')
    pre = 1
    cur = 0
    for i in xrange(n):
        pre, cur = cur, pre+cur
    return cur

it(fib(0)).should.be.equal(0)
it(fib(1)).should.be.equal(1)
it(fib(10)).should.be.equal(55)


it(lambda: fib(-1)).should.throw(RangeError)
it(lambda: fib(41)).should.throw(RangeError)
it(lambda: fib('string')).should.throw(ValueError)

