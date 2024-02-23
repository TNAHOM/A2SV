class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que = deque((key, val) for key, val in enumerate(tickets))
        count = 0

        while que:
            if tickets[que[0][0]] > 0:
                tickets[que[0][0]]-=1
                count+=1

            que.append(que.popleft())
            if tickets[que[-1][0]] == 0 and que[-1][0] == k:
                return count