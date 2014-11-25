#!/usr/bin/python3
from sys import argv as a

open(a[-1],'w').write("P2\n"+"\n".join(([lambda j,s,d:s[0:3]+[j([str((int(x)&254)+int(y)%2)for x,y in zip(s[3:],d[3:])])],lambda j,s:s[0:2]+['1', j([str(int(x)%2) for x in s[3:]])]]['de'in a[1]])(" ".join,*[open(x).read().split()[1:]for x in a[2:-1]])))if 3<len(a)<6 and a[1]in["codage","decodage"]else"bad parameters"

