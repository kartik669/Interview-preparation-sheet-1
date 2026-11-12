# Section 1: Data Structures & Algorithms (LeetCode Sheet 01)

This document provides production-ready, optimal solutions, dry runs, and time/space complexity analyses for all 5 LeetCode problems required for **Sheet 01** of Sheryians Coding School Weekly Interview Preparation.

---

## Problem 1: Two Sum (LeetCode #1)
- **Difficulty**: Easy
- **LeetCode Link**: [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)
- **Core Concept**: Hash Map / Complements

### Intuition & Approach
Instead of checking every pair with nested loops ($O(n^2)$ time), we can track previously visited numbers and their indices in a Hash Map (`Map`). For each number `x` at index `i`, its complement needed to reach `target` is `target - x`. If `target - x` exists in the map, we have found our pair in $O(1)$ lookup time.

### Optimal JavaScript Solution
```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map(); // stores: value -> index
    
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        
        map.set(nums[i], i);
    }
    
    return [];
};
```

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Single pass through the array with $\mathcal{O}(1)$ average hash map lookup.
- **Space Complexity**: $\mathcal{O}(n)$ — Extra memory for storing up to $n$ elements in the Map.

### Edge Cases Checked
- Array with exactly 2 elements.
- Negative numbers and zero (`nums = [-3, 4, 3, 90]`, `target = 0`).
- Duplicate values adding up to target (`nums = [3, 3]`, `target = 6`).

---

