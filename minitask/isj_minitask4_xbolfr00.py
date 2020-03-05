# minitask 4 rene bolf xbolfr00@stud.fit.vutbr.cz
mcase = {'a':10, 'b': 34, 'A': 7, 'Z':3}
wanted = {'a': 17, 'b': 34, 'z': 3}
print({ k.lower() : mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()})
