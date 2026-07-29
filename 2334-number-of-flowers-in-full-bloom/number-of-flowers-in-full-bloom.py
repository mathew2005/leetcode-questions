class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(f[0] for f in flowers)
        ends = sorted(f[1] for f in flowers)

        answer = []
        for t in people:
            started = bisect_right(starts, t)

            finished = bisect_left(ends, t)
            answer.append(started - finished)

        return answer
        