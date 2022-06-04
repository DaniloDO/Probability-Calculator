
import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.kwargs = kwargs
    
        for key,value in kwargs.items():
            for i in range(0, value):
                self.contents.append(key)
                   
    def draw(self, number):
        extracted_balls = []
        total_balls = len(self.contents)

        if(number >= total_balls):
            extracted_balls = self.contents
        else:
            for i in range(0, number):
                rand = random.randint(0, total_balls - 1)
                extracted_balls.append(self.contents.pop(rand))
                total_balls = len(self.contents)

        return extracted_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_list, extracted_list = [], []
    event_counter = 0
    not_repeated = []

    for key, value in expected_balls.items():
        expected_list += value * [key]

    for i in range(0, num_experiments):
        hat_copy = copy.deepcopy(hat)
        extracted_list = hat_copy.draw(num_balls_drawn)

        match = True
        for val in expected_list:
            if(val in extracted_list):
                extracted_list.remove(val)
            else:
                match = False
                break

        if(match):
            event_counter += 1

        probability = event_counter / num_experiments

    return probability
