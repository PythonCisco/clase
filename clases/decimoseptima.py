
"""
numeros binarios
"""

"""
101
010 +
___
111

0123456789
01

111
0111
0001 +
___
1111

  321
2^
 8421
  001=4*0 + 2*0 + 1*1=1
  010=4*0 + 2*1 + 1*0=2
  011=4*0 + 2*1 + 1*1=3
 1010=8*1 + 4*0 + 2*1 + 1*0 = 10
 0101=8*0 + 4*1 + 2*0 + 1*1 = 5
 1001=8*1 + 4*0 + 2*0 + 1*1 = 9
 0110=                      = 6
  100

3214324232433213212
1010101010101111010

6  5  4  3 2 1 0
64 32 16 8 4 2 1
1  0  1  0 0 0 1 = 64*1 + 32*0 + 16*1 + 8*0 + 4*0 + 2+0 + 1*1 = 81

2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64

11
489
134 +
623

 11
1011
0011 +
1110

  1 111
  110011
  010111 +
  ______
 1001010

12456
10111
1                                      11
 1111 1111  1111 1111  1111 1111  1111 1111
 0000 0000  0000 0000  0000 0000  0000 0001
 0000 0000  0000 0000  0000 0000  0000 0001 0000 0000  0000 0000  0000 0000  0000 0000


byte = 8 bits

1010 >>
0101 >>
0010 <<
0100 <<
1000

0100 >>
0010 >>
0001 <<
0010

0001 >>
0000 <<
0000

0101 >>
0010 <<
0100

101010
111111 &
101010

1001
0011 &
0001

&
11 1
10 0
01 0
00 0

|
11 1
10 1
01 1
00 0

iff
11 1
10 0
01 0
00 1

^
11 0
10 1
01 1
00 0


"""