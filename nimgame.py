import random

def computer_move(piles):
    selected_pile = random.randint(0, len(piles) - 1)
    selected_stones = random.randint(1, piles[selected_pile])
    return selected_pile, selected_stones

def nim_game():
    piles = [3, 4, 5]  # Example piles, you can change this
    player = 1
    
    while True:
        print("Current piles:", piles)
        
        if player == 1:
            print("Your turn")
            selected_pile = int(input("Select a pile (0-indexed): "))
            selected_stones = int(input("Select number of stones to remove: "))
        else:
            print("Computer's turn")
            selected_pile, selected_stones = computer_move(piles)
            print("Selected pile:", selected_pile)
            print("Selected stones:", selected_stones)
        
        if selected_pile < 0 or selected_pile >= len(piles) or selected_stones < 1 or selected_stones > piles[selected_pile]:
            print("Invalid move! Try again.")
            continue
        
        piles[selected_pile] -= selected_stones
        
        if sum(piles) == 0:
            if player == 1:
                print("You win!")
            else:
                print("Computer wins!")
            break
        
        player = 3 - player  # Switch player

# Run the game
nim_game()
