from enum import Enum


class HandType(Enum):
    FIVE = 7
    FOUR = 6
    FULL = 5
    THREE = 4
    TWO = 3
    ONE = 2
    HIGH = 1


CARD_MAP = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


class Hand:
    LENGTH = 5

    def __init__(self, input_str: str):
        assert len(input_str) == self.LENGTH
        self.cards = [CARD_MAP[c] for c in input_str]
        self.type = self._determine_type(input_str)
        self.letters = input_str

    @staticmethod
    def _determine_type(cards: str) -> HandType:
        letter_freq = {}
        for letter in cards:
            if letter not in letter_freq:
                letter_freq[letter] = 0
            letter_freq[letter] += 1

        freq_vals = letter_freq.values()
        if len(letter_freq) == 1:
            return HandType.FIVE
        elif len(letter_freq) == 2:
            if 4 in freq_vals:
                return HandType.FOUR
            else:
                return HandType.FULL
        elif len(letter_freq) == 3:
            if 3 in freq_vals:
                return HandType.THREE
            else:
                return HandType.TWO
        elif len(letter_freq) == 4:
            return HandType.ONE
        else:
            return HandType.HIGH

    def __eq__(self, other: 'Hand') -> bool:
        return self.cards == other.cards

    def __lt__(self, other: 'Hand') -> bool:
        if self.type.value < other.type.value:
            return True
        if self.type == other.type:
            for i in range(self.LENGTH):
                if self.cards[i] < other.cards[i]:
                    return True
                if self.cards[i] > other.cards[i]:
                    return False
        return False

    def __str__(self) -> str:
        return f'{self.type}: {self.letters}'

    def __repr__(self) -> str:
        return str(self)


with open('input.txt') as f:
    hands = [(Hand(s[0]), int(s[1])) for line in f if (s := line.split(' '))]

    total = [(score + 1) * hand[1] for score, hand in enumerate(sorted(hands, key=lambda x: x[0]))]

    print(sum(total))
