print(''' \n\n\n\n\n\n
████████╗██████╗░░█████╗░██╗██╗░░░░░  ░█████╗░███████╗  ████████╗███████╗░█████╗░██████╗░░██████╗
╚══██╔══╝██╔══██╗██╔══██╗██║██║░░░░░  ██╔══██╗██╔════╝  ╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔════╝
░░░██║░░░██████╔╝███████║██║██║░░░░░  ██║░░██║█████╗░░  ░░░██║░░░█████╗░░███████║██████╔╝╚█████╗░
░░░██║░░░██╔══██╗██╔══██║██║██║░░░░░  ██║░░██║██╔══╝░░  ░░░██║░░░██╔══╝░░██╔══██║██╔══██╗░╚═══██╗
░░░██║░░░██║░░██║██║░░██║██║███████╗  ╚█████╔╝██║░░░░░  ░░░██║░░░███████╗██║░░██║██║░░██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ░╚════╝░╚═╝░░░░░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
''')
from os import system
import input_manager
import party
import calamity_manager
import random
from time import sleep
import target_minigame
print('Imports OK')

clear = lambda : system('cls')

def prelude():
    input('''
All of the facts in this game are true, to the
best of my ability. All of the dangers exhibited 
were real dangers found on the Trail of Tears.
This game is a satirical parody of the Oregon
Trail (1971). Thus, this game adapts the monochrome
scheme of the original game and a low dependency
on visuals. However, as 40 percent of people died on
the Trail of Tears, you will find many artworks
comemorating the fact. While the game may seem to be very
difficult at times, keep in mind that the timing (in days)
and rate of travel is based off of the true rate of travel
of the Cherokee tribe. You must beat the game to
see the true ending. (Enter to contnue)'''
)
def quit_game():
    print("Your game session has ended. You may now close the window.")
    print("There are multiple endings to achieve.")
    print("Made by Noah Christensen (c) 2023")
    input("Press enter to leave game")
    quit()

def game_success():
    print('''
Congratulations!

Your party has made it to Fort Gibson, Oklahoma.
Your tribe will now live here, forever.

This marks a great signficant reduction to Cherokee 
and other Native American power. Where they were once
free to roam and hunt, they are now confined to
reservations a fraction of what they were used to.

This lifestyle is not suitible for some Native Americans.
Some leave reservations and assimilate into white culutre,
abandoning there heritage.

Your adventure ends here.
''')
    quit_game()

def create_party():
    global group
    clear()
    print("Name your characters:")
    group = party.party([party.person(str(input(f'Member {x}: '))) for x in range(1,7)])
    print('Success!')
    input('''Your part has been established.
Every member has 20 hit points. (Enter to continue)''')

def initialize_game():
    input('Press enter to start ...')
    clear()
    prelude()
    input('''
The year is 1830. You and your Cherokee tribe have been ordered to
"fair" and "equitable" reservation grounds. You will depart
as soon as possible and arrive at permenant reservation sites in 116 days.
You must manage your parties food and health in order to travel. However,
you must arrive before the end of 116 days, or else winter will arrive
and your part will die.
(Enter to continue)''')
    clear()
    create_party()
    play_cycle()

def press_forward():
    sleep(.1)
    clear()
    print('''
Your party presses forward.
Under normal walking conditions, you will achieve about 10 miles in
one day. However, you can elect to press forward beyond normal human limits.

How fast do you need to go?

1) Lightly: Low progress; low strain
2) Steadily: Normal progress; normal strain
3) Heavily: Fast progress; high strain
''')
    key = input_manager.wait_key()
    progress_lambda = lambda x: random.randint(x-5,x+6)
    toll_lambda = lambda x: random.randint(x-1,x+2)
    def charge_toll(x):
        for member in group.getMembers():
            toll = toll_lambda(x)
            member.damage(toll)
            print(f'{member.name} has taken {toll} damage from the strain.')
    if key == '1':
        progress = progress_lambda(5)
        charge_toll(1)
    elif key == '2':
        progress = progress_lambda(10)
        charge_toll(2)
    elif key == '3':
        progress = progress_lambda(15)
        charge_toll(4)
    else:
        press_forward()
    group.purge({"death_message":"{victim} died of exhaustion."})
    multi_days = random.randint(10,15)
    progress = progress*multi_days
    print(f'Your party has traveled {progress} miles in {multi_days} days.')
    sleep(3)
    return progress,multi_days

