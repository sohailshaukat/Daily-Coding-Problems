#!python 3


def is_head_present(head, flights):
    for ptr, flight in enumerate(flights):
        if flight[0] == head:
            return True, ptr
    return False, -1


# flights = [('SFO', 'COM'), ('COM', 'YYZ')]
flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
# head = 'COM'
head = 'YUL'
trigger = is_head_present(head, flights)
halts = [head]
while trigger[0]:
    loc = trigger[1]
    head = flights[loc][1]
    halts.append(head)
    del flights[loc]
    trigger = is_head_present(head, flights)
if len(flights) == 0:
    print(halts)
else:
    print(False)
