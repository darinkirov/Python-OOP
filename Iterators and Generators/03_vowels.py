class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0
        self.vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            char = self.string[self.index]
            self.index += 1
            if char in self.vowel_list:
                return char
        raise StopIteration
