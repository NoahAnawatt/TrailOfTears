import party
import calamity_manager
import unittest

try:
    dummy = party.person('dummy1',health=10)
    dummy.summary()
    dummy.damage(2)
    assert dummy.isAlive()
    dummy.damage(100)
    assert not dummy.isAlive()
    person_test = 'OK'
except Exception as err:
    print(err)
    person_test = 'X'


group = party.party([party.person(str(x)) for x in range(0,5)])
try:
    print(group.getRandomMember().summary())
    group_test = 'OK'
except Exception as err:
    group_test = 'X'

calamity_test = 'X'
try:
    events = calamity_manager.get_calamity()
    calamity_manager.interpet_calamity(group, events[0], events[1])
    calamity_test = 'OK'
except Exception as err:
    print(err)

print(f'''
person: {person_test}
party: {group_test}
calamity manager: {calamity_test}
''')
