# name: Jonathon Wisler
# My Integration project is a tool that can be used for Basketball players to compare their stats to NBA star, Steph Curry

print("Welcome to my project!","Today you will compare yourself to Stephen Curry")
print("Let's start with height!")
user_height= int(input("Enter your height in inches:"))
steph_curry_height = 74
#googled his height

if user_height > 74:
    print("You are taller than Steph Curry!")
else:
    print("You are shorter than Steph Curry!")

print("Weight is a good thing to know, your weight can drastically effect your performance.")
user_weight=int(input("Enter how many pounds you weigh:"))
steph_curry_weight = 185
#googled his weight

if user_weight > 185:
    print("You weigh more than Steph Curry!")
else:
    print("You weigh less than Steph Curry!")

print("Stephen Curry is best known for his shooting, let's take a look at some of his shooting stats and compare them to yours.")
print("An elite shooter is part of the 50, 40, 90 club, meaning they shoot 50 percent from the field, 40 percent from three, and 90 percent from the free throw line.")
#I am a big NBA fan and have prior knowledge to things like the 50,40,90 club

user_free_throw = int(input("Enter your free throw percentage:"))
user_three_point= int(input("Enter your three point percentage:"))
user_field_goal= int(input("Enter your field goal percentage:"))

club= user_field_goal,+user_three_point,+user_free_throw
#use the + to have the numbers for the 50,40,90 club

print("Your in the", club,"club!")
if user_free_throw >= 90 and user_three_point >= 40 and user_field_goal >= 50:
    print("You would be considered an elite NBA shooter, like Stephen Curry!")
else:
    print("You aren't an elite shooter, although many players have improved their shooting percentages throughout their carrer.")
#Lebron James, considered the greatest basketball player of all time, started with a 29 percent from three, which is below league average, now he shoots a respectable 36 percent

print("Assists are another important stat when it comes to basketball")
user_assists=int(input("Enter your average assists per game to the nearest integer:"))
steph_curry_assist= 7
#got stat from google

if user_assists > 7:
    print("You pass better than Steph Curry!")
else:
    print("You are not on the same assist level as Steph Curry")

print("To dive in deeper, an assist to turnover ratio is the best way to truly see how good of a playmaker a player is.")
user_turn_over= int(input("Enter your turnovers a game to the nearest integer:"))
step_curry_turn_over= 3
assist_ratio= user_assists/user_turn_over
#used - to find the quotent between the two numbers

print("Your assist to turn over ratio is",assist_ratio)
print("An elite passer has a turn over ratio of 3 or higher")
#statmuse.com

print("Stephen Curry holds the record for then most 3 pointers made in a season")
print("To compare yourself to the best, your numbers need to be near or higher than the best")
user_three_pointer= int(input("Enter how many three pointers you made last year"))
step_three_pointer= 402
#statmuse.com

if user_three_pointer < 402:
    print("You have not made more three pointers in a season than Curry")
else:
    print("You have made more threes than Steph, you should pursue your skill in shooting at the next level")

print("Now lets pick your jersey number!")  
player_number=int(input("Enter what jersey number do you want:"))
print("Congrats your number",player_number,"Would look good with Stephy Curry's number 30!")
#got his number from online

print("Now that you compared your stats to Curry's are you even good enough to be his teamate.")
print("Now we will compare your stats to the league average to see if you could even play on his team.")
print("Obviously your stats didn't compare well to Curry's, he is considered one of the greatest and most skilled players ever")

if user_height < 78:
    print("You are shorter than the average NBA player, which gives you an automatic disadvantage")
else:
    print("You are taller than the average NBA player, thus you have a slight advangtage over players your taller than")
#googled the average height 

print("Your average weight isn't as important due to the different body types and shape.")
print("Although, wingpsan is a great advangtage on the basketball court.")
print("Having a longer wingspan alows you to have better defense, offense, and all around game")

user_wing= int(input("Enter your wingspan in inches:"))
if user_wing < 82:
    print("Your arms are shorter than the average NBA player, giving you an automatic disadvantage.")
else:
    print("Your arms are very long, you should have the upper edge on smaller players.")

print("As you can see the average wingspan is significantly larger than the average height.")
print("This is due to most NBA players being blessed with longer arms, making them better players")


































print("Thankyou for playing my game!")

