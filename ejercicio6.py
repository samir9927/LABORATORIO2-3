def pasos(n):
    if n ==1 or n==2:
        return n
    else:
        return pasos(n-1)+pasos(n-2)
print(pasos(5))