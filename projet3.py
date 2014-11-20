#!/usr/bin/python3

def outterJoin(string, seq):
    return string + string.join(seq) + string


#cell = (a,b,c)
# a = 0 pas marqué, 1 marqué, 2 flag
# b = False pas de bomb, True bomb
# c = nombre de bombe adjacent

def cellToChar(cell):
    return ['*', 'B'if cell[1] else cell[2],'F'][cell[0]]

def showGrid(grid):
    Header = "    "+"   ".join(map(str,range(1,10))) 
    Body = outterJoin("\n  "+'-'*37+'\n', [chr(x+65) + outterJoin(" | ",map(cellToChar, grid[x])) for x in range(0,9) ])
    return Header+Body

def lose(grid):
    return sum([len(list(filter(lambda x:1==x[0]and x[1],y))) for y in grid])>0

def win(grid):
    return sum([len(list(filter(lambda x:(x[0]==1 and not x[1]) or (x[0]!=1 and x[1]),y))) for y in grid]) == 81

def basicGrid(grille):
    return [[(0,(x,y) in grille.keys(),'0') for x in range(0,9)] for y in range(0,9)]

def setGrid(grille,cX,cY, val):
    return [[val if x==cX and y==cY else grille[x][y] for y in range(0,9)] for x in range(0,9)]

grille = {(0,7):"B",(1,5):"B",(1,6):"B",(1,8):"B",(2,4):"B",(3,4):"B",(5,5):"B",(5,7):"B",(7,0):"B",(7,5):"B"}

def setCell(cell, val):
     return (val, cell[1], cell[2])


if __name__=='__main__' :
   grid = basicGrid(grille)
   while(not ( win(grid) or lose(grid) )):
       print( showGrid(grid) )
       x = '1'
       while len(x) > 1 or not ord(x) in range(65,75) :
           x = input('Indiquer une lettre : ')	
       x = ord(x) - 65

       y = '0'
       while len(y) > 1 or not ord(y) in range(49,59):
           y = input('Indiquer un nombre : ')
       y = ord(y) - 49

       ty = '0'
       while ty != 'M' and ty != 'F':
           ty = input('Voulez-vous miner(M) ou mettre un drapeau(F) ? :')
       ty = 1 if ty == 'M' else 2

       grid = setGrid(grid,x,y,setCell(grid[x][y],ty)) 
       
