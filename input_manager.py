import keyboard

actions = [
    'continue',
    'camp',
    'give up',
    'survive'
]
def on_key_press(key):
    print(key.name)
    if key.name == 'c' : return 'continue'
    elif key.name == 'a': return 'camp'
    elif key.name == 'g': return 'give up'
    elif key.name == 's': return 'survive'
    else: print('Invalid key press'); return None

def wait_key():
    action = keyboard.read_key()
    return action

if __name__ == '__main__':
    while True:
        keyboard.on_press(on_key_press)
        keyboard.wait()