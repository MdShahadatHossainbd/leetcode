class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.q = []

        def getCombination(start, length, txt):
            if length == 0:
                self.q.append(txt)
                return

            for i in range(start, len(characters) - length + 1):
                getCombination(i + 1, length - 1, txt + characters[i])

        getCombination(0, combinationLength, "")

    def next(self) -> str:
        str = self.q[0]
        self.q.pop(0)
        return str

    def hasNext(self) -> bool:
        return len(self.q) > 0

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
