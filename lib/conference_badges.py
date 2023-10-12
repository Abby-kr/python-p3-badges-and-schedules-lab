def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = list()
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges

def assign_rooms(names):
    speaker_rooms = list()
    index = 1
    for name in names:
        speaker_rooms.append(f"Hello, {name}! You'll be assigned to room {index}!")
        index += 1
    return speaker_rooms

def printer(names):
    for name in names:
        print(f"Hello, my name is {name}.",end="\n")
    index = 1
    for name in names:
        print(f"Hello, {name}! You'll be assigned to room {index}!",end="\n")
        index += 1
    