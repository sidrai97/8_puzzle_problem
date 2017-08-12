from hill_climbing import hill, solvable
init=[]
goal=[]
print('Solving 8 Puzzle!! (3 x 3)')
print('------\nInitial State')

for i in range(3):
    init.append(list(map(int,input('Row {}: '.format(i+1)).strip().split(' '))))
    
print('------\nGoal State')
for i in range(3):
    goal.append(list(map(int,input('Row {}: '.format(i+1)).strip().split(' '))))

if solvable(init) != solvable(goal):
    print('Unsolvable, Try another one!!')
    exit()

path=hill(init,goal)

for mat in path:
    print('------')
    for row in mat:
        print('{} {} {}'.format(row[0],row[1],row[2]))