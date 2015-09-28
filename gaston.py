from random import seed, randint

def pretty(string, time):
    print(string.format("{:02}:{:02}".format(9 + time//60, time%60)))

seed(int("0" + "".join(filter(str.isdigit, input("Entrez une seed: ")))))
time = 0
worktime = 0

pretty("{}\tGaston arrive au bureau.", time)
while time < 540:
    pretty("{}\tOK, pause !",time)
    time += 50
    if not randint(-1,1):
        x = time + randint(-50,0)
        pretty("{:02}:{:02}\tAttention, Prunelle arrive à {{}}".format(9+x//60, x%60), x+60)
        c = (x+59-time)//10

        if c < 5:
            while (c>1):
                pretty("{}\tC'est bon, encore le temps de faire une sieste. Zzz", time)
                time += 20
                if time >= 540:
                    break
                c -= 2
        else:
            pretty("{}\tOK, pause !", time)
            time += 50
            if time >= 540:
                break

        worktime += x+150-time
        pretty("{}\tIl faut travailler. M'enfin.", time)
        time = x + 150
        if time >= 540:
            worktime -= time - 540
            break
        pretty("{}\tPrunelle est parti. \\O/", time)

pretty("{}\tFin du service, dure journée", 540)
print("Temps total travaillé: {} h {} min".format(worktime//60, worktime%60))

