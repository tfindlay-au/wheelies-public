## Objective
This folder contains a schematic and PCB to construct a device
that will capture movement from a sensor.

This project will evolve over time, I will attempt to describe time
as phases of development.

### Phase 1
Design a PCB based off the Serpente R2 by Arturo182. The SAMD21 processor
is low power and simple to use and has Circuit Python available.

The Serpente project also provides open source schematic and PCB to get started
with.

The result of this phase is to have a working PCB produced with the addition of
a built-in motion sensor.

### Phase 2
Expanding on the learnings of Phase1, this will attempt to resolve
the issues. Namely:

1. Schematic fault with capacitor C9 which stops the board getting power without hacking away at it.
2. The omission of a LiPo charging circuit is an impediment to the devices use.
3. The on/off switch for the battery operation incorrectly spec'd as through-hole(THT) rather than Surface mount (SMD)

### Phase 3
With a usable device from phase 2, we now expand on its functionality
to provide feedback via LED's / Screen / Buzzer

## Getting started
The PCB is designed in KiCad and is tied to a nightly build. You must use this same version to open these files.

## Getting it made
To use an external service you will need to export a Gerber bundle and a bill of materials (BOM) file.
