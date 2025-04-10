from djitellopy import Tello

myDrone = Tello()
myDrone.connect()

# Hilfe text zum erklären der input möglichkeiten.
print("Folgende möglichkeiten stehen für saltos zur verfügung: l(leftflip),r(rightflip),f(frontflip),b(backflip)")
print("Folgende möglichkeiten stehen für bewegungen zur verfügung: L(left),R(right),F(forwards),B(backwards),D(downwards),U(upwards)")
print("Mit q kann das Programm beendet werden.")
print("Mehre bewegungen können einfach hintereinander angegeben werden. zb: llrUDR")

# Endlosschleife. Kann mit dem break Befehl beendet werden.
while True:
    # Einlesen von Usertext in die Variable sequence.
    sequence = input("Bitte gebe ein was die Drohne machen soll:")
    # Wenn die Eingabe nur "q" ist soll das Programm beendet werden.
    if sequence == "q":
        # Beendet der Schleife.
        break
    # Starten der Drohne
    myDrone.takeoff()
    # Für jeden buchstaben in der Variable sequence wird folgendes ausgeführt. Jeder durchlauf kann über die
    # Variable c auf den aktuellen Buchstaben zugreifen.
    for c in sequence:
        # Testen welcher Buchstabe es ist.
        match(c):
            # Wenn es ein "L" ist mache:
            case "L":
                myDrone.move_left(20)
            # Wenn es ein "R" ist mache:
            case "R":
                myDrone.move_right(20)
            # Wenn es ein "F" ist mache:
            case "F":
                myDrone.move_forward(20)
            # Wenn es ein "B" ist mache:
            case "B":
                myDrone.move_back(20)
            # Wenn es ein "D" ist mache:
            case "D":
                myDrone.move_down(20)
            # Wenn es ein "U" ist mache:
            case "U":
                myDrone.move_up(20)
            # Wenn es ein "l", "r", "f" oder "b" ist mache:
            case "l" | "r" | "f" | "b":
                # Führe einen Flip aus. Mithilfe des Parameters c, welcher l, r, f oder b ist, wird die Richtung bestimmt.
                # Nachzulesen in der API.
                myDrone.flip(c)
    # Drohne landen.
    myDrone.land()

# Die selbe Schleife nochmal, dieses mal jedoch mit if-elif anstelle von match case.
while True:
    sequence = input("Bitte gebe ein was die Drohne machen soll:")
    if sequence == "q":
        break
    myDrone.takeoff()
    for c in sequence:
        if c == "l" or c == "r" or c == "f" or c == "b":
            myDrone.flip(c)
        elif c == "L":
            myDrone.move_left(20)
        elif c == "R":
            myDrone.move_right(20)
        elif c == "F":
            myDrone.move_forward(20)
        elif c == "B":
            myDrone.move_back(20)
        elif c == "D":
            myDrone.move_down(20)
        elif c =="U":
            myDrone.move_up(20)
    myDrone.land()
            
    

# Neuen Code hier einfügen.
