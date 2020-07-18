import random

n = 100
a = []
for i in range(0, n):
    x = random.randint(0, 100)
    a.append(x)

print(a)

for i in range(1, n):  # i steht für den Phasenzähler
    # Wir führen eine Kaskade von Vergleichen benachbarter Elemente durch.
    # Man beachte, dass in der i-ten Phase nur n-i Vergleiche nötig sind.
    for j in range(0, n - i):  # j steht für den Vergleichszähler
        if a[j] > a[j + 1]:
            # Tausch der Werte zwischen den Variablen a[j] und a[j+1]
            hilf = a[j]
            a[j] = a[j + 1]
            a[j + 1] = hilf

print(a)
