class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        Id = num % 10
        if (Id == 2 or Id == 3 or Id == 7 or Id == 8):
            return False
        l = 1
        r = num
        while(l <= r):
            mid = int(l + (r-l)/2)
            sq = mid * mid
            if(sq == num):
                return True
            elif(sq < num):
                l =mid + 1
            else:
                r = mid - 1
        return False
