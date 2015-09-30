from sys import argv as a
print((lambda f,t,s,p:[f(-s,len(t)//p,t).rsplit('@',1)[0],f(s,p,t+'@#'+'#'*-((len(t)+2)%-p))]['e'==a[1]])(lambda s,k,t:"".join([chr(([(i-e+s)%y+e for(e,y)in[(48,10),(65,26),(97,26)]if e<=i<y+e]+[i])[0])for i in map(ord,sum(zip(*zip(*[iter(t)]*k)),()))]),' '.join(a[4:]),*map(int,a[2:4]))if 4<len(a)and''.join(a[2:4]).isdigit()*a[1]in'de'else'bad parameters')

