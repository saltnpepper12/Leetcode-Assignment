class Solution:
    def findAnagrams(self, s, p):
        char_freqs, indices, len_p, len_s = defaultdict(int), [], len(p), len(s)
        
        if len_p > len_s:
            return indices
       
        for char in p:
            char_freqs[char] += 1
        
        for i in range(len_p - 1):
            if s[i] in char_freqs:
                char_freqs[s[i]] -= 1
            
        for i in range(-1, len_s - len_p + 1):
            if i > -1 and s[i] in char_freqs:
                char_freqs[s[i]] += 1
            if i + len_p < len_s and s[i + len_p] in char_freqs: 
                char_freqs[s[i + len_p]] -= 1 
            if not any(char_freqs.values()): 
                indices.append(i + 1)
                
        return indices