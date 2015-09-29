r,p,t,w,_ = (lambda r,p,t,w,_: (r,p,t,w, p("{}\tGaston arrive au bureau.", t))) (__import__("random").randint,lambda s,t:print(s.format("{:02}:{:02}".format(9+t//60,t%60))),0,0,__import__("random").seed(int("0"+"".join(filter(str.isdigit,input("Entrez une seed: "))))))

def l(t,w):
    p("{}\tOK, pause !",t)
    t += 50
    if not r(-1,1):
        x = t + r(-50,0)
        p("{:02}:{:02}\tAttention, Prunelle arrive à {{}}".format(9+x//60, x%60), x+60)
        c = (x+59-t)//10

        if c < 5:
            while (c>1):
                p("{}\tC'est bon, encore le temps de faire une sieste. Zzz", t)
                t += 20
                if t >= 540:
                    return 540,w
                c -= 2
        else:
            p("{}\tOK, pause !", t)
            t += 50
            if t >= 540:
                return 540,w

        w += x+150-t
        p("{}\tIl faut travailler. M'enfin.", t)
        t = x + 150
        if t >= 540:
            w -= t - 540
            return 540,w
        p("{}\tPrunelle est parti. \\O/", t)
    if t < 540:
        return l(t,w)
    else:
        return 540,w

l(t,w)


(lambda w,t:(p("{}\tFin du service, dure journée", 540),print("Temps total travaillé: {} h {:02} min".format(w//60,w%60))))(w,t)
