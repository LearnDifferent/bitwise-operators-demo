"""
NOT Operator: ~  取反
0 变 1，1 变 0，类似于编程中的 !boolean

理论上，5 的二进制是 101，~5 的结果就是 010
As Python uses an 8 bit number to represent small numbers.
Five is going to look like 0000 0101 in binary.
If we use the NOT operator, all of the bits get reversed and therefore it becomes 1111 1010.
第 0 位置存储正负符号，所以最后会变成负数的 -6
"""
print(~5)
