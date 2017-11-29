import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs heart'.split()

    def __init__(self):
        self._cards =  [Card(rank, suit) for suit in self.suits
                                         for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

# 列表推导使用原则: 只用列表推导来创建新的列表,并且尽量保持简短
codes = [i*i for i in range(1, 10)]
print(codes)
symbols = '@#$%$$'
beyond_ascii =  [ord(s) for s in symbols if ord(s) > 35]
print(beyond_ascii)
