# Large PWR problems 

* P9 is 2D full-core model of Watts Bar reactor taken from VERA report (see vera2 directory)
* Nuscale is a very simple representation of the equilibrium Nuscale SMR reactor

## Geometry Notes

Note that each fuel rod is described individually.
I realize these problems could have been set up with lattices and universes.
However, there are a couple of reasons for this.
The first is that that the automation to create these files is set up that way.
I've found that the lattices have trouble with more complicated geometry,
like inter-assembly gaps and BWR control blades and it is easier to model the pins explicitly.

![plot](./misc/p9.svg)
