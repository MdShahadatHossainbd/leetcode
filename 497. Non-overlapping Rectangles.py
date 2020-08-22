class Solution:

    def __init__(self, rects: List[List[int]]):
        self.num_pts = 0
        self.rects = rects
        self.rect_cum_count = []
        for rect in rects:
            self.num_pts += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.rect_cum_count.append(self.num_pts)

    def pick(self) -> List[int]:
        pt_idx = random.randint(0, self.num_pts - 1)
        l, r = 0, len(self.rects) - 1
        while l < r:
            mid = l + (r - l) // 2
            if self.rect_cum_count[mid] <= pt_idx:
                l = mid + 1
            else:
                r = mid
        # l = rectangle index
        rect = self.rects[l]
        x_pts = rect[2] - rect[0] + 1
        y_pts = rect[3] - rect[1] + 1
        pts_in_rect = x_pts * y_pts
        pt_start = self.rect_cum_count[l] - pts_in_rect
        offset = pt_idx - pt_start;
        return [rect[0] + offset % x_pts, rect[1] + offset // x_pts]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()