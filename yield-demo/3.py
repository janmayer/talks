import collections


def worker(f):
    tasks = collections.deque()
    value = None
    while True:
        batch = yield value
        value = None
        if batch is not None:
            tasks.extend(batch)
        if tasks:
            args = tasks.popleft()
            value = f(*args)


w = worker(str)
print("-A-")
w.send(None) # here, first thing to send must be None

print("-B-")
print(w.send([(1,), (2,), (3,)]))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))

print("-C-")
w.send([(4,), (5,)])
print(next(w))

print("-D-")
# send() will also iterate - so it actually includes a next() call.
print(w.send([(6,), (7,)]))
print(next(w))
print(next(w))

#w.throw(ValueError)

#w.close()
#print(next(w))