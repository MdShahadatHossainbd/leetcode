class Solution:
    def bitwiseComplement(self, N: int) -> int:
        out = 0
        for i in bin(N)[2:]:
            out *= 2
            if i == '0':
                out += 1
        return out

