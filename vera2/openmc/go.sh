#!/bin/bash

date

conda activate openmc-env

export OMP_NUM_THREADS=12

echo "OpenMC Driver script"
echo "cross section file: $OPENMC_CROSS_SECTIONS"
echo "number of threads:  $OMP_NUM_THREADS"

CLIST=$(ls vera*.omc.py)

for CASE in $CLIST; do
  CASE=$(echo $CASE | sed 's/\.py$//')
  echo "========================================="
  echo " Running case $CASE"
  echo "========================================="
  rm -f *.xml plot_1.png summary.h5 tallies.out
  python3 $CASE
  if [ -f plot_1.png ]; then
     mv plot_1.png $CASE.png
  fi
  if [ -f summary.h5 ]; then
     mv summary.h5 $CASE.summary.h5
  fi
  if [ -f tallies.out ]; then
     mv tallies.out $CASE.tal
  fi
  mv statepoint*h5 $CASE.statepoint.h5
  h5dump -d '/k_combined'  $CASE.statepoint.h5
done

echo "finished"
date
