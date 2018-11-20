class Word(str):
    def __init__(self,words):
        self.words = len(str(words))

    def __lt__(self,other):
        return self.words < other.words

    def __le__(self,other):
        return self.words <= other.words

    def __gt__(self,other):
        return self.words > other.words

    def __ge__(self,other):
        return self.words >= other.words

    def __eq__(self,other):
        return self.words == other.words

    def __ne__(self,other):
        return self.words != other.words
