import matplotlib

import openmc
import openmc.mgxs as mgxs
import openmc.data          # need for hdf5

#  To run:
#  >python3 vera2i.omc
#
# OpenMC Input created by BUNBLD on 08/09/2025 11:48:06
#  VERA Benchmark #2 - Single Assembly
#  Uniform PWR Assembly
#  November 15, 2012
#  Number densities from KENO run
#  VERA Benchmark 2I - Like 2A + instrument thimble
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

# material 6 SS304
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
model.materials = openmc.Materials([matfuel01,matclad,matcool,matmod,matair,matss304])
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
cyl14 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl15 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell14 = openmc.Cell(fill=matmod)
cell14.region = -cyl14 & -bndn
cell15 = openmc.Cell(fill=matclad)
cell15.region = +cyl14 & -cyl15 & -bndn
cell16 = openmc.Cell(fill=matcool)
cell16.region = +cyl15 & +px3 & -px4 & -bndn & +py1
biguni.add_cell(cell14)
biguni.add_cell(cell15)
biguni.add_cell(cell16)
# rod number (13,9)
x=  5.040000
y= 10.750000
cyl17 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl18 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl19 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell17 = openmc.Cell(fill=matfuel01)
cell17.region = -cyl17 & -bndn
fuel_cell_list.append(cell17.id)
cell18 = openmc.Cell(fill=matair)
cell18.region = +cyl17 & -cyl18 & -bndn
cell19 = openmc.Cell(fill=matclad)
cell19.region = +cyl18 & -cyl19 & -bndn
cell20 = openmc.Cell(fill=matcool)
cell20.region = +cyl19 & +px4 & -px5 & -bndn & +py1
biguni.add_cell(cell17)
biguni.add_cell(cell18)
biguni.add_cell(cell19)
biguni.add_cell(cell20)
# rod number (14,9)
x=  6.300000
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
cell24.region = +cyl23 & +px5 & -px6 & -bndn & +py1
biguni.add_cell(cell21)
biguni.add_cell(cell22)
biguni.add_cell(cell23)
biguni.add_cell(cell24)
# rod number (15,9)
x=  7.560000
y= 10.750000
cyl25 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl26 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell25 = openmc.Cell(fill=matmod)
cell25.region = -cyl25 & -bndn
cell26 = openmc.Cell(fill=matclad)
cell26.region = +cyl25 & -cyl26 & -bndn
cell27 = openmc.Cell(fill=matcool)
cell27.region = +cyl26 & +px6 & -px7 & -bndn & +py1
biguni.add_cell(cell25)
biguni.add_cell(cell26)
biguni.add_cell(cell27)
# rod number (16,9)
x=  8.820000
y= 10.750000
cyl28 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl29 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl30 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell28 = openmc.Cell(fill=matfuel01)
cell28.region = -cyl28 & -bndn
fuel_cell_list.append(cell28.id)
cell29 = openmc.Cell(fill=matair)
cell29.region = +cyl28 & -cyl29 & -bndn
cell30 = openmc.Cell(fill=matclad)
cell30.region = +cyl29 & -cyl30 & -bndn
cell31 = openmc.Cell(fill=matcool)
cell31.region = +cyl30 & +px7 & -px8 & -bndn & +py1
biguni.add_cell(cell28)
biguni.add_cell(cell29)
biguni.add_cell(cell30)
biguni.add_cell(cell31)
# rod number (17,9)
x= 10.080000
y= 10.750000
cyl32 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl33 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl34 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell32 = openmc.Cell(fill=matfuel01)
cell32.region = -cyl32 & -bndn
fuel_cell_list.append(cell32.id)
cell33 = openmc.Cell(fill=matair)
cell33.region = +cyl32 & -cyl33 & -bndn
cell34 = openmc.Cell(fill=matclad)
cell34.region = +cyl33 & -cyl34 & -bndn
cell35 = openmc.Cell(fill=matcool)
cell35.region = +cyl34 & +px8 & -bnde & -bndn & +py1
biguni.add_cell(cell32)
biguni.add_cell(cell33)
biguni.add_cell(cell34)
biguni.add_cell(cell35)
# rod number (9,10)
x=  0.000000
y=  9.490000
cyl36 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl37 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl38 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell36 = openmc.Cell(fill=matfuel01)
cell36.region = -cyl36 & +bndw
fuel_cell_list.append(cell36.id)
cell37 = openmc.Cell(fill=matair)
cell37.region = +cyl36 & -cyl37 & +bndw
cell38 = openmc.Cell(fill=matclad)
cell38.region = +cyl37 & -cyl38 & +bndw
cell39 = openmc.Cell(fill=matcool)
cell39.region = +cyl38 & +bndw & -px1 & -py1 & +py2
biguni.add_cell(cell36)
biguni.add_cell(cell37)
biguni.add_cell(cell38)
biguni.add_cell(cell39)
# rod number (10,10)
x=  1.260000
y=  9.490000
cyl40 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl41 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl42 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell40 = openmc.Cell(fill=matfuel01)
cell40.region = -cyl40
fuel_cell_list.append(cell40.id)
cell41 = openmc.Cell(fill=matair)
cell41.region = +cyl40 & -cyl41
cell42 = openmc.Cell(fill=matclad)
cell42.region = +cyl41 & -cyl42
cell43 = openmc.Cell(fill=matcool)
cell43.region = +cyl42 & +px1 & -px2 & -py1 & +py2
biguni.add_cell(cell40)
biguni.add_cell(cell41)
biguni.add_cell(cell42)
biguni.add_cell(cell43)
# rod number (11,10)
x=  2.520000
y=  9.490000
cyl44 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl45 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl46 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell44 = openmc.Cell(fill=matfuel01)
cell44.region = -cyl44
fuel_cell_list.append(cell44.id)
cell45 = openmc.Cell(fill=matair)
cell45.region = +cyl44 & -cyl45
cell46 = openmc.Cell(fill=matclad)
cell46.region = +cyl45 & -cyl46
cell47 = openmc.Cell(fill=matcool)
cell47.region = +cyl46 & +px2 & -px3 & -py1 & +py2
biguni.add_cell(cell44)
biguni.add_cell(cell45)
biguni.add_cell(cell46)
biguni.add_cell(cell47)
# rod number (12,10)
x=  3.780000
y=  9.490000
cyl48 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl49 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl50 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell48 = openmc.Cell(fill=matfuel01)
cell48.region = -cyl48
fuel_cell_list.append(cell48.id)
cell49 = openmc.Cell(fill=matair)
cell49.region = +cyl48 & -cyl49
cell50 = openmc.Cell(fill=matclad)
cell50.region = +cyl49 & -cyl50
cell51 = openmc.Cell(fill=matcool)
cell51.region = +cyl50 & +px3 & -px4 & -py1 & +py2
biguni.add_cell(cell48)
biguni.add_cell(cell49)
biguni.add_cell(cell50)
biguni.add_cell(cell51)
# rod number (13,10)
x=  5.040000
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
cell55.region = +cyl54 & +px4 & -px5 & -py1 & +py2
biguni.add_cell(cell52)
biguni.add_cell(cell53)
biguni.add_cell(cell54)
biguni.add_cell(cell55)
# rod number (14,10)
x=  6.300000
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
cell59.region = +cyl58 & +px5 & -px6 & -py1 & +py2
biguni.add_cell(cell56)
biguni.add_cell(cell57)
biguni.add_cell(cell58)
biguni.add_cell(cell59)
# rod number (15,10)
x=  7.560000
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
cell63.region = +cyl62 & +px6 & -px7 & -py1 & +py2
biguni.add_cell(cell60)
biguni.add_cell(cell61)
biguni.add_cell(cell62)
biguni.add_cell(cell63)
# rod number (16,10)
x=  8.820000
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
cell67.region = +cyl66 & +px7 & -px8 & -py1 & +py2
biguni.add_cell(cell64)
biguni.add_cell(cell65)
biguni.add_cell(cell66)
biguni.add_cell(cell67)
# rod number (17,10)
x= 10.080000
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
cell71.region = +cyl70 & +px8 & -bnde & -py1 & +py2
biguni.add_cell(cell68)
biguni.add_cell(cell69)
biguni.add_cell(cell70)
biguni.add_cell(cell71)
# rod number (9,11)
x=  0.000000
y=  8.230000
cyl72 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl73 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl74 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell72 = openmc.Cell(fill=matfuel01)
cell72.region = -cyl72 & +bndw
fuel_cell_list.append(cell72.id)
cell73 = openmc.Cell(fill=matair)
cell73.region = +cyl72 & -cyl73 & +bndw
cell74 = openmc.Cell(fill=matclad)
cell74.region = +cyl73 & -cyl74 & +bndw
cell75 = openmc.Cell(fill=matcool)
cell75.region = +cyl74 & +bndw & -px1 & -py2 & +py3
biguni.add_cell(cell72)
biguni.add_cell(cell73)
biguni.add_cell(cell74)
biguni.add_cell(cell75)
# rod number (10,11)
x=  1.260000
y=  8.230000
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
cell79.region = +cyl78 & +px1 & -px2 & -py2 & +py3
biguni.add_cell(cell76)
biguni.add_cell(cell77)
biguni.add_cell(cell78)
biguni.add_cell(cell79)
# rod number (11,11)
x=  2.520000
y=  8.230000
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
cell83.region = +cyl82 & +px2 & -px3 & -py2 & +py3
biguni.add_cell(cell80)
biguni.add_cell(cell81)
biguni.add_cell(cell82)
biguni.add_cell(cell83)
# rod number (12,11)
x=  3.780000
y=  8.230000
cyl84 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl85 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl86 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell84 = openmc.Cell(fill=matfuel01)
cell84.region = -cyl84
fuel_cell_list.append(cell84.id)
cell85 = openmc.Cell(fill=matair)
cell85.region = +cyl84 & -cyl85
cell86 = openmc.Cell(fill=matclad)
cell86.region = +cyl85 & -cyl86
cell87 = openmc.Cell(fill=matcool)
cell87.region = +cyl86 & +px3 & -px4 & -py2 & +py3
biguni.add_cell(cell84)
biguni.add_cell(cell85)
biguni.add_cell(cell86)
biguni.add_cell(cell87)
# rod number (13,11)
x=  5.040000
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
cell91.region = +cyl90 & +px4 & -px5 & -py2 & +py3
biguni.add_cell(cell88)
biguni.add_cell(cell89)
biguni.add_cell(cell90)
biguni.add_cell(cell91)
# rod number (14,11)
x=  6.300000
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
cell95.region = +cyl94 & +px5 & -px6 & -py2 & +py3
biguni.add_cell(cell92)
biguni.add_cell(cell93)
biguni.add_cell(cell94)
biguni.add_cell(cell95)
# rod number (15,11)
x=  7.560000
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
cell99.region = +cyl98 & +px6 & -px7 & -py2 & +py3
biguni.add_cell(cell96)
biguni.add_cell(cell97)
biguni.add_cell(cell98)
biguni.add_cell(cell99)
# rod number (16,11)
x=  8.820000
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
cell103.region = +cyl102 & +px7 & -px8 & -py2 & +py3
biguni.add_cell(cell100)
biguni.add_cell(cell101)
biguni.add_cell(cell102)
biguni.add_cell(cell103)
# rod number (17,11)
x= 10.080000
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
cell107.region = +cyl106 & +px8 & -bnde & -py2 & +py3
biguni.add_cell(cell104)
biguni.add_cell(cell105)
biguni.add_cell(cell106)
biguni.add_cell(cell107)
# rod number (9,12)
x=  0.000000
y=  6.970000
cyl108 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl109 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell108 = openmc.Cell(fill=matmod)
cell108.region = -cyl108 & +bndw
cell109 = openmc.Cell(fill=matclad)
cell109.region = +cyl108 & -cyl109 & +bndw
cell110 = openmc.Cell(fill=matcool)
cell110.region = +cyl109 & +bndw & -px1 & -py3 & +py4
biguni.add_cell(cell108)
biguni.add_cell(cell109)
biguni.add_cell(cell110)
# rod number (10,12)
x=  1.260000
y=  6.970000
cyl111 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl112 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl113 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell111 = openmc.Cell(fill=matfuel01)
cell111.region = -cyl111
fuel_cell_list.append(cell111.id)
cell112 = openmc.Cell(fill=matair)
cell112.region = +cyl111 & -cyl112
cell113 = openmc.Cell(fill=matclad)
cell113.region = +cyl112 & -cyl113
cell114 = openmc.Cell(fill=matcool)
cell114.region = +cyl113 & +px1 & -px2 & -py3 & +py4
biguni.add_cell(cell111)
biguni.add_cell(cell112)
biguni.add_cell(cell113)
biguni.add_cell(cell114)
# rod number (11,12)
x=  2.520000
y=  6.970000
cyl115 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl116 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl117 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell115 = openmc.Cell(fill=matfuel01)
cell115.region = -cyl115
fuel_cell_list.append(cell115.id)
cell116 = openmc.Cell(fill=matair)
cell116.region = +cyl115 & -cyl116
cell117 = openmc.Cell(fill=matclad)
cell117.region = +cyl116 & -cyl117
cell118 = openmc.Cell(fill=matcool)
cell118.region = +cyl117 & +px2 & -px3 & -py3 & +py4
biguni.add_cell(cell115)
biguni.add_cell(cell116)
biguni.add_cell(cell117)
biguni.add_cell(cell118)
# rod number (12,12)
x=  3.780000
y=  6.970000
cyl119 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl120 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell119 = openmc.Cell(fill=matmod)
cell119.region = -cyl119
cell120 = openmc.Cell(fill=matclad)
cell120.region = +cyl119 & -cyl120
cell121 = openmc.Cell(fill=matcool)
cell121.region = +cyl120 & +px3 & -px4 & -py3 & +py4
biguni.add_cell(cell119)
biguni.add_cell(cell120)
biguni.add_cell(cell121)
# rod number (13,12)
x=  5.040000
y=  6.970000
cyl122 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl123 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl124 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell122 = openmc.Cell(fill=matfuel01)
cell122.region = -cyl122
fuel_cell_list.append(cell122.id)
cell123 = openmc.Cell(fill=matair)
cell123.region = +cyl122 & -cyl123
cell124 = openmc.Cell(fill=matclad)
cell124.region = +cyl123 & -cyl124
cell125 = openmc.Cell(fill=matcool)
cell125.region = +cyl124 & +px4 & -px5 & -py3 & +py4
biguni.add_cell(cell122)
biguni.add_cell(cell123)
biguni.add_cell(cell124)
biguni.add_cell(cell125)
# rod number (14,12)
x=  6.300000
y=  6.970000
cyl126 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl127 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl128 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell126 = openmc.Cell(fill=matfuel01)
cell126.region = -cyl126
fuel_cell_list.append(cell126.id)
cell127 = openmc.Cell(fill=matair)
cell127.region = +cyl126 & -cyl127
cell128 = openmc.Cell(fill=matclad)
cell128.region = +cyl127 & -cyl128
cell129 = openmc.Cell(fill=matcool)
cell129.region = +cyl128 & +px5 & -px6 & -py3 & +py4
biguni.add_cell(cell126)
biguni.add_cell(cell127)
biguni.add_cell(cell128)
biguni.add_cell(cell129)
# rod number (15,12)
x=  7.560000
y=  6.970000
cyl130 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl131 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell130 = openmc.Cell(fill=matmod)
cell130.region = -cyl130
cell131 = openmc.Cell(fill=matclad)
cell131.region = +cyl130 & -cyl131
cell132 = openmc.Cell(fill=matcool)
cell132.region = +cyl131 & +px6 & -px7 & -py3 & +py4
biguni.add_cell(cell130)
biguni.add_cell(cell131)
biguni.add_cell(cell132)
# rod number (16,12)
x=  8.820000
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
cell136.region = +cyl135 & +px7 & -px8 & -py3 & +py4
biguni.add_cell(cell133)
biguni.add_cell(cell134)
biguni.add_cell(cell135)
biguni.add_cell(cell136)
# rod number (17,12)
x= 10.080000
y=  6.970000
cyl137 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl138 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl139 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell137 = openmc.Cell(fill=matfuel01)
cell137.region = -cyl137
fuel_cell_list.append(cell137.id)
cell138 = openmc.Cell(fill=matair)
cell138.region = +cyl137 & -cyl138
cell139 = openmc.Cell(fill=matclad)
cell139.region = +cyl138 & -cyl139
cell140 = openmc.Cell(fill=matcool)
cell140.region = +cyl139 & +px8 & -bnde & -py3 & +py4
biguni.add_cell(cell137)
biguni.add_cell(cell138)
biguni.add_cell(cell139)
biguni.add_cell(cell140)
# rod number (9,13)
x=  0.000000
y=  5.710000
cyl141 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl142 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl143 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell141 = openmc.Cell(fill=matfuel01)
cell141.region = -cyl141 & +bndw
fuel_cell_list.append(cell141.id)
cell142 = openmc.Cell(fill=matair)
cell142.region = +cyl141 & -cyl142 & +bndw
cell143 = openmc.Cell(fill=matclad)
cell143.region = +cyl142 & -cyl143 & +bndw
cell144 = openmc.Cell(fill=matcool)
cell144.region = +cyl143 & +bndw & -px1 & -py4 & +py5
biguni.add_cell(cell141)
biguni.add_cell(cell142)
biguni.add_cell(cell143)
biguni.add_cell(cell144)
# rod number (10,13)
x=  1.260000
y=  5.710000
cyl145 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl146 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl147 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell145 = openmc.Cell(fill=matfuel01)
cell145.region = -cyl145
fuel_cell_list.append(cell145.id)
cell146 = openmc.Cell(fill=matair)
cell146.region = +cyl145 & -cyl146
cell147 = openmc.Cell(fill=matclad)
cell147.region = +cyl146 & -cyl147
cell148 = openmc.Cell(fill=matcool)
cell148.region = +cyl147 & +px1 & -px2 & -py4 & +py5
biguni.add_cell(cell145)
biguni.add_cell(cell146)
biguni.add_cell(cell147)
biguni.add_cell(cell148)
# rod number (11,13)
x=  2.520000
y=  5.710000
cyl149 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl150 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl151 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell149 = openmc.Cell(fill=matfuel01)
cell149.region = -cyl149
fuel_cell_list.append(cell149.id)
cell150 = openmc.Cell(fill=matair)
cell150.region = +cyl149 & -cyl150
cell151 = openmc.Cell(fill=matclad)
cell151.region = +cyl150 & -cyl151
cell152 = openmc.Cell(fill=matcool)
cell152.region = +cyl151 & +px2 & -px3 & -py4 & +py5
biguni.add_cell(cell149)
biguni.add_cell(cell150)
biguni.add_cell(cell151)
biguni.add_cell(cell152)
# rod number (12,13)
x=  3.780000
y=  5.710000
cyl153 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl154 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl155 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell153 = openmc.Cell(fill=matfuel01)
cell153.region = -cyl153
fuel_cell_list.append(cell153.id)
cell154 = openmc.Cell(fill=matair)
cell154.region = +cyl153 & -cyl154
cell155 = openmc.Cell(fill=matclad)
cell155.region = +cyl154 & -cyl155
cell156 = openmc.Cell(fill=matcool)
cell156.region = +cyl155 & +px3 & -px4 & -py4 & +py5
biguni.add_cell(cell153)
biguni.add_cell(cell154)
biguni.add_cell(cell155)
biguni.add_cell(cell156)
# rod number (13,13)
x=  5.040000
y=  5.710000
cyl157 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl158 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl159 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell157 = openmc.Cell(fill=matfuel01)
cell157.region = -cyl157
fuel_cell_list.append(cell157.id)
cell158 = openmc.Cell(fill=matair)
cell158.region = +cyl157 & -cyl158
cell159 = openmc.Cell(fill=matclad)
cell159.region = +cyl158 & -cyl159
cell160 = openmc.Cell(fill=matcool)
cell160.region = +cyl159 & +px4 & -px5 & -py4 & +py5
biguni.add_cell(cell157)
biguni.add_cell(cell158)
biguni.add_cell(cell159)
biguni.add_cell(cell160)
# rod number (14,13)
x=  6.300000
y=  5.710000
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
cell164.region = +cyl163 & +px5 & -px6 & -py4 & +py5
biguni.add_cell(cell161)
biguni.add_cell(cell162)
biguni.add_cell(cell163)
biguni.add_cell(cell164)
# rod number (15,13)
x=  7.560000
y=  5.710000
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
cell168.region = +cyl167 & +px6 & -px7 & -py4 & +py5
biguni.add_cell(cell165)
biguni.add_cell(cell166)
biguni.add_cell(cell167)
biguni.add_cell(cell168)
# rod number (16,13)
x=  8.820000
y=  5.710000
cyl169 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl170 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl171 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell169 = openmc.Cell(fill=matfuel01)
cell169.region = -cyl169
fuel_cell_list.append(cell169.id)
cell170 = openmc.Cell(fill=matair)
cell170.region = +cyl169 & -cyl170
cell171 = openmc.Cell(fill=matclad)
cell171.region = +cyl170 & -cyl171
cell172 = openmc.Cell(fill=matcool)
cell172.region = +cyl171 & +px7 & -px8 & -py4 & +py5
biguni.add_cell(cell169)
biguni.add_cell(cell170)
biguni.add_cell(cell171)
biguni.add_cell(cell172)
# rod number (17,13)
x= 10.080000
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
cell176.region = +cyl175 & +px8 & -bnde & -py4 & +py5
biguni.add_cell(cell173)
biguni.add_cell(cell174)
biguni.add_cell(cell175)
biguni.add_cell(cell176)
# rod number (9,14)
x=  0.000000
y=  4.450000
cyl177 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl178 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl179 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell177 = openmc.Cell(fill=matfuel01)
cell177.region = -cyl177 & +bndw
fuel_cell_list.append(cell177.id)
cell178 = openmc.Cell(fill=matair)
cell178.region = +cyl177 & -cyl178 & +bndw
cell179 = openmc.Cell(fill=matclad)
cell179.region = +cyl178 & -cyl179 & +bndw
cell180 = openmc.Cell(fill=matcool)
cell180.region = +cyl179 & +bndw & -px1 & -py5 & +py6
biguni.add_cell(cell177)
biguni.add_cell(cell178)
biguni.add_cell(cell179)
biguni.add_cell(cell180)
# rod number (10,14)
x=  1.260000
y=  4.450000
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
cell184.region = +cyl183 & +px1 & -px2 & -py5 & +py6
biguni.add_cell(cell181)
biguni.add_cell(cell182)
biguni.add_cell(cell183)
biguni.add_cell(cell184)
# rod number (11,14)
x=  2.520000
y=  4.450000
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
cell188.region = +cyl187 & +px2 & -px3 & -py5 & +py6
biguni.add_cell(cell185)
biguni.add_cell(cell186)
biguni.add_cell(cell187)
biguni.add_cell(cell188)
# rod number (12,14)
x=  3.780000
y=  4.450000
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
cell192.region = +cyl191 & +px3 & -px4 & -py5 & +py6
biguni.add_cell(cell189)
biguni.add_cell(cell190)
biguni.add_cell(cell191)
biguni.add_cell(cell192)
# rod number (13,14)
x=  5.040000
y=  4.450000
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
cell196.region = +cyl195 & +px4 & -px5 & -py5 & +py6
biguni.add_cell(cell193)
biguni.add_cell(cell194)
biguni.add_cell(cell195)
biguni.add_cell(cell196)
# rod number (14,14)
x=  6.300000
y=  4.450000
cyl197 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl198 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell197 = openmc.Cell(fill=matmod)
cell197.region = -cyl197
cell198 = openmc.Cell(fill=matclad)
cell198.region = +cyl197 & -cyl198
cell199 = openmc.Cell(fill=matcool)
cell199.region = +cyl198 & +px5 & -px6 & -py5 & +py6
biguni.add_cell(cell197)
biguni.add_cell(cell198)
biguni.add_cell(cell199)
# rod number (15,14)
x=  7.560000
y=  4.450000
cyl200 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl201 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl202 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell200 = openmc.Cell(fill=matfuel01)
cell200.region = -cyl200
fuel_cell_list.append(cell200.id)
cell201 = openmc.Cell(fill=matair)
cell201.region = +cyl200 & -cyl201
cell202 = openmc.Cell(fill=matclad)
cell202.region = +cyl201 & -cyl202
cell203 = openmc.Cell(fill=matcool)
cell203.region = +cyl202 & +px6 & -px7 & -py5 & +py6
biguni.add_cell(cell200)
biguni.add_cell(cell201)
biguni.add_cell(cell202)
biguni.add_cell(cell203)
# rod number (16,14)
x=  8.820000
y=  4.450000
cyl204 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl205 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl206 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell204 = openmc.Cell(fill=matfuel01)
cell204.region = -cyl204
fuel_cell_list.append(cell204.id)
cell205 = openmc.Cell(fill=matair)
cell205.region = +cyl204 & -cyl205
cell206 = openmc.Cell(fill=matclad)
cell206.region = +cyl205 & -cyl206
cell207 = openmc.Cell(fill=matcool)
cell207.region = +cyl206 & +px7 & -px8 & -py5 & +py6
biguni.add_cell(cell204)
biguni.add_cell(cell205)
biguni.add_cell(cell206)
biguni.add_cell(cell207)
# rod number (17,14)
x= 10.080000
y=  4.450000
cyl208 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl209 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl210 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell208 = openmc.Cell(fill=matfuel01)
cell208.region = -cyl208
fuel_cell_list.append(cell208.id)
cell209 = openmc.Cell(fill=matair)
cell209.region = +cyl208 & -cyl209
cell210 = openmc.Cell(fill=matclad)
cell210.region = +cyl209 & -cyl210
cell211 = openmc.Cell(fill=matcool)
cell211.region = +cyl210 & +px8 & -bnde & -py5 & +py6
biguni.add_cell(cell208)
biguni.add_cell(cell209)
biguni.add_cell(cell210)
biguni.add_cell(cell211)
# rod number (9,15)
x=  0.000000
y=  3.190000
cyl212 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl213 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell212 = openmc.Cell(fill=matmod)
cell212.region = -cyl212 & +bndw
cell213 = openmc.Cell(fill=matclad)
cell213.region = +cyl212 & -cyl213 & +bndw
cell214 = openmc.Cell(fill=matcool)
cell214.region = +cyl213 & +bndw & -px1 & -py6 & +py7
biguni.add_cell(cell212)
biguni.add_cell(cell213)
biguni.add_cell(cell214)
# rod number (10,15)
x=  1.260000
y=  3.190000
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
cell218.region = +cyl217 & +px1 & -px2 & -py6 & +py7
biguni.add_cell(cell215)
biguni.add_cell(cell216)
biguni.add_cell(cell217)
biguni.add_cell(cell218)
# rod number (11,15)
x=  2.520000
y=  3.190000
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
cell222.region = +cyl221 & +px2 & -px3 & -py6 & +py7
biguni.add_cell(cell219)
biguni.add_cell(cell220)
biguni.add_cell(cell221)
biguni.add_cell(cell222)
# rod number (12,15)
x=  3.780000
y=  3.190000
cyl223 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl224 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell223 = openmc.Cell(fill=matmod)
cell223.region = -cyl223
cell224 = openmc.Cell(fill=matclad)
cell224.region = +cyl223 & -cyl224
cell225 = openmc.Cell(fill=matcool)
cell225.region = +cyl224 & +px3 & -px4 & -py6 & +py7
biguni.add_cell(cell223)
biguni.add_cell(cell224)
biguni.add_cell(cell225)
# rod number (13,15)
x=  5.040000
y=  3.190000
cyl226 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl227 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl228 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell226 = openmc.Cell(fill=matfuel01)
cell226.region = -cyl226
fuel_cell_list.append(cell226.id)
cell227 = openmc.Cell(fill=matair)
cell227.region = +cyl226 & -cyl227
cell228 = openmc.Cell(fill=matclad)
cell228.region = +cyl227 & -cyl228
cell229 = openmc.Cell(fill=matcool)
cell229.region = +cyl228 & +px4 & -px5 & -py6 & +py7
biguni.add_cell(cell226)
biguni.add_cell(cell227)
biguni.add_cell(cell228)
biguni.add_cell(cell229)
# rod number (14,15)
x=  6.300000
y=  3.190000
cyl230 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl231 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl232 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell230 = openmc.Cell(fill=matfuel01)
cell230.region = -cyl230
fuel_cell_list.append(cell230.id)
cell231 = openmc.Cell(fill=matair)
cell231.region = +cyl230 & -cyl231
cell232 = openmc.Cell(fill=matclad)
cell232.region = +cyl231 & -cyl232
cell233 = openmc.Cell(fill=matcool)
cell233.region = +cyl232 & +px5 & -px6 & -py6 & +py7
biguni.add_cell(cell230)
biguni.add_cell(cell231)
biguni.add_cell(cell232)
biguni.add_cell(cell233)
# rod number (15,15)
x=  7.560000
y=  3.190000
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
cell237.region = +cyl236 & +px6 & -px7 & -py6 & +py7
biguni.add_cell(cell234)
biguni.add_cell(cell235)
biguni.add_cell(cell236)
biguni.add_cell(cell237)
# rod number (16,15)
x=  8.820000
y=  3.190000
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
cell241.region = +cyl240 & +px7 & -px8 & -py6 & +py7
biguni.add_cell(cell238)
biguni.add_cell(cell239)
biguni.add_cell(cell240)
biguni.add_cell(cell241)
# rod number (17,15)
x= 10.080000
y=  3.190000
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
cell245.region = +cyl244 & +px8 & -bnde & -py6 & +py7
biguni.add_cell(cell242)
biguni.add_cell(cell243)
biguni.add_cell(cell244)
biguni.add_cell(cell245)
# rod number (9,16)
x=  0.000000
y=  1.930000
cyl246 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl247 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl248 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell246 = openmc.Cell(fill=matfuel01)
cell246.region = -cyl246 & +bndw
fuel_cell_list.append(cell246.id)
cell247 = openmc.Cell(fill=matair)
cell247.region = +cyl246 & -cyl247 & +bndw
cell248 = openmc.Cell(fill=matclad)
cell248.region = +cyl247 & -cyl248 & +bndw
cell249 = openmc.Cell(fill=matcool)
cell249.region = +cyl248 & +bndw & -px1 & -py7 & +py8
biguni.add_cell(cell246)
biguni.add_cell(cell247)
biguni.add_cell(cell248)
biguni.add_cell(cell249)
# rod number (10,16)
x=  1.260000
y=  1.930000
cyl250 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl251 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl252 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell250 = openmc.Cell(fill=matfuel01)
cell250.region = -cyl250
fuel_cell_list.append(cell250.id)
cell251 = openmc.Cell(fill=matair)
cell251.region = +cyl250 & -cyl251
cell252 = openmc.Cell(fill=matclad)
cell252.region = +cyl251 & -cyl252
cell253 = openmc.Cell(fill=matcool)
cell253.region = +cyl252 & +px1 & -px2 & -py7 & +py8
biguni.add_cell(cell250)
biguni.add_cell(cell251)
biguni.add_cell(cell252)
biguni.add_cell(cell253)
# rod number (11,16)
x=  2.520000
y=  1.930000
cyl254 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl255 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl256 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell254 = openmc.Cell(fill=matfuel01)
cell254.region = -cyl254
fuel_cell_list.append(cell254.id)
cell255 = openmc.Cell(fill=matair)
cell255.region = +cyl254 & -cyl255
cell256 = openmc.Cell(fill=matclad)
cell256.region = +cyl255 & -cyl256
cell257 = openmc.Cell(fill=matcool)
cell257.region = +cyl256 & +px2 & -px3 & -py7 & +py8
biguni.add_cell(cell254)
biguni.add_cell(cell255)
biguni.add_cell(cell256)
biguni.add_cell(cell257)
# rod number (12,16)
x=  3.780000
y=  1.930000
cyl258 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl259 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl260 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell258 = openmc.Cell(fill=matfuel01)
cell258.region = -cyl258
fuel_cell_list.append(cell258.id)
cell259 = openmc.Cell(fill=matair)
cell259.region = +cyl258 & -cyl259
cell260 = openmc.Cell(fill=matclad)
cell260.region = +cyl259 & -cyl260
cell261 = openmc.Cell(fill=matcool)
cell261.region = +cyl260 & +px3 & -px4 & -py7 & +py8
biguni.add_cell(cell258)
biguni.add_cell(cell259)
biguni.add_cell(cell260)
biguni.add_cell(cell261)
# rod number (13,16)
x=  5.040000
y=  1.930000
cyl262 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl263 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl264 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell262 = openmc.Cell(fill=matfuel01)
cell262.region = -cyl262
fuel_cell_list.append(cell262.id)
cell263 = openmc.Cell(fill=matair)
cell263.region = +cyl262 & -cyl263
cell264 = openmc.Cell(fill=matclad)
cell264.region = +cyl263 & -cyl264
cell265 = openmc.Cell(fill=matcool)
cell265.region = +cyl264 & +px4 & -px5 & -py7 & +py8
biguni.add_cell(cell262)
biguni.add_cell(cell263)
biguni.add_cell(cell264)
biguni.add_cell(cell265)
# rod number (14,16)
x=  6.300000
y=  1.930000
cyl266 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl267 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl268 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell266 = openmc.Cell(fill=matfuel01)
cell266.region = -cyl266
fuel_cell_list.append(cell266.id)
cell267 = openmc.Cell(fill=matair)
cell267.region = +cyl266 & -cyl267
cell268 = openmc.Cell(fill=matclad)
cell268.region = +cyl267 & -cyl268
cell269 = openmc.Cell(fill=matcool)
cell269.region = +cyl268 & +px5 & -px6 & -py7 & +py8
biguni.add_cell(cell266)
biguni.add_cell(cell267)
biguni.add_cell(cell268)
biguni.add_cell(cell269)
# rod number (15,16)
x=  7.560000
y=  1.930000
cyl270 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl271 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl272 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell270 = openmc.Cell(fill=matfuel01)
cell270.region = -cyl270
fuel_cell_list.append(cell270.id)
cell271 = openmc.Cell(fill=matair)
cell271.region = +cyl270 & -cyl271
cell272 = openmc.Cell(fill=matclad)
cell272.region = +cyl271 & -cyl272
cell273 = openmc.Cell(fill=matcool)
cell273.region = +cyl272 & +px6 & -px7 & -py7 & +py8
biguni.add_cell(cell270)
biguni.add_cell(cell271)
biguni.add_cell(cell272)
biguni.add_cell(cell273)
# rod number (16,16)
x=  8.820000
y=  1.930000
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
cell277.region = +cyl276 & +px7 & -px8 & -py7 & +py8
biguni.add_cell(cell274)
biguni.add_cell(cell275)
biguni.add_cell(cell276)
biguni.add_cell(cell277)
# rod number (17,16)
x= 10.080000
y=  1.930000
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
cell281.region = +cyl280 & +px8 & -bnde & -py7 & +py8
biguni.add_cell(cell278)
biguni.add_cell(cell279)
biguni.add_cell(cell280)
biguni.add_cell(cell281)
# rod number (9,17)
x=  0.000000
y=  0.670000
cyl282 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl283 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl284 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell282 = openmc.Cell(fill=matfuel01)
cell282.region = -cyl282 & +bndw
fuel_cell_list.append(cell282.id)
cell283 = openmc.Cell(fill=matair)
cell283.region = +cyl282 & -cyl283 & +bndw
cell284 = openmc.Cell(fill=matclad)
cell284.region = +cyl283 & -cyl284 & +bndw
cell285 = openmc.Cell(fill=matcool)
cell285.region = +cyl284 & +bndw & -px1 & -py8 & +bnds
biguni.add_cell(cell282)
biguni.add_cell(cell283)
biguni.add_cell(cell284)
biguni.add_cell(cell285)
# rod number (10,17)
x=  1.260000
y=  0.670000
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
cell289.region = +cyl288 & +px1 & -px2 & -py8 & +bnds
biguni.add_cell(cell286)
biguni.add_cell(cell287)
biguni.add_cell(cell288)
biguni.add_cell(cell289)
# rod number (11,17)
x=  2.520000
y=  0.670000
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
cell293.region = +cyl292 & +px2 & -px3 & -py8 & +bnds
biguni.add_cell(cell290)
biguni.add_cell(cell291)
biguni.add_cell(cell292)
biguni.add_cell(cell293)
# rod number (12,17)
x=  3.780000
y=  0.670000
cyl294 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl295 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl296 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell294 = openmc.Cell(fill=matfuel01)
cell294.region = -cyl294
fuel_cell_list.append(cell294.id)
cell295 = openmc.Cell(fill=matair)
cell295.region = +cyl294 & -cyl295
cell296 = openmc.Cell(fill=matclad)
cell296.region = +cyl295 & -cyl296
cell297 = openmc.Cell(fill=matcool)
cell297.region = +cyl296 & +px3 & -px4 & -py8 & +bnds
biguni.add_cell(cell294)
biguni.add_cell(cell295)
biguni.add_cell(cell296)
biguni.add_cell(cell297)
# rod number (13,17)
x=  5.040000
y=  0.670000
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
cell301.region = +cyl300 & +px4 & -px5 & -py8 & +bnds
biguni.add_cell(cell298)
biguni.add_cell(cell299)
biguni.add_cell(cell300)
biguni.add_cell(cell301)
# rod number (14,17)
x=  6.300000
y=  0.670000
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
cell305.region = +cyl304 & +px5 & -px6 & -py8 & +bnds
biguni.add_cell(cell302)
biguni.add_cell(cell303)
biguni.add_cell(cell304)
biguni.add_cell(cell305)
# rod number (15,17)
x=  7.560000
y=  0.670000
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
cell309.region = +cyl308 & +px6 & -px7 & -py8 & +bnds
biguni.add_cell(cell306)
biguni.add_cell(cell307)
biguni.add_cell(cell308)
biguni.add_cell(cell309)
# rod number (16,17)
x=  8.820000
y=  0.670000
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
cell313.region = +cyl312 & +px7 & -px8 & -py8 & +bnds
biguni.add_cell(cell310)
biguni.add_cell(cell311)
biguni.add_cell(cell312)
biguni.add_cell(cell313)
# rod number (17,17)
x= 10.080000
y=  0.670000
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
cell317.region = +cyl316 & +px8 & -bnde & -py8 & +bnds
biguni.add_cell(cell314)
biguni.add_cell(cell315)
biguni.add_cell(cell316)
biguni.add_cell(cell317)

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
