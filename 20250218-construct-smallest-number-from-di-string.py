# https://leetcode.com/problems/construct-smallest-number-from-di-string/
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        if len(pattern) == 1 :
            if pattern == 'I' :
                return "12"
            else :
                return "21"
        num = []
        for item in range(len(pattern)) :
            num.append(item+1)
        num.append(num[-1]+1)
        index = 0
        p_ini = 0
        p_end = 1
        while index < len(pattern) :
            if pattern[index] == 'I' :
                p_ini = index+1
            else :
                tmp = num[index+1]
                num.remove(tmp)
                num.insert(p_ini, tmp)
            index += 1
        return "".join([str(i) for i in num])
