from random import choice 
from time import sleep

class person():

    def __init__(self,name,health=20):
        self.name = name
        self.health = health
        self.status = 'alive'

    def summary(self):
        summary_text = f'''
Person: {self.name}
==============================
Health: {self.health}
Status: {self.status}
==============================
'''
        print(summary_text)
        return None

    def getName(self):
        return self.name
    
    def getHealth(self):
        return self.health
    
    def isAlive(self):
        response = True
        if self.status != 'alive':
            response = False
        return response

    def damage(self,damage):
        self.health -= damage
        if self.health <= 0:
            self.status = 'dead'
        return None
    
    def kill(self):
        print(f'''
                 ______
           _____/      \\\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
             {self.name}
          |                  ||
          +==================++
''')

class party():
    def __init__(self,members):
        self.members = members
        assert type(self.members) is list
        self.food = 100

    def getRandomMember(self):
        return choice(self.members)    

    def getMembers(self):
        return self.members

    def damage_member(self,ammount):
        victim = self.getRandomMember()
        victim.damage(ammount)
        return victim,victim.status
    
    def purge(self,event):
        for member in self.members:
            if member.health <= 0:
                member.status = 'dead'
            if member.status == 'dead':
                member.kill()
                print(event['death_message'].format(victim=member.name))
                self.members.remove(member)
                sleep(4)
    
    def kill(self):
        self.members = []
        self.checkDead()

    def checkDead(self):
        if len(self.members) >= 1:
            return
        else:
            print("""
All of your party members have died. You have failed to complete
the Trail of Tears like the 4000 Native Americans who also died.
                 ______
           _____/      \\\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |    Your party    ||
          |                  ||
          | *   **    * **   |**  
   \))/.,(//,,..,,\||(,,.,..\,.((//
""")
        return True
