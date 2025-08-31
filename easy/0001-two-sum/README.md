# 0001. Two Sum

## Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

---

## Approaches

### 1. Brute Force
- **Idea:** Try every possible pair `(i, j)` and check if `nums[i] + nums[j] == target`.
- **Time Complexity:** O(n²)  
- **Space Complexity:** O(1)  

**Logic Description:**  
We loop through the array twice. For each element, we check all the following elements to see if they form a valid pair.  

**Dry Run Example:**  
nums = [2, 7, 11, 15], target = 9
i=0, j=1 → nums[0]+nums[1] = 2+7 = 9 ✅ found → return [0,1]


**Pros:** Very simple, no extra memory  
**Cons:** Very slow for large inputs  

---

### 2. Hash Map (Optimal)
- **Idea:** Use a dictionary to store numbers as we go and check if the complement exists.
- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)  

**Logic Description:**  
1. Iterate through the array.  
2. For each number, calculate `complement = target - num`.  
3. If the complement is already in the dictionary → return its index and current index.  
4. Otherwise, store the current number with its index in the dictionary.  

**Dry Run Example:**  
nums = [2, 7, 11, 15], target = 9
seen = {}
i=0, num=2 → complement=7 → not in seen → store {2:0}
i=1, num=7 → complement=2 → found in seen → return [0,1]


**Pros:** Fastest, works well for unsorted input  
**Cons:** Requires extra memory  

---

### 3. Sorting + Two Pointers
- **Idea:** Sort `(value, index)` pairs, then use two pointers from left and right to find the target sum.
- **Time Complexity:** O(n log n) (due to sorting)  
- **Space Complexity:** O(1) if sorted in place, O(n) if storing pairs  

**Logic Description:**  
1. Store `(num, index)` pairs.  
2. Sort by value.  
3. Use two pointers: `left=0`, `right=n-1`.  
4. If `arr[left] + arr[right] == target`, return indices.  
5. If sum < target → move left pointer; if sum > target → move right pointer.  

**Dry Run Example:**  
nums = [2, 7, 11, 15], target=9
arr = [(2,0), (7,1), (11,2), (15,3)]
left=0 (2), right=3 (15) → sum=17 > 9 → move right
left=0 (2), right=2 (11) → sum=13 > 9 → move right
left=0 (2), right=1 (7) → sum=9 ✅ return [0,1]


**Pros:** Saves space compared to hash map  
**Cons:** Sorting changes order, need to track indices  

---

### 4. Sorting + Binary Search
- **Idea:** Sort `(value, index)` pairs, then for each number do a binary search for the complement.
- **Time Complexity:** O(n log n) (loop + binary search)  
- **Space Complexity:** O(1) or O(n) depending on implementation  

**Logic Description:**  
1. Store `(num, index)` pairs.  
2. Sort by value.  
3. For each element `arr[i]`, do binary search for `target - arr[i].value`.  
4. If found, return indices.  

**Dry Run Example:**  
nums = [2, 7, 11, 15], target=9
arr = [(2,0), (7,1), (11,2), (15,3)]
i=0, num=2 → complement=7 → binary search finds (7,1) → return [0,1]


**Pros:** Clean, works well if binary search is familiar  
**Cons:** Slightly slower than hash map  


