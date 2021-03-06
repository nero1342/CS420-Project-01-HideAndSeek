from player import Player
import numpy as np 
import random

from collections import deque 
class Seeker(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.visited_map = None
        self.value = -2

    def move(self, view):
        self.update_own_map(view)
        return self.heuristic_level1()
        # return random.randint(0, 8)
        pass

    def update_own_map(self, view):
        if self.visited_map is None:
            self.visited_map = view 
        
        # view.print_map()
        
        for i in range(len(view.map)):
            for j in range(len(view.map[0])):
                if (view.map[i][j] > 2):
                    self.visited_map.map[i][j] = view.map[i][j]
                elif (view.map[i][j] == -1):
                    self.visited_map.map[i][j] = -1
                    # if self.visited_map.map[i][j] == 0 or :
                    #     self.visited_map.map[i][j] = -1
                if (self.visited_map.map[i][j] == self.id + 3 and view.map[i][j] < 2):
                    self.visited_map.map[i][j] = -1
        # self.visited_map.print_map()
        cnt_0 = 0
        for i in range(len(view.map)):
            for j in range(len(view.map[0])):
                if self.visited_map.map[i][j] == 0:
                    cnt_0 += 1
        if cnt_0 == 0:
            self.visited_map = view 

    def heuristic_level1(self):
        curr_map = self.visited_map.map
        inf = int(1e9)
        h = [[0 for i in range(len(curr_map[0]))] for j in range(len(curr_map))]
        d = [[-1 for i in range(len(curr_map[0]))] for j in range(len(curr_map))]
        trace = [[(-1, -1) for i in range(len(curr_map[0]))] for j in range(len(curr_map))]
        x, y = self.position
        d[x][y] = 0
        
        q = deque() 
        q.append(self.position)

        dir = self.visited_map.Direction()
        # print(type)
        best_val = inf 
        best_target = ()
        while len(q) > 0:
            u = q.popleft() 
            # print("Start at {}".format(u))
            for i in range(len(dir)):
                v = (u[0] + dir[i][0], u[1] + dir[i][1])
                # print("To {}, {}, {}".format(v, self.visited_map.valid(v), h[v[0]][v[1]]))
                if (self.visited_map.valid(v)) and d[v[0]][v[1]] == -1:
                    # print(self.visited_map.id[3])
                    if (self.visited_map.id.get(curr_map[v[0]][v[1]]) and self.visited_map.id[curr_map[v[0]][v[1]]] == self.__class__.__name__):
                        continue 
                    d[v[0]][v[1]] = d[u[0]][u[1]] + 1
                    if curr_map[v[0]][v[1]] == -1:
                        h[v[0]][v[1]] = inf
                    if curr_map[v[0]][v[1]] == -4:
                        h[v[0]][v[1]] -= inf // 2
                    
                    if (self.visited_map.id.get(curr_map[v[0]][v[1]])):
                        h[v[0]][v[1]] -= inf     
                    
                    trace[v[0]][v[1]] = (u, i)
                    q.append(v)

                    if (h[v[0]][v[1]] + d[v[0]][v[1]] <= best_val):
                        if (h[v[0]][v[1]] + d[v[0]][v[1]] == best_val) and random.randint(0, 1):
                            continue
                        best_val = h[v[0]][v[1]] + d[v[0]][v[1]]
                        best_target = v 
        
        # print("Best target:", best_target[0], best_target[1], best_val)
        try:
            while (trace[best_target[0]][best_target[1]][0] != self.position):
                best_target = trace[best_target[0]][best_target[1]][0]
        except Exception:
            return 1
            pass
        return trace[best_target[0]][best_target[1]][1]

        
    
        

