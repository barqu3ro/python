def fibonacci(n):
    def _fibonacci(n, memo={0:0,1:1}):
        if n not in memo:
            memo[n] = _fibonacci(n-1, memo) + _fibonacci(n-2, memo)
        return memo[n]
    return [_fibonacci(i) for i in range(n)]

result = fibonacci(10)
print("The first 10 numbers in the Fibonacci sequence: ", result) 