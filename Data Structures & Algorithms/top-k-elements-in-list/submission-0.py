class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for number in nums:
            if number not in num_dict:
                num_dict[number] = 0
            num_dict[number] += 1
        sorted_items = sorted(num_dict.items(), key=lambda item: item[1], reverse=True)
        top_k_keys = [key for key, value in sorted_items[:k]]
        return top_k_keys
        