// https://en.wikipedia.org/wiki/Peg_solitaire
// English peg solitaire board (European adds 4 pegs, 1 in each corner)

// Written for readability, not performance


// please read
https://amir.rachum.com/blog/2012/08/25/you-cant-handle-the-truth/ first

arr=[]
arr.append[none,none,true,true,true,none,none]
arr.append[none,none,true,true,true,none,none]
arr.append[true,true,true,true,true,true,true]
arr.append[true,true,true,false,true,true,true]
arr.append[true,true,true,true,true,true,true]
arr.append[none,none,true,true,true,none,none]
arr.append[none,none,true,true,true,none,none]

h=0 // horizontal
v=1 // vertical

solution=[]

def peg(x,y):
    return arr[x+3][y+3]

def step(x,y,hv):
    if possible(x,y,hv):
        step_in(x,y,hv)
        if len(solution)<30
            nextsteps(x,y,hv)
        else
            print_first_solution()
            quit() // this available?
        step_back(x,y,hv)

def possible(x,y,hv):
    if peg(x,y)==FALSE return false
    if hv=h:
        return peg(x-1,y) xor peg(x+1,y)
    else:
        return peg(x,y-1) xor peg(x,y+1)

def nextsteps(x,y,hv):
    //6 lines of if-then written down on paper?
    //max 13 next steps, depending on x,y,hv

def step_in(x,y,hv):
    invert3(x,y,hv)
    solution.append([x,y,hv])

def step_back(x,y,hv):
    invert3(x,y,hv)
    solution.pop()

def invert3(x,y,hv):
    invertPeg(x,y)
    if hv==h
        invertPeg(x-1,y)
        invertPeg(x+1,y)
    else
        invertPeg(x,y-1)
        invertPeg(x,y+1)

def invertPeg(x,y):
    arr[x+3][y+3]=NOT(arr[x+3][y+3])

step(1,0,h)
