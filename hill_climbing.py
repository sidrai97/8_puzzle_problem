import numpy as np
from copy import deepcopy

def solvable(init):
    t=np.array(init)
    t=t.flatten()
    t=t.tolist()
    t.remove(0)
    inversion_count=0
    for i in range(len(t)):
        for j in range(i+1,len(t)):
            if t[i] > t[j]:
                inversion_count+=1
    print(inversion_count)
    if inversion_count%2 == 0:
        return True
    else:
        return False

def diff(curr,goal):
    count=0
    for i in range(len(curr)):
        for j in range(len(curr[0])):
            if curr[i][j] != goal[i][j]:
                count+=1
    return count

def possible_moves(parent,curr):
    c=[]
    z_pos_i,z_pos_j=None,None
    for i in range(len(curr)):
        for j in range(len(curr[i])):
            if curr[i][j] == 0:
                z_pos_i,z_pos_j=i,j
    #up
    if 0 <= z_pos_i-1 < len(curr):
        c_up=deepcopy(curr)
        c_up[z_pos_i][z_pos_j]=c_up[z_pos_i-1][z_pos_j]
        c_up[z_pos_i-1][z_pos_j]=0
        if parent is None:
            c.append(c_up.copy())
        elif parent != c_up:
            c.append(c_up.copy())
        #print(c_up)
    #down
    if 0 <= z_pos_i+1 < len(curr):
        c_down=deepcopy(curr)
        c_down[z_pos_i][z_pos_j]=c_down[z_pos_i+1][z_pos_j]
        c_down[z_pos_i+1][z_pos_j]=0
        if parent is None:
            c.append(c_down.copy())
        elif parent != c_down:
            c.append(c_down.copy())
        #print(c_down)
    #left
    if 0 <= z_pos_j-1 < len(curr[z_pos_i]):
        c_left=deepcopy(curr)
        c_left[z_pos_i][z_pos_j]=c_left[z_pos_i][z_pos_j-1]
        c_left[z_pos_i][z_pos_j-1]=0
        if parent is None:
            c.append(c_left.copy())
        elif parent != c_left:
            c.append(c_left.copy())
        #print(c_left)
    #right            
    if 0 <= z_pos_j+1 < len(curr[z_pos_i]):
        c_right=deepcopy(curr)
        c_right[z_pos_i][z_pos_j]=c_right[z_pos_i][z_pos_j+1]
        c_right[z_pos_i][z_pos_j+1]=0
        if parent is None:
            c.append(c_right.copy())
        elif parent != c_right:
            c.append(c_right.copy())
        #print(c_right)
    return c

def cost(depth,combo,goal):
    c=[]
    for state in combo:
        c.append(depth+diff(state,goal))
    return c

def hill(init,goal):
    path=[]
    depth=0
    parent=None
    curr=init
    while True:
        if curr == goal:
            path.append(curr)
            break
        combo=possible_moves(parent,curr)
        #print(combo)
        costs=cost(depth,combo,goal)
        min_cost_idx=costs.index(min(costs))
        parent=curr
        curr=combo[min_cost_idx]
        #print(costs)
        #print(curr)
        depth+=1
        path.append(parent)
    return path