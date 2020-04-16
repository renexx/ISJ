#!/usr/bin/env python3

def first_with_given_key(iterable, key=lambda x: x):
    seen = set()
    it = iter(iterable) #get an iterator object
    while True:
        try:
            item = next(it) #get next item
            if key(item) not in seen:
                yield item
                seen.add(key(item))
        except StopIteration: # no more items
            break

print(tuple(first_with_given_key([[1],[2,3],[4],[5,6,7],[8,9]], key = len)))
