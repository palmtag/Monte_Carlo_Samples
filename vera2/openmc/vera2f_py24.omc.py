import matplotlib

import openmc
import openmc.mgxs as mgxs
import openmc.data          # need for hdf5

#  To run:
#  >python3 vera2f_py24.omc
#
# OpenMC Input created by BUNBLD on 08/09/2025 11:48:06
#  VERA Benchmark #2 - Single Assembly
#  Uniform PWR Assembly
#  November 15, 2012
#  Number densities from KENO run
#  VERA Benchmark 2F - Like 2A + 24 Pyrex rods
#

# create a model object to tie together geometry, materials, settings, and tallies
model = openmc.Model()

# Material definitions

# material 1 FUEL01
matfuel01 = openmc.Material(name='fuel01')
matfuel01.add_nuclide('O16',  4.576420E-02)
matfuel01.add_nuclide('U234',  6.118640E-06)
matfuel01.add_nuclide('U235',  7.181320E-04)
matfuel01.add_nuclide('U236',  3.298610E-06)
matfuel01.add_nuclide('U238',  2.215460E-02)
matfuel01.set_density('g/cm3', 10.25701)
matfuel01.temperature=  600.000

# material 2 CLAD
matclad = openmc.Material(name='clad')
matclad.add_nuclide('Cr50',  3.301210E-06)
matclad.add_nuclide('Cr52',  6.366060E-05)
matclad.add_nuclide('Cr53',  7.218600E-06)
matclad.add_nuclide('Cr54',  1.796860E-06)
matclad.add_nuclide('Fe54',  8.683070E-06)
matclad.add_nuclide('Fe56',  1.363060E-04)
matclad.add_nuclide('Fe57',  3.147890E-06)
matclad.add_nuclide('Fe58',  4.189260E-07)
matclad.add_nuclide('Zr90',  2.188650E-02)
matclad.add_nuclide('Zr91',  4.772920E-03)
matclad.add_nuclide('Zr92',  7.295510E-03)
matclad.add_nuclide('Zr94',  7.393350E-03)
matclad.add_nuclide('Zr96',  1.191100E-03)
matclad.add_nuclide('Sn112',  4.680660E-06)
matclad.add_nuclide('Sn114',  3.184780E-06)
matclad.add_nuclide('Sn115',  1.640640E-06)
matclad.add_nuclide('Sn116',  7.016160E-05)
matclad.add_nuclide('Sn117',  3.705920E-05)
matclad.add_nuclide('Sn118',  1.168720E-04)
matclad.add_nuclide('Sn119',  4.145040E-05)
matclad.add_nuclide('Sn120',  1.572120E-04)
matclad.add_nuclide('Sn122',  2.234170E-05)
matclad.add_nuclide('Sn124',  2.793920E-05)
matclad.add_nuclide('Hf174',  3.541380E-09)
matclad.add_nuclide('Hf176',  1.164230E-07)
matclad.add_nuclide('Hf177',  4.116860E-07)
matclad.add_nuclide('Hf178',  6.038060E-07)
matclad.add_nuclide('Hf179',  3.014600E-07)
matclad.add_nuclide('Hf180',  7.764490E-07)
matclad.set_density('g/cm3',  6.55999)
matclad.temperature=  600.000

# material 3 COOL
matcool = openmc.Material(name='cool')
matcool.add_nuclide('H1',  4.962240E-02)
matcool.add_nuclide('O16',  2.481120E-02)
matcool.add_nuclide('B10',  1.070700E-05)
matcool.add_nuclide('B11',  4.309710E-05)
matcool.set_density('g/cm3',  0.74300)
matcool.temperature=  600.000
matcool.add_s_alpha_beta('c_H_in_H2O')

# material 4 MOD
matmod = openmc.Material(name='mod')
matmod.add_nuclide('H1',  4.962240E-02)
matmod.add_nuclide('O16',  2.481120E-02)
matmod.add_nuclide('B10',  1.070700E-05)
matmod.add_nuclide('B11',  4.309710E-05)
matmod.set_density('g/cm3',  0.74300)
matmod.temperature=  600.000
matmod.add_s_alpha_beta('c_H_in_H2O')

# material 5 AIR
matair = openmc.Material(name='air')
matair.add_nuclide('He4',  2.687140E-05)
matair.set_density('g/cm3',  0.00018)
matair.temperature=  600.000

# material 6 BSOX
matbsox = openmc.Material(name='bsox')
matbsox.add_nuclide('B10',  9.632660E-04)
matbsox.add_nuclide('B11',  3.901720E-03)
matbsox.add_nuclide('O16',  4.677610E-02)
matbsox.add_nuclide('Si28',  1.819800E-02)
matbsox.add_nuclide('Si29',  9.244740E-04)
matbsox.add_nuclide('Si30',  6.101330E-04)
matbsox.set_density('g/cm3',  2.25000)
matbsox.temperature=  600.000

# material 7 SS304
matss304 = openmc.Material(name='ss304')
matss304.add_nuclide('C0',  3.208950E-04)
matss304.add_nuclide('Si28',  1.581970E-03)
matss304.add_nuclide('Si29',  8.036530E-05)
matss304.add_nuclide('Si30',  5.303940E-05)
matss304.add_nuclide('P31',  6.999380E-05)
matss304.add_nuclide('Cr50',  7.649150E-04)
matss304.add_nuclide('Cr52',  1.475060E-02)
matss304.add_nuclide('Cr53',  1.672600E-03)
matss304.add_nuclide('Cr54',  4.163460E-04)
matss304.add_nuclide('Mn55',  1.753870E-03)
matss304.add_nuclide('Fe54',  3.447760E-03)
matss304.add_nuclide('Fe56',  5.412250E-02)
matss304.add_nuclide('Fe57',  1.249920E-03)
matss304.add_nuclide('Fe58',  1.663420E-04)
matss304.add_nuclide('Ni58',  5.308540E-03)
matss304.add_nuclide('Ni60',  2.044840E-03)
matss304.add_nuclide('Ni61',  8.888790E-05)
matss304.add_nuclide('Ni62',  2.834130E-04)
matss304.add_nuclide('Ni64',  7.217700E-05)
matss304.set_density('g/cm3',  8.00000)
matss304.temperature=  600.000

# Material mixtures

# Instantiate a Materials collection
model.materials = openmc.Materials([matfuel01,matclad,matcool,matmod,matair,matbsox,matss304])
#
# ------------- Geometry ------------------------
#
# PINMAP
#  3  1  1  2  1  1  2  1  1  
#  1  1  1  1  1  1  1  1  1  
#  1  1  1  1  1  1  1  1  1  
#  2  1  1  2  1  1  2  1  1  
#  1  1  1  1  1  1  1  1  1  
#  1  1  1  1  1  2  1  1  1  
#  2  1  1  2  1  1  1  1  1  
#  1  1  1  1  1  1  1  1  1  
#  1  1  1  1  1  1  1  1  1  
# 
# FUEMAP
#  0  1  1  0  1  1  0  1  1
#  1  1  1  1  1  1  1  1  1
#  1  1  1  1  1  1  1  1  1
#  0  1  1  0  1  1  0  1  1
#  1  1  1  1  1  1  1  1  1
#  1  1  1  1  1  0  1  1  1
#  0  1  1  0  1  1  1  1  1
#  1  1  1  1  1  1  1  1  1
#  1  1  1  1  1  1  1  1  1
# 
biguni = openmc.Universe(name="biguni")
# boundary planes
bndn = openmc.YPlane(y0= 10.750000, boundary_type='reflective')
bnds = openmc.YPlane(y0=  0.000000, boundary_type='reflective')
bnde = openmc.XPlane(x0= 10.750000, boundary_type='reflective')
bndw = openmc.XPlane(x0=  0.000000, boundary_type='reflective')

px1 = openmc.XPlane(x0=  0.630000)
px2 = openmc.XPlane(x0=  1.890000)
px3 = openmc.XPlane(x0=  3.150000)
px4 = openmc.XPlane(x0=  4.410000)
px5 = openmc.XPlane(x0=  5.670000)
px6 = openmc.XPlane(x0=  6.930000)
px7 = openmc.XPlane(x0=  8.190000)
px8 = openmc.XPlane(x0=  9.450000)
py1 = openmc.YPlane(y0= 10.120000)
py2 = openmc.YPlane(y0=  8.860000)
py3 = openmc.YPlane(y0=  7.600000)
py4 = openmc.YPlane(y0=  6.340000)
py5 = openmc.YPlane(y0=  5.080000)
py6 = openmc.YPlane(y0=  3.820000)
py7 = openmc.YPlane(y0=  2.560000)
py8 = openmc.YPlane(y0=  1.300000)

# create fuel cell id list for tallies
fuel_cell_list=[]

