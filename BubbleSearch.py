arrayToSearchFor = []
valueToSearch = ''

n = len(arrayToSearchFor)
# Zu Beginn setzen wir die linke Grenze des Suchintervalls auf die Listenposition 0
# und die rechte Grenze auf die Position des Listenendes.
left = 0
right = n - 1

# Solange das Suchintervall nicht leer geworden ist, setzen wir die Suche fort.
while left <= right:
    # Wir berechnen die Mitte des Suchintervalls.
    mitte = (left + right) // 2
    # Wir geben zur Kontrolle das Wort in der Mitte des aktuellen Suchintervalls aus.
    print(arrayToSearchFor[mitte])

    # Wir entscheiden, ob wir die Suche links von der Mitte fortsetzen sollen.
    if valueToSearch < arrayToSearchFor[mitte]:
        # und passen dementsprechend die neue rechte Grenze an.
        right = mitte - 1
    # Wir überprüfen, ob wir die Suche rechts der Mitte fortsetzen sollen.
    elif valueToSearch > arrayToSearchFor[mitte]:
        # und passen die neue linke Grenze an.
        left = mitte + 1
    else:
        # Wir haben das Suchwort gefunden
        gefunden = True
        # und können die Suche abbrechen.
        break
else:
    # Das Suchwort konnte nicht gefunden werden.
    gefunden = False
