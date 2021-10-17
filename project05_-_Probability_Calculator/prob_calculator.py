import copy
import random


class Hat:
    
    def __init__(self, **kwargs):
        
        self.contents = []
       
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, number_balls):
        
        if number_balls < len(self.contents):
            response = []
            for i in range(number_balls):
                item = random.choice(self.contents)
                self.contents.remove(item)
                response.append(item)
            return response
        else:
            return self.contents
        
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    N = num_experiments

    expected_balls_list = []
       
    for key, value in expected_balls.items():
        for i in range(value):
            expected_balls_list.append(key)
    
    M = 0
    for i in range(N):
        
        hat_copy = copy.deepcopy(hat)
        result = hat_copy.draw(num_balls_drawn)
        
        
        counter = 0
        for i in range(len(expected_balls_list)):
            if expected_balls_list[i] in result:
                result.remove(expected_balls_list[i])
                counter += 1

        if counter == len(expected_balls_list):
            M += 1

    return M / N


hat = Hat(blue=3,red=2,green=6)

probability = experiment(hat, {"blue":2,"green":1}, 4, 1000)
print("\nProbability:", probability)