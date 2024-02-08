
# 1.Implement the solutions and upload it to github

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

n = int(input("Enter n value to calculate the fibonacci series"))

output= fib(n)
print("The Fibonacci series for given n is:")
print( {output})

''' Output:
Enter n value to calculate the fibonacci series10
The Fibonacci series for given n is:
{55} '''

# Below is the Function call stack for the fun(5):

Basically Fibonacci Series is the sequence of numbers defined recursively by using the values of fib(n-1) and fib(n-2) 
and summing up their values in each iteration to generate the series.

In the above the algorithm if we pass the 'n' value as '5',the following are the recursive calls and function call stack:
fib(5):

fib(5) calls fib(4) and fib(3) #fib(5) -> fib(4) -> fib(3)
fib(4) calls fib(3) and fib(2) #fib(4) -> fib(3) -> fib(2)
fib(3) calls fib(2) and fib(1) #fib(3) -> fib(2) -> fib(1)
fib(2) calls fib(1) and fib(0) #fib(2) -> fib(1) -> fib(0)
fib(1) returns 1
fib(0) returns 0
####################################################################
fib(0) returns 0
fib(1) returns 1
fib(2) returns 1+0=1 #the sum of fib(1) and fib(0)
fib(3) returns 1+1=2 #the sum of fib(2) and fib(1)
fib(4) returns 2+1=3 #the sum of fib(3) and fib(2)
fib(5) returns 3+2=5 #the sum of fib(4) and fib(3)

And So finally the fib(5)=5 as by using the above recursive calls.


# 2.Prove the time complexity of the algorithms

In the above algorithm which is implemented for Fibonacci series, the Recursion is used. Basically, this algorithms
time complexity is defined by using the Recurrence relation that is T(n) = T(n-1) + T(n-2) + O(1), where T(n) represents the time
complexity to compute the Fibonacci series of number 'n'.

 Here,every recursive call produces two further recursive calls which leads to form a binary tree structure of
 these recursive function calls.Since, at each level of Recursion tree there are O(1) operations will take place for comparioson and 
 return statements.
 
 Eventually, the height of recusion tree is nothing but the equal to the input value n of the function.Therefore,
 the algorithms time complexity is O(2^n) which is exponential. This is mainly because that the  binary recusion tree has 2^n 
 nodes overall, As a result and at each level the comparison size will be getting doubled than the previous operations.

 As a result, this will lead to the inefficient behaviour and more time complexity for the larger values of n due to more number of
 exponential computations.


 # 3.Comment on ways you could improve your implementation (you dont need to do it just discuss it)

 As the algorithm uses the recursive calls and so it becomes inefficient for larger values due to its exponential time
 complexity that is O(2^n). We have lot of ways to optimize it and make it efficient.

 Few of them are like Momoization,iterative approach and dynamic programming. Memoization is one of the way to increase the 
 efficiency of Fibonacci series algorithm.This is the process of storing the output of recursive function calls and returns
 it with same inputs further.Due to this, unnecessary computations are reduced, and the time complexity is greatly decreased
 resulting in a linear time complexity of O(n).

 Where as with the use of dynamic programming, by using optimal time and space usage can be achieved by dividing the 
 problem into smaller subproblems and solving them iteratively.And these two results in a linear time complexity of O(n).
 This will depends on factors such as input size.