class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0]*num_people
        idx, candies_count = 0, 1
        while candies > 0:
            result[idx] += candies_count
            candies -= candies_count
            idx, candies_count = idx+1, candies_count+1
            if idx == num_people: idx = 0
            if candies_count > candies: candies_count = candies
        return result