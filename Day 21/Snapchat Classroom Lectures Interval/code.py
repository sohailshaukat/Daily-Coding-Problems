#! python3


class Lecture:
    id = 0

    def __init__(self, timeperiod):
        self.timeperiod = timeperiod

    def liesDuringLecutre(self, time):
        return self.timeperiod[0] <= time <= self.timeperiod[1]


lectures = []
lecture_times = [(30, 75), (0, 50), (60, 150)]
lower_limit = 9999
upper_limit = 0
for lec_duration in lecture_times:
    if lec_duration[0] < lower_limit:
        lower_limit = lec_duration[0]
    if lec_duration[1] > upper_limit:
        upper_limit = lec_duration[1]
    lectures.append(Lecture((lec_duration)))
maximum_intersections = 0
# Checks for overlapping lectures for every five minutes
for time in range(lower_limit, upper_limit+6, 5):
    intersection = 0
    for lecture in lectures:
        if lecture.liesDuringLecutre(time):
            intersection += 1
    if intersection > maximum_intersections:
        maximum_intersections = intersection

print(maximum_intersections)
