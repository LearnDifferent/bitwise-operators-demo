"""
We have seen Unix file permissions with things like 644 or 777.
These 3 numbers make up the different groups, for the permissions on the Unix filesystem.
The first number will be the owner,
the second number will be the group they belong to,
and the third number will be everyone else.

每一组权限的数字，实际上是二进制的 [R][W][X] 转换为十进制的结果。
十进制的 7 转换为二进制的 111，表示 R W X 都是 1，这里的 1 可以理解为 true，也就表示拥有所有权限。
十进制的 6 转换为二进制的 110，表示 R W 都是 1，X 为 0，表示可以 read 和 write，但是不能 execute。
"""

# 假设只有读的权限，那么 [R] 的位置就是 1，[W][X] 都是 0，也就是 100，换成十进制就是 4
READ_PERMISSION = 4
# 假设只有写的权限，那么 [W] 的位置就是 1，[R][X] 都是 0，也就是 010，换成十进制就是 2
WRITE_PERMISSION = 2
# 假设只有执行的权限，那么 [X] 的位置就是 1，[R][W] 都是 0，也就是 001，换成十进制就是 1
EXECUTE_PERMISSION = 1

"""
AND Operator: &  与

& 可以类比 &&，二进制的 0 可以类比 false，二进制的 1 可以类比 true。
当 0 & 1 的时候，可以类比 false && true，也就是两边是否都为 true，其结果就是 false，也就是 0
当 0 & 0 的时候，就是 false，即 0
当 1 & 1 的时候，就是 true，即 1

假设是十进制的 7 & 6，转换为 truth table 就是：
| 7 | 6 | 7 & 6 |
-----------------
| 1 | 1 | 1 |
| 1 | 1 | 1 |
| 1 | 0 | 0 |

所以 7 & 6 就是二进制的 110，也就是 6
"""
# current user permissions variable
userPermissions = 6

# Going back to file permission example, the AND operator can actually be used
# as a test to see if the user has permissions to do something
if (userPermissions & READ_PERMISSION) == READ_PERMISSION:
    print("Can Read")
else:
    print("Cannot Read")

print(userPermissions & READ_PERMISSION)
# 执行的时候，使用 `python3 file.py`
