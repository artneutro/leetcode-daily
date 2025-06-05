# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Create a hashmap with each alphabet letter
        alphabet_eq = {}
        for i in string.ascii_lowercase :
            alphabet_eq[i] = [i]
        # Iterate over s1 and s2 to get equivalences 
        index = 0
        # Fill the hashmap for each equivalence
        while index < len(s1) :
            # Add s2 in s1
            if s2[index] not in alphabet_eq[s1[index]] :
                alphabet_eq[s1[index]].append(s2[index])
            # Add s2 in every equivalence of s1
            for item in alphabet_eq[s1[index]] :
                if s2[index] not in alphabet_eq[item] :
                    alphabet_eq[item].append(s2[index])
            # Add every equivalence of s1 in s2
            for item in alphabet_eq[s1[index]] :
                if item not in alphabet_eq[s2[index]] :
                    alphabet_eq[s2[index]].append(item)
            # Add s1 in s2
            if s1[index] not in alphabet_eq[s2[index]] :
                alphabet_eq[s2[index]].append(s1[index])
            # Add s1 in every equivalence of s2
            for item in alphabet_eq[s2[index]] :
                if s1[index] not in alphabet_eq[item] :
                    alphabet_eq[item].append(s1[index])
            # Add every equivalence of s2 in s1
            for item in alphabet_eq[s2[index]] :
                if item not in alphabet_eq[s1[index]] :
                    alphabet_eq[s1[index]].append(item)
            index += 1
        # Merge 
        for letter in string.ascii_lowercase :
            new_group = alphabet_eq[letter]
            for item in new_group :
                new_group = list(set(new_group+alphabet_eq[item]))
            alphabet_eq[letter] = new_group
        # For each char in baseStr, get the lowest value in its hashmap
        index = 0
        while index < len(baseStr) :
            baseStr = baseStr[:index]+min(alphabet_eq[baseStr[index]])+baseStr[index+1:]
            index += 1
        return baseStr
