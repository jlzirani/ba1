#!/usr/bin/python3
from random import randint
(lambda r,t,l:r(lambda p:(lambda n,m:p[0:2]+[m]if m<0 else(lambda x,t:(lambda y:[p[0],x,0])(print((t+' !\nVous avez %i euro dans votre poche\n')%x)))(*([p[1]+2*m,'Gagne']if r(lambda x:input('Veuillez indiquer le gobelet ou vous pensez que le jeton s\'y trouve (G pour celui de Gauche, M pour celui du Milieu et D pour celui de Droit): '),lambda x:x in l,lambda x:x,0)==l[randint(0,2)]else[p[1]-m,'Perdu'])))(print('* '*3),r(lambda x:input('Veuillez indiquer votre mise (ou -1 pour quitter le jeu) : '),lambda x:(x.isdigit()or'-1'==x)and int(x)<=p[1],lambda x:int(x),0)),lambda x:x[1]<=0 or x[2]<0,lambda x:print(t+' FIN '+t+'\n\nVous avez %i euro dans votre poche,\nVous avez %s %i euro'%(x[1],['perdu','gagne'][x[1]>x[0]],abs(x[0]-x[1]))),r(lambda x:input('Veuillez indiquer la quantite d\'argent que vous possedez : '),lambda x:x.isdigit()and int(x)>0,lambda x:([int(x)]*2)+[0],'a')))(lambda f,t,o,d:((lambda r: r(r,f(d)))(lambda r,v:o(v)if t(v)else r(r,f(v)))),'-'*8,list('GMD'))

