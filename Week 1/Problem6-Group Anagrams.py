#Problem6
#Given an array of strings, group anagrams together.
#Example:
#Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]
#Note:
#All inputs will be in lowercase.
#The order of your output does not matter.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        result = []
        for string in strs:
            sorted_string = sorted(string)
            sorted_string = "".join(sorted_string)
            if sorted_string in d:
                d[sorted_string].append(string)
            else:
                d[sorted_string] = [string]
        for value in d.values():
            result.append(value)
        return result