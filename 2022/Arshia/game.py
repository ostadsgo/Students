class Game:
    def __init__(self) -> None:
        self.score = 0

    def decide_score(self, cards):
        names = [card.name.get() for card in cards]
        unique = len(set(names))
        if unique == len(names):
            self.score = 3
        elif unique == 2:
            self.score = 2
        else:
            self.score = 0
        return self.score
