class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length) {
            return false;
        }

        let letterCount = new Array(26).fill(0)

        for (let i = 0; i < s.length; i++) {
            const sLetterCode = s.charCodeAt(i) % 26
            const tLetterCode = t.charCodeAt(i) % 26
            letterCount[sLetterCode]++
            letterCount[tLetterCode]--
        }
        
        return letterCount.every(letter => letter == 0)
    }
}
