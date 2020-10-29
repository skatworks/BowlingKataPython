class Game:

    score = 0
    
    def roll(self, pins):
        self.score += pins

    def getScore(self):
        return self.score
