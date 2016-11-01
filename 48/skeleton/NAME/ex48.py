# -*- coding:utf-8 -*-
class lexicon(object):

    def __init__(self):
        self.DIRECTIONS = ("north", "south", "east", "west",
                          "down", "up", "left", "right", "back")
        self.VERBS = ("go", "stop", "kill", "eat")
        self.STOPS = ("the", "in", "of", "from", "at", "it")
        self.NOUNS = ("door", "bear", "princess", "cabinet")

    def scan(self, str):
        words = self.DealWithString(str)
        result = []
        for word in words:
            if word in self.DIRECTIONS:
                temp = ('direction', word)
            elif word in self.VERBS:
                temp = ('verb', word)
            elif word in self.STOPS:
                temp = ('stop', word)
            elif word in self.NOUNS:
                temp = ('noun', word)
            elif self.Is_Number(word):
                temp = ('number', int(word))
            else:
                temp = ('error', word)
            result.append(temp)
        return result


    def DealWithString(self, s):
        words = s.split()
        return words

    def Is_Number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

l = lexicon()
print(l.scan("hh 123"))