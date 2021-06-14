# This is basically sliding window template
# Example - longest sub-array with sum  not exceeding 's'

"""
 Window sizing:

1. slowly move both boundaries to the right
2. as we move right pointer - if sum of the new segment is no more than s :
    then we can leave the left border in place
    It makes no sense to move it forward, since the current segment is already getting generated
3. If we added a right element and sum becomes more than s, then we move the left element forward
    Keep moving left forward until, the sum of the segment, becomes less than or equal to x
"""
"""
Some more notes:
1. It's easy to move the right border with for loop 
        easy to move left border with while loop

Some pseudo code for sliding window template = { for sum no more than s } :

sum = 0
L, R = 0, 0
res = 0

for R = 0.. n-1
   sum += arr[R]
   while sum > s:
     sum -= arr[L]
     L++
   res = max(res, R-L+1)

"""
"""
Now, consider the other scenario:
If we want to find a segment with a sum greater than or equal to s 
(in this case, the length of the segment, on the contrary, needs to be minimized), 
shortest subarray with sum greater than or equal to s.


sum = 0
L, R = 0, 0

for R = 0..n-1:
   sum += arr[R]
   
   while sum - A[L] >= s:
        sum -= arr[L]
        L++
    if sum >= s:
       res = min(res, R-L+1)

"""

"""
One more variant:
One more modification is to find the number of segments, the sum of elements on which does not exceed s

Funda:
If we have fixed r and found the minimum l such that the sum on the segment [l;r] does not exceed s, 
then there are exactly r−l+1 possible segments with such a right boundary.

x = 0, L = 0
for R = 0..n-1
    x += a[R]
    while x > s:
        x -= a[L]
        L++
    res += R - L + 1

"""

"""
Suppose you received a problem at the contest in which you need to do something similar: 
find the longest (shortest) good segment or count the number of good segments.
How do you know if you can apply the two-pointer method to it?

First, one of the following two properties must be met:

if the segment [L,R] is good, then any segment nested in it is also good 
(in this case, you can apply the code from the first problem);

if the segment [L,R] is good, then any segment that contains it is also good 
(in this case, you can apply the code from the second problem). 

Secondly, you should be able to recalculate your function 
(check if current segment is good or bad), while moving the left or right border by one to the right.

In such tasks, the code almost always looks like this:

L = 0
for R = 0..n-1
    add(a[R])
    while not good():
        remove(a[L])
        L++

To solve such contests, you need to implement three functions: add, remove, and good. 

"""