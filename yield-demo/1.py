def get_values():
    yield "hello"
    yield "world"
    yield 123
    return 42  # very uncommon to return something


for x in get_values():
    print(x)


print(list(get_values()))


gen = get_values()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))  # StopIteration
