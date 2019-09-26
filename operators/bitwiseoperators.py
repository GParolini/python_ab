#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:50:03 2019

@author: giudittaparolini
"""

'''
Bitwise operators
Python Bitwise Operators take one to two operands, and operate on it/them bit by bit
'''

'''
Bitwise AND (&)
1 has a Boolean value of True, and 0 has that of False
0 & 0	0
0 & 1	0
1 & 0	0
1 & 1	1


Bitwise OR (|)
returns 1 even if one of the two corresponding bits from the two operands is 1
0|0	0
0|1	1
1|0	1
1|1	1

Bitwise XOR (eXclusive OR) (^)
returns 1 if one operand is 0 and another is 1. Otherwise, it returns 0.
0^0	0
0^1	1
1^0	1
1^1	0

Bitwise 1’s Complement (~) or NOT
~x is the same as -x-1

Bitwise Left-Shift Operator (<<)
shifts the bits of the number by the specified number of places. This means it adds 0s to the empty least-significant places now.

Bitwise Right-Shift Operator (>>)
shifts the bits to the right by the specified number of places. 

'''

a = 10
b = 4

print(bin(a)) #0b1010
print(bin(b)) #0b100

# &
print(a&b) #Result 0

# |
print(a|b) #Result 14

# ~
print (~a) #Result -11

# ^
print(a^b) #Result 14

# >>
print(a>>2) #Result 2 (bin is 0010)

# <<
print(a<<2) #Result 40 (bin is 101000)