import copy
import sys
import random
import time
# min player='o'
# max player ='x'
# always x will start the game
initial_state=[['-']*3 for i in range(3)]
computer='o'
player='x'
possible_actions=[[i,j] for i in range(3) for j in range(3)]

def whose_turn(state):#if odd 1:'o' even 0:'x'
    count=0
    for i in range(3):
        count+=state[i].count('-')
    return (1+count)%2

def actions():
    return possible_actions

def response(state,action):
    new_state=copy.deepcopy(state)
    ch='o' if whose_turn(state)==1 else 'x'
    if new_state[action[0]][action[1]]=='-':
        new_state[action[0]][action[1]]=ch
    return new_state

def whose_sequence(state):# if '-' means sequence is not there if 'x' means max player won else 'o' min player won
    diagonal_list=[]
    for i in range(3):
        diagonal_list.append(state[i][i])
        if (state[i].count('o')==0 and state[i].count('x')==3 ):
            return  'x'
        elif (state[i].count('o')==3):
            return 'o'
        elif [state[x][i] for x in range(3)].count('o')==0 and [state[x][i] for x in range(3)].count('x')==3:
            return 'x'
        elif [state[x][i] for x in range(3)].count('o')==3:
            return 'o'
        else:
            continue
    diagonal_list2=[state[0][2],state[1][1],state[2][0]]
    if (diagonal_list.count('o')==0 and diagonal_list.count('x')==3):
        return  'x'
    elif (diagonal_list.count('o')==3):
        return 'o'
    if (diagonal_list2.count('o')==0 and diagonal_list2.count('x')==3):
        return  'x'
    elif (diagonal_list2.count('o')==3):
        return 'o'
    else:
        return '-'

def terminated(state,possible_actions):
    if possible_actions==[]:
        return True
    elif whose_sequence(state)!='-':
        return True
    else:
        return False

def utility(state):
    sign=whose_sequence(state)
    if sign=='o':
        return -1
    elif sign=='x':
        return 1
    else:
        return 0

def min(a,b):
    return a if a<b else b
def max(a,b):
    return a if a>b else b

def min_value_state(state,possible_actions):
    if terminated(state,possible_actions):
        return utility(state)
    value=2
    action_done=[]
    for action in possible_actions:
        value=min(value,max_value_state(response(copy.deepcopy(state),action),remove_action(copy.deepcopy(possible_actions),action)))
        action_done.append(action)
    possible_actions=action_done
    return value

def max_value_state(state,possible_actions):
    if terminated(state,possible_actions):
        return utility(state)
    value=-2
    action_done=[]
    for action in possible_actions:
        value=max(value,min_value_state(response(copy.deepcopy(state),action),remove_action(copy.deepcopy(possible_actions),action)))
        action_done.append(action)
    possible_actions=action_done
    return value

def remove_action(possible_actions,action):
    for a in range(len(possible_actions)):
        if possible_actions[a]==action:
            del possible_actions[a]
            break
    return possible_actions

def check_diagonal(state,action):
    diagonal_list2=[state[0][2],state[1][1],state[2][0]]
    diagonal_list1=[state[i][i] for i in range(3)]
    if diagonal_list2.count('x')==2 and diagonal_list2.count('o')!=1:
        if action in [[0,2],[1,1],[2,0]]:
            return True
    if diagonal_list1.count('x')==2 and diagonal_list2.count('o')!=1:
        if action in [[0,0],[1,1],[2,2]]:
            return True
    return False
def check_vertical(state,action):
    vertical_list=[state[action[0]][i] for i in range(3)]
    if vertical_list.count('x')==2 and vertical_list.count('o')!=1:
        if action  in [ [action[0],i] for i in range(3)]:
            return True
    return False

def check_horizontal(state,action):
    horizontal_list=[state[i][action[1]] for i in range(3)]
    if horizontal_list.count('x')==2 and horizontal_list.count('o')!=1:
        if action  in [[i,action[1]] for i in range(3)]:
            return True
    return False

def is_winning(state,action):
    a,b=action
    if (a+b)%2==0:
        result=check_diagonal(state,action)
        if result==True:
            return result
    result= check_horizontal(state,action) or check_vertical(state,action)
    if result==True:
        return result
    return False

def choose_action(state,possible_actions):
    win=0
    if (1,1) in possible_actions:
    	return list([1,1])
    for  action_index in range(len(possible_actions)):
        if utility(response(state,possible_actions[action_index]))==-1:
            win=1
            return possible_actions[action_index]
    if win==0:
        for action_index in range(len(possible_actions)):
            if is_winning(state=state,action=possible_actions[action_index]):
                return possible_actions[action_index]
    max=2
    action_list=[]
    for action in possible_actions:
        value=min_value_state(response(copy.deepcopy(state),action),remove_action(copy.deepcopy(possible_actions),action))
        if max>value:
            max=value
            action_list=[]
            action_list.append(action)
        elif max==value:
            action_list.append(action)
        else :
            continue
    length=len(action_list)
    win=0
    for  action_index in range(length):
        if utility(response(state,action_list[action_index]))==-1:
            win=1
            break
    if win==0:
        for action_index in range(length):
            if is_winning(state=state,action=action_list[action_index]):
                break
    index=action_index
    return action_list[index]

def print_state(state):
        for i in range(3):
            print(" ".join(str(x) for x in state[i] ))

def position(index):
    return index/3,int(index%3)
def play(state,possible_actions):
    while terminated(state,possible_actions)==False:
        print_state(state)
        turn=whose_turn(state)
        if turn==0:
            print("your turn mr x:")
            x,y=position(int(input("enter position:")))
            action=[x,y]
            state=response(state,action)
            time.sleep(1)
            print_state(state)
            print("computer's turn o:")
            possible_actions=remove_action(possible_actions,action)
            if (terminated(state,possible_actions)):
                break
        action=choose_action(copy.deepcopy(state),copy.deepcopy(possible_actions))
        state=response(state,action)
        possible_actions=remove_action(possible_actions,action)
        print("computer:let me think ")
        time.sleep(1)

    print_state(state)
    return state

#final_state=play(initial_state,possible_actions)
#result=utility(final_state)
#print("result is"+str(result))
#if result==-1:
#    print("computer won")
#elif result==0:
#    print("it's tie")
#else:
#    print("player won")
