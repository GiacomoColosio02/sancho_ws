# SANCHO — Battery Rover Software

Software ROS 2 del rover SANCHO per il progetto Design & Robotics (Politecnico di Milano, 14ª edizione, Gruppo 3 — Earthquakes).

## Struttura

- `sancho_perception/` — nodo di visione (camera + line detection)
- `sancho_control/` — logica decisionale (PID + state machine)
- `sancho_bridge/` — interfaccia hardware Arduino
- `sancho_bringup/` — launch files e configurazione

## Stack

- ROS 2 Humble (sviluppo su laptop Ubuntu 22.04)
- ROS 2 Jazzy dentro Docker (deploy su Arduino UNO Q)
- Python 3 + OpenCV + Arduino Bridge

## Setup

Istruzioni di installazione in arrivo.