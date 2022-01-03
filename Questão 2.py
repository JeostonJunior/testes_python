n = int(input(" Digite um teto para a sequência de Fibonacci :"))
t1 = 1
t2 = 0
t3 = 0
t4 = []

while t1 <= n:
    t4.append(t1)
    t3 = t1 + t2
    t2 = t1
    t1 = t3

if n in t4:
    print("\nO número digitado está presente na sequencia de Fibonacci\n")
    print(t4)
else:
    print('\nO número digitado não está presente na sequencia de Fibonacci\n')
    print(t4)
1
