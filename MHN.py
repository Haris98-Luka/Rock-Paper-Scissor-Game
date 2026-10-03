while True:
    player1=input("1.Enter rock,paper,scissor:")
    player2=input("2.Enter rock,paper,scissor:")
    if (player1=='rock' and player2=='rock') or (player1=='paper' and player2=='paper') or (player1=='scissor' and player2=='scissor'):
        print("Tie")
    elif (player1=='rock' and player2=='paper') or (player1=='rock' and player2=='scissor'):
        print("Player 1 won")
    elif (player1=='paper' and player2=='rock') or (player1=='paper' and player2=='scissor'):
        print("Player 2 won")
    elif (player1=='scissor' and player2=='rock') or (player1=='scissor' and player2=='paper'):
        print("Player 2 won")
    elif (player1=='quit') or (player2=='quit'):
        print("Quitting..")
        break
    else:
        print("Invalid Commands")
