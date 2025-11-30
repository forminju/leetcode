class Solution:

    def lps(self, pattern: str) -> list[int]:
        m = len(pattern)
        pi = [0] * m
        j = 0

        for i in range(1,m):
            while j>0 and pattern[i] !=pattern[j] :
                j = pi[j-1]

            if pattern[i] == pattern[j]:
                j +=1
                pi[i] = j

        return pi

    def kmp(self, text:str, pattern:str) -> bool:
        n,m = len(text), len(pattern)
        if m ==0 :
            return True

        pi = self.lps(pattern)
        j = 0

        for i in range(n):
            while j>0 and text[i] != pattern[j]:
                j = pi[j-1]

            if text[i] == pattern[j] :
                j+=1
                if j == m:
                    return True
        
        return False

    def repeatedStringMatch(self, a: str, b: str) -> int:

        times = (len(b) + len(a) -1) // len(a)

        s = a * times

        if self.kmp(s,b):
            return times

        s+=a

        if self.kmp(s,b):
            return times+1

        return -1



    
        