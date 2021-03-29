prob = [7,1,5,
        0,3,2,
        8,4,6]

goal = [1,2,3,
        4,5,6,
        7,8,0]

class Node:
    '''
    node 생성자
    f = g + h
    g = 왔던 거리
    h = 예상 거리 (hurestic)
    '''
    def __init__(self, board, parent = None, f = 0, g = 0, h = 0):
        self.board = board
        self.parent = parent
        self.g = g
        self.h = Estimate(self.board)
        self.f = self.g + self.h
    
    def Change_Node(self, a, b):
        tempNode = Node(self.board[:], parent = self, g = self.g+1)
        tempNode.board[a], tempNode.board[b] = tempNode.board[b], tempNode.board[a]
        tempNode.h = Estimate((tempNode.board))
        tempNode.f = tempNode.g + tempNode.h
        return tempNode


    def processing(self):
        i = self.board.index(0)
        result = []
        #Up
        if i not in [0,1,2]:
            result.append(self.Change_Node(i, i-3))
        #Down
        if i not in [6,7,8]:
            result.append(self.Change_Node(i, i+3))
        #Left
        if i not in [0,3,6]:
            result.append(self.Change_Node(i, i-1))
        #Right
        if i not in [2,5,8]:
            result.append(self.Change_Node(i, i+1))

        return result

    # 프린트 함수
    def __str__(self):
        return '\n' + str(self.board[:3]) + '\n'\
               + str(self.board[3:6]) + '\n'\
               + str(self.board[6:]) + '\n'

# goal과 prob가 몇개가 다른지 확인하는 함수 estimate
def Estimate(value):
    diff = 0
    for p in enumerate(value) :
        if(goal[p[0]] != p[1]) :
            #print(str(goal[p[0]]) + str(p[1]) + 'is different')
            diff += 1
    return diff

open_queue = []
close_queue = []
Goal_Node = None

if __name__ == '__main__':
    root = Node(prob)
    
    open_queue.append(root)

    while open_queue != []:

        index = 999
        # 가중치가 가장 작은 index값 찾기
        for i in range(len(open_queue)):
            if open_queue[i].f < index:
                index = i

        current = open_queue.pop(index)
        if current.board == goal:
            Goal_Node = current
            print("Success!")
            break
        for node in current.processing():
            flag = 0
            for i in range(len(close_queue)):
                if node.board == close_queue[i].board:
                    flag = 1
            for j in range(len(open_queue)):
                if node.board == open_queue[j].board:
                    flag = 1

            if flag == 0:
                open_queue.append(node)

        close_queue.append(current)

    re = []
    t_Node = Goal_Node

    while t_Node.parent != None:
        re.insert(0,t_Node)
        t_Node = t_Node.parent
    
    for i in range(len(re)):
        print(re[i])

    print(str(Goal_Node.f)+'번 움직였습니다.')
    
    
    