## Problem 2: Remove Duplicates from Sorted Array (LeetCode #26)
- **Difficulty**: Easy
- **LeetCode Link**: [https://leetcode.com/problems/remove-duplicates-from-sorted-array/](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- **Core Concept**: Two Pointers (In-place modification)

### Intuition & Approach
Since the input array is already sorted, all duplicates are adjacent. We can maintain a slow pointer `k` (pointing to the last known unique element) and a fast pointer `i` traversing the array. Whenever `nums[i] !== nums[k]`, we increment `k` and write `nums[k] = nums[i]`. Finally, the count of unique elements is `k + 1`.

### Optimal JavaScript Solution
```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length === 0) return 0;
    
    let k = 0; // index of the last placed unique element
    
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[k]) {
            k++;
            nums[k] = nums[i];
        }
    }
    
    return k + 1;
};
```

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — We iterate through the array once.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place modification, strictly constant additional memory.

### Edge Cases Checked
- Array of length 1 (returns 1).
- All elements identical (`[1, 1, 1, 1]` -> returns 1, array becomes `[1, ...]`).
- Array already containing unique elements (`[1, 2, 3, 4]` -> returns 4).

---

## Problem 3: Move Zeroes (LeetCode #283)
- **Difficulty**: Easy
- **LeetCode Link**: [https://leetcode.com/problems/move-zeroes/](https://leetcode.com/problems/move-zeroes/)
- **Core Concept**: Two Pointers (In-place swap)

### Intuition & Approach
We maintain a pointer `lastNonZeroFoundAt` representing the position where the next non-zero element should go. When iterating through the array with `i`, if `nums[i] !== 0`, we swap `nums[i]` with `nums[lastNonZeroFoundAt]` and increment `lastNonZeroFoundAt`. This preserves the relative order of all non-zero numbers while pushing all zeroes to the end.

### Optimal JavaScript Solution
```javascript
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let lastNonZeroFoundAt = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            // Swap non-zero element with the element at lastNonZeroFoundAt
            const temp = nums[lastNonZeroFoundAt];
            nums[lastNonZeroFoundAt] = nums[i];
            nums[i] = temp;
            
            lastNonZeroFoundAt++;
        }
    }
};
```

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Single pass over the array.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place swap, zero auxiliary memory.

### Edge Cases Checked
- All elements are 0 (`[0, 0, 0]`).
- No zeros present (`[1, 2, 3]`).
- Zero at the beginning (`[0, 1, 0, 3, 12]`).

---

## Problem 4: Rotate Array (LeetCode #189)
- **Difficulty**: Medium
- **LeetCode Link**: [https://leetcode.com/problems/rotate-array/](https://leetcode.com/problems/rotate-array/)
- **Core Concept**: Array Reversal Algorithm

### Intuition & Approach
Rotating an array to the right by $k$ positions can be achieved in $\mathcal{O}(1)$ space using the 3-step reversal algorithm:
1. Normalize $k$: `k = k % nums.length` (since rotating by $n$ returns the array to its original state).
2. Reverse the entire array.
3. Reverse the first $k$ elements (`0` to `k - 1`).
4. Reverse the remaining $n - k$ elements (`k` to `n - 1`).

### Optimal JavaScript Solution
```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    const n = nums.length;
    k = k % n;
    if (k === 0) return;
    
    // Helper function to reverse a subarray in-place
    const reverse = (arr, start, end) => {
        while (start < end) {
            const temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    };
    
    // Step 1: Reverse entire array
    reverse(nums, 0, n - 1);
    // Step 2: Reverse first k elements
    reverse(nums, 0, k - 1);
    // Step 3: Reverse the remaining n - k elements
    reverse(nums, k, n - 1);
};
```

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Each element is reversed twice (total $2n$ operations).
- **Space Complexity**: $\mathcal{O}(1)$ — Strictly in-place modification.

### Edge Cases Checked
- $k > n$ (`nums = [1, 2], k = 3` -> $k = 1$).
- $k = 0$ or $k = n$ (no changes required).
- Single element array (`nums = [1], k = 99`).

---

## Problem 5: 3Sum (LeetCode #15)
- **Difficulty**: Medium
- **LeetCode Link**: [https://leetcode.com/problems/3sum/](https://leetcode.com/problems/3sum/)
- **Core Concept**: Sorting + Two Pointers + Duplicate Avoidance

### Intuition & Approach
1. Sort `nums` in ascending order.
2. Iterate through each element `nums[i]` from index `0` to `n - 3`. If `nums[i] > 0`, break early (since three positive numbers cannot sum to 0).
3. Skip duplicate values for `nums[i]` (`if (i > 0 && nums[i] === nums[i - 1]) continue;`).
4. Use two pointers (`left = i + 1`, `right = n - 1`) to find pairs where `nums[left] + nums[right] === -nums[i]`:
   - If `sum === 0`: Push `[nums[i], nums[left], nums[right]]` to results. Skip all identical values for `left` and `right`, then move both pointers.
   - If `sum < 0`: Increase `left`.
   - If `sum > 0`: Decrease `right`.

### Optimal JavaScript Solution
```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const results = [];
    const n = nums.length;
    if (n < 3) return results;
    
    // Step 1: Sort the array
    nums.sort((a, b) => a - b);
    
    for (let i = 0; i < n - 2; i++) {
        // If smallest element is > 0, three numbers can never sum to 0
        if (nums[i] > 0) break;
        
        // Skip duplicate fixed element
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        
        let left = i + 1;
        let right = n - 1;
        
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            
            if (sum === 0) {
                results.push([nums[i], nums[left], nums[right]]);
                
                // Skip duplicates for left pointer
                while (left < right && nums[left] === nums[left + 1]) left++;
                // Skip duplicates for right pointer
                while (left < right && nums[right] === nums[right - 1]) right--;
                
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    
    return results;
};
```

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n^2)$ — Sorting takes $\mathcal{O}(n \log n)$, and the nested two-pointer search takes $\mathcal{O}(n^2)$.
- **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(\log n)$ auxiliary space (for sorting), ignoring the output array.

### Edge Cases Checked
- Array with fewer than 3 elements (returns `[]`).
- Multiple duplicate triplets (`[-2, 0, 0, 2, 2]` -> correctly returns unique `[[-2, 0, 2]]`).
- Array containing all zeroes (`[0, 0, 0, 0]` -> `[[0, 0, 0]]`).

