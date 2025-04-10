# P07_rcControll

## Ziele
- Die Drohne mit Hilfe der Tastatur steuern.
- Landen und starten soll ebenfalls mit der tastatur erfolgen.
- Kennenlernen einer neuen Bibliothek (pynput)
- Einführung von Dictionarys
- Einführung von Funktionen
- Kennenlernen des ActionListener Pattern

## Neue Befehle
- send_rc_control(left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity)
- from pynput.keyboard import Listener
- <Variable> = {<KEY1>:<VALUE1>, <KEY2>:<VALUE2>,...}
- def <FUNCTION_NAME>(<PARAMETER1>, <PARAMETER2>, ...):
- listener = Listener(on_press=<ON_PRESS_FUNCTION>, on_release=<ON_RELEASE_FUNCTION>)
- listener.start()

## Hinweiß
Damit diese Aufgabe funkitoniert, kann es sein, dass die Bibliothek `pynput` noch mit `pip install pynput` installiert werden muss.
