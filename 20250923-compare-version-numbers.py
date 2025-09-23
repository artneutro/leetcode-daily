# https://leetcode.com/problems/compare-version-numbers/
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_split = version1.split('.')
        version2_split = version2.split('.')
        min_len = min(len(version1_split), len(version2_split))
        # Look for major release
        index = 0
        while index < min_len :
            if int(version1_split[index]) < int(version2_split[index]) :
                return -1
            elif int(version1_split[index]) > int(version2_split[index]) :
                return 1
            index += 1
        # Look for any major release in remainings
        if len(version1_split) < len(version2_split) :
            if sum(int(x) for x in version2_split[index:]) == 0 :
                return 0
            else :
                return -1
        elif len(version1_split) > len(version2_split) :
            if sum(int(x) for x in version1_split[index:]) == 0 :
                return 0
            else :
                return 1
        return 0
