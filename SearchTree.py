"""
Die Klasse Baumknoten dient zur Repräsentation eines Knotens eines
binären Suchbaumes. Ein binärer Suchbaum hat die Eigenschaft, dass
alle Schlüsseleinträge im linken Unterbaum eines Knotens kleiner
(oder gleich) als der Schlüssel des betrachteten Knotens sind und alle
Schlüssel des rechten Unterbaums größer als dieser Schlüssel sind.
Mit Hilfe der Memberfunktionen dieser Klasse kann der Unterbaum
unterhalb eines Baumknotens zu verschiedenen Zwecken durchmustert werden.
"""


class Node:
    # Ein Knoten des Suchbaumes beinhaltet einen Schlüssel und den damit
    # verbundenen Inhalt. Desweiteren zwei Verweise auf die (Wurzel)Knoten
    # des linken und rechten Teilbaumes.
    def __init__(self, schluessel, inhalt):
        self.key = schluessel
        self.value = inhalt
        self.left = self.right = None

    # Eine Memberfunktion zum Einfügen eines neuen Baumknotens (knoten).
    def add(self, knoten):
        # Wenn der Schlüssel des einzufügenden Knotens gleich dem Schlüssel
        # des betrachteten Baumknotens (self) ist,
        if knoten.key == self.key:
            # überschreiben wir den alten Inhalt mit dem neuen.
            self.value = knoten.value
            return
        # Wenn der Schlüssel des einzufügenden Knotens kleiner ist als der Schlüssel
        # des betrachteten Baumknotens (self), verzweigen wir in den linken Unterbaum.
        if knoten.key < self.key:
            if self.left is None:
                # Wenn der linke Kindknoten nicht existiert, können wir dort den neuen
                # Knoten einfügen.
                self.left = knoten
            else:
                # Wenn der linke Kindknoten existiert, delegieren wir die Einfügeoperation
                # an diesen Knoten (self.links) durch einen rekursiven Aufruf.
                self.left.add(knoten)
        else:  # Analog für den rechten Unterbaum
            if self.right is None:
                self.right = knoten
            else:
                self.right.add(knoten)

    # Eine Memberfunktion zum Suchen eines Knotens mit dem Schlüssel schluessel.
    def search(self, key):
        if key == self.key:
            return self.value
        if key < self.key:
            if self.left is None:
                return None
            return self.left.search(key)
        else:
            if self.right is None:
                return None
            return self.right.search(key)

    # Erzeuge eine Zeichenkette für alle Schlüssel des Unterbaumes unterhalb des
    # aktuellen Knotens in sortierter Reihenfolge (Inorder).
    def __str__(self):
        s = ''
        # Wenn ein linker Unterbaum existiert, erzeugen wir eine sortierte Ausgabe
        # für alle Schlüssel in diesem Teilbaum.
        if self.left is not None:
            s += str(self.left)
        # Dann geben wir den Schlüssel des betrachteten Knotens (self) aus.
        s += str(self.key) + ' '
        # Anschließend die Schlüssel im rechten Unterbaum, sofern dieser existiert.
        if self.right is not None:
            s += str(self.right)
        return s


class SearchTree:
    def __init__(self):
        self.root = None

    def add(self, key, value):
        node = Node(key, value)
        if self.root is None:
            self.root = node
        self.root.add(node)

    # Suche nach einem Baumknoten, dessen Schlüssel dem Suchschlüssel entspricht.
    def search(self, key):
        if self.root is None:
            return None
        return self.root.search(key)

    # Überladen der str-Funktion zur sortierten Ausgabe des gesamten Suchbaumes.
    def __str__(self):
        if self.root is None:
            return ''
        # Wir deligieren die Arbeit an den Baumknoten wurzel.
        return str(self.root)


'''
L = [25,34,27,12,38,18,10,21,46,5,14,20,15,35,23,8,42]

S = Suchbaum()
for x in L:
    S.einfuege(x,x)
print(S)

print(S.suche(44))
'''
S = SearchTree()

datei = open('Woerterbuch.txt', encoding='utf-8')

for zeile in datei:
    wort = zeile.split('\t')
    S.add(wort[0], wort[1])

datei.close()

while True:
    wort = input('de = ')
    print(S.search(wort))
