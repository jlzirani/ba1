#!/usr/bin/python3
from sys import argv as a

open(a[-1],'w').write(["P2\n"+"\n".join((([lambda j,s,d:[print("Fichier source : "+a[2]+"\nFicher code : "+a[3]+"\nFichier destination : "+a[4]),s[0:3]+[j([str((int(x)&254)+int(y)%2)for x,y in zip(s[3:],d[3:])])]],lambda j,s:[print("Fichier contenant le message : "+a[2]+"\nFichier message decode : "+a[3]),s[0:2]+['1',j([str(int(x)%2)for x in s[3:]])]]]['de'in a[1]])(" ".join,*[open(x).read().split()[1:]for x in a[2:-1]]))[1]),print("Travil termine !")][0])if 3<len(a)<6 and a[1]in["codage","decodage"]else print("bad parameters")

