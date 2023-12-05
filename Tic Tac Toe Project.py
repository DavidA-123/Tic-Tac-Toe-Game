#!/usr/bin/env python
# coding: utf-8

# In[1]:


board = "| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |"
print(board)


# In[6]:


board = [' ' for x in range(10)]




def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print("\033[4m"+board[1]+"|"+board[2]+"|"+board[3]+"\n"+board[4]+"|"+board[5]+"|"+board[6]+"\n\033[0m"+board[7]+"|"+board[8]+"|"+board[9]) 


#checking if every single line on the board is a three in a row or a winning situation
def isWinner(red, blue):
    
    return (red [7] == blue and red[8] == blue and red[9] == blue) or (red[4] == blue and red[5] == blue and red[6] == blue) or (red[1] == blue and red[2] == blue and red[3] == blue) or (red[1] == blue and red[4] == blue and red[7] == blue) or(red[2] == blue and red[5] == blue and red[8] == blue) or(red[3] == blue and red[6] == blue and red[9] == blue) or (red [1] == blue and red[5] == blue and red[9] == blue) or (red [3] == blue and red[5] == blue and red[7] == blue)
    

def playerMove():
    run = True
    while run:
        move = input("Please select a postition to place an \"X\" (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter("X", move)
                else: 
                    print("Sorry this space is occupied! Choose another space")
            else:
                print("Please type a name in the range!")
        except:
            print("Please type a number!")

            
def compMove():
    
    #Get all information for the board(what letter is in what place and find all available spots open )
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0
    
    for let in ["〇", "X"]:
    #Going into each possible position on the copy of the board, we are going to place a letter in a spot 
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
    #In letting this happen, we will check if its a winner or not, if it is were going to say thats our move
    #and then proceed to return the move
            if isWinner (boardCopy, let):
                move = i
                return move
            
    cornersOpen = []
    #After looking through all the possible moves, if any of them are in the corner spots 
    #We'll add it into the empty corner spot
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    
    #this makes sure the list has at least one random 
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move
    
    edgesOpen = []
    #After looking through all the possible moves, if any of them are in the edges
    #We'll add it into the empty edge 
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    
    #this makes sure the list has at least one random 
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move
    
       


def selectRandom(li):
    import random 
    length = len(li) 
    ran = random.randrange(0, length)
    return li[ran]


def isBoardFull(board):
    if board.count (" ") > 1:
        return False
    else:
        return True


def main():
    print("Welcome to Tic Tac NO!")
    printBoard(board)
    
    
     
    while not (isBoardFull(board)):
        #checking to see if the computer has won
        if not(isWinner(board, "O")):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O\'s won this time!")
            break
            
        #checking to see if the user has won
        if not(isWinner(board, "X")):
            move = compMove()
            if move == 0:
                print("Tie Game!")
            else: 
                insertLetter("O", move)
                print("\n")
                print("Computer placed an \"O\" in position", move," ")
                printBoard(board)
            
        else:
            print("You've won this time! Great Work!")
            break
    
    
    if isBoardFull(board):
        print("Tie Game!")

        
        
main()

    
    


# In[ ]:




