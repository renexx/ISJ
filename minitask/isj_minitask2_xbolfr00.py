import re
# minitask 1.3
#Rene Bolf xbolfr00@vutbr.cz
# change the last du to DU
pattern = re.compile(r'du(?!.*du)') #negative lookahead
text = ['du du du', 'du po ledu', 'dopředu du', 'i dozadu du', 'dudu dupl']
for row in text:
     print(re.sub(pattern, 'DU', row))
