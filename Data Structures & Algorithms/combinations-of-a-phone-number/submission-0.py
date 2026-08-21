class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(curString, i):
            if len(curString) == len(digits):
                res.append(curString)
                return 

            for c in digitToChar[digits[i]]:
                backtrack(curString+c,i+1)

        if digits:
            backtrack("",0)
        
        return res
