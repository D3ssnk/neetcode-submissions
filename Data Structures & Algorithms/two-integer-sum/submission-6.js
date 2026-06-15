class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let pTargets = new Map()
        for (let i = 0; i < nums.length; i++) {
            const number = nums[i]
            const needNumber = target - number 
            if (pTargets.has(needNumber)) {
                return [i,pTargets.get(needNumber)]
            }
            pTargets.set(number,i)
        }
        return []
    }
}
