# coding:utf-8
'''

根据你的选择，选择算法。
'''
import time

SLOW = 3  # in seconds
LIMIT = 5  # in characters
WARNING = 'too bad, you picked the slow algorithm :('


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


class Strategy:
    def unique(self, s):
        pass


class Sort_Strategy(Strategy):
    def unique(self, s):
        if len(s) > LIMIT:
            print(WARNING)
            time.sleep(SLOW)
        # 排序后，后面一个跟前面一个相同证明有重复
        srtStr = sorted(s)
        for (c1, c2) in pairs(srtStr):
            if c1 == c2:
                return False
        return True


class Set_Strategy(Strategy):
    def unique(self, s):
        if len(s) < LIMIT:
            print(WARNING)
            time.sleep(SLOW)
        return True if len(set(s)) == len(s) else False


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def run_unique(self, s):
        return self.strategy.run_unique(s)


def main():
    while True:
        word = None
        while not word:
            word = input('Insert word (type quit to exit)> ')
        if word == 'quit':
            print('bye')
            return
        strategy_picked = None
        strategies = {'1': Set_Strategy(), '2': Sort_Strategy()}
        while strategy_picked not in strategies.keys():
            strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort and pair> ')
            try:
                strategy = strategies[strategy_picked]
                context = Context(strategy)
                print('allUnique({}): {}'.format(word, context.run_unique(word)))
            except KeyError as err:
                print('Incorrect option: {}'.format(strategy_picked))
        print()


if __name__ == '__main__':
    main()
