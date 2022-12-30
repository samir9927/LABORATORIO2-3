import time
def fibonacci_recursivo(n):
    if n == 0 or n ==1:
        return 1
    else:
        return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)
tiempo1=time.perf_counter()
fibonacci_recursivo(12)
tiempo2=time.perf_counter()
print("El Fibonacci recursivo demoró: ",tiempo2-tiempo1)