class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        m_length = 1
        seen = defaultdict(int)
        if s == "": return 0
        seen[s[l]] += 1
        while r < len(s):
            seen[s[r]] += 1
            if seen[s[r]] > 1:
                while seen[s[r]] > 1:
                    seen[s[l]] -= 1
                    l += 1
            length = r - l + 1
            m_length = max(m_length, length)
            r += 1
        return m_length