# rod number (9,9)
x=  0.000000
y= 10.750000
cyl1 = openmc.ZCylinder(x0=x, y0=y, r= 0.55900)  # MOD
cyl2 = openmc.ZCylinder(x0=x, y0=y, r= 0.60500)  # CLAD
cell1 = openmc.Cell(fill=matmod)
cell1.region = -cyl1 & +bndw & -bndn
cell2 = openmc.Cell(fill=matclad)
cell2.region = +cyl1 & -cyl2 & +bndw & -bndn
cell3 = openmc.Cell(fill=matcool)
cell3.region = +cyl2 & +bndw & -px1 & -bndn & +py1
biguni.add_cell(cell1)
biguni.add_cell(cell2)
biguni.add_cell(cell3)
# rod number (10,9)
x=  1.260000
y= 10.750000
cyl4 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl5 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl6 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell4 = openmc.Cell(fill=matfuel01)
cell4.region = -cyl4 & -bndn
fuel_cell_list.append(cell4.id)
cell5 = openmc.Cell(fill=matair)
cell5.region = +cyl4 & -cyl5 & -bndn
cell6 = openmc.Cell(fill=matclad)
cell6.region = +cyl5 & -cyl6 & -bndn
cell7 = openmc.Cell(fill=matcool)
cell7.region = +cyl6 & +px1 & -px2 & -bndn & +py1
biguni.add_cell(cell4)
biguni.add_cell(cell5)
biguni.add_cell(cell6)
biguni.add_cell(cell7)
# rod number (11,9)
x=  2.520000
y= 10.750000
cyl8 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl9 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl10 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell8 = openmc.Cell(fill=matfuel01)
cell8.region = -cyl8 & -bndn
fuel_cell_list.append(cell8.id)
cell9 = openmc.Cell(fill=matair)
cell9.region = +cyl8 & -cyl9 & -bndn
cell10 = openmc.Cell(fill=matclad)
cell10.region = +cyl9 & -cyl10 & -bndn
cell11 = openmc.Cell(fill=matcool)
cell11.region = +cyl10 & +px2 & -px3 & -bndn & +py1
biguni.add_cell(cell8)
biguni.add_cell(cell9)
biguni.add_cell(cell10)
biguni.add_cell(cell11)
# rod number (12,9)
x=  3.780000
y= 10.750000
cyl12 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl13 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl14 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl15 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl16 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl17 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl18 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl19 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell12 = openmc.Cell(fill=matair)
cell12.region = -cyl12 & -bndn
cell13 = openmc.Cell(fill=matss304)
cell13.region = +cyl12 & -cyl13 & -bndn
cell14 = openmc.Cell(fill=matair)
cell14.region = +cyl13 & -cyl14 & -bndn
cell15 = openmc.Cell(fill=matbsox)
cell15.region = +cyl14 & -cyl15 & -bndn
cell16 = openmc.Cell(fill=matair)
cell16.region = +cyl15 & -cyl16 & -bndn
cell17 = openmc.Cell(fill=matss304)
cell17.region = +cyl16 & -cyl17 & -bndn
cell18 = openmc.Cell(fill=matmod)
cell18.region = +cyl17 & -cyl18 & -bndn
cell19 = openmc.Cell(fill=matclad)
cell19.region = +cyl18 & -cyl19 & -bndn
cell20 = openmc.Cell(fill=matcool)
cell20.region = +cyl19 & +px3 & -px4 & -bndn & +py1
biguni.add_cell(cell12)
biguni.add_cell(cell13)
biguni.add_cell(cell14)
biguni.add_cell(cell15)
biguni.add_cell(cell16)
biguni.add_cell(cell17)
biguni.add_cell(cell18)
biguni.add_cell(cell19)
biguni.add_cell(cell20)
# rod number (13,9)
x=  5.040000
y= 10.750000
cyl21 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl22 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl23 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell21 = openmc.Cell(fill=matfuel01)
cell21.region = -cyl21 & -bndn
fuel_cell_list.append(cell21.id)
cell22 = openmc.Cell(fill=matair)
cell22.region = +cyl21 & -cyl22 & -bndn
cell23 = openmc.Cell(fill=matclad)
cell23.region = +cyl22 & -cyl23 & -bndn
cell24 = openmc.Cell(fill=matcool)
cell24.region = +cyl23 & +px4 & -px5 & -bndn & +py1
biguni.add_cell(cell21)
biguni.add_cell(cell22)
biguni.add_cell(cell23)
biguni.add_cell(cell24)
# rod number (14,9)
x=  6.300000
y= 10.750000
cyl25 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl26 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl27 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell25 = openmc.Cell(fill=matfuel01)
cell25.region = -cyl25 & -bndn
fuel_cell_list.append(cell25.id)
cell26 = openmc.Cell(fill=matair)
cell26.region = +cyl25 & -cyl26 & -bndn
cell27 = openmc.Cell(fill=matclad)
cell27.region = +cyl26 & -cyl27 & -bndn
cell28 = openmc.Cell(fill=matcool)
cell28.region = +cyl27 & +px5 & -px6 & -bndn & +py1
biguni.add_cell(cell25)
biguni.add_cell(cell26)
biguni.add_cell(cell27)
biguni.add_cell(cell28)
# rod number (15,9)
x=  7.560000
y= 10.750000
cyl29 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl30 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl31 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl32 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl33 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl34 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl35 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl36 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell29 = openmc.Cell(fill=matair)
cell29.region = -cyl29 & -bndn
cell30 = openmc.Cell(fill=matss304)
cell30.region = +cyl29 & -cyl30 & -bndn
cell31 = openmc.Cell(fill=matair)
cell31.region = +cyl30 & -cyl31 & -bndn
cell32 = openmc.Cell(fill=matbsox)
cell32.region = +cyl31 & -cyl32 & -bndn
cell33 = openmc.Cell(fill=matair)
cell33.region = +cyl32 & -cyl33 & -bndn
cell34 = openmc.Cell(fill=matss304)
cell34.region = +cyl33 & -cyl34 & -bndn
cell35 = openmc.Cell(fill=matmod)
cell35.region = +cyl34 & -cyl35 & -bndn
cell36 = openmc.Cell(fill=matclad)
cell36.region = +cyl35 & -cyl36 & -bndn
cell37 = openmc.Cell(fill=matcool)
cell37.region = +cyl36 & +px6 & -px7 & -bndn & +py1
biguni.add_cell(cell29)
biguni.add_cell(cell30)
biguni.add_cell(cell31)
biguni.add_cell(cell32)
biguni.add_cell(cell33)
biguni.add_cell(cell34)
biguni.add_cell(cell35)
biguni.add_cell(cell36)
biguni.add_cell(cell37)
# rod number (16,9)
x=  8.820000
y= 10.750000
cyl38 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl39 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl40 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell38 = openmc.Cell(fill=matfuel01)
cell38.region = -cyl38 & -bndn
fuel_cell_list.append(cell38.id)
cell39 = openmc.Cell(fill=matair)
cell39.region = +cyl38 & -cyl39 & -bndn
cell40 = openmc.Cell(fill=matclad)
cell40.region = +cyl39 & -cyl40 & -bndn
cell41 = openmc.Cell(fill=matcool)
cell41.region = +cyl40 & +px7 & -px8 & -bndn & +py1
biguni.add_cell(cell38)
biguni.add_cell(cell39)
biguni.add_cell(cell40)
biguni.add_cell(cell41)
# rod number (17,9)
x= 10.080000
y= 10.750000
cyl42 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl43 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl44 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell42 = openmc.Cell(fill=matfuel01)
cell42.region = -cyl42 & -bndn
fuel_cell_list.append(cell42.id)
cell43 = openmc.Cell(fill=matair)
cell43.region = +cyl42 & -cyl43 & -bndn
cell44 = openmc.Cell(fill=matclad)
cell44.region = +cyl43 & -cyl44 & -bndn
cell45 = openmc.Cell(fill=matcool)
cell45.region = +cyl44 & +px8 & -bnde & -bndn & +py1
biguni.add_cell(cell42)
biguni.add_cell(cell43)
biguni.add_cell(cell44)
biguni.add_cell(cell45)
# rod number (9,10)
x=  0.000000
y=  9.490000
cyl46 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl47 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl48 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell46 = openmc.Cell(fill=matfuel01)
cell46.region = -cyl46 & +bndw
fuel_cell_list.append(cell46.id)
cell47 = openmc.Cell(fill=matair)
cell47.region = +cyl46 & -cyl47 & +bndw
cell48 = openmc.Cell(fill=matclad)
cell48.region = +cyl47 & -cyl48 & +bndw
cell49 = openmc.Cell(fill=matcool)
cell49.region = +cyl48 & +bndw & -px1 & -py1 & +py2
biguni.add_cell(cell46)
biguni.add_cell(cell47)
biguni.add_cell(cell48)
biguni.add_cell(cell49)
# rod number (10,10)
x=  1.260000
y=  9.490000
cyl50 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl51 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl52 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell50 = openmc.Cell(fill=matfuel01)
cell50.region = -cyl50
fuel_cell_list.append(cell50.id)
cell51 = openmc.Cell(fill=matair)
cell51.region = +cyl50 & -cyl51
cell52 = openmc.Cell(fill=matclad)
cell52.region = +cyl51 & -cyl52
cell53 = openmc.Cell(fill=matcool)
cell53.region = +cyl52 & +px1 & -px2 & -py1 & +py2
biguni.add_cell(cell50)
biguni.add_cell(cell51)
biguni.add_cell(cell52)
biguni.add_cell(cell53)
# rod number (11,10)
x=  2.520000
y=  9.490000
cyl54 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl55 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl56 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell54 = openmc.Cell(fill=matfuel01)
cell54.region = -cyl54
fuel_cell_list.append(cell54.id)
cell55 = openmc.Cell(fill=matair)
cell55.region = +cyl54 & -cyl55
cell56 = openmc.Cell(fill=matclad)
cell56.region = +cyl55 & -cyl56
cell57 = openmc.Cell(fill=matcool)
cell57.region = +cyl56 & +px2 & -px3 & -py1 & +py2
biguni.add_cell(cell54)
biguni.add_cell(cell55)
biguni.add_cell(cell56)
biguni.add_cell(cell57)
# rod number (12,10)
x=  3.780000
y=  9.490000
cyl58 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl59 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl60 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell58 = openmc.Cell(fill=matfuel01)
cell58.region = -cyl58
fuel_cell_list.append(cell58.id)
cell59 = openmc.Cell(fill=matair)
cell59.region = +cyl58 & -cyl59
cell60 = openmc.Cell(fill=matclad)
cell60.region = +cyl59 & -cyl60
cell61 = openmc.Cell(fill=matcool)
cell61.region = +cyl60 & +px3 & -px4 & -py1 & +py2
biguni.add_cell(cell58)
biguni.add_cell(cell59)
biguni.add_cell(cell60)
biguni.add_cell(cell61)
# rod number (13,10)
x=  5.040000
y=  9.490000
cyl62 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl63 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl64 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell62 = openmc.Cell(fill=matfuel01)
cell62.region = -cyl62
fuel_cell_list.append(cell62.id)
cell63 = openmc.Cell(fill=matair)
cell63.region = +cyl62 & -cyl63
cell64 = openmc.Cell(fill=matclad)
cell64.region = +cyl63 & -cyl64
cell65 = openmc.Cell(fill=matcool)
cell65.region = +cyl64 & +px4 & -px5 & -py1 & +py2
biguni.add_cell(cell62)
biguni.add_cell(cell63)
biguni.add_cell(cell64)
biguni.add_cell(cell65)
# rod number (14,10)
x=  6.300000
y=  9.490000
cyl66 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl67 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl68 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell66 = openmc.Cell(fill=matfuel01)
cell66.region = -cyl66
fuel_cell_list.append(cell66.id)
cell67 = openmc.Cell(fill=matair)
cell67.region = +cyl66 & -cyl67
cell68 = openmc.Cell(fill=matclad)
cell68.region = +cyl67 & -cyl68
cell69 = openmc.Cell(fill=matcool)
cell69.region = +cyl68 & +px5 & -px6 & -py1 & +py2
biguni.add_cell(cell66)
biguni.add_cell(cell67)
biguni.add_cell(cell68)
biguni.add_cell(cell69)
# rod number (15,10)
x=  7.560000
y=  9.490000
cyl70 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl71 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl72 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell70 = openmc.Cell(fill=matfuel01)
cell70.region = -cyl70
fuel_cell_list.append(cell70.id)
cell71 = openmc.Cell(fill=matair)
cell71.region = +cyl70 & -cyl71
cell72 = openmc.Cell(fill=matclad)
cell72.region = +cyl71 & -cyl72
cell73 = openmc.Cell(fill=matcool)
cell73.region = +cyl72 & +px6 & -px7 & -py1 & +py2
biguni.add_cell(cell70)
biguni.add_cell(cell71)
biguni.add_cell(cell72)
biguni.add_cell(cell73)
# rod number (16,10)
x=  8.820000
y=  9.490000
cyl74 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl75 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl76 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell74 = openmc.Cell(fill=matfuel01)
cell74.region = -cyl74
fuel_cell_list.append(cell74.id)
cell75 = openmc.Cell(fill=matair)
cell75.region = +cyl74 & -cyl75
cell76 = openmc.Cell(fill=matclad)
cell76.region = +cyl75 & -cyl76
cell77 = openmc.Cell(fill=matcool)
cell77.region = +cyl76 & +px7 & -px8 & -py1 & +py2
biguni.add_cell(cell74)
biguni.add_cell(cell75)
biguni.add_cell(cell76)
biguni.add_cell(cell77)
# rod number (17,10)
x= 10.080000
y=  9.490000
cyl78 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl79 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl80 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell78 = openmc.Cell(fill=matfuel01)
cell78.region = -cyl78
fuel_cell_list.append(cell78.id)
cell79 = openmc.Cell(fill=matair)
cell79.region = +cyl78 & -cyl79
cell80 = openmc.Cell(fill=matclad)
cell80.region = +cyl79 & -cyl80
cell81 = openmc.Cell(fill=matcool)
cell81.region = +cyl80 & +px8 & -bnde & -py1 & +py2
biguni.add_cell(cell78)
biguni.add_cell(cell79)
biguni.add_cell(cell80)
biguni.add_cell(cell81)
# rod number (9,11)
x=  0.000000
y=  8.230000
cyl82 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl83 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl84 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell82 = openmc.Cell(fill=matfuel01)
cell82.region = -cyl82 & +bndw
fuel_cell_list.append(cell82.id)
cell83 = openmc.Cell(fill=matair)
cell83.region = +cyl82 & -cyl83 & +bndw
cell84 = openmc.Cell(fill=matclad)
cell84.region = +cyl83 & -cyl84 & +bndw
cell85 = openmc.Cell(fill=matcool)
cell85.region = +cyl84 & +bndw & -px1 & -py2 & +py3
biguni.add_cell(cell82)
biguni.add_cell(cell83)
biguni.add_cell(cell84)
biguni.add_cell(cell85)
# rod number (10,11)
x=  1.260000
y=  8.230000
cyl86 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl87 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl88 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell86 = openmc.Cell(fill=matfuel01)
cell86.region = -cyl86
fuel_cell_list.append(cell86.id)
cell87 = openmc.Cell(fill=matair)
cell87.region = +cyl86 & -cyl87
cell88 = openmc.Cell(fill=matclad)
cell88.region = +cyl87 & -cyl88
cell89 = openmc.Cell(fill=matcool)
cell89.region = +cyl88 & +px1 & -px2 & -py2 & +py3
biguni.add_cell(cell86)
biguni.add_cell(cell87)
biguni.add_cell(cell88)
biguni.add_cell(cell89)
# rod number (11,11)
x=  2.520000
y=  8.230000
cyl90 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl91 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl92 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell90 = openmc.Cell(fill=matfuel01)
cell90.region = -cyl90
fuel_cell_list.append(cell90.id)
cell91 = openmc.Cell(fill=matair)
cell91.region = +cyl90 & -cyl91
cell92 = openmc.Cell(fill=matclad)
cell92.region = +cyl91 & -cyl92
cell93 = openmc.Cell(fill=matcool)
cell93.region = +cyl92 & +px2 & -px3 & -py2 & +py3
biguni.add_cell(cell90)
biguni.add_cell(cell91)
biguni.add_cell(cell92)
biguni.add_cell(cell93)
# rod number (12,11)
x=  3.780000
y=  8.230000
cyl94 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl95 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl96 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell94 = openmc.Cell(fill=matfuel01)
cell94.region = -cyl94
fuel_cell_list.append(cell94.id)
cell95 = openmc.Cell(fill=matair)
cell95.region = +cyl94 & -cyl95
cell96 = openmc.Cell(fill=matclad)
cell96.region = +cyl95 & -cyl96
cell97 = openmc.Cell(fill=matcool)
cell97.region = +cyl96 & +px3 & -px4 & -py2 & +py3
biguni.add_cell(cell94)
biguni.add_cell(cell95)
biguni.add_cell(cell96)
biguni.add_cell(cell97)
# rod number (13,11)
x=  5.040000
y=  8.230000
cyl98 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl99 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl100 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell98 = openmc.Cell(fill=matfuel01)
cell98.region = -cyl98
fuel_cell_list.append(cell98.id)
cell99 = openmc.Cell(fill=matair)
cell99.region = +cyl98 & -cyl99
cell100 = openmc.Cell(fill=matclad)
cell100.region = +cyl99 & -cyl100
cell101 = openmc.Cell(fill=matcool)
cell101.region = +cyl100 & +px4 & -px5 & -py2 & +py3
biguni.add_cell(cell98)
biguni.add_cell(cell99)
biguni.add_cell(cell100)
biguni.add_cell(cell101)
# rod number (14,11)
x=  6.300000
y=  8.230000
cyl102 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl103 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl104 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell102 = openmc.Cell(fill=matfuel01)
cell102.region = -cyl102
fuel_cell_list.append(cell102.id)
cell103 = openmc.Cell(fill=matair)
cell103.region = +cyl102 & -cyl103
cell104 = openmc.Cell(fill=matclad)
cell104.region = +cyl103 & -cyl104
cell105 = openmc.Cell(fill=matcool)
cell105.region = +cyl104 & +px5 & -px6 & -py2 & +py3
biguni.add_cell(cell102)
biguni.add_cell(cell103)
biguni.add_cell(cell104)
biguni.add_cell(cell105)
# rod number (15,11)
x=  7.560000
y=  8.230000
cyl106 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl107 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl108 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell106 = openmc.Cell(fill=matfuel01)
cell106.region = -cyl106
fuel_cell_list.append(cell106.id)
cell107 = openmc.Cell(fill=matair)
cell107.region = +cyl106 & -cyl107
cell108 = openmc.Cell(fill=matclad)
cell108.region = +cyl107 & -cyl108
cell109 = openmc.Cell(fill=matcool)
cell109.region = +cyl108 & +px6 & -px7 & -py2 & +py3
biguni.add_cell(cell106)
biguni.add_cell(cell107)
biguni.add_cell(cell108)
biguni.add_cell(cell109)
# rod number (16,11)
x=  8.820000
y=  8.230000
cyl110 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl111 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl112 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell110 = openmc.Cell(fill=matfuel01)
cell110.region = -cyl110
fuel_cell_list.append(cell110.id)
cell111 = openmc.Cell(fill=matair)
cell111.region = +cyl110 & -cyl111
cell112 = openmc.Cell(fill=matclad)
cell112.region = +cyl111 & -cyl112
cell113 = openmc.Cell(fill=matcool)
cell113.region = +cyl112 & +px7 & -px8 & -py2 & +py3
biguni.add_cell(cell110)
biguni.add_cell(cell111)
biguni.add_cell(cell112)
biguni.add_cell(cell113)
# rod number (17,11)
x= 10.080000
y=  8.230000
cyl114 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl115 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl116 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell114 = openmc.Cell(fill=matfuel01)
cell114.region = -cyl114
fuel_cell_list.append(cell114.id)
cell115 = openmc.Cell(fill=matair)
cell115.region = +cyl114 & -cyl115
cell116 = openmc.Cell(fill=matclad)
cell116.region = +cyl115 & -cyl116
cell117 = openmc.Cell(fill=matcool)
cell117.region = +cyl116 & +px8 & -bnde & -py2 & +py3
biguni.add_cell(cell114)
biguni.add_cell(cell115)
biguni.add_cell(cell116)
biguni.add_cell(cell117)
# rod number (9,12)
x=  0.000000
y=  6.970000
cyl118 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl119 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl120 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl121 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl122 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl123 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl124 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl125 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell118 = openmc.Cell(fill=matair)
cell118.region = -cyl118 & +bndw
cell119 = openmc.Cell(fill=matss304)
cell119.region = +cyl118 & -cyl119 & +bndw
cell120 = openmc.Cell(fill=matair)
cell120.region = +cyl119 & -cyl120 & +bndw
cell121 = openmc.Cell(fill=matbsox)
cell121.region = +cyl120 & -cyl121 & +bndw
cell122 = openmc.Cell(fill=matair)
cell122.region = +cyl121 & -cyl122 & +bndw
cell123 = openmc.Cell(fill=matss304)
cell123.region = +cyl122 & -cyl123 & +bndw
cell124 = openmc.Cell(fill=matmod)
cell124.region = +cyl123 & -cyl124 & +bndw
cell125 = openmc.Cell(fill=matclad)
cell125.region = +cyl124 & -cyl125 & +bndw
cell126 = openmc.Cell(fill=matcool)
cell126.region = +cyl125 & +bndw & -px1 & -py3 & +py4
biguni.add_cell(cell118)
biguni.add_cell(cell119)
biguni.add_cell(cell120)
biguni.add_cell(cell121)
biguni.add_cell(cell122)
biguni.add_cell(cell123)
biguni.add_cell(cell124)
biguni.add_cell(cell125)
biguni.add_cell(cell126)
# rod number (10,12)
x=  1.260000
y=  6.970000
cyl127 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl128 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl129 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell127 = openmc.Cell(fill=matfuel01)
cell127.region = -cyl127
fuel_cell_list.append(cell127.id)
cell128 = openmc.Cell(fill=matair)
cell128.region = +cyl127 & -cyl128
cell129 = openmc.Cell(fill=matclad)
cell129.region = +cyl128 & -cyl129
cell130 = openmc.Cell(fill=matcool)
cell130.region = +cyl129 & +px1 & -px2 & -py3 & +py4
biguni.add_cell(cell127)
biguni.add_cell(cell128)
biguni.add_cell(cell129)
biguni.add_cell(cell130)
# rod number (11,12)
x=  2.520000
y=  6.970000
cyl131 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl132 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl133 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell131 = openmc.Cell(fill=matfuel01)
cell131.region = -cyl131
fuel_cell_list.append(cell131.id)
cell132 = openmc.Cell(fill=matair)
cell132.region = +cyl131 & -cyl132
cell133 = openmc.Cell(fill=matclad)
cell133.region = +cyl132 & -cyl133
cell134 = openmc.Cell(fill=matcool)
cell134.region = +cyl133 & +px2 & -px3 & -py3 & +py4
biguni.add_cell(cell131)
biguni.add_cell(cell132)
biguni.add_cell(cell133)
biguni.add_cell(cell134)
# rod number (12,12)
x=  3.780000
y=  6.970000
cyl135 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl136 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl137 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl138 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl139 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl140 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl141 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl142 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell135 = openmc.Cell(fill=matair)
cell135.region = -cyl135
cell136 = openmc.Cell(fill=matss304)
cell136.region = +cyl135 & -cyl136
cell137 = openmc.Cell(fill=matair)
cell137.region = +cyl136 & -cyl137
cell138 = openmc.Cell(fill=matbsox)
cell138.region = +cyl137 & -cyl138
cell139 = openmc.Cell(fill=matair)
cell139.region = +cyl138 & -cyl139
cell140 = openmc.Cell(fill=matss304)
cell140.region = +cyl139 & -cyl140
cell141 = openmc.Cell(fill=matmod)
cell141.region = +cyl140 & -cyl141
cell142 = openmc.Cell(fill=matclad)
cell142.region = +cyl141 & -cyl142
cell143 = openmc.Cell(fill=matcool)
cell143.region = +cyl142 & +px3 & -px4 & -py3 & +py4
biguni.add_cell(cell135)
biguni.add_cell(cell136)
biguni.add_cell(cell137)
biguni.add_cell(cell138)
biguni.add_cell(cell139)
biguni.add_cell(cell140)
biguni.add_cell(cell141)
biguni.add_cell(cell142)
biguni.add_cell(cell143)
# rod number (13,12)
x=  5.040000
y=  6.970000
cyl144 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl145 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl146 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell144 = openmc.Cell(fill=matfuel01)
cell144.region = -cyl144
fuel_cell_list.append(cell144.id)
cell145 = openmc.Cell(fill=matair)
cell145.region = +cyl144 & -cyl145
cell146 = openmc.Cell(fill=matclad)
cell146.region = +cyl145 & -cyl146
cell147 = openmc.Cell(fill=matcool)
cell147.region = +cyl146 & +px4 & -px5 & -py3 & +py4
biguni.add_cell(cell144)
biguni.add_cell(cell145)
biguni.add_cell(cell146)
biguni.add_cell(cell147)
# rod number (14,12)
x=  6.300000
y=  6.970000
cyl148 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl149 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl150 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell148 = openmc.Cell(fill=matfuel01)
cell148.region = -cyl148
fuel_cell_list.append(cell148.id)
cell149 = openmc.Cell(fill=matair)
cell149.region = +cyl148 & -cyl149
cell150 = openmc.Cell(fill=matclad)
cell150.region = +cyl149 & -cyl150
cell151 = openmc.Cell(fill=matcool)
cell151.region = +cyl150 & +px5 & -px6 & -py3 & +py4
biguni.add_cell(cell148)
biguni.add_cell(cell149)
biguni.add_cell(cell150)
biguni.add_cell(cell151)
# rod number (15,12)
x=  7.560000
y=  6.970000
cyl152 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl153 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl154 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl155 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl156 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl157 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl158 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl159 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell152 = openmc.Cell(fill=matair)
cell152.region = -cyl152
cell153 = openmc.Cell(fill=matss304)
cell153.region = +cyl152 & -cyl153
cell154 = openmc.Cell(fill=matair)
cell154.region = +cyl153 & -cyl154
cell155 = openmc.Cell(fill=matbsox)
cell155.region = +cyl154 & -cyl155
cell156 = openmc.Cell(fill=matair)
cell156.region = +cyl155 & -cyl156
cell157 = openmc.Cell(fill=matss304)
cell157.region = +cyl156 & -cyl157
cell158 = openmc.Cell(fill=matmod)
cell158.region = +cyl157 & -cyl158
cell159 = openmc.Cell(fill=matclad)
cell159.region = +cyl158 & -cyl159
cell160 = openmc.Cell(fill=matcool)
cell160.region = +cyl159 & +px6 & -px7 & -py3 & +py4
biguni.add_cell(cell152)
biguni.add_cell(cell153)
biguni.add_cell(cell154)
biguni.add_cell(cell155)
biguni.add_cell(cell156)
biguni.add_cell(cell157)
biguni.add_cell(cell158)
biguni.add_cell(cell159)
biguni.add_cell(cell160)
# rod number (16,12)
x=  8.820000
y=  6.970000
cyl161 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl162 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl163 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell161 = openmc.Cell(fill=matfuel01)
cell161.region = -cyl161
fuel_cell_list.append(cell161.id)
cell162 = openmc.Cell(fill=matair)
cell162.region = +cyl161 & -cyl162
cell163 = openmc.Cell(fill=matclad)
cell163.region = +cyl162 & -cyl163
cell164 = openmc.Cell(fill=matcool)
cell164.region = +cyl163 & +px7 & -px8 & -py3 & +py4
biguni.add_cell(cell161)
biguni.add_cell(cell162)
biguni.add_cell(cell163)
biguni.add_cell(cell164)
# rod number (17,12)
x= 10.080000
y=  6.970000
cyl165 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl166 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl167 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell165 = openmc.Cell(fill=matfuel01)
cell165.region = -cyl165
fuel_cell_list.append(cell165.id)
cell166 = openmc.Cell(fill=matair)
cell166.region = +cyl165 & -cyl166
cell167 = openmc.Cell(fill=matclad)
cell167.region = +cyl166 & -cyl167
cell168 = openmc.Cell(fill=matcool)
cell168.region = +cyl167 & +px8 & -bnde & -py3 & +py4
biguni.add_cell(cell165)
biguni.add_cell(cell166)
biguni.add_cell(cell167)
biguni.add_cell(cell168)
# rod number (9,13)
x=  0.000000
y=  5.710000
cyl169 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl170 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl171 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell169 = openmc.Cell(fill=matfuel01)
cell169.region = -cyl169 & +bndw
fuel_cell_list.append(cell169.id)
cell170 = openmc.Cell(fill=matair)
cell170.region = +cyl169 & -cyl170 & +bndw
cell171 = openmc.Cell(fill=matclad)
cell171.region = +cyl170 & -cyl171 & +bndw
cell172 = openmc.Cell(fill=matcool)
cell172.region = +cyl171 & +bndw & -px1 & -py4 & +py5
biguni.add_cell(cell169)
biguni.add_cell(cell170)
biguni.add_cell(cell171)
biguni.add_cell(cell172)
# rod number (10,13)
x=  1.260000
y=  5.710000
cyl173 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl174 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl175 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell173 = openmc.Cell(fill=matfuel01)
cell173.region = -cyl173
fuel_cell_list.append(cell173.id)
cell174 = openmc.Cell(fill=matair)
cell174.region = +cyl173 & -cyl174
cell175 = openmc.Cell(fill=matclad)
cell175.region = +cyl174 & -cyl175
cell176 = openmc.Cell(fill=matcool)
cell176.region = +cyl175 & +px1 & -px2 & -py4 & +py5
biguni.add_cell(cell173)
biguni.add_cell(cell174)
biguni.add_cell(cell175)
biguni.add_cell(cell176)
# rod number (11,13)
x=  2.520000
y=  5.710000
cyl177 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl178 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl179 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell177 = openmc.Cell(fill=matfuel01)
cell177.region = -cyl177
fuel_cell_list.append(cell177.id)
cell178 = openmc.Cell(fill=matair)
cell178.region = +cyl177 & -cyl178
cell179 = openmc.Cell(fill=matclad)
cell179.region = +cyl178 & -cyl179
cell180 = openmc.Cell(fill=matcool)
cell180.region = +cyl179 & +px2 & -px3 & -py4 & +py5
biguni.add_cell(cell177)
biguni.add_cell(cell178)
biguni.add_cell(cell179)
biguni.add_cell(cell180)
# rod number (12,13)
x=  3.780000
y=  5.710000
cyl181 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl182 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl183 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell181 = openmc.Cell(fill=matfuel01)
cell181.region = -cyl181
fuel_cell_list.append(cell181.id)
cell182 = openmc.Cell(fill=matair)
cell182.region = +cyl181 & -cyl182
cell183 = openmc.Cell(fill=matclad)
cell183.region = +cyl182 & -cyl183
cell184 = openmc.Cell(fill=matcool)
cell184.region = +cyl183 & +px3 & -px4 & -py4 & +py5
biguni.add_cell(cell181)
biguni.add_cell(cell182)
biguni.add_cell(cell183)
biguni.add_cell(cell184)
# rod number (13,13)
x=  5.040000
y=  5.710000
cyl185 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl186 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl187 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell185 = openmc.Cell(fill=matfuel01)
cell185.region = -cyl185
fuel_cell_list.append(cell185.id)
cell186 = openmc.Cell(fill=matair)
cell186.region = +cyl185 & -cyl186
cell187 = openmc.Cell(fill=matclad)
cell187.region = +cyl186 & -cyl187
cell188 = openmc.Cell(fill=matcool)
cell188.region = +cyl187 & +px4 & -px5 & -py4 & +py5
biguni.add_cell(cell185)
biguni.add_cell(cell186)
biguni.add_cell(cell187)
biguni.add_cell(cell188)
# rod number (14,13)
x=  6.300000
y=  5.710000
cyl189 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl190 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl191 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell189 = openmc.Cell(fill=matfuel01)
cell189.region = -cyl189
fuel_cell_list.append(cell189.id)
cell190 = openmc.Cell(fill=matair)
cell190.region = +cyl189 & -cyl190
cell191 = openmc.Cell(fill=matclad)
cell191.region = +cyl190 & -cyl191
cell192 = openmc.Cell(fill=matcool)
cell192.region = +cyl191 & +px5 & -px6 & -py4 & +py5
biguni.add_cell(cell189)
biguni.add_cell(cell190)
biguni.add_cell(cell191)
biguni.add_cell(cell192)
# rod number (15,13)
x=  7.560000
y=  5.710000
cyl193 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl194 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl195 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell193 = openmc.Cell(fill=matfuel01)
cell193.region = -cyl193
fuel_cell_list.append(cell193.id)
cell194 = openmc.Cell(fill=matair)
cell194.region = +cyl193 & -cyl194
cell195 = openmc.Cell(fill=matclad)
cell195.region = +cyl194 & -cyl195
cell196 = openmc.Cell(fill=matcool)
cell196.region = +cyl195 & +px6 & -px7 & -py4 & +py5
biguni.add_cell(cell193)
biguni.add_cell(cell194)
biguni.add_cell(cell195)
biguni.add_cell(cell196)
# rod number (16,13)
x=  8.820000
y=  5.710000
cyl197 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl198 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl199 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell197 = openmc.Cell(fill=matfuel01)
cell197.region = -cyl197
fuel_cell_list.append(cell197.id)
cell198 = openmc.Cell(fill=matair)
cell198.region = +cyl197 & -cyl198
cell199 = openmc.Cell(fill=matclad)
cell199.region = +cyl198 & -cyl199
cell200 = openmc.Cell(fill=matcool)
cell200.region = +cyl199 & +px7 & -px8 & -py4 & +py5
biguni.add_cell(cell197)
biguni.add_cell(cell198)
biguni.add_cell(cell199)
biguni.add_cell(cell200)
# rod number (17,13)
x= 10.080000
y=  5.710000
cyl201 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl202 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl203 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell201 = openmc.Cell(fill=matfuel01)
cell201.region = -cyl201
fuel_cell_list.append(cell201.id)
cell202 = openmc.Cell(fill=matair)
cell202.region = +cyl201 & -cyl202
cell203 = openmc.Cell(fill=matclad)
cell203.region = +cyl202 & -cyl203
cell204 = openmc.Cell(fill=matcool)
cell204.region = +cyl203 & +px8 & -bnde & -py4 & +py5
biguni.add_cell(cell201)
biguni.add_cell(cell202)
biguni.add_cell(cell203)
biguni.add_cell(cell204)
# rod number (9,14)
x=  0.000000
y=  4.450000
cyl205 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl206 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl207 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell205 = openmc.Cell(fill=matfuel01)
cell205.region = -cyl205 & +bndw
fuel_cell_list.append(cell205.id)
cell206 = openmc.Cell(fill=matair)
cell206.region = +cyl205 & -cyl206 & +bndw
cell207 = openmc.Cell(fill=matclad)
cell207.region = +cyl206 & -cyl207 & +bndw
cell208 = openmc.Cell(fill=matcool)
cell208.region = +cyl207 & +bndw & -px1 & -py5 & +py6
biguni.add_cell(cell205)
biguni.add_cell(cell206)
biguni.add_cell(cell207)
biguni.add_cell(cell208)
# rod number (10,14)
x=  1.260000
y=  4.450000
cyl209 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl210 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl211 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell209 = openmc.Cell(fill=matfuel01)
cell209.region = -cyl209
fuel_cell_list.append(cell209.id)
cell210 = openmc.Cell(fill=matair)
cell210.region = +cyl209 & -cyl210
cell211 = openmc.Cell(fill=matclad)
cell211.region = +cyl210 & -cyl211
cell212 = openmc.Cell(fill=matcool)
cell212.region = +cyl211 & +px1 & -px2 & -py5 & +py6
biguni.add_cell(cell209)
biguni.add_cell(cell210)
biguni.add_cell(cell211)
biguni.add_cell(cell212)
# rod number (11,14)
x=  2.520000
y=  4.450000
cyl213 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl214 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl215 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell213 = openmc.Cell(fill=matfuel01)
cell213.region = -cyl213
fuel_cell_list.append(cell213.id)
cell214 = openmc.Cell(fill=matair)
cell214.region = +cyl213 & -cyl214
cell215 = openmc.Cell(fill=matclad)
cell215.region = +cyl214 & -cyl215
cell216 = openmc.Cell(fill=matcool)
cell216.region = +cyl215 & +px2 & -px3 & -py5 & +py6
biguni.add_cell(cell213)
biguni.add_cell(cell214)
biguni.add_cell(cell215)
biguni.add_cell(cell216)
# rod number (12,14)
x=  3.780000
y=  4.450000
cyl217 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl218 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl219 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell217 = openmc.Cell(fill=matfuel01)
cell217.region = -cyl217
fuel_cell_list.append(cell217.id)
cell218 = openmc.Cell(fill=matair)
cell218.region = +cyl217 & -cyl218
cell219 = openmc.Cell(fill=matclad)
cell219.region = +cyl218 & -cyl219
cell220 = openmc.Cell(fill=matcool)
cell220.region = +cyl219 & +px3 & -px4 & -py5 & +py6
biguni.add_cell(cell217)
biguni.add_cell(cell218)
biguni.add_cell(cell219)
biguni.add_cell(cell220)
# rod number (13,14)
x=  5.040000
y=  4.450000
cyl221 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl222 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl223 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell221 = openmc.Cell(fill=matfuel01)
cell221.region = -cyl221
fuel_cell_list.append(cell221.id)
cell222 = openmc.Cell(fill=matair)
cell222.region = +cyl221 & -cyl222
cell223 = openmc.Cell(fill=matclad)
cell223.region = +cyl222 & -cyl223
cell224 = openmc.Cell(fill=matcool)
cell224.region = +cyl223 & +px4 & -px5 & -py5 & +py6
biguni.add_cell(cell221)
biguni.add_cell(cell222)
biguni.add_cell(cell223)
biguni.add_cell(cell224)
# rod number (14,14)
x=  6.300000
y=  4.450000
cyl225 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl226 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl227 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl228 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl229 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl230 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl231 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl232 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell225 = openmc.Cell(fill=matair)
cell225.region = -cyl225
cell226 = openmc.Cell(fill=matss304)
cell226.region = +cyl225 & -cyl226
cell227 = openmc.Cell(fill=matair)
cell227.region = +cyl226 & -cyl227
cell228 = openmc.Cell(fill=matbsox)
cell228.region = +cyl227 & -cyl228
cell229 = openmc.Cell(fill=matair)
cell229.region = +cyl228 & -cyl229
cell230 = openmc.Cell(fill=matss304)
cell230.region = +cyl229 & -cyl230
cell231 = openmc.Cell(fill=matmod)
cell231.region = +cyl230 & -cyl231
cell232 = openmc.Cell(fill=matclad)
cell232.region = +cyl231 & -cyl232
cell233 = openmc.Cell(fill=matcool)
cell233.region = +cyl232 & +px5 & -px6 & -py5 & +py6
biguni.add_cell(cell225)
biguni.add_cell(cell226)
biguni.add_cell(cell227)
biguni.add_cell(cell228)
biguni.add_cell(cell229)
biguni.add_cell(cell230)
biguni.add_cell(cell231)
biguni.add_cell(cell232)
biguni.add_cell(cell233)
# rod number (15,14)
x=  7.560000
y=  4.450000
cyl234 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl235 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl236 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell234 = openmc.Cell(fill=matfuel01)
cell234.region = -cyl234
fuel_cell_list.append(cell234.id)
cell235 = openmc.Cell(fill=matair)
cell235.region = +cyl234 & -cyl235
cell236 = openmc.Cell(fill=matclad)
cell236.region = +cyl235 & -cyl236
cell237 = openmc.Cell(fill=matcool)
cell237.region = +cyl236 & +px6 & -px7 & -py5 & +py6
biguni.add_cell(cell234)
biguni.add_cell(cell235)
biguni.add_cell(cell236)
biguni.add_cell(cell237)
# rod number (16,14)
x=  8.820000
y=  4.450000
cyl238 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl239 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl240 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell238 = openmc.Cell(fill=matfuel01)
cell238.region = -cyl238
fuel_cell_list.append(cell238.id)
cell239 = openmc.Cell(fill=matair)
cell239.region = +cyl238 & -cyl239
cell240 = openmc.Cell(fill=matclad)
cell240.region = +cyl239 & -cyl240
cell241 = openmc.Cell(fill=matcool)
cell241.region = +cyl240 & +px7 & -px8 & -py5 & +py6
biguni.add_cell(cell238)
biguni.add_cell(cell239)
biguni.add_cell(cell240)
biguni.add_cell(cell241)
# rod number (17,14)
x= 10.080000
y=  4.450000
cyl242 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl243 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl244 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell242 = openmc.Cell(fill=matfuel01)
cell242.region = -cyl242
fuel_cell_list.append(cell242.id)
cell243 = openmc.Cell(fill=matair)
cell243.region = +cyl242 & -cyl243
cell244 = openmc.Cell(fill=matclad)
cell244.region = +cyl243 & -cyl244
cell245 = openmc.Cell(fill=matcool)
cell245.region = +cyl244 & +px8 & -bnde & -py5 & +py6
biguni.add_cell(cell242)
biguni.add_cell(cell243)
biguni.add_cell(cell244)
biguni.add_cell(cell245)
# rod number (9,15)
x=  0.000000
y=  3.190000
cyl246 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl247 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl248 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl249 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl250 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl251 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl252 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl253 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell246 = openmc.Cell(fill=matair)
cell246.region = -cyl246 & +bndw
cell247 = openmc.Cell(fill=matss304)
cell247.region = +cyl246 & -cyl247 & +bndw
cell248 = openmc.Cell(fill=matair)
cell248.region = +cyl247 & -cyl248 & +bndw
cell249 = openmc.Cell(fill=matbsox)
cell249.region = +cyl248 & -cyl249 & +bndw
cell250 = openmc.Cell(fill=matair)
cell250.region = +cyl249 & -cyl250 & +bndw
cell251 = openmc.Cell(fill=matss304)
cell251.region = +cyl250 & -cyl251 & +bndw
cell252 = openmc.Cell(fill=matmod)
cell252.region = +cyl251 & -cyl252 & +bndw
cell253 = openmc.Cell(fill=matclad)
cell253.region = +cyl252 & -cyl253 & +bndw
cell254 = openmc.Cell(fill=matcool)
cell254.region = +cyl253 & +bndw & -px1 & -py6 & +py7
biguni.add_cell(cell246)
biguni.add_cell(cell247)
biguni.add_cell(cell248)
biguni.add_cell(cell249)
biguni.add_cell(cell250)
biguni.add_cell(cell251)
biguni.add_cell(cell252)
biguni.add_cell(cell253)
biguni.add_cell(cell254)
# rod number (10,15)
x=  1.260000
y=  3.190000
cyl255 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl256 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl257 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell255 = openmc.Cell(fill=matfuel01)
cell255.region = -cyl255
fuel_cell_list.append(cell255.id)
cell256 = openmc.Cell(fill=matair)
cell256.region = +cyl255 & -cyl256
cell257 = openmc.Cell(fill=matclad)
cell257.region = +cyl256 & -cyl257
cell258 = openmc.Cell(fill=matcool)
cell258.region = +cyl257 & +px1 & -px2 & -py6 & +py7
biguni.add_cell(cell255)
biguni.add_cell(cell256)
biguni.add_cell(cell257)
biguni.add_cell(cell258)
# rod number (11,15)
x=  2.520000
y=  3.190000
cyl259 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl260 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl261 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell259 = openmc.Cell(fill=matfuel01)
cell259.region = -cyl259
fuel_cell_list.append(cell259.id)
cell260 = openmc.Cell(fill=matair)
cell260.region = +cyl259 & -cyl260
cell261 = openmc.Cell(fill=matclad)
cell261.region = +cyl260 & -cyl261
cell262 = openmc.Cell(fill=matcool)
cell262.region = +cyl261 & +px2 & -px3 & -py6 & +py7
biguni.add_cell(cell259)
biguni.add_cell(cell260)
biguni.add_cell(cell261)
biguni.add_cell(cell262)
# rod number (12,15)
x=  3.780000
y=  3.190000
cyl263 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl264 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl265 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl266 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl267 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl268 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl269 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl270 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell263 = openmc.Cell(fill=matair)
cell263.region = -cyl263
cell264 = openmc.Cell(fill=matss304)
cell264.region = +cyl263 & -cyl264
cell265 = openmc.Cell(fill=matair)
cell265.region = +cyl264 & -cyl265
cell266 = openmc.Cell(fill=matbsox)
cell266.region = +cyl265 & -cyl266
cell267 = openmc.Cell(fill=matair)
cell267.region = +cyl266 & -cyl267
cell268 = openmc.Cell(fill=matss304)
cell268.region = +cyl267 & -cyl268
cell269 = openmc.Cell(fill=matmod)
cell269.region = +cyl268 & -cyl269
cell270 = openmc.Cell(fill=matclad)
cell270.region = +cyl269 & -cyl270
cell271 = openmc.Cell(fill=matcool)
cell271.region = +cyl270 & +px3 & -px4 & -py6 & +py7
biguni.add_cell(cell263)
biguni.add_cell(cell264)
biguni.add_cell(cell265)
biguni.add_cell(cell266)
biguni.add_cell(cell267)
biguni.add_cell(cell268)
biguni.add_cell(cell269)
biguni.add_cell(cell270)
biguni.add_cell(cell271)
# rod number (13,15)
x=  5.040000
y=  3.190000
cyl272 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl273 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl274 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell272 = openmc.Cell(fill=matfuel01)
cell272.region = -cyl272
fuel_cell_list.append(cell272.id)
cell273 = openmc.Cell(fill=matair)
cell273.region = +cyl272 & -cyl273
cell274 = openmc.Cell(fill=matclad)
cell274.region = +cyl273 & -cyl274
cell275 = openmc.Cell(fill=matcool)
cell275.region = +cyl274 & +px4 & -px5 & -py6 & +py7
biguni.add_cell(cell272)
biguni.add_cell(cell273)
biguni.add_cell(cell274)
biguni.add_cell(cell275)
# rod number (14,15)
x=  6.300000
y=  3.190000
cyl276 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl277 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl278 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell276 = openmc.Cell(fill=matfuel01)
cell276.region = -cyl276
fuel_cell_list.append(cell276.id)
cell277 = openmc.Cell(fill=matair)
cell277.region = +cyl276 & -cyl277
cell278 = openmc.Cell(fill=matclad)
cell278.region = +cyl277 & -cyl278
cell279 = openmc.Cell(fill=matcool)
cell279.region = +cyl278 & +px5 & -px6 & -py6 & +py7
biguni.add_cell(cell276)
biguni.add_cell(cell277)
biguni.add_cell(cell278)
biguni.add_cell(cell279)
# rod number (15,15)
x=  7.560000
y=  3.190000
cyl280 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl281 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl282 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell280 = openmc.Cell(fill=matfuel01)
cell280.region = -cyl280
fuel_cell_list.append(cell280.id)
cell281 = openmc.Cell(fill=matair)
cell281.region = +cyl280 & -cyl281
cell282 = openmc.Cell(fill=matclad)
cell282.region = +cyl281 & -cyl282
cell283 = openmc.Cell(fill=matcool)
cell283.region = +cyl282 & +px6 & -px7 & -py6 & +py7
biguni.add_cell(cell280)
biguni.add_cell(cell281)
biguni.add_cell(cell282)
biguni.add_cell(cell283)
# rod number (16,15)
x=  8.820000
y=  3.190000
cyl284 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl285 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl286 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell284 = openmc.Cell(fill=matfuel01)
cell284.region = -cyl284
fuel_cell_list.append(cell284.id)
cell285 = openmc.Cell(fill=matair)
cell285.region = +cyl284 & -cyl285
cell286 = openmc.Cell(fill=matclad)
cell286.region = +cyl285 & -cyl286
cell287 = openmc.Cell(fill=matcool)
cell287.region = +cyl286 & +px7 & -px8 & -py6 & +py7
biguni.add_cell(cell284)
biguni.add_cell(cell285)
biguni.add_cell(cell286)
biguni.add_cell(cell287)
# rod number (17,15)
x= 10.080000
y=  3.190000
cyl288 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl289 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl290 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell288 = openmc.Cell(fill=matfuel01)
cell288.region = -cyl288
fuel_cell_list.append(cell288.id)
cell289 = openmc.Cell(fill=matair)
cell289.region = +cyl288 & -cyl289
cell290 = openmc.Cell(fill=matclad)
cell290.region = +cyl289 & -cyl290
cell291 = openmc.Cell(fill=matcool)
cell291.region = +cyl290 & +px8 & -bnde & -py6 & +py7
biguni.add_cell(cell288)
biguni.add_cell(cell289)
biguni.add_cell(cell290)
biguni.add_cell(cell291)
# rod number (9,16)
x=  0.000000
y=  1.930000
cyl292 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl293 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl294 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell292 = openmc.Cell(fill=matfuel01)
cell292.region = -cyl292 & +bndw
fuel_cell_list.append(cell292.id)
cell293 = openmc.Cell(fill=matair)
cell293.region = +cyl292 & -cyl293 & +bndw
cell294 = openmc.Cell(fill=matclad)
cell294.region = +cyl293 & -cyl294 & +bndw
cell295 = openmc.Cell(fill=matcool)
cell295.region = +cyl294 & +bndw & -px1 & -py7 & +py8
biguni.add_cell(cell292)
biguni.add_cell(cell293)
biguni.add_cell(cell294)
biguni.add_cell(cell295)
# rod number (10,16)
x=  1.260000
y=  1.930000
cyl296 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl297 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl298 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell296 = openmc.Cell(fill=matfuel01)
cell296.region = -cyl296
fuel_cell_list.append(cell296.id)
cell297 = openmc.Cell(fill=matair)
cell297.region = +cyl296 & -cyl297
cell298 = openmc.Cell(fill=matclad)
cell298.region = +cyl297 & -cyl298
cell299 = openmc.Cell(fill=matcool)
cell299.region = +cyl298 & +px1 & -px2 & -py7 & +py8
biguni.add_cell(cell296)
biguni.add_cell(cell297)
biguni.add_cell(cell298)
biguni.add_cell(cell299)
# rod number (11,16)
x=  2.520000
y=  1.930000
cyl300 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl301 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl302 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell300 = openmc.Cell(fill=matfuel01)
cell300.region = -cyl300
fuel_cell_list.append(cell300.id)
cell301 = openmc.Cell(fill=matair)
cell301.region = +cyl300 & -cyl301
cell302 = openmc.Cell(fill=matclad)
cell302.region = +cyl301 & -cyl302
cell303 = openmc.Cell(fill=matcool)
cell303.region = +cyl302 & +px2 & -px3 & -py7 & +py8
biguni.add_cell(cell300)
biguni.add_cell(cell301)
biguni.add_cell(cell302)
biguni.add_cell(cell303)
# rod number (12,16)
x=  3.780000
y=  1.930000
cyl304 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl305 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl306 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell304 = openmc.Cell(fill=matfuel01)
cell304.region = -cyl304
fuel_cell_list.append(cell304.id)
cell305 = openmc.Cell(fill=matair)
cell305.region = +cyl304 & -cyl305
cell306 = openmc.Cell(fill=matclad)
cell306.region = +cyl305 & -cyl306
cell307 = openmc.Cell(fill=matcool)
cell307.region = +cyl306 & +px3 & -px4 & -py7 & +py8
biguni.add_cell(cell304)
biguni.add_cell(cell305)
biguni.add_cell(cell306)
biguni.add_cell(cell307)
# rod number (13,16)
x=  5.040000
y=  1.930000
cyl308 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl309 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl310 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell308 = openmc.Cell(fill=matfuel01)
cell308.region = -cyl308
fuel_cell_list.append(cell308.id)
cell309 = openmc.Cell(fill=matair)
cell309.region = +cyl308 & -cyl309
cell310 = openmc.Cell(fill=matclad)
cell310.region = +cyl309 & -cyl310
cell311 = openmc.Cell(fill=matcool)
cell311.region = +cyl310 & +px4 & -px5 & -py7 & +py8
biguni.add_cell(cell308)
biguni.add_cell(cell309)
biguni.add_cell(cell310)
biguni.add_cell(cell311)
# rod number (14,16)
x=  6.300000
y=  1.930000
cyl312 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl313 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl314 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell312 = openmc.Cell(fill=matfuel01)
cell312.region = -cyl312
fuel_cell_list.append(cell312.id)
cell313 = openmc.Cell(fill=matair)
cell313.region = +cyl312 & -cyl313
cell314 = openmc.Cell(fill=matclad)
cell314.region = +cyl313 & -cyl314
cell315 = openmc.Cell(fill=matcool)
cell315.region = +cyl314 & +px5 & -px6 & -py7 & +py8
biguni.add_cell(cell312)
biguni.add_cell(cell313)
biguni.add_cell(cell314)
biguni.add_cell(cell315)
# rod number (15,16)
x=  7.560000
y=  1.930000
cyl316 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl317 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl318 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell316 = openmc.Cell(fill=matfuel01)
cell316.region = -cyl316
fuel_cell_list.append(cell316.id)
cell317 = openmc.Cell(fill=matair)
cell317.region = +cyl316 & -cyl317
cell318 = openmc.Cell(fill=matclad)
cell318.region = +cyl317 & -cyl318
cell319 = openmc.Cell(fill=matcool)
cell319.region = +cyl318 & +px6 & -px7 & -py7 & +py8
biguni.add_cell(cell316)
biguni.add_cell(cell317)
biguni.add_cell(cell318)
biguni.add_cell(cell319)
# rod number (16,16)
x=  8.820000
y=  1.930000
cyl320 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl321 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl322 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell320 = openmc.Cell(fill=matfuel01)
cell320.region = -cyl320
fuel_cell_list.append(cell320.id)
cell321 = openmc.Cell(fill=matair)
cell321.region = +cyl320 & -cyl321
cell322 = openmc.Cell(fill=matclad)
cell322.region = +cyl321 & -cyl322
cell323 = openmc.Cell(fill=matcool)
cell323.region = +cyl322 & +px7 & -px8 & -py7 & +py8
biguni.add_cell(cell320)
biguni.add_cell(cell321)
biguni.add_cell(cell322)
biguni.add_cell(cell323)
# rod number (17,16)
x= 10.080000
y=  1.930000
cyl324 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl325 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl326 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell324 = openmc.Cell(fill=matfuel01)
cell324.region = -cyl324
fuel_cell_list.append(cell324.id)
cell325 = openmc.Cell(fill=matair)
cell325.region = +cyl324 & -cyl325
cell326 = openmc.Cell(fill=matclad)
cell326.region = +cyl325 & -cyl326
cell327 = openmc.Cell(fill=matcool)
cell327.region = +cyl326 & +px8 & -bnde & -py7 & +py8
biguni.add_cell(cell324)
biguni.add_cell(cell325)
biguni.add_cell(cell326)
biguni.add_cell(cell327)
# rod number (9,17)
x=  0.000000
y=  0.670000
cyl328 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl329 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl330 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell328 = openmc.Cell(fill=matfuel01)
cell328.region = -cyl328 & +bndw
fuel_cell_list.append(cell328.id)
cell329 = openmc.Cell(fill=matair)
cell329.region = +cyl328 & -cyl329 & +bndw
cell330 = openmc.Cell(fill=matclad)
cell330.region = +cyl329 & -cyl330 & +bndw
cell331 = openmc.Cell(fill=matcool)
cell331.region = +cyl330 & +bndw & -px1 & -py8 & +bnds
biguni.add_cell(cell328)
biguni.add_cell(cell329)
biguni.add_cell(cell330)
biguni.add_cell(cell331)
# rod number (10,17)
x=  1.260000
y=  0.670000
cyl332 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl333 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl334 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell332 = openmc.Cell(fill=matfuel01)
cell332.region = -cyl332
fuel_cell_list.append(cell332.id)
cell333 = openmc.Cell(fill=matair)
cell333.region = +cyl332 & -cyl333
cell334 = openmc.Cell(fill=matclad)
cell334.region = +cyl333 & -cyl334
cell335 = openmc.Cell(fill=matcool)
cell335.region = +cyl334 & +px1 & -px2 & -py8 & +bnds
biguni.add_cell(cell332)
biguni.add_cell(cell333)
biguni.add_cell(cell334)
biguni.add_cell(cell335)
# rod number (11,17)
x=  2.520000
y=  0.670000
cyl336 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl337 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl338 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell336 = openmc.Cell(fill=matfuel01)
cell336.region = -cyl336
fuel_cell_list.append(cell336.id)
cell337 = openmc.Cell(fill=matair)
cell337.region = +cyl336 & -cyl337
cell338 = openmc.Cell(fill=matclad)
cell338.region = +cyl337 & -cyl338
cell339 = openmc.Cell(fill=matcool)
cell339.region = +cyl338 & +px2 & -px3 & -py8 & +bnds
biguni.add_cell(cell336)
biguni.add_cell(cell337)
biguni.add_cell(cell338)
biguni.add_cell(cell339)
# rod number (12,17)
x=  3.780000
y=  0.670000
cyl340 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl341 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl342 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell340 = openmc.Cell(fill=matfuel01)
cell340.region = -cyl340
fuel_cell_list.append(cell340.id)
cell341 = openmc.Cell(fill=matair)
cell341.region = +cyl340 & -cyl341
cell342 = openmc.Cell(fill=matclad)
cell342.region = +cyl341 & -cyl342
cell343 = openmc.Cell(fill=matcool)
cell343.region = +cyl342 & +px3 & -px4 & -py8 & +bnds
biguni.add_cell(cell340)
biguni.add_cell(cell341)
biguni.add_cell(cell342)
biguni.add_cell(cell343)
# rod number (13,17)
x=  5.040000
y=  0.670000
cyl344 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl345 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl346 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell344 = openmc.Cell(fill=matfuel01)
cell344.region = -cyl344
fuel_cell_list.append(cell344.id)
cell345 = openmc.Cell(fill=matair)
cell345.region = +cyl344 & -cyl345
cell346 = openmc.Cell(fill=matclad)
cell346.region = +cyl345 & -cyl346
cell347 = openmc.Cell(fill=matcool)
cell347.region = +cyl346 & +px4 & -px5 & -py8 & +bnds
biguni.add_cell(cell344)
biguni.add_cell(cell345)
biguni.add_cell(cell346)
biguni.add_cell(cell347)
# rod number (14,17)
x=  6.300000
y=  0.670000
cyl348 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl349 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl350 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell348 = openmc.Cell(fill=matfuel01)
cell348.region = -cyl348
fuel_cell_list.append(cell348.id)
cell349 = openmc.Cell(fill=matair)
cell349.region = +cyl348 & -cyl349
cell350 = openmc.Cell(fill=matclad)
cell350.region = +cyl349 & -cyl350
cell351 = openmc.Cell(fill=matcool)
cell351.region = +cyl350 & +px5 & -px6 & -py8 & +bnds
biguni.add_cell(cell348)
biguni.add_cell(cell349)
biguni.add_cell(cell350)
biguni.add_cell(cell351)
# rod number (15,17)
x=  7.560000
y=  0.670000
cyl352 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl353 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl354 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell352 = openmc.Cell(fill=matfuel01)
cell352.region = -cyl352
fuel_cell_list.append(cell352.id)
cell353 = openmc.Cell(fill=matair)
cell353.region = +cyl352 & -cyl353
cell354 = openmc.Cell(fill=matclad)
cell354.region = +cyl353 & -cyl354
cell355 = openmc.Cell(fill=matcool)
cell355.region = +cyl354 & +px6 & -px7 & -py8 & +bnds
biguni.add_cell(cell352)
biguni.add_cell(cell353)
biguni.add_cell(cell354)
biguni.add_cell(cell355)
# rod number (16,17)
x=  8.820000
y=  0.670000
cyl356 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl357 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl358 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell356 = openmc.Cell(fill=matfuel01)
cell356.region = -cyl356
fuel_cell_list.append(cell356.id)
cell357 = openmc.Cell(fill=matair)
cell357.region = +cyl356 & -cyl357
cell358 = openmc.Cell(fill=matclad)
cell358.region = +cyl357 & -cyl358
cell359 = openmc.Cell(fill=matcool)
cell359.region = +cyl358 & +px7 & -px8 & -py8 & +bnds
biguni.add_cell(cell356)
biguni.add_cell(cell357)
biguni.add_cell(cell358)
biguni.add_cell(cell359)
# rod number (17,17)
x= 10.080000
y=  0.670000
cyl360 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl361 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl362 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell360 = openmc.Cell(fill=matfuel01)
cell360.region = -cyl360
fuel_cell_list.append(cell360.id)
cell361 = openmc.Cell(fill=matair)
cell361.region = +cyl360 & -cyl361
cell362 = openmc.Cell(fill=matclad)
cell362.region = +cyl361 & -cyl362
cell363 = openmc.Cell(fill=matcool)
cell363.region = +cyl362 & +px8 & -bnde & -py8 & +bnds
biguni.add_cell(cell360)
biguni.add_cell(cell361)
biguni.add_cell(cell362)
biguni.add_cell(cell363)

