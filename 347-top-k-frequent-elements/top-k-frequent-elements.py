class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash_map = Counter(nums)
        # most_common = hash_map.most_common(k)
        # result = [key for key,value in most_common] 
        # return result
        pairs = []
        for num,count in hash_map.items():
            pairs.append((count,num))
        pairs.sort(reverse = True)
        result = []
        for i in range(k):
            result.append(pairs[i][1])
        return result
        