startstory = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.

Type 'left' to go left or 'right' to go right.
'''
leftfork_1 = '''
You decide to go left and you run into a dead end.
When you turn to go back, you find the way has been closed off.
You are trapped.

Will you find a way out or wait?
Type 'find a way out' or 'wait' to continue.
'''
leftfork_1a = '''
You are determined to escape and search all over for an exit and eventually find one.
You continue on and make it out of the maze.

The end.
'''
leftfork_1b = '''
You lose hope and give up.
Your time runs out and you are trapped in the maze.

The end.
'''
rightfork_1 = '''
You choose to go right and you eventually come to a room where a group of bandits have been waiting for you.

Will you fight or yield?
Type 'fight' or 'yield' to continue.
'''
rightfork_1a = '''
You won't go down easily and you decide to fight.
You defeat the bandits and are able to escape the maze.

The end.
'''
rightfork_1b = '''
You are outnumbered and no match for the bandits. You yield and give up all your belongings to them.
You are captured by them and can't escape the maze.

The end.
'''

print(startstory)

user_input = input()
user_error = True
while user_error is True:
	user_input = input("Type 'left' or 'right'")
	if user_input == "left" or user_input == "right":
		user_error = False
if user_input == "left":
	print(leftfork_1)
	user_input = input()
if user_input == "find a way out":
	print(leftfork_1a)
	done = True
elif user_input == "wait":
	print(leftfork_1b)	
	done = True	
elif user_input == "right":
    print(rightfork_1)
    user_input = input()
if user_input == "fight":
    print(rightfork_1a)
    done = True
elif user_input == "yeild":
    print(rightfork_1b)
    done = True
