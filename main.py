from hill_climbing import hill
init=[]
goal=[]
print('Solving 8 Puzzle!! (3 x 3)')
print('Initial State:')
for i in range(3):
    init.append(list(map(int,input('Row {}: '.format(i+1)).strip().split(' '))))
    
print('Goal State:')
for i in range(3):
    goal.append(list(map(int,input('Row {}: '.format(i+1)).strip().split(' '))))

res=hill(init,goal)
