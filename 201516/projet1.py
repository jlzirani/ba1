(lambda r,p,_:(p("Gaston arrive au bureau.",0),(lambda w,t:(p("Fin du service, dure journée",540),print("Temps total travaillé: %d h %02d min"%(w//60,w%60))))(*(lambda l,*a:l(l,*a))(lambda l,w,t:l(l,*(lambda w,t,x:(lambda w,x,t:(lambda t,w:(w-t+540,t)if t>=540else(p("Prunelle est parti. \\O/",t)or w,t))(p("Il faut travailler. M'enfin.",t)or x+150,w+x+150-t)if t<540else(w,t))(w,x,(lambda x,c,t:(lambda f,*a:f(f,*a))(lambda f,c,t:f(p("C'est bon, encore le temps de faire une sieste. Zzz",t)or f,c-2,t+20)if c>1else t,c,t)if c<5else p("OK, pause !",t)or t+50)(x,p("Attention, Prunelle arrive à %02d:%02d"%(10+x//60,x%60),x)or(x+59-t)//10,t))if x+60<540and 0==r(-1,1)else(w,t))(p("OK, pause !",t)or w,t+50,t+r(0,50)))if t<540else(w,540),0,0))))(__import__("random").randint,lambda s,t:print("%02d:%02d\t%s"%(9+t//60,t%60,s)),__import__("random").seed(int("0"+"".join(filter(str.isdigit,input("Entrez une seed: "))))))
