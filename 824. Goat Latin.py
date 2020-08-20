class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        result, suffix = "", ""
        for word in S.split():
            suffix += 'a'
            if not word[0] in vowels:
                word = word[1:] + word[0]
            result += word + "ma" + suffix + ' '
        return result[:-1]