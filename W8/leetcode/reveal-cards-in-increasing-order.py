class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        que = deque(range(len(deck)))
        ans = [0 for _ in range(len(deck))]
        l = 0

        while que:
            # print(ans)
            ans[que.popleft()] = deck[l]
            l+=1
            if que:
                que.append(que.popleft())
            
        return ans