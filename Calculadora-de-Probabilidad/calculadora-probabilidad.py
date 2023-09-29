import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls_to_draw):
        drawn_balls = []
        if num_balls_to_draw >= len(self.contents):
            return self.contents
        
        for _ in range(num_balls_to_draw):
            random_index = random.randint(0, len(self.contents) - 1)
            drawn_balls.append(self.contents.pop(random_index))
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        
        success = True
        for color, count in expected_balls.items():
            if color not in drawn_balls_dict or drawn_balls_dict[color] < count:
                success = False
                break
        
        if success:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability