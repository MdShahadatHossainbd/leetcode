class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1: return True
        st, en = 0, len(s)-1
        while st < en:
            while st < en and not s[st].isalnum(): st += 1
            while st < en and not s[en].isalnum(): en -= 1
            if st < en and s[st].lower() != s[en].lower(): return False
            st, en = st+1, en-1
        return True