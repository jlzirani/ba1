#!/usr/bin/python3
# implémente un démineur comme indiqué sur le pdf !
eval("({0}r,d,p:r({0}g:({0}x,y,a:({0}l:[[(a,g[z][w][1],g[z][w][2])if(z,w)in l and g[z][w][0]!=1 else g[z][w]for w in {1}0,9)]for z in {1}0,9)])([(x,y)]+[(z,w)for z in {1}x-1,x+2)for w in {1}y-1,y+2)if 0<=z<=9 and 0<=w<=9 and a<2 and(not g[x][y][1])and g[x][y][2]=='0']))(*([p(g),r({0}x:input('Indiquer une lettre :').upper(),{0}x:(len(x)==1)and(64<ord(x)<75),{0}x:ord(x)-65,'0'),r({0}x:input('Indiquer un nombre :'),{0}x:(len(x)==1)and(48<ord(x)<59),{0}x:ord(x)-49,'0'),r({0}x:input('Voulez-vous miner(M) ou mettre un drapeau(F) ? : ').upper(),{0}x:x in'MF'and(len(x)==1),{0}x:(x<'M')+1,'0')][1:])),{0}g:({2}1==x[0]and x[1],y)))for y in g])>0 or {2}(1==x[0]and not x[1])or(x[0]!=1 and x[1]),y)))for y in g])==81),{0}o:print('Vous avez '+['Gagne','Perdu'][{2}1==x[0]and x[1],y)))for y in o])>0]+' !'),[[(0,(x,y)in d.keys(),str(len([1 for(z,w)in [(z,w)for z in {1}x-1,x+2)for w in {1}y-1,y+2)if 0<=z<=9 and 0<=y<=9]if(z,w)in d.keys()])))for y in {1}0,9)]for x in {1}0,9)]))({0}f,t,o,d:(({0}r:r(r,f(d)))({0}r,v:o(v)if t(v)else r(r,f(v)))),{3},{0}g:print('    '+'   '.join(map(str,{1}1,10)))+'\\n  '+'-'*37+'\\n'+('\\n  '+'-'*37+'\\n').join([chr(x+65)+' | '+' | '.join(map({0}c:['*','B'if c[1]else c[2],'F'][c[0]],g[x]))+' | 'for x in {1}0,9)])+'\\n  '+'-'*37+'\\n'))".format("lambda ","range(","sum([len(list(filter(lambda x:","{(0,7):'B',(1,5):'B',(1,6):'B',(1,8):'B',(2,4):'B',(3,4):'B',(5,5):'B',(5,7):'B',(7,0):'B',(7,5):'B'}"))
# https://www.youtube.com/watch?v=1VDgOXVsosg
