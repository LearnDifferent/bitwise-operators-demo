"""
XOR Operator (Exclusive OR Operator): ^  异或

Exclusive OR 类似与 !=（不等于），当两边结果不想等时，为 true，也就是 1；当两边想等就为 false，也就是 0

Exclusive 是「排他」或「独立」的意思，Exclusive OR 表达的就是 A or B is exclusive，A 或 B 是排他的，A 或 B 是独立的。
"""

READ_PERMISSION = 4
WRITE_PERMISSION = 2
EXECUTE_PERMISSION = 1

"""
| 5 | 6 | 5 ^ 6 |
-----------------
| 1 | 1 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |

所以 5 ^ 6 就是二进制的结果 011，也就是 3
"""

# We can use the exclusive OR operator to remove a permission from an existing permissions set.
# e.g. The user has read, write permissions, but you want to remove the write permissions from the user.

userPermissions = READ_PERMISSION | WRITE_PERMISSION
print("The user has read, write permissions:")
print(userPermissions)

print("Remove the write permissions from the user:")
userPermissions ^= WRITE_PERMISSION
print(userPermissions)
