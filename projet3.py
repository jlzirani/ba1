#!/usr/bin/python3

def outterJoin(string, seq):
    return string + string.join(seq) + string

#cell = (a,b,c)
# a = 0 pas marqué, 1 marqué, 2 flag
# b = False pas de bomb, True bomb
# c = nombre de bombe adjacent

def showGrid(grid):
    return "    "+"   ".join(map(str,range(1,10)))+outterJoin("\n  "+'-'*37+'\n', [chr(x+65)+outterJoin(" | ",map(lambda c:['*','B'if c[1]else c[2],'F'][c[0]],grid[x]))for x in range(0,9)])

def lose(grid):
    return sum([len(list(filter(lambda x:1==x[0]and x[1],y))) for y in grid])>0

def win(grid):
    return sum([len(list(filter(lambda x:(1==x[0]and not x[1])or(1==x[0]and x[1]),y)))for y in grid])==81

def basicGrid(grille):
    return [[(0,(x,y)in grille.keys(),str(len([1 for(z,w)in getAdjCells(x,y)if(z,w)in grille.keys()])))for x in range(0,9)]for y in range(0,9)]

def setGrid(grille,cX,cY, val):
    return [[val if x==cX and y==cY else grille[x][y] for y in range(0,9)] for x in range(0,9)]

grille = {(0,7):"B",(1,5):"B",(1,6):"B",(1,8):"B",(2,4):"B",(3,4):"B",(5,5):"B",(5,7):"B",(7,0):"B",(7,5):"B"}

def setCell(cell, val):
     return (val,cell[1],cell[2])

def foldl(func, z, seq):
    return z if len(seq) == 0 else func(foldl(func,z,seq[1:]), seq[0])

def getAdjCells(x,y):
    return [(z,w) for z in range(x-1,x+2) for w in range(y-1,y+2) if z in range(0,9) and y in range(0,9)]

def setPropagation(grid, cX, cY):
    return foldl(lambda nGrid,c: setGrid(nGrid,c[0],c[1],setCell(nGrid[c[0]][c[1]],1)),grid,getAdjCells(cX,cY)) if grid[cX][cY][2] == '0' and not grid[cX][cY][1] else grid

#if __name__=='__main__' :
#   grid = [[(0,(x,y)in grille.keys(),str(len([1 for(z,w)in getAdjCells(x,y)if(z,w)in grille.keys()])))for x in range(0,9)]for y in range(0,9)]
#   while(not ( win(grid) or lose(grid) )):
#       print( showGrid(grid) )
#       x = '1'
#       while len(x) > 1 or not ord(x) in range(65,75) :
#           x = input('Indiquer une lettre : ').upper()	
#       x = ord(x) - 65
#
#       y = '0'
#       while len(y) > 1 or not ord(y) in range(49,59):
#           y = input('Indiquer un nombre : ')
#       y = ord(y) - 49
#
#       ty = '0'
#       while ty != 'M' and ty != 'F':
#           ty = input('Voulez-vous miner(M) ou mettre un drapeau(F) ? :')
#       ty = 1 if ty == 'M' else 2
#
#       grid = setGrid(grid,x,y,setCell(grid[x][y],ty)) 
#       if (ty == 1):
#           grid = setPropagation(grid, x,y) 


#r = lambda f,t,o,d:((lambda r:r(r,f(d)))(lambda r,v:o(v)if t(v)else r(r,f(v))))
#r(lambda x:input('Indiquer une lettre :').upper(),lambda x:(len(x)==1)and(64<ord(x)<75),lambda x:ord(x)-65,'0')
#r(lambda x:input('Indiquer un nombre :'),lambda x:(len(x)==1)and(48<ord(x)<59),lambda x:ord(x)-49,'0')
#print(r(lambda x:input('Voulez-vous miner(M) ou mettre un drapeau(F) ? : ').upper(),lambda x:x in'MF'and(len(x)==1),lambda x:(x<'M')+1,'0'))


(lambda r,d,p:r(lambda g:(lambda x,y,a:(lambda l:[[(a,g[z][w][1],g[z][w][2]) if(z,w)in l and g[z][w][0]!=1 else g[z][w] for w in range(0,9)] for z in range(0,9)])(([(x,y)]+[(z,w) for z in range(x-1,x+2) for w in range(y-1,y-2) if a==1 and 0<=x<9 and 0<=y<9 and not g[x][y][1]])))(*([p(g),r(lambda x:input('Indiquer une lettre :').upper(),lambda x:(len(x)==1)and(64<ord(x)<75),lambda x:ord(x)-65,'0'),r(lambda x:input('Indiquer un nombre :'),lambda x:(len(x)==1)and(48<ord(x)<59),lambda x:ord(x)-49,'0'),r(lambda x:input('Voulez-vous miner(M) ou mettre un drapeau(F) ? : ').upper(),lambda x:x in'MF'and(len(x)==1),lambda x:(x<'M')+1,'0')][1:])),lambda g:win(g)or lose(g), lambda o:print("End"),[[(0,(x,y)in d.keys(),str(len([1 for(z,w)in getAdjCells(x,y)if(z,w)in d.keys()])))for x in range(0,9)]for y in range(0,9)]))(lambda f,t,o,d:((lambda r:r(r,f(d)))(lambda r,v:o(v)if t(v)else r(r,f(v)))),{(0,7):"B",(1,5):"B",(1,6):"B",(1,8):"B",(2,4):"B",(3,4):"B",(5,5):"B",(5,7):"B",(7,0):"B",(7,5):"B"},lambda g:print("    "+"   ".join(map(str,range(1,10)))+outterJoin("\n  "+'-'*37+'\n', [chr(x+65)+outterJoin(" | ",map(lambda c:['*','B'if c[1]else c[2],'F'][c[0]],g[x]))for x in range(0,9)])))



