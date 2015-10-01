#!/usr/bin/python3

#Version de rom1


#(lambda r,p:(p("Gaston arrive au bureau.",0),(lambda w,t:(p("Fin du service, dure journée",540),print("Temps total travaillé: %d h %02d min"%(w//60,w%60))))(*(lambda l:l(l,0,0))(lambda l,w,t:l(l,*(lambda w,t,x:(lambda w,x,t:(lambda t,w:(w-t+540,t)if t>=540else(p("Prunelle est parti. \\O/",t)or w,t))(p("Il faut travailler. M'enfin.",t)or x+150,w+x+150-t)if t<540else(w,t))(w,x,(lambda x,c,t:(lambda f,*a:f(f,*a))(lambda f,c,t:f(p("C'est bon, encore le temps de faire une sieste. Zzz",t)or f,c-2,t+20)if c>1else t,c,t)if c<5else p("OK, pause !",t)or t+50)(x,p("Attention, Prunelle arrive à %02d:%02d"%(10+x//60,x%60),x)or(x+59-t)//10,t))if x+60<540and 1==r(1,3)else(w,t))(p("OK, pause !",t)or w,t+50,t+r(0,50)))if t<540else(w,540)))))((lambda m:m.seed(int("0"+"".join(filter(str.isdigit,input("Entrez une seed: ")))))or m.randint)(__import__("random")),lambda s,t:print("%02d:%02d\t%s"%(9+t//60,t%60,s)))
#Version de JL

(lambda l,r=__import__("random"),f=lambda t,o=9,p="%02d:%02d\t":p%(o+t//60,t%60),p=print,t=540:r.seed(int(l(lambda _:input("Entrez une seed: "),str.isdigit)))or(p(f(l(lambda b,d=r.randint:((b[0]+20,b[1]-20,b[2],p(f(b[0])+"C'est bon, encore le temps de faire une sieste. Zzz"))if 20<=b[1]<50else(lambda m,s=b[0]+b[1]+90:(m(s,t),-1,b[2]+m(s,t)-b[0],p(f(b[0])+"Il faut travailler. M'enfin."+("\n%sPrunelle est parti. \\O/"%f(s)if t>s else""))))(min))if-1<b[1]<50else(p(f(b[0])+"OK, pause !")or b[0]+50,max(-1,b[1]-50)if-1!=b[1]or d(0,2)else(lambda a,t=b[0]+50:p(f(t)+"Attention, Prunelle arrive à "+f(t+a))or a)(d(10,60)),b[2]),lambda b:b[0]>=t,(0,-1,0,p(f(0)+"Gaston arrive au bureau.")))[2],0,f(t)+"Fin du service, dure journée\nTemps total travaillé : %d h %02d min"))))(lambda a,c,i=0,s=lambda a,c,x,s:x if c(x)else s(a,c,a(x),s):s(a,c,a(i),s))