def camp():
    clear()
    sleep(.1)
    print(''' 
Your party decides to establish a small camp.
For how long will your party camp?
However, winter is approaching, and you must arrive
at the reservation soon. Your time is limited.
1) 1 night = 1 health restored
2) 2 nights = 3 health restored
3) 5 nights = 7 health restored
''')
    key = input_manager.wait_key()
    key = int(key)
    if key == 1:
        h_mod = 1
        days = 1
    elif key == 2:
        h_mod = 3
        days = 2
    elif key == 3:
        h_mod = 7
        days = 5
    else:
        print('Invalid key; try again')
        camp()
    print('NAME === HEALTH')
    for member in group.getMembers():
        member.health += h_mod
        print(f'{member.name} --> {member.health}')
    sleep(5)
    return 0,days

def give_up():
    clear()
    input('''
You have assimilated to white culture. You will 
attend the United States Indian Reservation School
system, where you will learn to conform.
Your culture dies here.

███████╗███╗░░██╗██████╗░
██╔════╝████╗░██║██╔══██╗
█████╗░░██╔██╗██║██║░░██║
██╔══╝░░██║╚████║██║░░██║
███████╗██║░╚███║██████╔╝
╚══════╝╚═╝░░╚══╝╚═════╝░
''')
    quit_game()
    
def forage():
    clear()
    sleep(.1)
    try:
        trials=int(input('''
Food is scarce and your people are hungry. The cornmeal, flour,
salted pork, some vegetables and dried beans that the government
has given you dwindles. John Ross has managed to allow your party
to break away from the group and forage for food and small game.
Each attempt costs 5 days and yields 5 days of food for 6 people.
  many days would you like to forage? Type a number and press enter.\n
'''))
    except ValueError:
        print('You did not enter a real number. Skipping this turn...')
        sleep(1)
        return 0,0
    food = target_minigame.game_func(trials=trials)*30
    group.food += food
    group.food += trials*5*len(group.getMembers())
    print(f'You gained {food} ration units!')
    sleep(2)
    return 0,trials*5    

def play_cycle():
    global distance
    distance = 0
    days = 1
    day_goal = 116

    def turn(days=days,distance=distance):
        clear()
        print(f'''
DAY {days}
====================================================================
It is day {days}. You are {day_goal-days} days away from arriving at the
reservation camp. So far, you've covered {distance} of 1200 miles({round(distance/12)}%)
You have enough food to last a single person for {group.food} days.
The following party members are still alive:
{' '.join([x.name  for x in group.getMembers()])}
You have serval options. They are:
1) Press forward
2) Camp and Heal
3) Forage for food
4) Give Up
Press the number key that corrosponds with your choice.''')
        key = input_manager.wait_key()
        if key == '1':
            return press_forward()
        elif key == '2':
            return camp()
        elif key == '3':
            return forage()
        elif key == '4':
            give_up()
        else:
            print('Invalid key... please try again.')
            return
        days += random.randint(10,20)            

    while days <= day_goal:
        if group.checkDead():
            quit_game()
        results = turn(days,distance)
        if results is None:
            continue
        if len(results) == 2:
            distance += results[0]
            days += results[1]
            group.food -= results[1]*len(group.members)
        if group.food <= 0:
            group.kill()
        if distance >= 1200:
            game_success()
        if random.random() <= .4:
            clear()
            print('A calamity occured!')
            calamity = calamity_manager.get_calamity()
            calamity_manager.interpet_calamity(group, calamity[1], calamity[0])
    else:
        print('''
Unfortunately, your party's time has come. You did not complete
the trail of tears in time. Winter has arrived, and everyone has died.

███████╗███╗░░██╗██████╗░
██╔════╝████╗░██║██╔══██╗
█████╗░░██╔██╗██║██║░░██║
██╔══╝░░██║╚████║██║░░██║
███████╗██║░╚███║██████╔╝
╚══════╝╚═╝░░╚══╝╚═════╝░
''')
        quit_game()
if __name__ == '__main__':
    initialize_game()