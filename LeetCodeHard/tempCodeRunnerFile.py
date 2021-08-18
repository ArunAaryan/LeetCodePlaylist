            while nums[current] > 0 and nums[current] <= n and nums[nums[current] - 1] != nums[current]:
                nums[nums[current] - 1], nums[current] = nums[current], nums[nums[current]]