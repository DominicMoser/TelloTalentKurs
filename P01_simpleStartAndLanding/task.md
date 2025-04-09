# P01_simpleTakeoffAndLanding

## Ziele
- Sich mit der Drohne verbinden.
- Drohne starten und landen

## Neue Befehle
- `from djitellopy import Tello`
- `tello = Tello()`
- `tello.connect()`
- `tello.takeoff()` 
- `tell.land()`
- `print()`

## Mögliche Probleme
- `tello.connect()` gibt einen fehler aus wenn die firewall nicht richtig eingestellt ist. Wenn dies der fall ist reicht fürs erste statt `tello.connect()` `tello.connect(False)` zu benutzen