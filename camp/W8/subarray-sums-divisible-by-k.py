class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        dic = {0:1}
        count = 0

        for x in nums:
            prefix+=x
            count += dic.get(prefix%k,0)

            dic[prefix%k] = dic.get(prefix%k, 0) +1
        return count
