class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for i in magazine:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in range(len(ransomNote)):
            if ransomNote[i] in dic and dic[ransomNote[i]]>0:
                dic[ransomNote[i]] -=1
            else:
                return False
        return True