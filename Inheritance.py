import math


# Die Basisklasse zur Repräsentation einer geometrischen Form
class GeoForm:
    # Der Konstruktor
    def __init__(self, f, x, y):
        # Initialisierung der Attribute farbe und der Koordinaten (cx,cy) des Referenzpunktes
        self.color = f
        self.cx = x
        self.cy = y

    # Eine Methode zum Verschieben des Referenzpunktes der geometrischen Form
    def move(self, dx, dy):
        self.cx += dx
        self.cy += dy

    # Überladen der str-Funktion
    def __str__(self):
        return ('Ich bin eine GeoForm mit Farbe ' + self.color + ' und den Koordinaten ' + str(self.cx) + ' ' + str(
            self.cy))


# Ableitung einer neuen Klasse Rechteck von der Basisklasse GeoForm
class Rectangle(GeoForm):

    def __init__(self, f, x, y, height, width):
        # Durch den Methodenaufruf super() haben wir Zugriff auf die Attribute und Methoden der Basisklasse.
        # Wir rufen den Konstruktor der Basisklasse GeoForm auf.
        super().__init__(f, x, y)
        # Wir setzen die Länge und Breite des Rechtecks als zwei weitere Attribute fest.
        self.height = height
        self.width = width

    # Eine Methode zur Berechnung der Fläche des Rechtecks.
    def area(self):
        return self.height * self.width

    # Wir überladen die str-Funktion der Basisklasse.
    def __str__(self):
        return ('Ich bin ein Rechteck mit Farbe ' + self.color + ' und den Koordinaten ' + str(self.cx) + ' ' + str(
            self.cy))


# Ableitung der Klasse Raute von GeoForm analog zu Rechteck
class Raute(GeoForm):
    def __init__(self, f, x, y, l, phi):
        super().__init__(f, x, y)
        self.laenge = l
        self.winkel = phi

    def area(self):
        return self.laenge * self.laenge * math.sin(self.winkel * math.pi / 180.0)

    def __str__(self):
        return ('Ich bin ein Raute mit Farbe ' + self.color + ' und den Koordinaten ' + str(self.cx) + ' ' + str(
            self.cy))


# Ableitung der Klasse Ellipse von GeoForm analog zu Rechteck
class Ellipse(GeoForm):
    def __init__(self, f, x, y, a, b):
        super().__init__(f, x, y)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b * math.pi

    def __str__(self):
        return ('Ich bin ein Ellipse mit Farbe ' + self.color + ' und den Koordinaten ' + str(self.cx) + ' ' + str(
            self.cy))


# Ableitung der Klasse Kreis von der Basisklasse Ellipse, die ihrerseits von GeoForm abgeleitet ist.
class Kreis(Ellipse):
    def __init__(self, f, x, y, r):
        super().__init__(f, x, y, r, r)

    def __str__(self):
        return ('Ich bin ein Kreis mit Farbe ' + self.color + ' und den Koordinaten ' + str(self.cx) + ' ' + str(
            self.cy))


# Ableitung der Klasse Quadrat von der Basisklasse Rechteck, die ihrerseits von GeoForm abgeleitet ist.
# Eine Mehrfachvererbung
# class Quadrat(Rechteck,Raute):
# ist möglich, führt in diesem Beispiel aber zu Konflikten bei den Konstruktoraufrufen.
# Näheres zu dieser Problematik siehe MRO (Method Resolution Order).
class Quadrat(Rectangle):
    def __init__(self, f, x, y, height):
        super().__init__(f, x, y, height, height)

    def __str__(self):
        return ('Ich bin ein Quadrat mit Farbe ' + self.color + ' und den Koordinaten ' + str(self.cx) + ' ' + str(
            self.cy))


# Aufruf des Konstruktors für ein Quadrat.
Q = Quadrat('rot', 0.0, 0.0, 1.0)
# Flächenberechnung für das Quadrat Q. Die Quadrat-Klasse verfügt selbst nicht über die Member-Funktion flaeche.
# Sie erbt diese Funktion von ihrer Basisklasse Rechteck.
print(Q.area())
# Aufruf der verschiebe-Funktion. Diese ist über die Rechteck-Klasse von deren Basisklasse GeoForm geerbt worden.
Q.move(1.0, 2.0)
# Ausgabe aller geerbten und eigenen Attribute in Form des internen Dictionaries,
# das zur Verwaltung der Attribute dient.
print(Q.__dict__)
