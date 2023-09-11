#each test has four scores from -1 to 1:
#affirmative to the test adds to users total score and negative subtracts
"""
c_score - consequentialism
d_score - deontology
v_score - virtue ethics
n_score - nhilism (hardest one to measure)

"""

class User:
    def __init__(self):
        self.scores = {'c':0,'d':0,'v':0,'n':0}

    def identify(self):
        max_val = 0
        for score in self.scores:
            if score > max_val:
                max_val = score

    


class Dilemma:
    def __init__(self):
        self.scores = {'c':0,'d':0,'v':0,'n':0}
    def add(self, user):
        for key in self.scores.keys():
            user.scores[key]+=self.scores[key]

    def subtract(self, user):
        for key in self.scores.keys():
            user.scores[key]-=self.scores[key]