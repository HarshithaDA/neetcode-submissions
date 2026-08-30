class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # check every single word in worddict and check if it matches the prefix
        # go from behind if we can match any of the words from dict

        
        dp = [False] * (len(s)+1)
        dp[len(s)] = True # last position base case set to true

        # iterate from reverse
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                # does string from i even has enough characters for word comparision from wordDict - enough characters in s to compare them
                # and if they are equal the substring and word
                if (i+len(w)) <= len(s) and s[i: i+len(w)] == w:
                    dp[i] = dp[i+len(w)]

                if dp[i]:
                    break
        return dp[0]




