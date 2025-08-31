# 🚀 LeetCode Solutions Repository

This repository contains my solutions to **LeetCode problems** with detailed explanations, multiple approaches, and analysis of **time & space complexity**.  
The goal is not just to solve problems but to **understand trade-offs between different solutions** (brute force, optimal, etc.).

---

## 📂 Repository Structure
- **problems/** → Each problem has its own folder (`0001-two-sum/`) with multiple approaches & explanation.  
- **categorized/** → Organizes problems by difficulty (**Easy, Medium, Hard**).  

---

## 📘 Problem README Format

Each problem folder contains a `README.md` like this:

### Example: `0001. Two Sum`

#### Problem  
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

---

#### Approaches  

##### 1. Brute Force  
- **Idea:** Try all pairs.  
- **Time Complexity:** O(n²)  
- **Space Complexity:** O(1)  
- **Pros:** Very simple, no extra memory  
- **Cons:** Very slow for large inputs  

**Dry Run Example**  
nums = [2, 7, 11, 15], target = 9
Check (2,7) → 9 ✅ → return [0,1]

---

##### 2. Hash Map (Optimal)  
- **Idea:** Store seen numbers in a hash map and check for complement.  
- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)  
- **Pros:** Fastest, works on unsorted input  
- **Cons:** Uses extra memory  

**Dry Run Example**  
nums = [2, 7, 11, 15], target = 9
i=0 → 2, store {2:0}
i=1 → 7, check (9-7=2) found in map ✅ → return [0,1]


---

##### 3. Sorting + Two Pointers  
- **Idea:** Sort array, then move left/right pointers.  
- **Time Complexity:** O(n log n)  
- **Space Complexity:** O(1) if in-place sorting  
- **Pros:** Saves memory  
- **Cons:** Need to track original indices  

---

##### 4. Sorting + Binary Search  
- **Idea:** For each element, binary search the complement.  
- **Time Complexity:** O(n log n)  
- **Space Complexity:** O(1) / O(n)  
- **Pros:** Elegant  
- **Cons:** Slower than hash map  

---

## ⚡ Features

- ✅ Multiple approaches for each problem  
- ✅ Dry run examples for clarity  
- ✅ Time and space complexity analysis  
- ✅ Well-structured repository (problem-wise & difficulty-wise)  
- ✅ Beginner and advanced-friendly  

---

## 📌 Contribution

- Fork the repo 🍴  
- Add your solution in respective problem folder  
- Ensure **README.md is updated** with approach and complexity  
- Submit a PR ✅  

---

## 🎯 Goals

- Strengthen **problem-solving skills**  
- Build a **solid reference repo** for future prep  
- Help others understand **different solution strategies**  

---

## 🔗 Resources

- [LeetCode](https://leetcode.com/)  
- [Big-O Complexity Cheatsheet](https://www.bigocheatsheet.com/)  
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

---

💡 *This repository is a work in progress and will keep growing as I solve more problems.*

