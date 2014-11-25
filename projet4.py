#!/usr/bin/python3


encode = lambda *s:[[(x&254)+(y&1)for x,y in w]for w in map(zip,*s)]  
decode = lambda s:[[x&1 for x in y]for y in s]


