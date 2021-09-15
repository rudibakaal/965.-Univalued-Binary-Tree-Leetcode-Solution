# 965.-Univalued-Binary-Tree-Leetcode-Solution

## Motivation
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.


![image](https://user-images.githubusercontent.com/48378196/133423678-1a948b89-7e30-4ad1-a99d-3906d6336f84.png)

Input: root = [1,1,1,1,1,null,1]
Output: true

![image](https://user-images.githubusercontent.com/48378196/133423717-ec97e360-1491-4a83-bd93-d86453e17a17.png)

Input: root = [2,2,2,5,2]
Output: false


## Method
The instance variable 'start' in the 'isUnivalTree' class is used to capture the original root node value. This value is subsequently compared against all node values through preorder traversal. If any node encountered during this traversal differs from 'start', line 16 sets the instance variable 'status' of the 'isUnivalTree' class to False.


## Results 
This program outperforms 88.81% of Python online submissions for Univalued Binary Tree.

![image](https://user-images.githubusercontent.com/48378196/133424610-3f28e2a8-cea9-4d90-bead-8295d74a23f2.png)


## License
MIT

## References
https://leetcode.com/problems/univalued-binary-tree/submissions/
