import random 
random_num = random.randint(1,10)
print ("Hello, ladies and gentlemen! Welcome to Guess That Number!")
print ("I'm Mettaton, your fabulous mechanical host!")
print ("In this episode, we have a special guest with us.")
name = input('')
print ("Hello, %! Welcome to my show!") % name
print ("Here are the rules:")
print ("You guess a number between 1 and 10, selected randomly from the computer.")
print ("There are three rounds.")
print ("For each number you get correct, you earn 5,000 dollars.")
print ("In the bonus round you have a chance to earn 10,000 dollars, along with the money you earned in the previous rounds.")
print ("If you lose, you go home with nothing!")
print ("Do you want to play?")
play = input()
if play=='Yes':
	print ("Okay! Let's start!")
	print ("What's your guess?")
else:
	print ("Aww, that's too bad. I hope I see you on the next episode!")
guess = int(input())
if guess==4:
	print ("Correct! You just won your first 5,000 dollars!")
	print ("Onto the next round!")
	print ("What's your next guess?")
else:
	print ("Sorry, that's incorrect. The number was %r.") % int(random_num)
	print ("You were so close, yet so far away!")
	print ("That's it for tonight folks!")
	print ("I'm Mettaton, and this has been...")
	print ("GUESS THAT NUMBER!")
guess2 = int(input())
if guess2==4:
	print ("You're correct!")
	print ("Onto the next round!")
	print ("What's your guess?")
else:
	print ("Sorry, that's incorrect. The number was %r.") % (random_num)
	print ("You were so close, yet so far away!")
	print ("That's it for tonight folks!")
	print ("I'm Mettaton, and this has been...")
	print ("GUESS THAT NUMBER!")
guess3 = int(input())
if guess3==4:
	print ("Congratulations! You are now entering the bonus round.")
	print ("Do you want to participate?")
else:
	print ("Well, %r, you are taking home 15,000 dollars!") % (name)
	print ("Congratulations!")
	print ("That's it for tonight, folks!")
	print ("I'm Mettaton, and this has been...")
	print ("GUESS THAT NUMBER!")
answer = input()
if answer=='Yes':
	print ("Okay! This is your chance to earn 25,000 dollars.")
	print ("Last guess.")
guess4 = int(input())
if guess4==4:
	print ("Congratulations, %r! You are this week's lucky winner!") % (name)
	print ("You'll be taking home 25,000 dollars!")
	print ("That's it for tonight, folks!")
	print ("I'm Mettaton, and this has been...")
	print ("GUESS THAT NUMBER!")
else:
	print ("Sorry, that's incorrect. The number was %r.") % (random_num)
	print ("You were so close, yet so far away!")
	print ("That's it for tonight, folks!")
	print ("I'm Mettaton, and this has been...")
	print ("GUESS THAT NUMBER!")