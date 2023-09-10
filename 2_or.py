"""
OR Operator: |  或
类似的，| 可以类比 ||，二进制的 0 可以类比 false，二进制的 1 可以类比 true，也就是两边是否有一个为 true
当 0 | 1 的时候，可以类比 false || true，其结果就是 true，也就是 1
当 0 | 0 的时候，就是 false，即 0
当 1 | 1 的时候，就是 true，即 1

| 5 | 6 | (5 | 6) |
-----------------
| 1 | 1 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |

所以 5 | 6 就是二进制的 111，也就是 7
"""

READ_PERMISSION = 4
WRITE_PERMISSION = 2
EXECUTE_PERMISSION = 1

"""
Use the OR operator to combine multiple permissions.
也就是将 2 个权限合并为一个新的权限
"""
# 这里是将 R 和 W 的权限都赋给 User
userPermissions = READ_PERMISSION | WRITE_PERMISSION

# 得到的结果就是将 [R][W][X] 中的 100(R) 和 010(W) 进行 OR 运算，得到 110，也就是 6
print(userPermissions)
