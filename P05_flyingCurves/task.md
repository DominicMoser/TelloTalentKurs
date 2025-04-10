# P05_flyingCurves
## Ziele
- Die Drohne Kurven fliegen lasse.

## Neue Befehle
- curve_xyz_speed(x1, y1, z1, x2, y2, z2, sped)

## Mögliche Probleme
Für das fliegen von Kurven gibt es einige Einschränkungen:
- Die Aktuelle Position der Drohne und der Punkte p1 und p2 müssen eine Kreiskurve ergeben.
- Der Radius der Kreiskurve muss zwischen 50 cm und 10 Meter liegen.
- Die Werte der x,y und z werten müssen zwischen -500 und 500 liegen, dürfen jedoch nicht kleiner als -20 und 20 sein, außer sie sind 0. Das liegt daran, dass die Mindestdistanz für Bewegungen bei 20 cm liegt.