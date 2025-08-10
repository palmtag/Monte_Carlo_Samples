import matplotlib

import openmc
import openmc.mgxs as mgxs
import openmc.data          # need for hdf5

#  To run:
#  >python3 vera2j.omc
#
# OpenMC Input created by BUNBLD on 08/09/2025 11:48:06
#  VERA Benchmark #2 - Single Assembly
#  Uniform PWR Assembly
#  November 15, 2012
#  Number densities from KENO run
#  VERA Benchmark 2J - Like 2A + 24 Pyrex rods + instrument thimble
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
cyl1 = openmc.ZCylinder(x0=x, y0=y, r= 0.25800)  # AIR
cyl2 = openmc.ZCylinder(x0=x, y0=y, r= 0.38200)  # SS304
cyl3 = openmc.ZCylinder(x0=x, y0=y, r= 0.55900)  # MOD
cyl4 = openmc.ZCylinder(x0=x, y0=y, r= 0.60500)  # CLAD
cell1 = openmc.Cell(fill=matair)
cell1.region = -cyl1 & +bndw & -bndn
cell2 = openmc.Cell(fill=matss304)
cell2.region = +cyl1 & -cyl2 & +bndw & -bndn
cell3 = openmc.Cell(fill=matmod)
cell3.region = +cyl2 & -cyl3 & +bndw & -bndn
cell4 = openmc.Cell(fill=matclad)
cell4.region = +cyl3 & -cyl4 & +bndw & -bndn
cell5 = openmc.Cell(fill=matcool)
cell5.region = +cyl4 & +bndw & -px1 & -bndn & +py1
biguni.add_cell(cell1)
biguni.add_cell(cell2)
biguni.add_cell(cell3)
biguni.add_cell(cell4)
biguni.add_cell(cell5)
# rod number (10,9)
x=  1.260000
y= 10.750000
cyl6 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl7 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl8 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell6 = openmc.Cell(fill=matfuel01)
cell6.region = -cyl6 & -bndn
fuel_cell_list.append(cell6.id)
cell7 = openmc.Cell(fill=matair)
cell7.region = +cyl6 & -cyl7 & -bndn
cell8 = openmc.Cell(fill=matclad)
cell8.region = +cyl7 & -cyl8 & -bndn
cell9 = openmc.Cell(fill=matcool)
cell9.region = +cyl8 & +px1 & -px2 & -bndn & +py1
biguni.add_cell(cell6)
biguni.add_cell(cell7)
biguni.add_cell(cell8)
biguni.add_cell(cell9)
# rod number (11,9)
x=  2.520000
y= 10.750000
cyl10 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl11 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl12 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell10 = openmc.Cell(fill=matfuel01)
cell10.region = -cyl10 & -bndn
fuel_cell_list.append(cell10.id)
cell11 = openmc.Cell(fill=matair)
cell11.region = +cyl10 & -cyl11 & -bndn
cell12 = openmc.Cell(fill=matclad)
cell12.region = +cyl11 & -cyl12 & -bndn
cell13 = openmc.Cell(fill=matcool)
cell13.region = +cyl12 & +px2 & -px3 & -bndn & +py1
biguni.add_cell(cell10)
biguni.add_cell(cell11)
biguni.add_cell(cell12)
biguni.add_cell(cell13)
# rod number (12,9)
x=  3.780000
y= 10.750000
cyl14 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl15 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl16 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl17 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl18 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl19 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl20 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl21 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell14 = openmc.Cell(fill=matair)
cell14.region = -cyl14 & -bndn
cell15 = openmc.Cell(fill=matss304)
cell15.region = +cyl14 & -cyl15 & -bndn
cell16 = openmc.Cell(fill=matair)
cell16.region = +cyl15 & -cyl16 & -bndn
cell17 = openmc.Cell(fill=matbsox)
cell17.region = +cyl16 & -cyl17 & -bndn
cell18 = openmc.Cell(fill=matair)
cell18.region = +cyl17 & -cyl18 & -bndn
cell19 = openmc.Cell(fill=matss304)
cell19.region = +cyl18 & -cyl19 & -bndn
cell20 = openmc.Cell(fill=matmod)
cell20.region = +cyl19 & -cyl20 & -bndn
cell21 = openmc.Cell(fill=matclad)
cell21.region = +cyl20 & -cyl21 & -bndn
cell22 = openmc.Cell(fill=matcool)
cell22.region = +cyl21 & +px3 & -px4 & -bndn & +py1
biguni.add_cell(cell14)
biguni.add_cell(cell15)
biguni.add_cell(cell16)
biguni.add_cell(cell17)
biguni.add_cell(cell18)
biguni.add_cell(cell19)
biguni.add_cell(cell20)
biguni.add_cell(cell21)
biguni.add_cell(cell22)
# rod number (13,9)
x=  5.040000
y= 10.750000
cyl23 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl24 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl25 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell23 = openmc.Cell(fill=matfuel01)
cell23.region = -cyl23 & -bndn
fuel_cell_list.append(cell23.id)
cell24 = openmc.Cell(fill=matair)
cell24.region = +cyl23 & -cyl24 & -bndn
cell25 = openmc.Cell(fill=matclad)
cell25.region = +cyl24 & -cyl25 & -bndn
cell26 = openmc.Cell(fill=matcool)
cell26.region = +cyl25 & +px4 & -px5 & -bndn & +py1
biguni.add_cell(cell23)
biguni.add_cell(cell24)
biguni.add_cell(cell25)
biguni.add_cell(cell26)
# rod number (14,9)
x=  6.300000
y= 10.750000
cyl27 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl28 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl29 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell27 = openmc.Cell(fill=matfuel01)
cell27.region = -cyl27 & -bndn
fuel_cell_list.append(cell27.id)
cell28 = openmc.Cell(fill=matair)
cell28.region = +cyl27 & -cyl28 & -bndn
cell29 = openmc.Cell(fill=matclad)
cell29.region = +cyl28 & -cyl29 & -bndn
cell30 = openmc.Cell(fill=matcool)
cell30.region = +cyl29 & +px5 & -px6 & -bndn & +py1
biguni.add_cell(cell27)
biguni.add_cell(cell28)
biguni.add_cell(cell29)
biguni.add_cell(cell30)
# rod number (15,9)
x=  7.560000
y= 10.750000
cyl31 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl32 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl33 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl34 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl35 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl36 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl37 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl38 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell31 = openmc.Cell(fill=matair)
cell31.region = -cyl31 & -bndn
cell32 = openmc.Cell(fill=matss304)
cell32.region = +cyl31 & -cyl32 & -bndn
cell33 = openmc.Cell(fill=matair)
cell33.region = +cyl32 & -cyl33 & -bndn
cell34 = openmc.Cell(fill=matbsox)
cell34.region = +cyl33 & -cyl34 & -bndn
cell35 = openmc.Cell(fill=matair)
cell35.region = +cyl34 & -cyl35 & -bndn
cell36 = openmc.Cell(fill=matss304)
cell36.region = +cyl35 & -cyl36 & -bndn
cell37 = openmc.Cell(fill=matmod)
cell37.region = +cyl36 & -cyl37 & -bndn
cell38 = openmc.Cell(fill=matclad)
cell38.region = +cyl37 & -cyl38 & -bndn
cell39 = openmc.Cell(fill=matcool)
cell39.region = +cyl38 & +px6 & -px7 & -bndn & +py1
biguni.add_cell(cell31)
biguni.add_cell(cell32)
biguni.add_cell(cell33)
biguni.add_cell(cell34)
biguni.add_cell(cell35)
biguni.add_cell(cell36)
biguni.add_cell(cell37)
biguni.add_cell(cell38)
biguni.add_cell(cell39)
# rod number (16,9)
x=  8.820000
y= 10.750000
cyl40 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl41 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl42 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell40 = openmc.Cell(fill=matfuel01)
cell40.region = -cyl40 & -bndn
fuel_cell_list.append(cell40.id)
cell41 = openmc.Cell(fill=matair)
cell41.region = +cyl40 & -cyl41 & -bndn
cell42 = openmc.Cell(fill=matclad)
cell42.region = +cyl41 & -cyl42 & -bndn
cell43 = openmc.Cell(fill=matcool)
cell43.region = +cyl42 & +px7 & -px8 & -bndn & +py1
biguni.add_cell(cell40)
biguni.add_cell(cell41)
biguni.add_cell(cell42)
biguni.add_cell(cell43)
# rod number (17,9)
x= 10.080000
y= 10.750000
cyl44 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl45 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl46 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell44 = openmc.Cell(fill=matfuel01)
cell44.region = -cyl44 & -bndn
fuel_cell_list.append(cell44.id)
cell45 = openmc.Cell(fill=matair)
cell45.region = +cyl44 & -cyl45 & -bndn
cell46 = openmc.Cell(fill=matclad)
cell46.region = +cyl45 & -cyl46 & -bndn
cell47 = openmc.Cell(fill=matcool)
cell47.region = +cyl46 & +px8 & -bnde & -bndn & +py1
biguni.add_cell(cell44)
biguni.add_cell(cell45)
biguni.add_cell(cell46)
biguni.add_cell(cell47)
# rod number (9,10)
x=  0.000000
y=  9.490000
cyl48 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl49 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl50 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell48 = openmc.Cell(fill=matfuel01)
cell48.region = -cyl48 & +bndw
fuel_cell_list.append(cell48.id)
cell49 = openmc.Cell(fill=matair)
cell49.region = +cyl48 & -cyl49 & +bndw
cell50 = openmc.Cell(fill=matclad)
cell50.region = +cyl49 & -cyl50 & +bndw
cell51 = openmc.Cell(fill=matcool)
cell51.region = +cyl50 & +bndw & -px1 & -py1 & +py2
biguni.add_cell(cell48)
biguni.add_cell(cell49)
biguni.add_cell(cell50)
biguni.add_cell(cell51)
# rod number (10,10)
x=  1.260000
y=  9.490000
cyl52 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl53 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl54 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell52 = openmc.Cell(fill=matfuel01)
cell52.region = -cyl52
fuel_cell_list.append(cell52.id)
cell53 = openmc.Cell(fill=matair)
cell53.region = +cyl52 & -cyl53
cell54 = openmc.Cell(fill=matclad)
cell54.region = +cyl53 & -cyl54
cell55 = openmc.Cell(fill=matcool)
cell55.region = +cyl54 & +px1 & -px2 & -py1 & +py2
biguni.add_cell(cell52)
biguni.add_cell(cell53)
biguni.add_cell(cell54)
biguni.add_cell(cell55)
# rod number (11,10)
x=  2.520000
y=  9.490000
cyl56 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl57 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl58 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell56 = openmc.Cell(fill=matfuel01)
cell56.region = -cyl56
fuel_cell_list.append(cell56.id)
cell57 = openmc.Cell(fill=matair)
cell57.region = +cyl56 & -cyl57
cell58 = openmc.Cell(fill=matclad)
cell58.region = +cyl57 & -cyl58
cell59 = openmc.Cell(fill=matcool)
cell59.region = +cyl58 & +px2 & -px3 & -py1 & +py2
biguni.add_cell(cell56)
biguni.add_cell(cell57)
biguni.add_cell(cell58)
biguni.add_cell(cell59)
# rod number (12,10)
x=  3.780000
y=  9.490000
cyl60 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl61 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl62 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell60 = openmc.Cell(fill=matfuel01)
cell60.region = -cyl60
fuel_cell_list.append(cell60.id)
cell61 = openmc.Cell(fill=matair)
cell61.region = +cyl60 & -cyl61
cell62 = openmc.Cell(fill=matclad)
cell62.region = +cyl61 & -cyl62
cell63 = openmc.Cell(fill=matcool)
cell63.region = +cyl62 & +px3 & -px4 & -py1 & +py2
biguni.add_cell(cell60)
biguni.add_cell(cell61)
biguni.add_cell(cell62)
biguni.add_cell(cell63)
# rod number (13,10)
x=  5.040000
y=  9.490000
cyl64 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl65 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl66 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell64 = openmc.Cell(fill=matfuel01)
cell64.region = -cyl64
fuel_cell_list.append(cell64.id)
cell65 = openmc.Cell(fill=matair)
cell65.region = +cyl64 & -cyl65
cell66 = openmc.Cell(fill=matclad)
cell66.region = +cyl65 & -cyl66
cell67 = openmc.Cell(fill=matcool)
cell67.region = +cyl66 & +px4 & -px5 & -py1 & +py2
biguni.add_cell(cell64)
biguni.add_cell(cell65)
biguni.add_cell(cell66)
biguni.add_cell(cell67)
# rod number (14,10)
x=  6.300000
y=  9.490000
cyl68 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl69 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl70 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell68 = openmc.Cell(fill=matfuel01)
cell68.region = -cyl68
fuel_cell_list.append(cell68.id)
cell69 = openmc.Cell(fill=matair)
cell69.region = +cyl68 & -cyl69
cell70 = openmc.Cell(fill=matclad)
cell70.region = +cyl69 & -cyl70
cell71 = openmc.Cell(fill=matcool)
cell71.region = +cyl70 & +px5 & -px6 & -py1 & +py2
biguni.add_cell(cell68)
biguni.add_cell(cell69)
biguni.add_cell(cell70)
biguni.add_cell(cell71)
# rod number (15,10)
x=  7.560000
y=  9.490000
cyl72 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl73 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl74 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell72 = openmc.Cell(fill=matfuel01)
cell72.region = -cyl72
fuel_cell_list.append(cell72.id)
cell73 = openmc.Cell(fill=matair)
cell73.region = +cyl72 & -cyl73
cell74 = openmc.Cell(fill=matclad)
cell74.region = +cyl73 & -cyl74
cell75 = openmc.Cell(fill=matcool)
cell75.region = +cyl74 & +px6 & -px7 & -py1 & +py2
biguni.add_cell(cell72)
biguni.add_cell(cell73)
biguni.add_cell(cell74)
biguni.add_cell(cell75)
# rod number (16,10)
x=  8.820000
y=  9.490000
cyl76 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl77 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl78 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell76 = openmc.Cell(fill=matfuel01)
cell76.region = -cyl76
fuel_cell_list.append(cell76.id)
cell77 = openmc.Cell(fill=matair)
cell77.region = +cyl76 & -cyl77
cell78 = openmc.Cell(fill=matclad)
cell78.region = +cyl77 & -cyl78
cell79 = openmc.Cell(fill=matcool)
cell79.region = +cyl78 & +px7 & -px8 & -py1 & +py2
biguni.add_cell(cell76)
biguni.add_cell(cell77)
biguni.add_cell(cell78)
biguni.add_cell(cell79)
# rod number (17,10)
x= 10.080000
y=  9.490000
cyl80 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl81 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl82 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell80 = openmc.Cell(fill=matfuel01)
cell80.region = -cyl80
fuel_cell_list.append(cell80.id)
cell81 = openmc.Cell(fill=matair)
cell81.region = +cyl80 & -cyl81
cell82 = openmc.Cell(fill=matclad)
cell82.region = +cyl81 & -cyl82
cell83 = openmc.Cell(fill=matcool)
cell83.region = +cyl82 & +px8 & -bnde & -py1 & +py2
biguni.add_cell(cell80)
biguni.add_cell(cell81)
biguni.add_cell(cell82)
biguni.add_cell(cell83)
# rod number (9,11)
x=  0.000000
y=  8.230000
cyl84 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl85 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl86 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell84 = openmc.Cell(fill=matfuel01)
cell84.region = -cyl84 & +bndw
fuel_cell_list.append(cell84.id)
cell85 = openmc.Cell(fill=matair)
cell85.region = +cyl84 & -cyl85 & +bndw
cell86 = openmc.Cell(fill=matclad)
cell86.region = +cyl85 & -cyl86 & +bndw
cell87 = openmc.Cell(fill=matcool)
cell87.region = +cyl86 & +bndw & -px1 & -py2 & +py3
biguni.add_cell(cell84)
biguni.add_cell(cell85)
biguni.add_cell(cell86)
biguni.add_cell(cell87)
# rod number (10,11)
x=  1.260000
y=  8.230000
cyl88 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl89 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl90 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell88 = openmc.Cell(fill=matfuel01)
cell88.region = -cyl88
fuel_cell_list.append(cell88.id)
cell89 = openmc.Cell(fill=matair)
cell89.region = +cyl88 & -cyl89
cell90 = openmc.Cell(fill=matclad)
cell90.region = +cyl89 & -cyl90
cell91 = openmc.Cell(fill=matcool)
cell91.region = +cyl90 & +px1 & -px2 & -py2 & +py3
biguni.add_cell(cell88)
biguni.add_cell(cell89)
biguni.add_cell(cell90)
biguni.add_cell(cell91)
# rod number (11,11)
x=  2.520000
y=  8.230000
cyl92 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl93 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl94 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell92 = openmc.Cell(fill=matfuel01)
cell92.region = -cyl92
fuel_cell_list.append(cell92.id)
cell93 = openmc.Cell(fill=matair)
cell93.region = +cyl92 & -cyl93
cell94 = openmc.Cell(fill=matclad)
cell94.region = +cyl93 & -cyl94
cell95 = openmc.Cell(fill=matcool)
cell95.region = +cyl94 & +px2 & -px3 & -py2 & +py3
biguni.add_cell(cell92)
biguni.add_cell(cell93)
biguni.add_cell(cell94)
biguni.add_cell(cell95)
# rod number (12,11)
x=  3.780000
y=  8.230000
cyl96 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl97 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl98 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell96 = openmc.Cell(fill=matfuel01)
cell96.region = -cyl96
fuel_cell_list.append(cell96.id)
cell97 = openmc.Cell(fill=matair)
cell97.region = +cyl96 & -cyl97
cell98 = openmc.Cell(fill=matclad)
cell98.region = +cyl97 & -cyl98
cell99 = openmc.Cell(fill=matcool)
cell99.region = +cyl98 & +px3 & -px4 & -py2 & +py3
biguni.add_cell(cell96)
biguni.add_cell(cell97)
biguni.add_cell(cell98)
biguni.add_cell(cell99)
# rod number (13,11)
x=  5.040000
y=  8.230000
cyl100 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl101 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl102 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell100 = openmc.Cell(fill=matfuel01)
cell100.region = -cyl100
fuel_cell_list.append(cell100.id)
cell101 = openmc.Cell(fill=matair)
cell101.region = +cyl100 & -cyl101
cell102 = openmc.Cell(fill=matclad)
cell102.region = +cyl101 & -cyl102
cell103 = openmc.Cell(fill=matcool)
cell103.region = +cyl102 & +px4 & -px5 & -py2 & +py3
biguni.add_cell(cell100)
biguni.add_cell(cell101)
biguni.add_cell(cell102)
biguni.add_cell(cell103)
# rod number (14,11)
x=  6.300000
y=  8.230000
cyl104 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl105 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl106 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell104 = openmc.Cell(fill=matfuel01)
cell104.region = -cyl104
fuel_cell_list.append(cell104.id)
cell105 = openmc.Cell(fill=matair)
cell105.region = +cyl104 & -cyl105
cell106 = openmc.Cell(fill=matclad)
cell106.region = +cyl105 & -cyl106
cell107 = openmc.Cell(fill=matcool)
cell107.region = +cyl106 & +px5 & -px6 & -py2 & +py3
biguni.add_cell(cell104)
biguni.add_cell(cell105)
biguni.add_cell(cell106)
biguni.add_cell(cell107)
# rod number (15,11)
x=  7.560000
y=  8.230000
cyl108 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl109 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl110 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell108 = openmc.Cell(fill=matfuel01)
cell108.region = -cyl108
fuel_cell_list.append(cell108.id)
cell109 = openmc.Cell(fill=matair)
cell109.region = +cyl108 & -cyl109
cell110 = openmc.Cell(fill=matclad)
cell110.region = +cyl109 & -cyl110
cell111 = openmc.Cell(fill=matcool)
cell111.region = +cyl110 & +px6 & -px7 & -py2 & +py3
biguni.add_cell(cell108)
biguni.add_cell(cell109)
biguni.add_cell(cell110)
biguni.add_cell(cell111)
# rod number (16,11)
x=  8.820000
y=  8.230000
cyl112 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl113 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl114 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell112 = openmc.Cell(fill=matfuel01)
cell112.region = -cyl112
fuel_cell_list.append(cell112.id)
cell113 = openmc.Cell(fill=matair)
cell113.region = +cyl112 & -cyl113
cell114 = openmc.Cell(fill=matclad)
cell114.region = +cyl113 & -cyl114
cell115 = openmc.Cell(fill=matcool)
cell115.region = +cyl114 & +px7 & -px8 & -py2 & +py3
biguni.add_cell(cell112)
biguni.add_cell(cell113)
biguni.add_cell(cell114)
biguni.add_cell(cell115)
# rod number (17,11)
x= 10.080000
y=  8.230000
cyl116 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl117 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl118 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell116 = openmc.Cell(fill=matfuel01)
cell116.region = -cyl116
fuel_cell_list.append(cell116.id)
cell117 = openmc.Cell(fill=matair)
cell117.region = +cyl116 & -cyl117
cell118 = openmc.Cell(fill=matclad)
cell118.region = +cyl117 & -cyl118
cell119 = openmc.Cell(fill=matcool)
cell119.region = +cyl118 & +px8 & -bnde & -py2 & +py3
biguni.add_cell(cell116)
biguni.add_cell(cell117)
biguni.add_cell(cell118)
biguni.add_cell(cell119)
# rod number (9,12)
x=  0.000000
y=  6.970000
cyl120 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl121 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl122 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl123 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl124 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl125 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl126 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl127 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell120 = openmc.Cell(fill=matair)
cell120.region = -cyl120 & +bndw
cell121 = openmc.Cell(fill=matss304)
cell121.region = +cyl120 & -cyl121 & +bndw
cell122 = openmc.Cell(fill=matair)
cell122.region = +cyl121 & -cyl122 & +bndw
cell123 = openmc.Cell(fill=matbsox)
cell123.region = +cyl122 & -cyl123 & +bndw
cell124 = openmc.Cell(fill=matair)
cell124.region = +cyl123 & -cyl124 & +bndw
cell125 = openmc.Cell(fill=matss304)
cell125.region = +cyl124 & -cyl125 & +bndw
cell126 = openmc.Cell(fill=matmod)
cell126.region = +cyl125 & -cyl126 & +bndw
cell127 = openmc.Cell(fill=matclad)
cell127.region = +cyl126 & -cyl127 & +bndw
cell128 = openmc.Cell(fill=matcool)
cell128.region = +cyl127 & +bndw & -px1 & -py3 & +py4
biguni.add_cell(cell120)
biguni.add_cell(cell121)
biguni.add_cell(cell122)
biguni.add_cell(cell123)
biguni.add_cell(cell124)
biguni.add_cell(cell125)
biguni.add_cell(cell126)
biguni.add_cell(cell127)
biguni.add_cell(cell128)
# rod number (10,12)
x=  1.260000
y=  6.970000
cyl129 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl130 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl131 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell129 = openmc.Cell(fill=matfuel01)
cell129.region = -cyl129
fuel_cell_list.append(cell129.id)
cell130 = openmc.Cell(fill=matair)
cell130.region = +cyl129 & -cyl130
cell131 = openmc.Cell(fill=matclad)
cell131.region = +cyl130 & -cyl131
cell132 = openmc.Cell(fill=matcool)
cell132.region = +cyl131 & +px1 & -px2 & -py3 & +py4
biguni.add_cell(cell129)
biguni.add_cell(cell130)
biguni.add_cell(cell131)
biguni.add_cell(cell132)
# rod number (11,12)
x=  2.520000
y=  6.970000
cyl133 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl134 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl135 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell133 = openmc.Cell(fill=matfuel01)
cell133.region = -cyl133
fuel_cell_list.append(cell133.id)
cell134 = openmc.Cell(fill=matair)
cell134.region = +cyl133 & -cyl134
cell135 = openmc.Cell(fill=matclad)
cell135.region = +cyl134 & -cyl135
cell136 = openmc.Cell(fill=matcool)
cell136.region = +cyl135 & +px2 & -px3 & -py3 & +py4
biguni.add_cell(cell133)
biguni.add_cell(cell134)
biguni.add_cell(cell135)
biguni.add_cell(cell136)
# rod number (12,12)
x=  3.780000
y=  6.970000
cyl137 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl138 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl139 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl140 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl141 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl142 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl143 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl144 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell137 = openmc.Cell(fill=matair)
cell137.region = -cyl137
cell138 = openmc.Cell(fill=matss304)
cell138.region = +cyl137 & -cyl138
cell139 = openmc.Cell(fill=matair)
cell139.region = +cyl138 & -cyl139
cell140 = openmc.Cell(fill=matbsox)
cell140.region = +cyl139 & -cyl140
cell141 = openmc.Cell(fill=matair)
cell141.region = +cyl140 & -cyl141
cell142 = openmc.Cell(fill=matss304)
cell142.region = +cyl141 & -cyl142
cell143 = openmc.Cell(fill=matmod)
cell143.region = +cyl142 & -cyl143
cell144 = openmc.Cell(fill=matclad)
cell144.region = +cyl143 & -cyl144
cell145 = openmc.Cell(fill=matcool)
cell145.region = +cyl144 & +px3 & -px4 & -py3 & +py4
biguni.add_cell(cell137)
biguni.add_cell(cell138)
biguni.add_cell(cell139)
biguni.add_cell(cell140)
biguni.add_cell(cell141)
biguni.add_cell(cell142)
biguni.add_cell(cell143)
biguni.add_cell(cell144)
biguni.add_cell(cell145)
# rod number (13,12)
x=  5.040000
y=  6.970000
cyl146 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl147 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl148 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell146 = openmc.Cell(fill=matfuel01)
cell146.region = -cyl146
fuel_cell_list.append(cell146.id)
cell147 = openmc.Cell(fill=matair)
cell147.region = +cyl146 & -cyl147
cell148 = openmc.Cell(fill=matclad)
cell148.region = +cyl147 & -cyl148
cell149 = openmc.Cell(fill=matcool)
cell149.region = +cyl148 & +px4 & -px5 & -py3 & +py4
biguni.add_cell(cell146)
biguni.add_cell(cell147)
biguni.add_cell(cell148)
biguni.add_cell(cell149)
# rod number (14,12)
x=  6.300000
y=  6.970000
cyl150 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl151 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl152 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell150 = openmc.Cell(fill=matfuel01)
cell150.region = -cyl150
fuel_cell_list.append(cell150.id)
cell151 = openmc.Cell(fill=matair)
cell151.region = +cyl150 & -cyl151
cell152 = openmc.Cell(fill=matclad)
cell152.region = +cyl151 & -cyl152
cell153 = openmc.Cell(fill=matcool)
cell153.region = +cyl152 & +px5 & -px6 & -py3 & +py4
biguni.add_cell(cell150)
biguni.add_cell(cell151)
biguni.add_cell(cell152)
biguni.add_cell(cell153)
# rod number (15,12)
x=  7.560000
y=  6.970000
cyl154 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl155 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl156 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl157 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl158 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl159 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl160 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl161 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell154 = openmc.Cell(fill=matair)
cell154.region = -cyl154
cell155 = openmc.Cell(fill=matss304)
cell155.region = +cyl154 & -cyl155
cell156 = openmc.Cell(fill=matair)
cell156.region = +cyl155 & -cyl156
cell157 = openmc.Cell(fill=matbsox)
cell157.region = +cyl156 & -cyl157
cell158 = openmc.Cell(fill=matair)
cell158.region = +cyl157 & -cyl158
cell159 = openmc.Cell(fill=matss304)
cell159.region = +cyl158 & -cyl159
cell160 = openmc.Cell(fill=matmod)
cell160.region = +cyl159 & -cyl160
cell161 = openmc.Cell(fill=matclad)
cell161.region = +cyl160 & -cyl161
cell162 = openmc.Cell(fill=matcool)
cell162.region = +cyl161 & +px6 & -px7 & -py3 & +py4
biguni.add_cell(cell154)
biguni.add_cell(cell155)
biguni.add_cell(cell156)
biguni.add_cell(cell157)
biguni.add_cell(cell158)
biguni.add_cell(cell159)
biguni.add_cell(cell160)
biguni.add_cell(cell161)
biguni.add_cell(cell162)
# rod number (16,12)
x=  8.820000
y=  6.970000
cyl163 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl164 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl165 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell163 = openmc.Cell(fill=matfuel01)
cell163.region = -cyl163
fuel_cell_list.append(cell163.id)
cell164 = openmc.Cell(fill=matair)
cell164.region = +cyl163 & -cyl164
cell165 = openmc.Cell(fill=matclad)
cell165.region = +cyl164 & -cyl165
cell166 = openmc.Cell(fill=matcool)
cell166.region = +cyl165 & +px7 & -px8 & -py3 & +py4
biguni.add_cell(cell163)
biguni.add_cell(cell164)
biguni.add_cell(cell165)
biguni.add_cell(cell166)
# rod number (17,12)
x= 10.080000
y=  6.970000
cyl167 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl168 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl169 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell167 = openmc.Cell(fill=matfuel01)
cell167.region = -cyl167
fuel_cell_list.append(cell167.id)
cell168 = openmc.Cell(fill=matair)
cell168.region = +cyl167 & -cyl168
cell169 = openmc.Cell(fill=matclad)
cell169.region = +cyl168 & -cyl169
cell170 = openmc.Cell(fill=matcool)
cell170.region = +cyl169 & +px8 & -bnde & -py3 & +py4
biguni.add_cell(cell167)
biguni.add_cell(cell168)
biguni.add_cell(cell169)
biguni.add_cell(cell170)
# rod number (9,13)
x=  0.000000
y=  5.710000
cyl171 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl172 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl173 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell171 = openmc.Cell(fill=matfuel01)
cell171.region = -cyl171 & +bndw
fuel_cell_list.append(cell171.id)
cell172 = openmc.Cell(fill=matair)
cell172.region = +cyl171 & -cyl172 & +bndw
cell173 = openmc.Cell(fill=matclad)
cell173.region = +cyl172 & -cyl173 & +bndw
cell174 = openmc.Cell(fill=matcool)
cell174.region = +cyl173 & +bndw & -px1 & -py4 & +py5
biguni.add_cell(cell171)
biguni.add_cell(cell172)
biguni.add_cell(cell173)
biguni.add_cell(cell174)
# rod number (10,13)
x=  1.260000
y=  5.710000
cyl175 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl176 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl177 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell175 = openmc.Cell(fill=matfuel01)
cell175.region = -cyl175
fuel_cell_list.append(cell175.id)
cell176 = openmc.Cell(fill=matair)
cell176.region = +cyl175 & -cyl176
cell177 = openmc.Cell(fill=matclad)
cell177.region = +cyl176 & -cyl177
cell178 = openmc.Cell(fill=matcool)
cell178.region = +cyl177 & +px1 & -px2 & -py4 & +py5
biguni.add_cell(cell175)
biguni.add_cell(cell176)
biguni.add_cell(cell177)
biguni.add_cell(cell178)
# rod number (11,13)
x=  2.520000
y=  5.710000
cyl179 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl180 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl181 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell179 = openmc.Cell(fill=matfuel01)
cell179.region = -cyl179
fuel_cell_list.append(cell179.id)
cell180 = openmc.Cell(fill=matair)
cell180.region = +cyl179 & -cyl180
cell181 = openmc.Cell(fill=matclad)
cell181.region = +cyl180 & -cyl181
cell182 = openmc.Cell(fill=matcool)
cell182.region = +cyl181 & +px2 & -px3 & -py4 & +py5
biguni.add_cell(cell179)
biguni.add_cell(cell180)
biguni.add_cell(cell181)
biguni.add_cell(cell182)
# rod number (12,13)
x=  3.780000
y=  5.710000
cyl183 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl184 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl185 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell183 = openmc.Cell(fill=matfuel01)
cell183.region = -cyl183
fuel_cell_list.append(cell183.id)
cell184 = openmc.Cell(fill=matair)
cell184.region = +cyl183 & -cyl184
cell185 = openmc.Cell(fill=matclad)
cell185.region = +cyl184 & -cyl185
cell186 = openmc.Cell(fill=matcool)
cell186.region = +cyl185 & +px3 & -px4 & -py4 & +py5
biguni.add_cell(cell183)
biguni.add_cell(cell184)
biguni.add_cell(cell185)
biguni.add_cell(cell186)
# rod number (13,13)
x=  5.040000
y=  5.710000
cyl187 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl188 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl189 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell187 = openmc.Cell(fill=matfuel01)
cell187.region = -cyl187
fuel_cell_list.append(cell187.id)
cell188 = openmc.Cell(fill=matair)
cell188.region = +cyl187 & -cyl188
cell189 = openmc.Cell(fill=matclad)
cell189.region = +cyl188 & -cyl189
cell190 = openmc.Cell(fill=matcool)
cell190.region = +cyl189 & +px4 & -px5 & -py4 & +py5
biguni.add_cell(cell187)
biguni.add_cell(cell188)
biguni.add_cell(cell189)
biguni.add_cell(cell190)
# rod number (14,13)
x=  6.300000
y=  5.710000
cyl191 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl192 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl193 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell191 = openmc.Cell(fill=matfuel01)
cell191.region = -cyl191
fuel_cell_list.append(cell191.id)
cell192 = openmc.Cell(fill=matair)
cell192.region = +cyl191 & -cyl192
cell193 = openmc.Cell(fill=matclad)
cell193.region = +cyl192 & -cyl193
cell194 = openmc.Cell(fill=matcool)
cell194.region = +cyl193 & +px5 & -px6 & -py4 & +py5
biguni.add_cell(cell191)
biguni.add_cell(cell192)
biguni.add_cell(cell193)
biguni.add_cell(cell194)
# rod number (15,13)
x=  7.560000
y=  5.710000
cyl195 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl196 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl197 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell195 = openmc.Cell(fill=matfuel01)
cell195.region = -cyl195
fuel_cell_list.append(cell195.id)
cell196 = openmc.Cell(fill=matair)
cell196.region = +cyl195 & -cyl196
cell197 = openmc.Cell(fill=matclad)
cell197.region = +cyl196 & -cyl197
cell198 = openmc.Cell(fill=matcool)
cell198.region = +cyl197 & +px6 & -px7 & -py4 & +py5
biguni.add_cell(cell195)
biguni.add_cell(cell196)
biguni.add_cell(cell197)
biguni.add_cell(cell198)
# rod number (16,13)
x=  8.820000
y=  5.710000
cyl199 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl200 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl201 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell199 = openmc.Cell(fill=matfuel01)
cell199.region = -cyl199
fuel_cell_list.append(cell199.id)
cell200 = openmc.Cell(fill=matair)
cell200.region = +cyl199 & -cyl200
cell201 = openmc.Cell(fill=matclad)
cell201.region = +cyl200 & -cyl201
cell202 = openmc.Cell(fill=matcool)
cell202.region = +cyl201 & +px7 & -px8 & -py4 & +py5
biguni.add_cell(cell199)
biguni.add_cell(cell200)
biguni.add_cell(cell201)
biguni.add_cell(cell202)
# rod number (17,13)
x= 10.080000
y=  5.710000
cyl203 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl204 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl205 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell203 = openmc.Cell(fill=matfuel01)
cell203.region = -cyl203
fuel_cell_list.append(cell203.id)
cell204 = openmc.Cell(fill=matair)
cell204.region = +cyl203 & -cyl204
cell205 = openmc.Cell(fill=matclad)
cell205.region = +cyl204 & -cyl205
cell206 = openmc.Cell(fill=matcool)
cell206.region = +cyl205 & +px8 & -bnde & -py4 & +py5
biguni.add_cell(cell203)
biguni.add_cell(cell204)
biguni.add_cell(cell205)
biguni.add_cell(cell206)
# rod number (9,14)
x=  0.000000
y=  4.450000
cyl207 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl208 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl209 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell207 = openmc.Cell(fill=matfuel01)
cell207.region = -cyl207 & +bndw
fuel_cell_list.append(cell207.id)
cell208 = openmc.Cell(fill=matair)
cell208.region = +cyl207 & -cyl208 & +bndw
cell209 = openmc.Cell(fill=matclad)
cell209.region = +cyl208 & -cyl209 & +bndw
cell210 = openmc.Cell(fill=matcool)
cell210.region = +cyl209 & +bndw & -px1 & -py5 & +py6
biguni.add_cell(cell207)
biguni.add_cell(cell208)
biguni.add_cell(cell209)
biguni.add_cell(cell210)
# rod number (10,14)
x=  1.260000
y=  4.450000
cyl211 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl212 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl213 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell211 = openmc.Cell(fill=matfuel01)
cell211.region = -cyl211
fuel_cell_list.append(cell211.id)
cell212 = openmc.Cell(fill=matair)
cell212.region = +cyl211 & -cyl212
cell213 = openmc.Cell(fill=matclad)
cell213.region = +cyl212 & -cyl213
cell214 = openmc.Cell(fill=matcool)
cell214.region = +cyl213 & +px1 & -px2 & -py5 & +py6
biguni.add_cell(cell211)
biguni.add_cell(cell212)
biguni.add_cell(cell213)
biguni.add_cell(cell214)
# rod number (11,14)
x=  2.520000
y=  4.450000
cyl215 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl216 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl217 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell215 = openmc.Cell(fill=matfuel01)
cell215.region = -cyl215
fuel_cell_list.append(cell215.id)
cell216 = openmc.Cell(fill=matair)
cell216.region = +cyl215 & -cyl216
cell217 = openmc.Cell(fill=matclad)
cell217.region = +cyl216 & -cyl217
cell218 = openmc.Cell(fill=matcool)
cell218.region = +cyl217 & +px2 & -px3 & -py5 & +py6
biguni.add_cell(cell215)
biguni.add_cell(cell216)
biguni.add_cell(cell217)
biguni.add_cell(cell218)
# rod number (12,14)
x=  3.780000
y=  4.450000
cyl219 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl220 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl221 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell219 = openmc.Cell(fill=matfuel01)
cell219.region = -cyl219
fuel_cell_list.append(cell219.id)
cell220 = openmc.Cell(fill=matair)
cell220.region = +cyl219 & -cyl220
cell221 = openmc.Cell(fill=matclad)
cell221.region = +cyl220 & -cyl221
cell222 = openmc.Cell(fill=matcool)
cell222.region = +cyl221 & +px3 & -px4 & -py5 & +py6
biguni.add_cell(cell219)
biguni.add_cell(cell220)
biguni.add_cell(cell221)
biguni.add_cell(cell222)
# rod number (13,14)
x=  5.040000
y=  4.450000
cyl223 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl224 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl225 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell223 = openmc.Cell(fill=matfuel01)
cell223.region = -cyl223
fuel_cell_list.append(cell223.id)
cell224 = openmc.Cell(fill=matair)
cell224.region = +cyl223 & -cyl224
cell225 = openmc.Cell(fill=matclad)
cell225.region = +cyl224 & -cyl225
cell226 = openmc.Cell(fill=matcool)
cell226.region = +cyl225 & +px4 & -px5 & -py5 & +py6
biguni.add_cell(cell223)
biguni.add_cell(cell224)
biguni.add_cell(cell225)
biguni.add_cell(cell226)
# rod number (14,14)
x=  6.300000
y=  4.450000
cyl227 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl228 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl229 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl230 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl231 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl232 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl233 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl234 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell227 = openmc.Cell(fill=matair)
cell227.region = -cyl227
cell228 = openmc.Cell(fill=matss304)
cell228.region = +cyl227 & -cyl228
cell229 = openmc.Cell(fill=matair)
cell229.region = +cyl228 & -cyl229
cell230 = openmc.Cell(fill=matbsox)
cell230.region = +cyl229 & -cyl230
cell231 = openmc.Cell(fill=matair)
cell231.region = +cyl230 & -cyl231
cell232 = openmc.Cell(fill=matss304)
cell232.region = +cyl231 & -cyl232
cell233 = openmc.Cell(fill=matmod)
cell233.region = +cyl232 & -cyl233
cell234 = openmc.Cell(fill=matclad)
cell234.region = +cyl233 & -cyl234
cell235 = openmc.Cell(fill=matcool)
cell235.region = +cyl234 & +px5 & -px6 & -py5 & +py6
biguni.add_cell(cell227)
biguni.add_cell(cell228)
biguni.add_cell(cell229)
biguni.add_cell(cell230)
biguni.add_cell(cell231)
biguni.add_cell(cell232)
biguni.add_cell(cell233)
biguni.add_cell(cell234)
biguni.add_cell(cell235)
# rod number (15,14)
x=  7.560000
y=  4.450000
cyl236 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl237 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl238 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell236 = openmc.Cell(fill=matfuel01)
cell236.region = -cyl236
fuel_cell_list.append(cell236.id)
cell237 = openmc.Cell(fill=matair)
cell237.region = +cyl236 & -cyl237
cell238 = openmc.Cell(fill=matclad)
cell238.region = +cyl237 & -cyl238
cell239 = openmc.Cell(fill=matcool)
cell239.region = +cyl238 & +px6 & -px7 & -py5 & +py6
biguni.add_cell(cell236)
biguni.add_cell(cell237)
biguni.add_cell(cell238)
biguni.add_cell(cell239)
# rod number (16,14)
x=  8.820000
y=  4.450000
cyl240 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl241 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl242 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell240 = openmc.Cell(fill=matfuel01)
cell240.region = -cyl240
fuel_cell_list.append(cell240.id)
cell241 = openmc.Cell(fill=matair)
cell241.region = +cyl240 & -cyl241
cell242 = openmc.Cell(fill=matclad)
cell242.region = +cyl241 & -cyl242
cell243 = openmc.Cell(fill=matcool)
cell243.region = +cyl242 & +px7 & -px8 & -py5 & +py6
biguni.add_cell(cell240)
biguni.add_cell(cell241)
biguni.add_cell(cell242)
biguni.add_cell(cell243)
# rod number (17,14)
x= 10.080000
y=  4.450000
cyl244 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl245 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl246 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell244 = openmc.Cell(fill=matfuel01)
cell244.region = -cyl244
fuel_cell_list.append(cell244.id)
cell245 = openmc.Cell(fill=matair)
cell245.region = +cyl244 & -cyl245
cell246 = openmc.Cell(fill=matclad)
cell246.region = +cyl245 & -cyl246
cell247 = openmc.Cell(fill=matcool)
cell247.region = +cyl246 & +px8 & -bnde & -py5 & +py6
biguni.add_cell(cell244)
biguni.add_cell(cell245)
biguni.add_cell(cell246)
biguni.add_cell(cell247)
# rod number (9,15)
x=  0.000000
y=  3.190000
cyl248 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl249 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl250 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl251 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl252 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl253 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl254 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl255 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell248 = openmc.Cell(fill=matair)
cell248.region = -cyl248 & +bndw
cell249 = openmc.Cell(fill=matss304)
cell249.region = +cyl248 & -cyl249 & +bndw
cell250 = openmc.Cell(fill=matair)
cell250.region = +cyl249 & -cyl250 & +bndw
cell251 = openmc.Cell(fill=matbsox)
cell251.region = +cyl250 & -cyl251 & +bndw
cell252 = openmc.Cell(fill=matair)
cell252.region = +cyl251 & -cyl252 & +bndw
cell253 = openmc.Cell(fill=matss304)
cell253.region = +cyl252 & -cyl253 & +bndw
cell254 = openmc.Cell(fill=matmod)
cell254.region = +cyl253 & -cyl254 & +bndw
cell255 = openmc.Cell(fill=matclad)
cell255.region = +cyl254 & -cyl255 & +bndw
cell256 = openmc.Cell(fill=matcool)
cell256.region = +cyl255 & +bndw & -px1 & -py6 & +py7
biguni.add_cell(cell248)
biguni.add_cell(cell249)
biguni.add_cell(cell250)
biguni.add_cell(cell251)
biguni.add_cell(cell252)
biguni.add_cell(cell253)
biguni.add_cell(cell254)
biguni.add_cell(cell255)
biguni.add_cell(cell256)
# rod number (10,15)
x=  1.260000
y=  3.190000
cyl257 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl258 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl259 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell257 = openmc.Cell(fill=matfuel01)
cell257.region = -cyl257
fuel_cell_list.append(cell257.id)
cell258 = openmc.Cell(fill=matair)
cell258.region = +cyl257 & -cyl258
cell259 = openmc.Cell(fill=matclad)
cell259.region = +cyl258 & -cyl259
cell260 = openmc.Cell(fill=matcool)
cell260.region = +cyl259 & +px1 & -px2 & -py6 & +py7
biguni.add_cell(cell257)
biguni.add_cell(cell258)
biguni.add_cell(cell259)
biguni.add_cell(cell260)
# rod number (11,15)
x=  2.520000
y=  3.190000
cyl261 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl262 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl263 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell261 = openmc.Cell(fill=matfuel01)
cell261.region = -cyl261
fuel_cell_list.append(cell261.id)
cell262 = openmc.Cell(fill=matair)
cell262.region = +cyl261 & -cyl262
cell263 = openmc.Cell(fill=matclad)
cell263.region = +cyl262 & -cyl263
cell264 = openmc.Cell(fill=matcool)
cell264.region = +cyl263 & +px2 & -px3 & -py6 & +py7
biguni.add_cell(cell261)
biguni.add_cell(cell262)
biguni.add_cell(cell263)
biguni.add_cell(cell264)
# rod number (12,15)
x=  3.780000
y=  3.190000
cyl265 = openmc.ZCylinder(x0=x, y0=y, r= 0.21400)  # AIR
cyl266 = openmc.ZCylinder(x0=x, y0=y, r= 0.23100)  # SS304
cyl267 = openmc.ZCylinder(x0=x, y0=y, r= 0.24100)  # AIR
cyl268 = openmc.ZCylinder(x0=x, y0=y, r= 0.42700)  # BSOX
cyl269 = openmc.ZCylinder(x0=x, y0=y, r= 0.43700)  # AIR
cyl270 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # SS304
cyl271 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl272 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell265 = openmc.Cell(fill=matair)
cell265.region = -cyl265
cell266 = openmc.Cell(fill=matss304)
cell266.region = +cyl265 & -cyl266
cell267 = openmc.Cell(fill=matair)
cell267.region = +cyl266 & -cyl267
cell268 = openmc.Cell(fill=matbsox)
cell268.region = +cyl267 & -cyl268
cell269 = openmc.Cell(fill=matair)
cell269.region = +cyl268 & -cyl269
cell270 = openmc.Cell(fill=matss304)
cell270.region = +cyl269 & -cyl270
cell271 = openmc.Cell(fill=matmod)
cell271.region = +cyl270 & -cyl271
cell272 = openmc.Cell(fill=matclad)
cell272.region = +cyl271 & -cyl272
cell273 = openmc.Cell(fill=matcool)
cell273.region = +cyl272 & +px3 & -px4 & -py6 & +py7
biguni.add_cell(cell265)
biguni.add_cell(cell266)
biguni.add_cell(cell267)
biguni.add_cell(cell268)
biguni.add_cell(cell269)
biguni.add_cell(cell270)
biguni.add_cell(cell271)
biguni.add_cell(cell272)
biguni.add_cell(cell273)
# rod number (13,15)
x=  5.040000
y=  3.190000
cyl274 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl275 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl276 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell274 = openmc.Cell(fill=matfuel01)
cell274.region = -cyl274
fuel_cell_list.append(cell274.id)
cell275 = openmc.Cell(fill=matair)
cell275.region = +cyl274 & -cyl275
cell276 = openmc.Cell(fill=matclad)
cell276.region = +cyl275 & -cyl276
cell277 = openmc.Cell(fill=matcool)
cell277.region = +cyl276 & +px4 & -px5 & -py6 & +py7
biguni.add_cell(cell274)
biguni.add_cell(cell275)
biguni.add_cell(cell276)
biguni.add_cell(cell277)
# rod number (14,15)
x=  6.300000
y=  3.190000
cyl278 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl279 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl280 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell278 = openmc.Cell(fill=matfuel01)
cell278.region = -cyl278
fuel_cell_list.append(cell278.id)
cell279 = openmc.Cell(fill=matair)
cell279.region = +cyl278 & -cyl279
cell280 = openmc.Cell(fill=matclad)
cell280.region = +cyl279 & -cyl280
cell281 = openmc.Cell(fill=matcool)
cell281.region = +cyl280 & +px5 & -px6 & -py6 & +py7
biguni.add_cell(cell278)
biguni.add_cell(cell279)
biguni.add_cell(cell280)
biguni.add_cell(cell281)
# rod number (15,15)
x=  7.560000
y=  3.190000
cyl282 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl283 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl284 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell282 = openmc.Cell(fill=matfuel01)
cell282.region = -cyl282
fuel_cell_list.append(cell282.id)
cell283 = openmc.Cell(fill=matair)
cell283.region = +cyl282 & -cyl283
cell284 = openmc.Cell(fill=matclad)
cell284.region = +cyl283 & -cyl284
cell285 = openmc.Cell(fill=matcool)
cell285.region = +cyl284 & +px6 & -px7 & -py6 & +py7
biguni.add_cell(cell282)
biguni.add_cell(cell283)
biguni.add_cell(cell284)
biguni.add_cell(cell285)
# rod number (16,15)
x=  8.820000
y=  3.190000
cyl286 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl287 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl288 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell286 = openmc.Cell(fill=matfuel01)
cell286.region = -cyl286
fuel_cell_list.append(cell286.id)
cell287 = openmc.Cell(fill=matair)
cell287.region = +cyl286 & -cyl287
cell288 = openmc.Cell(fill=matclad)
cell288.region = +cyl287 & -cyl288
cell289 = openmc.Cell(fill=matcool)
cell289.region = +cyl288 & +px7 & -px8 & -py6 & +py7
biguni.add_cell(cell286)
biguni.add_cell(cell287)
biguni.add_cell(cell288)
biguni.add_cell(cell289)
# rod number (17,15)
x= 10.080000
y=  3.190000
cyl290 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl291 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl292 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell290 = openmc.Cell(fill=matfuel01)
cell290.region = -cyl290
fuel_cell_list.append(cell290.id)
cell291 = openmc.Cell(fill=matair)
cell291.region = +cyl290 & -cyl291
cell292 = openmc.Cell(fill=matclad)
cell292.region = +cyl291 & -cyl292
cell293 = openmc.Cell(fill=matcool)
cell293.region = +cyl292 & +px8 & -bnde & -py6 & +py7
biguni.add_cell(cell290)
biguni.add_cell(cell291)
biguni.add_cell(cell292)
biguni.add_cell(cell293)
# rod number (9,16)
x=  0.000000
y=  1.930000
cyl294 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl295 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl296 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell294 = openmc.Cell(fill=matfuel01)
cell294.region = -cyl294 & +bndw
fuel_cell_list.append(cell294.id)
cell295 = openmc.Cell(fill=matair)
cell295.region = +cyl294 & -cyl295 & +bndw
cell296 = openmc.Cell(fill=matclad)
cell296.region = +cyl295 & -cyl296 & +bndw
cell297 = openmc.Cell(fill=matcool)
cell297.region = +cyl296 & +bndw & -px1 & -py7 & +py8
biguni.add_cell(cell294)
biguni.add_cell(cell295)
biguni.add_cell(cell296)
biguni.add_cell(cell297)
# rod number (10,16)
x=  1.260000
y=  1.930000
cyl298 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl299 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl300 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell298 = openmc.Cell(fill=matfuel01)
cell298.region = -cyl298
fuel_cell_list.append(cell298.id)
cell299 = openmc.Cell(fill=matair)
cell299.region = +cyl298 & -cyl299
cell300 = openmc.Cell(fill=matclad)
cell300.region = +cyl299 & -cyl300
cell301 = openmc.Cell(fill=matcool)
cell301.region = +cyl300 & +px1 & -px2 & -py7 & +py8
biguni.add_cell(cell298)
biguni.add_cell(cell299)
biguni.add_cell(cell300)
biguni.add_cell(cell301)
# rod number (11,16)
x=  2.520000
y=  1.930000
cyl302 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl303 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl304 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell302 = openmc.Cell(fill=matfuel01)
cell302.region = -cyl302
fuel_cell_list.append(cell302.id)
cell303 = openmc.Cell(fill=matair)
cell303.region = +cyl302 & -cyl303
cell304 = openmc.Cell(fill=matclad)
cell304.region = +cyl303 & -cyl304
cell305 = openmc.Cell(fill=matcool)
cell305.region = +cyl304 & +px2 & -px3 & -py7 & +py8
biguni.add_cell(cell302)
biguni.add_cell(cell303)
biguni.add_cell(cell304)
biguni.add_cell(cell305)
# rod number (12,16)
x=  3.780000
y=  1.930000
cyl306 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl307 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl308 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell306 = openmc.Cell(fill=matfuel01)
cell306.region = -cyl306
fuel_cell_list.append(cell306.id)
cell307 = openmc.Cell(fill=matair)
cell307.region = +cyl306 & -cyl307
cell308 = openmc.Cell(fill=matclad)
cell308.region = +cyl307 & -cyl308
cell309 = openmc.Cell(fill=matcool)
cell309.region = +cyl308 & +px3 & -px4 & -py7 & +py8
biguni.add_cell(cell306)
biguni.add_cell(cell307)
biguni.add_cell(cell308)
biguni.add_cell(cell309)
# rod number (13,16)
x=  5.040000
y=  1.930000
cyl310 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl311 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl312 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell310 = openmc.Cell(fill=matfuel01)
cell310.region = -cyl310
fuel_cell_list.append(cell310.id)
cell311 = openmc.Cell(fill=matair)
cell311.region = +cyl310 & -cyl311
cell312 = openmc.Cell(fill=matclad)
cell312.region = +cyl311 & -cyl312
cell313 = openmc.Cell(fill=matcool)
cell313.region = +cyl312 & +px4 & -px5 & -py7 & +py8
biguni.add_cell(cell310)
biguni.add_cell(cell311)
biguni.add_cell(cell312)
biguni.add_cell(cell313)
# rod number (14,16)
x=  6.300000
y=  1.930000
cyl314 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl315 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl316 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell314 = openmc.Cell(fill=matfuel01)
cell314.region = -cyl314
fuel_cell_list.append(cell314.id)
cell315 = openmc.Cell(fill=matair)
cell315.region = +cyl314 & -cyl315
cell316 = openmc.Cell(fill=matclad)
cell316.region = +cyl315 & -cyl316
cell317 = openmc.Cell(fill=matcool)
cell317.region = +cyl316 & +px5 & -px6 & -py7 & +py8
biguni.add_cell(cell314)
biguni.add_cell(cell315)
biguni.add_cell(cell316)
biguni.add_cell(cell317)
# rod number (15,16)
x=  7.560000
y=  1.930000
cyl318 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl319 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl320 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell318 = openmc.Cell(fill=matfuel01)
cell318.region = -cyl318
fuel_cell_list.append(cell318.id)
cell319 = openmc.Cell(fill=matair)
cell319.region = +cyl318 & -cyl319
cell320 = openmc.Cell(fill=matclad)
cell320.region = +cyl319 & -cyl320
cell321 = openmc.Cell(fill=matcool)
cell321.region = +cyl320 & +px6 & -px7 & -py7 & +py8
biguni.add_cell(cell318)
biguni.add_cell(cell319)
biguni.add_cell(cell320)
biguni.add_cell(cell321)
# rod number (16,16)
x=  8.820000
y=  1.930000
cyl322 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl323 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl324 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell322 = openmc.Cell(fill=matfuel01)
cell322.region = -cyl322
fuel_cell_list.append(cell322.id)
cell323 = openmc.Cell(fill=matair)
cell323.region = +cyl322 & -cyl323
cell324 = openmc.Cell(fill=matclad)
cell324.region = +cyl323 & -cyl324
cell325 = openmc.Cell(fill=matcool)
cell325.region = +cyl324 & +px7 & -px8 & -py7 & +py8
biguni.add_cell(cell322)
biguni.add_cell(cell323)
biguni.add_cell(cell324)
biguni.add_cell(cell325)
# rod number (17,16)
x= 10.080000
y=  1.930000
cyl326 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl327 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl328 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell326 = openmc.Cell(fill=matfuel01)
cell326.region = -cyl326
fuel_cell_list.append(cell326.id)
cell327 = openmc.Cell(fill=matair)
cell327.region = +cyl326 & -cyl327
cell328 = openmc.Cell(fill=matclad)
cell328.region = +cyl327 & -cyl328
cell329 = openmc.Cell(fill=matcool)
cell329.region = +cyl328 & +px8 & -bnde & -py7 & +py8
biguni.add_cell(cell326)
biguni.add_cell(cell327)
biguni.add_cell(cell328)
biguni.add_cell(cell329)
# rod number (9,17)
x=  0.000000
y=  0.670000
cyl330 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl331 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl332 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell330 = openmc.Cell(fill=matfuel01)
cell330.region = -cyl330 & +bndw
fuel_cell_list.append(cell330.id)
cell331 = openmc.Cell(fill=matair)
cell331.region = +cyl330 & -cyl331 & +bndw
cell332 = openmc.Cell(fill=matclad)
cell332.region = +cyl331 & -cyl332 & +bndw
cell333 = openmc.Cell(fill=matcool)
cell333.region = +cyl332 & +bndw & -px1 & -py8 & +bnds
biguni.add_cell(cell330)
biguni.add_cell(cell331)
biguni.add_cell(cell332)
biguni.add_cell(cell333)
# rod number (10,17)
x=  1.260000
y=  0.670000
cyl334 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl335 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl336 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell334 = openmc.Cell(fill=matfuel01)
cell334.region = -cyl334
fuel_cell_list.append(cell334.id)
cell335 = openmc.Cell(fill=matair)
cell335.region = +cyl334 & -cyl335
cell336 = openmc.Cell(fill=matclad)
cell336.region = +cyl335 & -cyl336
cell337 = openmc.Cell(fill=matcool)
cell337.region = +cyl336 & +px1 & -px2 & -py8 & +bnds
biguni.add_cell(cell334)
biguni.add_cell(cell335)
biguni.add_cell(cell336)
biguni.add_cell(cell337)
# rod number (11,17)
x=  2.520000
y=  0.670000
cyl338 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl339 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl340 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell338 = openmc.Cell(fill=matfuel01)
cell338.region = -cyl338
fuel_cell_list.append(cell338.id)
cell339 = openmc.Cell(fill=matair)
cell339.region = +cyl338 & -cyl339
cell340 = openmc.Cell(fill=matclad)
cell340.region = +cyl339 & -cyl340
cell341 = openmc.Cell(fill=matcool)
cell341.region = +cyl340 & +px2 & -px3 & -py8 & +bnds
biguni.add_cell(cell338)
biguni.add_cell(cell339)
biguni.add_cell(cell340)
biguni.add_cell(cell341)
# rod number (12,17)
x=  3.780000
y=  0.670000
cyl342 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl343 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl344 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell342 = openmc.Cell(fill=matfuel01)
cell342.region = -cyl342
fuel_cell_list.append(cell342.id)
cell343 = openmc.Cell(fill=matair)
cell343.region = +cyl342 & -cyl343
cell344 = openmc.Cell(fill=matclad)
cell344.region = +cyl343 & -cyl344
cell345 = openmc.Cell(fill=matcool)
cell345.region = +cyl344 & +px3 & -px4 & -py8 & +bnds
biguni.add_cell(cell342)
biguni.add_cell(cell343)
biguni.add_cell(cell344)
biguni.add_cell(cell345)
# rod number (13,17)
x=  5.040000
y=  0.670000
cyl346 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl347 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl348 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell346 = openmc.Cell(fill=matfuel01)
cell346.region = -cyl346
fuel_cell_list.append(cell346.id)
cell347 = openmc.Cell(fill=matair)
cell347.region = +cyl346 & -cyl347
cell348 = openmc.Cell(fill=matclad)
cell348.region = +cyl347 & -cyl348
cell349 = openmc.Cell(fill=matcool)
cell349.region = +cyl348 & +px4 & -px5 & -py8 & +bnds
biguni.add_cell(cell346)
biguni.add_cell(cell347)
biguni.add_cell(cell348)
biguni.add_cell(cell349)
# rod number (14,17)
x=  6.300000
y=  0.670000
cyl350 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl351 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl352 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell350 = openmc.Cell(fill=matfuel01)
cell350.region = -cyl350
fuel_cell_list.append(cell350.id)
cell351 = openmc.Cell(fill=matair)
cell351.region = +cyl350 & -cyl351
cell352 = openmc.Cell(fill=matclad)
cell352.region = +cyl351 & -cyl352
cell353 = openmc.Cell(fill=matcool)
cell353.region = +cyl352 & +px5 & -px6 & -py8 & +bnds
biguni.add_cell(cell350)
biguni.add_cell(cell351)
biguni.add_cell(cell352)
biguni.add_cell(cell353)
# rod number (15,17)
x=  7.560000
y=  0.670000
cyl354 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl355 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl356 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell354 = openmc.Cell(fill=matfuel01)
cell354.region = -cyl354
fuel_cell_list.append(cell354.id)
cell355 = openmc.Cell(fill=matair)
cell355.region = +cyl354 & -cyl355
cell356 = openmc.Cell(fill=matclad)
cell356.region = +cyl355 & -cyl356
cell357 = openmc.Cell(fill=matcool)
cell357.region = +cyl356 & +px6 & -px7 & -py8 & +bnds
biguni.add_cell(cell354)
biguni.add_cell(cell355)
biguni.add_cell(cell356)
biguni.add_cell(cell357)
# rod number (16,17)
x=  8.820000
y=  0.670000
cyl358 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl359 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl360 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell358 = openmc.Cell(fill=matfuel01)
cell358.region = -cyl358
fuel_cell_list.append(cell358.id)
cell359 = openmc.Cell(fill=matair)
cell359.region = +cyl358 & -cyl359
cell360 = openmc.Cell(fill=matclad)
cell360.region = +cyl359 & -cyl360
cell361 = openmc.Cell(fill=matcool)
cell361.region = +cyl360 & +px7 & -px8 & -py8 & +bnds
biguni.add_cell(cell358)
biguni.add_cell(cell359)
biguni.add_cell(cell360)
biguni.add_cell(cell361)
# rod number (17,17)
x= 10.080000
y=  0.670000
cyl362 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl363 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl364 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell362 = openmc.Cell(fill=matfuel01)
cell362.region = -cyl362
fuel_cell_list.append(cell362.id)
cell363 = openmc.Cell(fill=matair)
cell363.region = +cyl362 & -cyl363
cell364 = openmc.Cell(fill=matclad)
cell364.region = +cyl363 & -cyl364
cell365 = openmc.Cell(fill=matcool)
cell365.region = +cyl364 & +px8 & -bnde & -py8 & +bnds
biguni.add_cell(cell362)
biguni.add_cell(cell363)
biguni.add_cell(cell364)
biguni.add_cell(cell365)

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
