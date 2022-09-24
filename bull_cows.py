import random


class Play:
    def __init__(self):
        self.number = []
        for i in range(4):
            self.number.append(str(random.randint(0, 9)))

    def compare(self, guess):
        listed_guess = []
        for dig in str(guess):
            listed_guess.append(dig)
        result = []
        data = dict()
        for i in self.number:
            if i not in data:
                data[i] = 1
            else:
                data[i] += 1
        taken_care = []
        for i in range(4):
            if listed_guess[i] == self.number[i]:
                result.append('B')
                data[listed_guess[i]] -= 1
                taken_care.append(i)
        for i in range(4):
            if listed_guess[i] in self.number and i not in taken_care and data[listed_guess[i]] != 0:
                result.append('C')
                data[listed_guess[i]] -= 1
        return result
