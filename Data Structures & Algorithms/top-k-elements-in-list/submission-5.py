class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for number in nums:
            if number not in numbers:
                numbers[number] = 0
            numbers[number] += 1

        array_list = sorted(list(numbers.items()), key= lambda x: x[1], reverse= True )
        answer = [keys for keys, values in array_list[:k]]

        return answer
        
        