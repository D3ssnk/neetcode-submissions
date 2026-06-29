class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1: R+1]

            arr_p, left_p, right_p = L, 0, 0

            while left_p < len(left) and right_p < len(right):
                if left[left_p] <= right[right_p]:
                    arr[arr_p] = left[left_p]
                    left_p += 1
                else:
                    arr[arr_p] = right[right_p]
                    right_p += 1

                arr_p += 1
            
            while left_p < len(left):
                arr[arr_p] = left[left_p]
                left_p += 1
                arr_p += 1
            
            while right_p < len(right):
                arr[arr_p] = right[right_p]
                right_p += 1
                arr_p += 1
            
            return arr

        def mergeSort(arr, L, R):
            if L == R:
                return arr
            
            M = (L + R) // 2
            mergeSort(arr, L, M)
            mergeSort(arr, M+1, R)
            merge(arr, L, M, R)

            return arr
        
        mergeSort(nums,0, len(nums))


        """
        Do not return anything, modify nums in-place instead.
        """
        