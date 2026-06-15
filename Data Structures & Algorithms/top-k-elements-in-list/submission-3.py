class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for number in nums:
            if number not in numbers:
                numbers[number] = 0
            numbers[number] += 1

        array_list = sorted(list(numbers.items()), key= lambda x: x[1] )[::-1]
        print(array_list)
        answer = []
        for n in range(k):
            answer.append(array_list[n][0])

        return answer
        
        