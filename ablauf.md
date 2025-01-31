[api](https://djitellopy.readthedocs.io/en/latest/)

# P01_simpleTakeoffAndLanding
## Ziele
- Drohne connecten
- Drohne starten und landen
## Neue Befehle
- `from djitellopy import Tello`
- `tello = Tello()`
- `̀tello.connect()`
- `tello.takeoff()` 
- `tell.land()`
- `print()`

# P02_moveAround
## Ziele
- Starten 
- "Durch den raum fliegen"
- Landen
## Neue Befehle
- `tello.move_left(centimeters)` <- mindestens 20cm maximal 500cm
- `tello.move_right(centimeters)`
- `tello.move_forward(centimeters)`
- `tello.move_back(centimeters)`
- `tello.move_up(centimeters)`
- `tello.move_down(centimeters)`
- `tello.rotate_clockwise(degree)` <- 1-360
- `tello.rotate_counter_clockwise(degree)`

# P03_Dance
## Ziele
Durch den Raum bewegen mit ein paar aktionen verbinden. Ablauf mit schleifen steuern.
## Neue Befehle
- `for i in Range():`
- `while <Value> == True:`
- `flip_back()`
- `flip_forward()`
- `flip_right()`
- `flip_left()`

# P04_Input_Dance
## Ziele
Mithilfe der input funktion und match case den ablauf der aktionen angeben. Alles in einer Endlosschleife
Datentyp String kennenlernen und liste erkennen
## Neue Befehle
- `value = input(text)`
-
```
match(value):
    case 'l':
        # do something
    case 'b'
        # do something different  
```
- `flip(direction)` l,r,f,b
- `move(direction, distance)` up,down,left,right,forward,back
## unteraufgaben
### `input()` und `print()`
Mithilfe der input funktion einen text einlesen in einer variable speichern und wieder ausgeben.
### `for s in str:` und str[]
Ausgabe der einzelnen Buchstaben des strings in einzelnen zeilen.
### `Match Case`
Je nachdem welcher buchstabe geschrieben steht soll etwas anderes gemacht werden.
Mehrere buchstaben gleichzeitig in einem statement verwenden.
### Ende
Mit dem input `UUlLFbBUfdd` soll die Drohne zwei mal hoch fliegen, dann einen Flip nach links, nach Links fliegen, nach vorne Fliegen, einen rückwärts flip machen, nach hinten fliegen, nach oben fliegen, einen front flip machen und dann zweimal nach unten fliegen.
Das in richtungen fliegen soll jedes mal mit der mindestdistanz passieren.


