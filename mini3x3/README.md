# Mini 3x3 PWR with Gad

Purpose: generate sample 8-group multigroup cross sections for
representative fuel and gad fuel rods

Problem consists of:
* dimensions based on VERA problem "2o" (Watts Bar)
* 3x3 rod geometry
* gad rod in the center, fuel on the outside
* 8-group cross section edits

Material numbers correspond to the following regions:
* MAT13 fuelgad
* MAT16 fuel   - no gad
* MAT17 gap
* MAT18 clad
* MAT28 cool

## Results: 
* OpenMC  Version | 0.15.0
* ENDFB-VII.1
* Combined k-effective = 0.88459 +/- 0.00006


