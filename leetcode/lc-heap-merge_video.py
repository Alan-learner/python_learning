# encoding: utf-8
# author: Alan-learner
from heapq import heappush, heappop
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # 视频片段剪辑拼接的最小个数
        ans = 0
        clips.sort()
        mx = 0
        hp = []
        while clips:
            start, end = clips.pop(0)
            if start <= mx:
                contribute = end - mx
                if contribute > 0:
                    heappush(hp, -contribute)
            else:
                if hp:
                    mx += -heappop(hp)
                    hp = []
                    ans += 1
                    if mx >= time:
                        return ans
                    clips.insert(0, [start, end])
        if hp:
            mx += -heappop(hp)
            ans += 1
        if mx >= time:
            return ans
        return -1


def main():
    s = Solution()
    res = s.videoStitching([[5, 7], [1, 8], [0, 0], [2, 3], [4, 5], [0, 6], [5, 10], [7, 10]], 5)
    print(res)


if __name__ == '__main__':
    main()
