# Berechnung der Fibonacci-Zahlen mit Hilfe von Memoization.
# Wir haben zuvor gesehen, dass eine naive Implementierung der Rekursionsformel
# für die Fibonacci-Zahl f(n) zu einer exponentiellen Laufzeit in n führt.
# Am Aufrufbaum erkennt man, dass dies auf die Mehrfachauswertung der Teilausdrücke
# zurückzuführen ist. Um diese Mehrfachauswertung zu vermeiden, verwenden wir ein
# Gedächtnis, in dem wir uns schon berechnete Fibonacci-Zahlen zu merken, damit wir
# diese bei erneutem Bedarf nicht nochmal erneut ausrechnen müssen.

# Das Gedächtnis realisieren wir in Form eines Feldes F, das mit den beiden
# ersten Fibonacci-Zahlen initialisiert ist.

F = [0, 1]


def fibMemo(n):
    # Wenn wir die n-te Fibonacci-Zahl ausrechen sollen, schauen wir zunächst
    # in unserem Gedächtnis nach, ob wir diese schon zuvor berechnet haben.
    if n < len(F):
        # Wir kennen den Wert der n-ten Fibonacci-Zahl schon und geben diesen zurück.
        return F[n]
    # Wir berechen die n-te Fibonacci-Zahl gemäß ihrer rekursiven Definition ...
    x = fibMemo(n - 2) + fibMemo(n - 1)
    # ... und merken uns den Wert im Gedächtnis.
    F.append(x)
    # Frage: Warum wird der Wert für die n-te Fibonacci-Zahl auf diese Weise im Feldeintrag F[n] gespeichert?
    return x


# Auf diese Weise reduziert sich die Laufzeit auf linear viele Operationen im Parameter n.
print(fibMemo(500))