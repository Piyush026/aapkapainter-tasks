"""Write a code that prints out individual scores of two players in a game of cricket where score is given as runs per ball in an array. In a game of cricket a person changes strike if he scores an odd number, and keeps strike with him if he scores an even number. No need to consider changing strike after every 6 balls or an over.
Sample Input1: [1,2]
Output1: p1: 1, p2: 2
Sample Input2: [1,2,3,2,1]
Output2: p1: 4, p2: 5"""

s = [1, 2, 3, 2, 1]

p1 = 0
c1 = 0
p2 = 0
c2 = 0
for x in range(len(s)):
    if c1 == 0:
        if s[x] % 2 != 0:
            p1 += s[x]
            c1 = 1
        else:
            p1 += s[x]
            c1 = 0
    else:
        if s[x] % 2 != 0:
            p2 += s[x]
            c2 = 1
            c1 = 0
        else:
            p2 += s[x]
            c2 = 0
temp = {"p1": p1, "p2": p2}
print(temp)
