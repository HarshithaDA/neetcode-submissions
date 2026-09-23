class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        # it is possible that strs[0] first string in array is not the shortest - in that case we handle it
        for i in range(len(strs[0])):
            for s in strs:
                # chekc out of bounds condition 
                # check if every character @ index i is the same
                if i==len(s) or s[i] != strs[0][i]:
                    # if not eqqual return the result
                    return result

            result += strs[0][i]
        return result

                

