import math
def numSquares( n: int) -> int:
    # https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
    while (n & 3) == 0:
        n >>= 2  # 4^a part
    if (n % 8) == 7:  # check if is 4^a(8b + 7)
        return 4

    if int(math.sqrt(n)) ** 2 == n:
        return 1
    # check if the number can be represented as the sum of three squares of integers
    for i in range(int(math.sqrt(n)), 0, -1):
        if int(math.sqrt(n - i * i)) ** 2 == n - i * i:
            return 2
    # worst case from the three-square theorem
    return 3

print(numSquares(20))
print(10 & 2)
print(100 & 3)

def numSquares(paths, perfectSqNums, n):
    if (paths.get(n)):
        return paths[n]
    min =190000000
    thisPath = 0
    import math
    for i in range(0, len(perfectSqNums)):
        if (n - perfectSqNums[i] >= 0):
            difference = n - perfectSqNums[i]
            thisPath = numSquares(paths, perfectSqNums, difference)
            min = math.min(min, thisPath)
    min+=1
    paths[n] = min
    return min

def howManySquares(n):
    perfectSqNumsLength = 1

    while (perfectSqNumsLength * perfectSqNumsLength < n):
        perfectSqNumsLength+=1
    if (perfectSqNumsLength * perfectSqNumsLength > n) :
        perfectSqNumsLength-=1
    perfectSqNums = []

    for i in range(perfectSqNumsLength - 1, 0, -1):
        perfectSqNums[perfectSqNumsLength - i - 1] = (i + 1) * (i + 1)

    paths = {}
    paths[1] = 1
    paths[0] = 0
    return numSquares(paths, perfectSqNums, n)


#howManySquares(17)

# nfunction howManySquares(n) {
#   let perfectSqNumsLength = 1;
#   while (perfectSqNumsLength * perfectSqNumsLength < n) {
#     perfectSqNumsLength++;
#   }
#
#   if (perfectSqNumsLength * perfectSqNumsLength > n) {
#     perfectSqNumsLength--;
#   }
#
#   const perfectSqNums = [];
#
#   // Fill the array backwards so we get the numbers to work with
#   for (let i = perfectSqNumsLength - 1; i >= 0; i--) {
#     perfectSqNums[perfectSqNumsLength - i - 1] = (i + 1) * (i + 1);
#   }
#
#   // instantiate a hashmap of possible paths
#   const paths = {};
#   paths[1] = 1; // 1 = 1
#   paths[0] = 0; // 0 means you need 0 numbers to get 0
#
#   return numSquares(paths, perfectSqNums, n);
# }


#
#
#
#   for (let i = 0; i < perfectSqNums.length; i++) {
#     if (n - perfectSqNums[i] >= 0) {
#       const difference = n - perfectSqNums[i];
#       // this is key - recursively solve for the next perfect square
#       // that could sum to n by traversing a graph of possible perfect square sums
#       thisPath = numSquares(paths, perfectSqNums, difference);
#
#       // compare the number of nodes required in this path
#       // to the current minimum
#       min = Math.min(min, thisPath);
#     }
#   }
#
#   min++; // increment the number of nodes seen
#   paths[n] = min; // set the difference for this number to be the min so far
#
#   return min;
# }
