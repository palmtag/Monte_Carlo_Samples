# VERA2 input problems

Problems described in CASL Report:

Godfrey, A., "VERA Core Physics Benchmark Progression Problem Specifications", Revision 4,
CASL Technical Report: CASL-U-2012-0131-004, August 29, 2014.

## Geometry Notes

Note that each fuel rod is described individually.
I realize these problems could have been set up with lattices and universes.
However, there are a couple of reasons for this.
The first is that that the automation to create these files is set up that way.
I've found that the lattices have trouble with more complicated geometry,
like inter-assembly gaps and BWR control blades and it is easier to model the pins explicitly.

## MCNP
The MCNP directory contains an auxilary text file (tmap) that helps 
map the tally numbers to the pin numbers.


## Typical Results

| Case         | MCNP     |         | OpenMC  |         | Serpent  |         |
|--------------|----------|---------|---------|---------|----------|---------|
| vera2a       | 1.180300 | 0.00004 | 1.18070 | 0.00002 | 1.180360 | 4.4E-05 |
| vera2b       | 1.182910 | 0.00004 | 1.18336 | 0.00002 | 1.183010 | 4.6E-05 |
| vera2c       | 1.173610 | 0.00005 | 1.17413 | 0.00002 | 1.173690 | 4.6E-05 |
| vera2d       | 1.165880 | 0.00004 | 1.16629 | 0.00002 | 1.165910 | 4.7E-05 |
| vera2e_py12  | 1.068960 | 0.00005 | 1.06951 | 0.00002 | 1.069080 | 6.0E-05 |
| vera2f_py24  | 0.975280 | 0.00005 | 0.97582 | 0.00002 | 0.975440 | 6.7E-05 |
| vera2g_aic   | 0.847380 | 0.00004 | 0.84804 | 0.00002 | 0.847333 | 8.3E-05 |
| vera2h_b4c   | 0.787290 | 0.00004 | 0.78801 | 0.00002 | 0.787547 | 9.0E-05 |
| vera2i       | 1.179410 | 0.00004 | 1.17986 | 0.00002 | 1.179540 | 4.4E-05 |
| vera2j       | 0.974650 | 0.00005 | 0.97507 | 0.00002 | 0.974534 | 6.8E-05 |
| vera2k_py24  | 1.019390 | 0.00005 | 1.01996 | 0.00002 | 1.019560 | 6.4E-05 |
| vera2l_ifba  | 1.018340 | 0.00005 | 1.01876 | 0.00002 | 1.018490 | 6.4E-05 |
| vera2m_ifba  | 0.938320 | 0.00005 | 0.93872 | 0.00002 | 0.938568 | 7.2E-05 |
| vera2n_waba  | 0.869010 | 0.00004 | 0.86951 | 0.00002 | 0.869196 | 7.8E-05 |
| vera2o_gad12 | 1.047020 | 0.00005 | 1.04747 | 0.00002 | 1.047110 | 5.9E-05 |
| vera2p_gad24 | 0.926680 | 0.00004 | 0.92700 | 0.00002 | 0.926739 | 7.2E-05 |

