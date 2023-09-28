def badge_maker(name="Guido van Rossum"):
    return f'Hello, my name is {name}.'
    

def batch_badge_creator(names):
    new_list = []
    for name in names:
        new_list.append(badge_maker(name))
    return new_list

def assign_rooms(names):
    new_list = []
    for name in names:
        new_list.append(f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!")
    return new_list

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)
    return None


names = ['Guido', 'Edsger', 'Ada', 'Charles', 'Alan', 'Grace']
printer(names)