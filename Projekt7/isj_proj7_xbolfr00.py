#!/usr/bin/env python3
import collections
my_counter = collections.Counter()

def log_and_count(key=None, counts = my_counter):
    def decorator(original_func):
        def wrap_func(*args, **kwargs):
            if key is None:
                counts[original_func.__name__] +=1
            else:
                counts["basic function"] += 1
            print("called {} with {} and {}".format(original_func.__name__,args,kwargs))
            return original_func(*args,**kwargs)
        return wrap_func
    return decorator


@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
    """ test na f1
    >>>f1(2)
    'called f1 with (2,) and {}'
    >>> f1(a=2, b=4)
    'called f1 with () and {'a': 2, 'b': 4}'
    """
    return a ** b

@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
    """ test na f1
    >>>f2(2, b=4)
    'called f2 with (2,) and {'b': 4}'
    >>> f2(4)
    'called f2 with (4,) and {}'
    >>> f2(5)
    'called f2 with (5,) and {}'
    """
    return a ** 2 + b

@log_and_count(counts = my_counter)
def f3(a, b=5):
    """ test na f1
    >>>f3(5)
    'called f3 with (5,) and {}'
    >>> f3(5,4)
    'called f3 with (5, 4) and {}'
    
    """
    return a ** 3 - b
if __name__ == "__main__":
    import doctest
    doctest.testmod()
