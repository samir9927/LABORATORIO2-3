def main(args):
    sc = Scanner(System.in_)
    num = None
    condition = True
    while condition:
        System.out.print("Introduce un número entero >=0 ")
        num = sc.nextint()
        condition = num<0
    System.out.println("2 ^ " + num + " = " + potencia(num))
def potencia(n):
    if n == 0: #caso base
        return 1
    else:
        return 2 * potencia(n-1)
print(potencia(4))