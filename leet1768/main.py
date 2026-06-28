class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""  
        idx = 0
        while(idx < len(word1) and idx < len(word2)):  
            merged += word1[idx]
            merged += word2[idx]
            idx+=1
        if(idx+1 <= len(word1)):
            merged += word1[idx:]
        if(idx+1 <= len(word2)):
            merged += word2[idx:]

        return merged
    #  time: O(m+n)
    #  space: O(m+n)