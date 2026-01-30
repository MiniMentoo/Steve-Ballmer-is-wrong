import random
from enum import Enum

NUM_OF_TRIALS = 100000
UPPERBOUND = 100
LOWERBOUND = 1

class result(Enum):
    HIGHER  = 1
    LOWER   = -1
    CORRECT = 0
    

class NumberGame:
    def __init__(self):
        self.number = random.randint(LOWERBOUND, UPPERBOUND)

    def guess(self, guess):
        if guess == self.number:
            return result.CORRECT
        elif guess > self.number:
            return result.LOWER
        elif guess < self.number:
            return result.HIGHER
    
    def reset(self):
        self.number = random.randint(LOWERBOUND,UPPERBOUND)

class BinarySearcher:
    def __init__(self, initialGuess = None):
        self.guessCount = 0
        self.env = NumberGame()
        self.upper = UPPERBOUND
        self.lower = LOWERBOUND
        self.previousGuessResult = None
        if initialGuess == None:
            self.guess = self.setGuess()
            self.initialguess = None
        else:
            self.guess = initialGuess
            self.initialguess = initialGuess
    
    def setGuess(self):
        return (self.upper - self.lower) // 2 + self.lower

    def playGame(self):
        while(not self.previousGuessResult == result.CORRECT):
            self.previousGuessResult = self.env.guess(self.guess)
            #print(f"Guessed {self.guess}, got {self.previousGuessResult}")
            self.guessCount += 1
            match self.previousGuessResult:
                case result.LOWER:
                    self.upper = self.guess - 1
                case result.HIGHER:
                    self.lower = self.guess + 1
                case result.CORRECT:
                    return self.guessCount
                case _:
                    raise Exception("Environment guess method returned something unexpected")
            self.guess = self.setGuess()
    
    def reset(self):
        self.env.reset()
        self.guessCount = 0
        self.upper = UPPERBOUND
        self.lower = LOWERBOUND
        self.previousGuessResult = None
        if self.initialguess == None:
            self.guess = self.setGuess()
        else:
            self.guess = self.initialguess

if __name__ == "__main__":
    sum = 0
    bs = BinarySearcher()
    for _ in range(NUM_OF_TRIALS):
        sum += bs.playGame()
        bs.reset()
    average = sum / NUM_OF_TRIALS
    print(average)