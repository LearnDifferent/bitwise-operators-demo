"""
Left Shift: <<  左移
Right Shift: >>  右移

左移和右移就是 shift the bits of a number either left or right，
然后移出去的就舍弃，空出来的位置就补 0
"""
# 5 的二进制是 0000 0101，左移 2 位就是 0001 0100，也就是 20
print(5 << 2)
# 同理，向右移 2 位就从 0000 0101 变为 0000 0001，也就是 1
print(5 >> 2)
