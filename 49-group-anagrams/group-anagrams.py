class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaHash = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            if s == "":
                anaHash[tuple(arr)].append(s)
            else:
                for char in s:
                    arr[ord(char)- 97] += 1
                anaHash[tuple(arr)].append(s)
        return list(anaHash.values())