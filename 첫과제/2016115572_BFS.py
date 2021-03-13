class Node:
    def __init__(self, data, depth = 0, parent = None, one = None, two = None, three = None, four = None):
        self.data = data
        self.parent = parent
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.depth = depth
    
    def __str__(self):
        return str(self.data[:3]) +"\n"+\
        str(self.data[3:6]) +"\n"+\
        str(self.data[6:]) +"\n"+\
        "-----------------"

    def InsertNode(self, node):
        if self.one == None:
            self.one = node
        elif self.two == None:
            self.two = node
        elif self.three == None:
            self.three = node
        else : self.four = node
        node.parent = self
        node.depth += 1

    def make_new_Node(self, a, b):
        new_data = self.data[:]
        new_data[a], new_data[b] = new_data[b], new_data[a]
        return Node(new_data, depth = self.depth) 
    
    def func(self):
        result = []
        i = self.data.index(0)
        if not i in [0, 1, 2] :         # UP
            result.append(self.make_new_Node(i, i-3))
        if not i in [0, 3, 6] :         # LEFT
            result.append(self.make_new_Node(i, i-1))
        if not i in [2, 5, 8] :          # RIGHT
            result.append(self.make_new_Node(i, i+1))
        if not i in [6, 7, 8] :          # Down
            result.append(self.make_new_Node(i, i+3))
        return result
        

prob = [5,1,2,
        0,6,3,
        4,7,8]

goal = [1,2,3,
        4,5,6,
        7,8,0]

open_queue = []
closed_queue = []

goal_Node = None

if __name__ == '__main__':
    root = Node(prob)
    open_queue.append(root)
    
    while open_queue != []:
        current = open_queue.pop(0)
        #print('current : ', current)

        if(current.data == goal):
            print("Success!")
            goal_Node = current
            break
        closed_queue.insert(0, current)

        for i in current.func():
            flag = 0
            for j in range(len(closed_queue)):
                if i.data == closed_queue[j].data:
                    #print('중복')
                    flag = 1
            for k in range(len(open_queue)):
                if i.data == open_queue[k].data:
                    #print('중복')
                    flag = 1
            if flag == 0:
                current.InsertNode(i)
                open_queue.append(i)
    Final_result = []
    while goal_Node.parent != None:
        Final_result.insert(0,goal_Node)
        goal_Node = goal_Node.parent

    print(closed_queue[-1])
    for i in range(len(Final_result)):
        print(Final_result[i])
    

