from random import choice

u_score = 0
c_score = 0
score = 3

while u_score < score and  c_score < score:
	print(f"Player Score: {u_score} Computer Score: {c_score}")
	computer = choice(['rock','paper','scissors'])
	user = input("Enter your choice: ")
	print(f"Computer plays: {computer}")
	if user == computer:
		print("Its a Tie")
	elif user == "rock":
		if computer == "paper":
			print("Computer Wins!")
			c_score += 1
		else:
			print("Player Wins!")
			u_score += 1
	elif user == "paper":
		if computer == "rock":
			print("Player Wins!")
			u_score += 1
		else:
			print("Computer Wins!")
			c_score += 1
	elif user == "scissors":
		if computer == "rock":
			print("Computer Wins!")
			c_score += 1
		else:
			print("Player Wins!")
			u_score += 1
	else:
		print("Invalid Input")

if u_score > c_score:
	print("\nYou Won the Game!")
elif u_score == c_score:
	print("Its a Tie, Game Over")
else:
	print("\nComputer Won the Game")
print(f"Final Score is \n Player Score: {u_score} Computer Score: {c_score}")