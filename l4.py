import random
#4,5,7, in one 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        storage: dict = {}
        for i, item in enumerate(nums):
            missing_num = target-item
            if storage.get(missing_num) is not None:
                return [i, storage.get(missing_num)]
            storage[item] = i
    
    @classmethod
    def generate_random_nums(cls, n, min_val, max_val):
        nums = [random.randint(min_val, max_val) for _ in range(n)]
        
        return nums
#4,5,7, in one 

solution = Solution()
nums =solution.generate_random_nums(100, 1, 100)
target=solution.generate_random_nums(1,1,100)[0]
print(nums)
print(target)
result = solution.twoSum(nums, target)

print(result) 