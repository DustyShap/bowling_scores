
class Game:

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total = 0
        roll_index = 0
        for roll in range(10):
            if self.isSpare(roll_index):
                total += self.scoreSpare(roll_index)
                roll_index += 2
            elif self.isStrike(roll_index):
                total += self.scoreStrike(roll_index)
                roll_index += 1
            else:
                total += self.scoreFrame(roll_index)
                roll_index += 2
        return total


    def isSpare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def isStrike(self, roll_index):
        return self.rolls[roll_index] == 10

    def scoreSpare(self, roll_index):
        return 10 + self.rolls[roll_index + 2]

    def scoreStrike(self, roll_index):
        return 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def scoreFrame(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
