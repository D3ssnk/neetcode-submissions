class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        let copyArray = nums.slice()
        let ans = copyArray.concat(nums)
        return ans
    }
}
