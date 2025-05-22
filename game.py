def main():

  x = "x"
  o = "o"
  
  print("We are playing tic tac toe")
  
def AI(o):
    
    
    if o == "o":
        print("O")
    else: 
        print("idk what game we are playing but it's tik tac toe big fella")

def user(x):
    
    if x == "x" :
        print("X")
        
    else:
        print("Please make your move")
        
user(str(input("make your move player 1 ")))
   
AI("o")
main()
