#!/usr/bin/python3

def outterJoin(string, seq):
    return string + string.join(seq) + string

#cell = (a,b,c)
# a = 0 pas marqué, 1 marqué, 2 flag
# b = False pas de bomb, True bomb
# c = nombre de bombe adjacent

#One-liner version
(lambda r,d,p:r(lambda g:(lambda x,y,a:(lambda l:[[(a,g[z][w][1],g[z][w][2]) if(z,w)in l and g[z][w][0]!=1 else g[z][w] for w in range(0,9)] for z in range(0,9)])([(x,y)]+[(z,w) for z in range(x-1,x+2) for w in range(y-1,y+2) if 0<=z<=9 and 0<=w<=9 and a<2 and(not g[x][y][1])and g[x][y][2]=='0']))(*([p(g),r(lambda x:input('Indiquer une lettre :').upper(),lambda x:(len(x)==1)and(64<ord(x)<75),lambda x:ord(x)-65,'0'),r(lambda x:input('Indiquer un nombre :'),lambda x:(len(x)==1)and(48<ord(x)<59),lambda x:ord(x)-49,'0'),r(lambda x:input('Voulez-vous miner(M) ou mettre un drapeau(F) ? : ').upper(),lambda x:x in'MF'and(len(x)==1),lambda x:(x<'M')+1,'0')][1:])),lambda g:(sum([len(list(filter(lambda x:1==x[0]and x[1],y))) for y in g])>0 or sum([len(list(filter(lambda x:(1==x[0]and not x[1])or(x[0]!=1 and x[1]),y)))for y in g])==81), lambda o:print("Vous avez "+["Gagne","Perdu"][sum([len(list(filter(lambda x:1==x[0]and x[1],y))) for y in o])>0]+" !"),[[(0,(x,y)in d.keys(),str(len([1 for(z,w)in [(z,w) for z in range(x-1,x+2) for w in range(y-1,y+2) if 0<=z<=9 and 0<=y<=9]if(z,w)in d.keys()])))for y in range(0,9)]for x in range(0,9)]))(lambda f,t,o,d:((lambda r:r(r,f(d)))(lambda r,v:o(v)if t(v)else r(r,f(v)))),{(0,7):"B",(1,5):"B",(1,6):"B",(1,8):"B",(2,4):"B",(3,4):"B",(5,5):"B",(5,7):"B",(7,0):"B",(7,5):"B"},lambda g:print("    "+"   ".join(map(str,range(1,10)))+outterJoin("\n  "+'-'*37+'\n', [chr(x+65)+outterJoin(" | ",map(lambda c:['*','B'if c[1]else c[2],'F'][c[0]],g[x]))for x in range(0,9)])))



