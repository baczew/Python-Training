class Number():
    '''Example Class containing number'''
    def __init__(self, num):
        self._num = num
    def __repr__(self):
        return str(self._num)

class Letter():
    '''Ecample Class containing letter'''
    def __init__(self, let):
        self._let = let
    def __repr__(self):
        return self._let

class SetOfLettersAndNumbers():
    '''A Class storing letters and numbers objects'''
    def __init__(self, letters = [], numbers = []):
        self._numbers = numbers
        self._letters = letters
    def __iter__(self):
        '''Returns an Iterator'''
        return IterSetOfLettersAndNumbers(self)

class IterSetOfLettersAndNumbers():
    '''Iterator class for SetOfLettersAndNumbers class'''
    def __init__(self, Set:SetOfLettersAndNumbers):
        self.letters = Set._letters
        self.numbers = Set._numbers
        self.size = len(Set._letters) + len(Set._numbers)
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.size:

            if self.current_index < len(self.numbers):
                m = self.numbers[self.current_index]
            else:
                m = self.letters[self.current_index - len(self.numbers)]

            self.current_index += 1
            return m
        else:
            raise StopIteration




jedynka = Number(1)
dwojka = Number(2)
trojka = Number(3)
be = Letter("B")

set = SetOfLettersAndNumbers(letters=[be], numbers=[jedynka, dwojka, trojka])

for i in set:
    print(i)
