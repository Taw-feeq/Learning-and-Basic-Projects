class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r = 0,len(nums) - 1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
x = [0, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7, 9, 9, 11, 11, 11, 12, 12, 12, 12, 56, 3, 547, 35, 22, 5687, 34, 2, 74, 65325]
x.sort()
sq=Solution()
print(sq.search(x, 12))