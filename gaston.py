(lambda r,p,t,w,_:(p("{}\tGaston arrive au bureau.",t),(lambda w,t:(p("{}\tFin du service, dure journée",540),print("Temps total travaillé: {} h {:02} min".format(w//60,w%60))))(*(lambda l,w,t:l(l,w,t))((lambda l,w,t:l(l,*(lambda w,t,x:(lambda w,x,t:(lambda t,w:(w-t+540,t)if t>=540 else([w,p("{}\tPrunelle est parti. \\O/", t),t][0],t))([x+150,p("{}\tIl faut travailler. M'enfin.",t)][0],w+x+150-t)if t<540 else(w,t))(w,x,(lambda x,c,t:(lambda f,c,t:f(f,c,t))(lambda f,c,t:f((f,p("{}\tC'est bon, encore le temps de faire une sieste. Zzz",t))[0],c-2,t+20)if c>=1 else(t),c,t)if c<5 else[t+50,p("{}\tOK, pause !",t)][0])(x,[(x+59-t)//10,p("{:02}:{:02}\tAttention, Prunelle arrive à {{}}".format(9+x//60,x%60),x+60)][0],t))if x+60<540 and not r(-1,1)else(w,t))((w,p("{}\tOK, pause !",t))[0],t+50,t+r(-50,0)))if t<540 else(w,540)),w,t))))(__import__("random").randint,lambda s,t:print(s.format("{:02}:{:02}".format(9+t//60,t%60))),0,0,__import__("random").seed(int("0"+"".join(filter(str.isdigit,input("Entrez une seed: "))))))
