# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. 
# Return an array of the results.

N = int(input())
numbers = list()
counts = list()

for i in range(0,N):
    numbers.append(input())

Q = int(input())
for i in range(0,Q):
    checkstring = input()
    count = 0
    for num in numbers:
        if num == checkstring:
            count = count + 1
    counts.append(count)
    
for count in counts:
    print(count)