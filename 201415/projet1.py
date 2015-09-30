#!/usr/bin/python3
from random import randint
eval("({0}r,l,i,e,c:r({0}p:({0}n,m:p[0:2]+[m]if m<0 else({0}x,t:({0}y:[p[0],x,0])(e((t+' !{3}{4}\\n')%x)))(*([p[1]+2*m,'Gagne']if r({0}x:c('{2}le gobelet ou vous pensez que le jeton s\\'y trouve (G pour celui de Gauche, M pour celui du Milieu et D pour celui de Droit): '),{0}x:x in l,{0}x:x,0)==l[randint(0,2)]else[p[1]-m,'Perdu'])))(e('* '*3),r({0}x:c('{2}votre mise (ou -1 pour quitter le jeu) : '),{0}x:(x.isdigit()or'-1'==x)and i(x)<=p[1],i,0)),{0}x:x[1]<=0 or x[2]<0,{0}x:e('{1} FIN {1}\\n{3}{4},{3}%s %i euro'%(x[1],['perdu','gagne'][x[1]>x[0]],abs(x[0]-x[1]))),[r({0}x:c('{2}la quantite d\\'argent que vous possedez : '),{0}x:x.isdigit()and i(x)>0,i,'')]*2+[0]))({0}f,t,o,d:(({0}r:r(r,f(d)))({0}r,v:o(v)if t(v)else r(r,f(v)))),list('GMD'),int,print,input)".format('lambda ','-'*8,'Veuillez indiquer ','\\nVous avez ','%i euro dans votre poche'))


