#! python3

class Lecture:
    id = 0
    def __init__(self, timeperiod):
        self.timeperiod = timeperiod
    
lectures = []    
lecture_times = [(30, 75), (0, 50), (60, 150)]
for lec_duration in lecture_times:
    lectures.append(Lecture((lec_duration)))
    
print(lectures[1].timeperiod)
