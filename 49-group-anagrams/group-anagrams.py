class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # anagram_map = defaultdict(list)
        # for word in strs:
        #     sorted_key = "".join(sorted(word))
        #     anagram_map[sorted_key].append(word)
        # return [group for group in anagram_map.values()]
        groups = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in groups:
                groups[key] = []
            groups[key].append(i)
        return list(groups.values())



        