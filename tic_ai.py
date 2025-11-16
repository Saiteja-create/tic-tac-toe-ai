class tictactoe:
    def __init__(self,):
      self.board = [
    [' ', ' ', ' '], 
    [' ', ' ', ' '],  
    [' ', ' ', ' ']   
         ]         
      self.current_player ="x"
      self.priority = ["1,1","0,0","0,2","2,0","2,2","0,1","1,0","1,2","2,1"]

    def print_board(self):
      for row in self.board:
       print(row)

    def Play_turn(self):
        board = self.board
        symbol = self.current_player
        while True :
          try:
           pair_str = input(f"Player '{symbol}', enter row,col (e.g., 1,2): ").split(",")
           pair1 = [int(i) for i in pair_str]
           if board[pair1[0]][pair1[1]] == " ":
            board[pair1[0]][pair1[1]] = symbol
            break
           else:
             print("the Box is already occupied. ")
          except(ValueError,IndexError):
           print("Invalid input.Please enter numbers like 0,1 0r 2,2.")


      
      
    def switch_player(self):
      if self.current_player == "x":
        self.current_player = "o"
      else:
        self.current_player = 'x'

    def win_check(self):
      board = self.board
  # Check rows
      for i in range(3):
       if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
        return True # Tell the caller that the game is over
  # Check columns
      for i in range(3):
       if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
        return True # Tell the caller that the game is over
  # Check diagonals
      if board[0][0] == board[1][1] == board[2][2] and board[1][1] != " ":
       return True # Tell the caller that the game is over
      if board[0][2] == board[1][1] == board[2][0] and board[1][1] != " ":
       return True # Tell the caller that the game is over
  
      return False # If no winner is found, return 
    

    def AI(self):
      board = self.board
      symbol = self.current_player
      print("Now ai turn")
      priority = ["1,1","0,0","0,2","2,0","2,2","0,1","1,0","1,2","2,1"]
      if self.wining_move():
        return  
      elif self.blocking_move():
        return
      else:
        j = self.random_move()
    


    def wining_move(self):
       symbol = self.current_player
       j = 0
       while True :
           if j == 9:
             break
           else:
            pair2 = self.priority[j]
            pair_str = pair2.split(",") 
            pair1 = [int(i) for i in pair_str]
            if self.board[pair1[0]][pair1[1]] == " ":
             self.board[pair1[0]][pair1[1]] = symbol
             if self.win_check():
               self.board[pair1[0]][pair1[1]] = symbol
               return True
             else:
               self.board[pair1[0]][pair1[1]] = " "
               j +=1
            else:
              j+=1

    def blocking_move(self):
       symbol = "x"
       j = 0
       while True :
           if j == 9:
             break
           else:
            pair2 = self.priority[j]
            pair_str = pair2.split(",") 
            pair1 = [int(i) for i in pair_str]
            if self.board[pair1[0]][pair1[1]] == " ":
             self.board[pair1[0]][pair1[1]] = symbol
             if self.win_check():
              self.board[pair1[0]][pair1[1]] = self.current_player
              return True
             else:
               self.board[pair1[0]][pair1[1]] = " "
               j +=1
            else:
              j+=1

    def random_move(self):
       symbol = self.current_player
       j = 0
       while True :
           pair2 = self.priority[j]
           pair_str = pair2.split(",") 
           pair1 = [int(i) for i in pair_str]
           if self.board[pair1[0]][pair1[1]] == " ":
            self.board[pair1[0]][pair1[1]] = symbol
            j+= 1
            break
           else:
             j+= 1
              






    
def main():
      game = tictactoe()
      n = 0
      while True:
        game.print_board()
        if game.current_player =="x":
         game.Play_turn()
         if game.win_check():
          game.print_board()
          print("you won the game")
          print("Game over!")
          break
        else:
         game.AI()
         if game.win_check():
          game.print_board()
          print("Ai won the game")
          print("Game over!")
          break
        n+=1
        if n == 9:
          print("It is draw")
          break
        game.switch_player()

main()