# export geometry
model.geometry = openmc.Geometry(biguni)

# -------------- Plot ------------

model.export_to_xml()
plot1 = openmc.Plot()
plot1.basis = 'xy'
plot1.origin = (  5.385,  5.385, 0)
plot1.width  = ( 10.750, 10.750)
plot1.pixels = (400,400)
plot1.color_by = 'material'
plot1.colors = {matclad: 'gray'}

plots = openmc.Plots([plot1])
plots.export_to_xml()
openmc.plot_geometry()

# OpenMC simulation parameters

lower_left  = [   0.0000,   0.0000,-20]
upper_right = [  10.7499,  10.7499, 20]
uniform_dist = openmc.stats.Box(lower_left, upper_right)
src = openmc.IndependentSource(space=uniform_dist, constraints={'fissionable': True})

settings = openmc.Settings()
settings.source = src
settings.batches = 2000  # active
settings.inactive = 100
settings.particles = 200000
settings.output = {'tallies': True}

model.settings = settings
#==================== Set up fission rate tallies =================

# cell filter of all cells with fuel
cell_filter = openmc.CellFilter(fuel_cell_list)

# Instantiate an empty Tallies object
tally = openmc.Tally(name='fission')
tally.filters.append(cell_filter)
tally.scores = ['fission']

tallies = openmc.Tallies([tally])

model.tallies = tallies

#======================= Run ==========================

statepoint_file = model.run()
