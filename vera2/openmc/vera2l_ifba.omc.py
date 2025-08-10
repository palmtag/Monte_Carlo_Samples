import matplotlib

import openmc
import openmc.mgxs as mgxs
import openmc.data          # need for hdf5

#  To run:
#  >python3 vera2l_ifba.omc
#
# OpenMC Input created by BUNBLD on 08/09/2025 11:48:06
#  VERA Benchmark #2 - Single Assembly
#  Uniform PWR Assembly
#  November 15, 2012
#  Number densities from KENO run
#  VERA Benchmark 2L - like 2A + 80 IFBA pins
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

# material 6 IFBA
matifba = openmc.Material(name='ifba')
matifba.add_nuclide('B10',  2.164100E-02)
matifba.add_nuclide('B11',  1.968240E-02)
matifba.add_nuclide('Zr90',  1.063040E-02)
matifba.add_nuclide('Zr91',  2.318240E-03)
matifba.add_nuclide('Zr92',  3.543480E-03)
matifba.add_nuclide('Zr94',  3.591000E-03)
matifba.add_nuclide('Zr96',  5.785280E-04)
matifba.set_density('g/cm3',  3.84948)
matifba.temperature=  600.000

# Material mixtures

# Instantiate a Materials collection
model.materials = openmc.Materials([matfuel01,matclad,matcool,matmod,matair,matifba])
#
# ------------- Geometry ------------------------
#
# PINMAP
#  3  8  1  2  8  1  2  8  1  
#  8  1  1  8  1  1  8  1  1  
#  1  1  8  1  1  1  1  1  1  
#  2  8  1  2  8  8  2  8  1  
#  8  1  1  8  1  8  8  1  1  
#  1  1  1  8  8  2  1  1  1  
#  2  8  1  2  8  1  8  1  1  
#  8  1  1  8  1  1  1  1  1  
#  1  1  1  1  1  1  1  1  8  
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
cyl5 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl6 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl7 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell4 = openmc.Cell(fill=matfuel01)
cell4.region = -cyl4 & -bndn
fuel_cell_list.append(cell4.id)
cell5 = openmc.Cell(fill=matifba)
cell5.region = +cyl4 & -cyl5 & -bndn
cell6 = openmc.Cell(fill=matair)
cell6.region = +cyl5 & -cyl6 & -bndn
cell7 = openmc.Cell(fill=matclad)
cell7.region = +cyl6 & -cyl7 & -bndn
cell8 = openmc.Cell(fill=matcool)
cell8.region = +cyl7 & +px1 & -px2 & -bndn & +py1
biguni.add_cell(cell4)
biguni.add_cell(cell5)
biguni.add_cell(cell6)
biguni.add_cell(cell7)
biguni.add_cell(cell8)
# rod number (11,9)
x=  2.520000
y= 10.750000
cyl9 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl10 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl11 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell9 = openmc.Cell(fill=matfuel01)
cell9.region = -cyl9 & -bndn
fuel_cell_list.append(cell9.id)
cell10 = openmc.Cell(fill=matair)
cell10.region = +cyl9 & -cyl10 & -bndn
cell11 = openmc.Cell(fill=matclad)
cell11.region = +cyl10 & -cyl11 & -bndn
cell12 = openmc.Cell(fill=matcool)
cell12.region = +cyl11 & +px2 & -px3 & -bndn & +py1
biguni.add_cell(cell9)
biguni.add_cell(cell10)
biguni.add_cell(cell11)
biguni.add_cell(cell12)
# rod number (12,9)
x=  3.780000
y= 10.750000
cyl13 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl14 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell13 = openmc.Cell(fill=matmod)
cell13.region = -cyl13 & -bndn
cell14 = openmc.Cell(fill=matclad)
cell14.region = +cyl13 & -cyl14 & -bndn
cell15 = openmc.Cell(fill=matcool)
cell15.region = +cyl14 & +px3 & -px4 & -bndn & +py1
biguni.add_cell(cell13)
biguni.add_cell(cell14)
biguni.add_cell(cell15)
# rod number (13,9)
x=  5.040000
y= 10.750000
cyl16 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl17 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl18 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl19 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell16 = openmc.Cell(fill=matfuel01)
cell16.region = -cyl16 & -bndn
fuel_cell_list.append(cell16.id)
cell17 = openmc.Cell(fill=matifba)
cell17.region = +cyl16 & -cyl17 & -bndn
cell18 = openmc.Cell(fill=matair)
cell18.region = +cyl17 & -cyl18 & -bndn
cell19 = openmc.Cell(fill=matclad)
cell19.region = +cyl18 & -cyl19 & -bndn
cell20 = openmc.Cell(fill=matcool)
cell20.region = +cyl19 & +px4 & -px5 & -bndn & +py1
biguni.add_cell(cell16)
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
cyl29 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl30 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl31 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell28 = openmc.Cell(fill=matfuel01)
cell28.region = -cyl28 & -bndn
fuel_cell_list.append(cell28.id)
cell29 = openmc.Cell(fill=matifba)
cell29.region = +cyl28 & -cyl29 & -bndn
cell30 = openmc.Cell(fill=matair)
cell30.region = +cyl29 & -cyl30 & -bndn
cell31 = openmc.Cell(fill=matclad)
cell31.region = +cyl30 & -cyl31 & -bndn
cell32 = openmc.Cell(fill=matcool)
cell32.region = +cyl31 & +px7 & -px8 & -bndn & +py1
biguni.add_cell(cell28)
biguni.add_cell(cell29)
biguni.add_cell(cell30)
biguni.add_cell(cell31)
biguni.add_cell(cell32)
# rod number (17,9)
x= 10.080000
y= 10.750000
cyl33 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl34 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl35 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell33 = openmc.Cell(fill=matfuel01)
cell33.region = -cyl33 & -bndn
fuel_cell_list.append(cell33.id)
cell34 = openmc.Cell(fill=matair)
cell34.region = +cyl33 & -cyl34 & -bndn
cell35 = openmc.Cell(fill=matclad)
cell35.region = +cyl34 & -cyl35 & -bndn
cell36 = openmc.Cell(fill=matcool)
cell36.region = +cyl35 & +px8 & -bnde & -bndn & +py1
biguni.add_cell(cell33)
biguni.add_cell(cell34)
biguni.add_cell(cell35)
biguni.add_cell(cell36)
# rod number (9,10)
x=  0.000000
y=  9.490000
cyl37 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl38 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl39 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl40 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell37 = openmc.Cell(fill=matfuel01)
cell37.region = -cyl37 & +bndw
fuel_cell_list.append(cell37.id)
cell38 = openmc.Cell(fill=matifba)
cell38.region = +cyl37 & -cyl38 & +bndw
cell39 = openmc.Cell(fill=matair)
cell39.region = +cyl38 & -cyl39 & +bndw
cell40 = openmc.Cell(fill=matclad)
cell40.region = +cyl39 & -cyl40 & +bndw
cell41 = openmc.Cell(fill=matcool)
cell41.region = +cyl40 & +bndw & -px1 & -py1 & +py2
biguni.add_cell(cell37)
biguni.add_cell(cell38)
biguni.add_cell(cell39)
biguni.add_cell(cell40)
biguni.add_cell(cell41)
# rod number (10,10)
x=  1.260000
y=  9.490000
cyl42 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl43 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl44 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell42 = openmc.Cell(fill=matfuel01)
cell42.region = -cyl42
fuel_cell_list.append(cell42.id)
cell43 = openmc.Cell(fill=matair)
cell43.region = +cyl42 & -cyl43
cell44 = openmc.Cell(fill=matclad)
cell44.region = +cyl43 & -cyl44
cell45 = openmc.Cell(fill=matcool)
cell45.region = +cyl44 & +px1 & -px2 & -py1 & +py2
biguni.add_cell(cell42)
biguni.add_cell(cell43)
biguni.add_cell(cell44)
biguni.add_cell(cell45)
# rod number (11,10)
x=  2.520000
y=  9.490000
cyl46 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl47 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl48 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell46 = openmc.Cell(fill=matfuel01)
cell46.region = -cyl46
fuel_cell_list.append(cell46.id)
cell47 = openmc.Cell(fill=matair)
cell47.region = +cyl46 & -cyl47
cell48 = openmc.Cell(fill=matclad)
cell48.region = +cyl47 & -cyl48
cell49 = openmc.Cell(fill=matcool)
cell49.region = +cyl48 & +px2 & -px3 & -py1 & +py2
biguni.add_cell(cell46)
biguni.add_cell(cell47)
biguni.add_cell(cell48)
biguni.add_cell(cell49)
# rod number (12,10)
x=  3.780000
y=  9.490000
cyl50 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl51 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl52 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl53 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell50 = openmc.Cell(fill=matfuel01)
cell50.region = -cyl50
fuel_cell_list.append(cell50.id)
cell51 = openmc.Cell(fill=matifba)
cell51.region = +cyl50 & -cyl51
cell52 = openmc.Cell(fill=matair)
cell52.region = +cyl51 & -cyl52
cell53 = openmc.Cell(fill=matclad)
cell53.region = +cyl52 & -cyl53
cell54 = openmc.Cell(fill=matcool)
cell54.region = +cyl53 & +px3 & -px4 & -py1 & +py2
biguni.add_cell(cell50)
biguni.add_cell(cell51)
biguni.add_cell(cell52)
biguni.add_cell(cell53)
biguni.add_cell(cell54)
# rod number (13,10)
x=  5.040000
y=  9.490000
cyl55 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl56 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl57 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell55 = openmc.Cell(fill=matfuel01)
cell55.region = -cyl55
fuel_cell_list.append(cell55.id)
cell56 = openmc.Cell(fill=matair)
cell56.region = +cyl55 & -cyl56
cell57 = openmc.Cell(fill=matclad)
cell57.region = +cyl56 & -cyl57
cell58 = openmc.Cell(fill=matcool)
cell58.region = +cyl57 & +px4 & -px5 & -py1 & +py2
biguni.add_cell(cell55)
biguni.add_cell(cell56)
biguni.add_cell(cell57)
biguni.add_cell(cell58)
# rod number (14,10)
x=  6.300000
y=  9.490000
cyl59 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl60 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl61 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell59 = openmc.Cell(fill=matfuel01)
cell59.region = -cyl59
fuel_cell_list.append(cell59.id)
cell60 = openmc.Cell(fill=matair)
cell60.region = +cyl59 & -cyl60
cell61 = openmc.Cell(fill=matclad)
cell61.region = +cyl60 & -cyl61
cell62 = openmc.Cell(fill=matcool)
cell62.region = +cyl61 & +px5 & -px6 & -py1 & +py2
biguni.add_cell(cell59)
biguni.add_cell(cell60)
biguni.add_cell(cell61)
biguni.add_cell(cell62)
# rod number (15,10)
x=  7.560000
y=  9.490000
cyl63 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl64 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl65 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl66 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell63 = openmc.Cell(fill=matfuel01)
cell63.region = -cyl63
fuel_cell_list.append(cell63.id)
cell64 = openmc.Cell(fill=matifba)
cell64.region = +cyl63 & -cyl64
cell65 = openmc.Cell(fill=matair)
cell65.region = +cyl64 & -cyl65
cell66 = openmc.Cell(fill=matclad)
cell66.region = +cyl65 & -cyl66
cell67 = openmc.Cell(fill=matcool)
cell67.region = +cyl66 & +px6 & -px7 & -py1 & +py2
biguni.add_cell(cell63)
biguni.add_cell(cell64)
biguni.add_cell(cell65)
biguni.add_cell(cell66)
biguni.add_cell(cell67)
# rod number (16,10)
x=  8.820000
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
cell71.region = +cyl70 & +px7 & -px8 & -py1 & +py2
biguni.add_cell(cell68)
biguni.add_cell(cell69)
biguni.add_cell(cell70)
biguni.add_cell(cell71)
# rod number (17,10)
x= 10.080000
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
cell75.region = +cyl74 & +px8 & -bnde & -py1 & +py2
biguni.add_cell(cell72)
biguni.add_cell(cell73)
biguni.add_cell(cell74)
biguni.add_cell(cell75)
# rod number (9,11)
x=  0.000000
y=  8.230000
cyl76 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl77 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl78 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell76 = openmc.Cell(fill=matfuel01)
cell76.region = -cyl76 & +bndw
fuel_cell_list.append(cell76.id)
cell77 = openmc.Cell(fill=matair)
cell77.region = +cyl76 & -cyl77 & +bndw
cell78 = openmc.Cell(fill=matclad)
cell78.region = +cyl77 & -cyl78 & +bndw
cell79 = openmc.Cell(fill=matcool)
cell79.region = +cyl78 & +bndw & -px1 & -py2 & +py3
biguni.add_cell(cell76)
biguni.add_cell(cell77)
biguni.add_cell(cell78)
biguni.add_cell(cell79)
# rod number (10,11)
x=  1.260000
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
cell83.region = +cyl82 & +px1 & -px2 & -py2 & +py3
biguni.add_cell(cell80)
biguni.add_cell(cell81)
biguni.add_cell(cell82)
biguni.add_cell(cell83)
# rod number (11,11)
x=  2.520000
y=  8.230000
cyl84 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl85 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl86 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl87 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell84 = openmc.Cell(fill=matfuel01)
cell84.region = -cyl84
fuel_cell_list.append(cell84.id)
cell85 = openmc.Cell(fill=matifba)
cell85.region = +cyl84 & -cyl85
cell86 = openmc.Cell(fill=matair)
cell86.region = +cyl85 & -cyl86
cell87 = openmc.Cell(fill=matclad)
cell87.region = +cyl86 & -cyl87
cell88 = openmc.Cell(fill=matcool)
cell88.region = +cyl87 & +px2 & -px3 & -py2 & +py3
biguni.add_cell(cell84)
biguni.add_cell(cell85)
biguni.add_cell(cell86)
biguni.add_cell(cell87)
biguni.add_cell(cell88)
# rod number (12,11)
x=  3.780000
y=  8.230000
cyl89 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl90 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl91 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell89 = openmc.Cell(fill=matfuel01)
cell89.region = -cyl89
fuel_cell_list.append(cell89.id)
cell90 = openmc.Cell(fill=matair)
cell90.region = +cyl89 & -cyl90
cell91 = openmc.Cell(fill=matclad)
cell91.region = +cyl90 & -cyl91
cell92 = openmc.Cell(fill=matcool)
cell92.region = +cyl91 & +px3 & -px4 & -py2 & +py3
biguni.add_cell(cell89)
biguni.add_cell(cell90)
biguni.add_cell(cell91)
biguni.add_cell(cell92)
# rod number (13,11)
x=  5.040000
y=  8.230000
cyl93 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl94 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl95 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell93 = openmc.Cell(fill=matfuel01)
cell93.region = -cyl93
fuel_cell_list.append(cell93.id)
cell94 = openmc.Cell(fill=matair)
cell94.region = +cyl93 & -cyl94
cell95 = openmc.Cell(fill=matclad)
cell95.region = +cyl94 & -cyl95
cell96 = openmc.Cell(fill=matcool)
cell96.region = +cyl95 & +px4 & -px5 & -py2 & +py3
biguni.add_cell(cell93)
biguni.add_cell(cell94)
biguni.add_cell(cell95)
biguni.add_cell(cell96)
# rod number (14,11)
x=  6.300000
y=  8.230000
cyl97 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl98 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl99 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell97 = openmc.Cell(fill=matfuel01)
cell97.region = -cyl97
fuel_cell_list.append(cell97.id)
cell98 = openmc.Cell(fill=matair)
cell98.region = +cyl97 & -cyl98
cell99 = openmc.Cell(fill=matclad)
cell99.region = +cyl98 & -cyl99
cell100 = openmc.Cell(fill=matcool)
cell100.region = +cyl99 & +px5 & -px6 & -py2 & +py3
biguni.add_cell(cell97)
biguni.add_cell(cell98)
biguni.add_cell(cell99)
biguni.add_cell(cell100)
# rod number (15,11)
x=  7.560000
y=  8.230000
cyl101 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl102 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl103 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell101 = openmc.Cell(fill=matfuel01)
cell101.region = -cyl101
fuel_cell_list.append(cell101.id)
cell102 = openmc.Cell(fill=matair)
cell102.region = +cyl101 & -cyl102
cell103 = openmc.Cell(fill=matclad)
cell103.region = +cyl102 & -cyl103
cell104 = openmc.Cell(fill=matcool)
cell104.region = +cyl103 & +px6 & -px7 & -py2 & +py3
biguni.add_cell(cell101)
biguni.add_cell(cell102)
biguni.add_cell(cell103)
biguni.add_cell(cell104)
# rod number (16,11)
x=  8.820000
y=  8.230000
cyl105 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl106 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl107 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell105 = openmc.Cell(fill=matfuel01)
cell105.region = -cyl105
fuel_cell_list.append(cell105.id)
cell106 = openmc.Cell(fill=matair)
cell106.region = +cyl105 & -cyl106
cell107 = openmc.Cell(fill=matclad)
cell107.region = +cyl106 & -cyl107
cell108 = openmc.Cell(fill=matcool)
cell108.region = +cyl107 & +px7 & -px8 & -py2 & +py3
biguni.add_cell(cell105)
biguni.add_cell(cell106)
biguni.add_cell(cell107)
biguni.add_cell(cell108)
# rod number (17,11)
x= 10.080000
y=  8.230000
cyl109 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl110 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl111 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell109 = openmc.Cell(fill=matfuel01)
cell109.region = -cyl109
fuel_cell_list.append(cell109.id)
cell110 = openmc.Cell(fill=matair)
cell110.region = +cyl109 & -cyl110
cell111 = openmc.Cell(fill=matclad)
cell111.region = +cyl110 & -cyl111
cell112 = openmc.Cell(fill=matcool)
cell112.region = +cyl111 & +px8 & -bnde & -py2 & +py3
biguni.add_cell(cell109)
biguni.add_cell(cell110)
biguni.add_cell(cell111)
biguni.add_cell(cell112)
# rod number (9,12)
x=  0.000000
y=  6.970000
cyl113 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl114 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell113 = openmc.Cell(fill=matmod)
cell113.region = -cyl113 & +bndw
cell114 = openmc.Cell(fill=matclad)
cell114.region = +cyl113 & -cyl114 & +bndw
cell115 = openmc.Cell(fill=matcool)
cell115.region = +cyl114 & +bndw & -px1 & -py3 & +py4
biguni.add_cell(cell113)
biguni.add_cell(cell114)
biguni.add_cell(cell115)
# rod number (10,12)
x=  1.260000
y=  6.970000
cyl116 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl117 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl118 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl119 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell116 = openmc.Cell(fill=matfuel01)
cell116.region = -cyl116
fuel_cell_list.append(cell116.id)
cell117 = openmc.Cell(fill=matifba)
cell117.region = +cyl116 & -cyl117
cell118 = openmc.Cell(fill=matair)
cell118.region = +cyl117 & -cyl118
cell119 = openmc.Cell(fill=matclad)
cell119.region = +cyl118 & -cyl119
cell120 = openmc.Cell(fill=matcool)
cell120.region = +cyl119 & +px1 & -px2 & -py3 & +py4
biguni.add_cell(cell116)
biguni.add_cell(cell117)
biguni.add_cell(cell118)
biguni.add_cell(cell119)
biguni.add_cell(cell120)
# rod number (11,12)
x=  2.520000
y=  6.970000
cyl121 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl122 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl123 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell121 = openmc.Cell(fill=matfuel01)
cell121.region = -cyl121
fuel_cell_list.append(cell121.id)
cell122 = openmc.Cell(fill=matair)
cell122.region = +cyl121 & -cyl122
cell123 = openmc.Cell(fill=matclad)
cell123.region = +cyl122 & -cyl123
cell124 = openmc.Cell(fill=matcool)
cell124.region = +cyl123 & +px2 & -px3 & -py3 & +py4
biguni.add_cell(cell121)
biguni.add_cell(cell122)
biguni.add_cell(cell123)
biguni.add_cell(cell124)
# rod number (12,12)
x=  3.780000
y=  6.970000
cyl125 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl126 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell125 = openmc.Cell(fill=matmod)
cell125.region = -cyl125
cell126 = openmc.Cell(fill=matclad)
cell126.region = +cyl125 & -cyl126
cell127 = openmc.Cell(fill=matcool)
cell127.region = +cyl126 & +px3 & -px4 & -py3 & +py4
biguni.add_cell(cell125)
biguni.add_cell(cell126)
biguni.add_cell(cell127)
# rod number (13,12)
x=  5.040000
y=  6.970000
cyl128 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl129 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl130 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl131 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell128 = openmc.Cell(fill=matfuel01)
cell128.region = -cyl128
fuel_cell_list.append(cell128.id)
cell129 = openmc.Cell(fill=matifba)
cell129.region = +cyl128 & -cyl129
cell130 = openmc.Cell(fill=matair)
cell130.region = +cyl129 & -cyl130
cell131 = openmc.Cell(fill=matclad)
cell131.region = +cyl130 & -cyl131
cell132 = openmc.Cell(fill=matcool)
cell132.region = +cyl131 & +px4 & -px5 & -py3 & +py4
biguni.add_cell(cell128)
biguni.add_cell(cell129)
biguni.add_cell(cell130)
biguni.add_cell(cell131)
biguni.add_cell(cell132)
# rod number (14,12)
x=  6.300000
y=  6.970000
cyl133 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl134 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl135 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl136 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell133 = openmc.Cell(fill=matfuel01)
cell133.region = -cyl133
fuel_cell_list.append(cell133.id)
cell134 = openmc.Cell(fill=matifba)
cell134.region = +cyl133 & -cyl134
cell135 = openmc.Cell(fill=matair)
cell135.region = +cyl134 & -cyl135
cell136 = openmc.Cell(fill=matclad)
cell136.region = +cyl135 & -cyl136
cell137 = openmc.Cell(fill=matcool)
cell137.region = +cyl136 & +px5 & -px6 & -py3 & +py4
biguni.add_cell(cell133)
biguni.add_cell(cell134)
biguni.add_cell(cell135)
biguni.add_cell(cell136)
biguni.add_cell(cell137)
# rod number (15,12)
x=  7.560000
y=  6.970000
cyl138 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl139 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell138 = openmc.Cell(fill=matmod)
cell138.region = -cyl138
cell139 = openmc.Cell(fill=matclad)
cell139.region = +cyl138 & -cyl139
cell140 = openmc.Cell(fill=matcool)
cell140.region = +cyl139 & +px6 & -px7 & -py3 & +py4
biguni.add_cell(cell138)
biguni.add_cell(cell139)
biguni.add_cell(cell140)
# rod number (16,12)
x=  8.820000
y=  6.970000
cyl141 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl142 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl143 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl144 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell141 = openmc.Cell(fill=matfuel01)
cell141.region = -cyl141
fuel_cell_list.append(cell141.id)
cell142 = openmc.Cell(fill=matifba)
cell142.region = +cyl141 & -cyl142
cell143 = openmc.Cell(fill=matair)
cell143.region = +cyl142 & -cyl143
cell144 = openmc.Cell(fill=matclad)
cell144.region = +cyl143 & -cyl144
cell145 = openmc.Cell(fill=matcool)
cell145.region = +cyl144 & +px7 & -px8 & -py3 & +py4
biguni.add_cell(cell141)
biguni.add_cell(cell142)
biguni.add_cell(cell143)
biguni.add_cell(cell144)
biguni.add_cell(cell145)
# rod number (17,12)
x= 10.080000
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
cell149.region = +cyl148 & +px8 & -bnde & -py3 & +py4
biguni.add_cell(cell146)
biguni.add_cell(cell147)
biguni.add_cell(cell148)
biguni.add_cell(cell149)
# rod number (9,13)
x=  0.000000
y=  5.710000
cyl150 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl151 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl152 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl153 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell150 = openmc.Cell(fill=matfuel01)
cell150.region = -cyl150 & +bndw
fuel_cell_list.append(cell150.id)
cell151 = openmc.Cell(fill=matifba)
cell151.region = +cyl150 & -cyl151 & +bndw
cell152 = openmc.Cell(fill=matair)
cell152.region = +cyl151 & -cyl152 & +bndw
cell153 = openmc.Cell(fill=matclad)
cell153.region = +cyl152 & -cyl153 & +bndw
cell154 = openmc.Cell(fill=matcool)
cell154.region = +cyl153 & +bndw & -px1 & -py4 & +py5
biguni.add_cell(cell150)
biguni.add_cell(cell151)
biguni.add_cell(cell152)
biguni.add_cell(cell153)
biguni.add_cell(cell154)
# rod number (10,13)
x=  1.260000
y=  5.710000
cyl155 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl156 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl157 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell155 = openmc.Cell(fill=matfuel01)
cell155.region = -cyl155
fuel_cell_list.append(cell155.id)
cell156 = openmc.Cell(fill=matair)
cell156.region = +cyl155 & -cyl156
cell157 = openmc.Cell(fill=matclad)
cell157.region = +cyl156 & -cyl157
cell158 = openmc.Cell(fill=matcool)
cell158.region = +cyl157 & +px1 & -px2 & -py4 & +py5
biguni.add_cell(cell155)
biguni.add_cell(cell156)
biguni.add_cell(cell157)
biguni.add_cell(cell158)
# rod number (11,13)
x=  2.520000
y=  5.710000
cyl159 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl160 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl161 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell159 = openmc.Cell(fill=matfuel01)
cell159.region = -cyl159
fuel_cell_list.append(cell159.id)
cell160 = openmc.Cell(fill=matair)
cell160.region = +cyl159 & -cyl160
cell161 = openmc.Cell(fill=matclad)
cell161.region = +cyl160 & -cyl161
cell162 = openmc.Cell(fill=matcool)
cell162.region = +cyl161 & +px2 & -px3 & -py4 & +py5
biguni.add_cell(cell159)
biguni.add_cell(cell160)
biguni.add_cell(cell161)
biguni.add_cell(cell162)
# rod number (12,13)
x=  3.780000
y=  5.710000
cyl163 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl164 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl165 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl166 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell163 = openmc.Cell(fill=matfuel01)
cell163.region = -cyl163
fuel_cell_list.append(cell163.id)
cell164 = openmc.Cell(fill=matifba)
cell164.region = +cyl163 & -cyl164
cell165 = openmc.Cell(fill=matair)
cell165.region = +cyl164 & -cyl165
cell166 = openmc.Cell(fill=matclad)
cell166.region = +cyl165 & -cyl166
cell167 = openmc.Cell(fill=matcool)
cell167.region = +cyl166 & +px3 & -px4 & -py4 & +py5
biguni.add_cell(cell163)
biguni.add_cell(cell164)
biguni.add_cell(cell165)
biguni.add_cell(cell166)
biguni.add_cell(cell167)
# rod number (13,13)
x=  5.040000
y=  5.710000
cyl168 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl169 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl170 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell168 = openmc.Cell(fill=matfuel01)
cell168.region = -cyl168
fuel_cell_list.append(cell168.id)
cell169 = openmc.Cell(fill=matair)
cell169.region = +cyl168 & -cyl169
cell170 = openmc.Cell(fill=matclad)
cell170.region = +cyl169 & -cyl170
cell171 = openmc.Cell(fill=matcool)
cell171.region = +cyl170 & +px4 & -px5 & -py4 & +py5
biguni.add_cell(cell168)
biguni.add_cell(cell169)
biguni.add_cell(cell170)
biguni.add_cell(cell171)
# rod number (14,13)
x=  6.300000
y=  5.710000
cyl172 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl173 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl174 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl175 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell172 = openmc.Cell(fill=matfuel01)
cell172.region = -cyl172
fuel_cell_list.append(cell172.id)
cell173 = openmc.Cell(fill=matifba)
cell173.region = +cyl172 & -cyl173
cell174 = openmc.Cell(fill=matair)
cell174.region = +cyl173 & -cyl174
cell175 = openmc.Cell(fill=matclad)
cell175.region = +cyl174 & -cyl175
cell176 = openmc.Cell(fill=matcool)
cell176.region = +cyl175 & +px5 & -px6 & -py4 & +py5
biguni.add_cell(cell172)
biguni.add_cell(cell173)
biguni.add_cell(cell174)
biguni.add_cell(cell175)
biguni.add_cell(cell176)
# rod number (15,13)
x=  7.560000
y=  5.710000
cyl177 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl178 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl179 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl180 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell177 = openmc.Cell(fill=matfuel01)
cell177.region = -cyl177
fuel_cell_list.append(cell177.id)
cell178 = openmc.Cell(fill=matifba)
cell178.region = +cyl177 & -cyl178
cell179 = openmc.Cell(fill=matair)
cell179.region = +cyl178 & -cyl179
cell180 = openmc.Cell(fill=matclad)
cell180.region = +cyl179 & -cyl180
cell181 = openmc.Cell(fill=matcool)
cell181.region = +cyl180 & +px6 & -px7 & -py4 & +py5
biguni.add_cell(cell177)
biguni.add_cell(cell178)
biguni.add_cell(cell179)
biguni.add_cell(cell180)
biguni.add_cell(cell181)
# rod number (16,13)
x=  8.820000
y=  5.710000
cyl182 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl183 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl184 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell182 = openmc.Cell(fill=matfuel01)
cell182.region = -cyl182
fuel_cell_list.append(cell182.id)
cell183 = openmc.Cell(fill=matair)
cell183.region = +cyl182 & -cyl183
cell184 = openmc.Cell(fill=matclad)
cell184.region = +cyl183 & -cyl184
cell185 = openmc.Cell(fill=matcool)
cell185.region = +cyl184 & +px7 & -px8 & -py4 & +py5
biguni.add_cell(cell182)
biguni.add_cell(cell183)
biguni.add_cell(cell184)
biguni.add_cell(cell185)
# rod number (17,13)
x= 10.080000
y=  5.710000
cyl186 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl187 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl188 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell186 = openmc.Cell(fill=matfuel01)
cell186.region = -cyl186
fuel_cell_list.append(cell186.id)
cell187 = openmc.Cell(fill=matair)
cell187.region = +cyl186 & -cyl187
cell188 = openmc.Cell(fill=matclad)
cell188.region = +cyl187 & -cyl188
cell189 = openmc.Cell(fill=matcool)
cell189.region = +cyl188 & +px8 & -bnde & -py4 & +py5
biguni.add_cell(cell186)
biguni.add_cell(cell187)
biguni.add_cell(cell188)
biguni.add_cell(cell189)
# rod number (9,14)
x=  0.000000
y=  4.450000
cyl190 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl191 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl192 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell190 = openmc.Cell(fill=matfuel01)
cell190.region = -cyl190 & +bndw
fuel_cell_list.append(cell190.id)
cell191 = openmc.Cell(fill=matair)
cell191.region = +cyl190 & -cyl191 & +bndw
cell192 = openmc.Cell(fill=matclad)
cell192.region = +cyl191 & -cyl192 & +bndw
cell193 = openmc.Cell(fill=matcool)
cell193.region = +cyl192 & +bndw & -px1 & -py5 & +py6
biguni.add_cell(cell190)
biguni.add_cell(cell191)
biguni.add_cell(cell192)
biguni.add_cell(cell193)
# rod number (10,14)
x=  1.260000
y=  4.450000
cyl194 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl195 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl196 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell194 = openmc.Cell(fill=matfuel01)
cell194.region = -cyl194
fuel_cell_list.append(cell194.id)
cell195 = openmc.Cell(fill=matair)
cell195.region = +cyl194 & -cyl195
cell196 = openmc.Cell(fill=matclad)
cell196.region = +cyl195 & -cyl196
cell197 = openmc.Cell(fill=matcool)
cell197.region = +cyl196 & +px1 & -px2 & -py5 & +py6
biguni.add_cell(cell194)
biguni.add_cell(cell195)
biguni.add_cell(cell196)
biguni.add_cell(cell197)
# rod number (11,14)
x=  2.520000
y=  4.450000
cyl198 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl199 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl200 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell198 = openmc.Cell(fill=matfuel01)
cell198.region = -cyl198
fuel_cell_list.append(cell198.id)
cell199 = openmc.Cell(fill=matair)
cell199.region = +cyl198 & -cyl199
cell200 = openmc.Cell(fill=matclad)
cell200.region = +cyl199 & -cyl200
cell201 = openmc.Cell(fill=matcool)
cell201.region = +cyl200 & +px2 & -px3 & -py5 & +py6
biguni.add_cell(cell198)
biguni.add_cell(cell199)
biguni.add_cell(cell200)
biguni.add_cell(cell201)
# rod number (12,14)
x=  3.780000
y=  4.450000
cyl202 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl203 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl204 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl205 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell202 = openmc.Cell(fill=matfuel01)
cell202.region = -cyl202
fuel_cell_list.append(cell202.id)
cell203 = openmc.Cell(fill=matifba)
cell203.region = +cyl202 & -cyl203
cell204 = openmc.Cell(fill=matair)
cell204.region = +cyl203 & -cyl204
cell205 = openmc.Cell(fill=matclad)
cell205.region = +cyl204 & -cyl205
cell206 = openmc.Cell(fill=matcool)
cell206.region = +cyl205 & +px3 & -px4 & -py5 & +py6
biguni.add_cell(cell202)
biguni.add_cell(cell203)
biguni.add_cell(cell204)
biguni.add_cell(cell205)
biguni.add_cell(cell206)
# rod number (13,14)
x=  5.040000
y=  4.450000
cyl207 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl208 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl209 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl210 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell207 = openmc.Cell(fill=matfuel01)
cell207.region = -cyl207
fuel_cell_list.append(cell207.id)
cell208 = openmc.Cell(fill=matifba)
cell208.region = +cyl207 & -cyl208
cell209 = openmc.Cell(fill=matair)
cell209.region = +cyl208 & -cyl209
cell210 = openmc.Cell(fill=matclad)
cell210.region = +cyl209 & -cyl210
cell211 = openmc.Cell(fill=matcool)
cell211.region = +cyl210 & +px4 & -px5 & -py5 & +py6
biguni.add_cell(cell207)
biguni.add_cell(cell208)
biguni.add_cell(cell209)
biguni.add_cell(cell210)
biguni.add_cell(cell211)
# rod number (14,14)
x=  6.300000
y=  4.450000
cyl212 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl213 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell212 = openmc.Cell(fill=matmod)
cell212.region = -cyl212
cell213 = openmc.Cell(fill=matclad)
cell213.region = +cyl212 & -cyl213
cell214 = openmc.Cell(fill=matcool)
cell214.region = +cyl213 & +px5 & -px6 & -py5 & +py6
biguni.add_cell(cell212)
biguni.add_cell(cell213)
biguni.add_cell(cell214)
# rod number (15,14)
x=  7.560000
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
cell218.region = +cyl217 & +px6 & -px7 & -py5 & +py6
biguni.add_cell(cell215)
biguni.add_cell(cell216)
biguni.add_cell(cell217)
biguni.add_cell(cell218)
# rod number (16,14)
x=  8.820000
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
cell222.region = +cyl221 & +px7 & -px8 & -py5 & +py6
biguni.add_cell(cell219)
biguni.add_cell(cell220)
biguni.add_cell(cell221)
biguni.add_cell(cell222)
# rod number (17,14)
x= 10.080000
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
cell226.region = +cyl225 & +px8 & -bnde & -py5 & +py6
biguni.add_cell(cell223)
biguni.add_cell(cell224)
biguni.add_cell(cell225)
biguni.add_cell(cell226)
# rod number (9,15)
x=  0.000000
y=  3.190000
cyl227 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl228 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell227 = openmc.Cell(fill=matmod)
cell227.region = -cyl227 & +bndw
cell228 = openmc.Cell(fill=matclad)
cell228.region = +cyl227 & -cyl228 & +bndw
cell229 = openmc.Cell(fill=matcool)
cell229.region = +cyl228 & +bndw & -px1 & -py6 & +py7
biguni.add_cell(cell227)
biguni.add_cell(cell228)
biguni.add_cell(cell229)
# rod number (10,15)
x=  1.260000
y=  3.190000
cyl230 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl231 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl232 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl233 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell230 = openmc.Cell(fill=matfuel01)
cell230.region = -cyl230
fuel_cell_list.append(cell230.id)
cell231 = openmc.Cell(fill=matifba)
cell231.region = +cyl230 & -cyl231
cell232 = openmc.Cell(fill=matair)
cell232.region = +cyl231 & -cyl232
cell233 = openmc.Cell(fill=matclad)
cell233.region = +cyl232 & -cyl233
cell234 = openmc.Cell(fill=matcool)
cell234.region = +cyl233 & +px1 & -px2 & -py6 & +py7
biguni.add_cell(cell230)
biguni.add_cell(cell231)
biguni.add_cell(cell232)
biguni.add_cell(cell233)
biguni.add_cell(cell234)
# rod number (11,15)
x=  2.520000
y=  3.190000
cyl235 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl236 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl237 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell235 = openmc.Cell(fill=matfuel01)
cell235.region = -cyl235
fuel_cell_list.append(cell235.id)
cell236 = openmc.Cell(fill=matair)
cell236.region = +cyl235 & -cyl236
cell237 = openmc.Cell(fill=matclad)
cell237.region = +cyl236 & -cyl237
cell238 = openmc.Cell(fill=matcool)
cell238.region = +cyl237 & +px2 & -px3 & -py6 & +py7
biguni.add_cell(cell235)
biguni.add_cell(cell236)
biguni.add_cell(cell237)
biguni.add_cell(cell238)
# rod number (12,15)
x=  3.780000
y=  3.190000
cyl239 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl240 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell239 = openmc.Cell(fill=matmod)
cell239.region = -cyl239
cell240 = openmc.Cell(fill=matclad)
cell240.region = +cyl239 & -cyl240
cell241 = openmc.Cell(fill=matcool)
cell241.region = +cyl240 & +px3 & -px4 & -py6 & +py7
biguni.add_cell(cell239)
biguni.add_cell(cell240)
biguni.add_cell(cell241)
# rod number (13,15)
x=  5.040000
y=  3.190000
cyl242 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl243 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl244 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl245 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell242 = openmc.Cell(fill=matfuel01)
cell242.region = -cyl242
fuel_cell_list.append(cell242.id)
cell243 = openmc.Cell(fill=matifba)
cell243.region = +cyl242 & -cyl243
cell244 = openmc.Cell(fill=matair)
cell244.region = +cyl243 & -cyl244
cell245 = openmc.Cell(fill=matclad)
cell245.region = +cyl244 & -cyl245
cell246 = openmc.Cell(fill=matcool)
cell246.region = +cyl245 & +px4 & -px5 & -py6 & +py7
biguni.add_cell(cell242)
biguni.add_cell(cell243)
biguni.add_cell(cell244)
biguni.add_cell(cell245)
biguni.add_cell(cell246)
# rod number (14,15)
x=  6.300000
y=  3.190000
cyl247 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl248 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl249 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell247 = openmc.Cell(fill=matfuel01)
cell247.region = -cyl247
fuel_cell_list.append(cell247.id)
cell248 = openmc.Cell(fill=matair)
cell248.region = +cyl247 & -cyl248
cell249 = openmc.Cell(fill=matclad)
cell249.region = +cyl248 & -cyl249
cell250 = openmc.Cell(fill=matcool)
cell250.region = +cyl249 & +px5 & -px6 & -py6 & +py7
biguni.add_cell(cell247)
biguni.add_cell(cell248)
biguni.add_cell(cell249)
biguni.add_cell(cell250)
# rod number (15,15)
x=  7.560000
y=  3.190000
cyl251 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl252 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl253 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl254 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell251 = openmc.Cell(fill=matfuel01)
cell251.region = -cyl251
fuel_cell_list.append(cell251.id)
cell252 = openmc.Cell(fill=matifba)
cell252.region = +cyl251 & -cyl252
cell253 = openmc.Cell(fill=matair)
cell253.region = +cyl252 & -cyl253
cell254 = openmc.Cell(fill=matclad)
cell254.region = +cyl253 & -cyl254
cell255 = openmc.Cell(fill=matcool)
cell255.region = +cyl254 & +px6 & -px7 & -py6 & +py7
biguni.add_cell(cell251)
biguni.add_cell(cell252)
biguni.add_cell(cell253)
biguni.add_cell(cell254)
biguni.add_cell(cell255)
# rod number (16,15)
x=  8.820000
y=  3.190000
cyl256 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl257 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl258 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell256 = openmc.Cell(fill=matfuel01)
cell256.region = -cyl256
fuel_cell_list.append(cell256.id)
cell257 = openmc.Cell(fill=matair)
cell257.region = +cyl256 & -cyl257
cell258 = openmc.Cell(fill=matclad)
cell258.region = +cyl257 & -cyl258
cell259 = openmc.Cell(fill=matcool)
cell259.region = +cyl258 & +px7 & -px8 & -py6 & +py7
biguni.add_cell(cell256)
biguni.add_cell(cell257)
biguni.add_cell(cell258)
biguni.add_cell(cell259)
# rod number (17,15)
x= 10.080000
y=  3.190000
cyl260 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl261 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl262 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell260 = openmc.Cell(fill=matfuel01)
cell260.region = -cyl260
fuel_cell_list.append(cell260.id)
cell261 = openmc.Cell(fill=matair)
cell261.region = +cyl260 & -cyl261
cell262 = openmc.Cell(fill=matclad)
cell262.region = +cyl261 & -cyl262
cell263 = openmc.Cell(fill=matcool)
cell263.region = +cyl262 & +px8 & -bnde & -py6 & +py7
biguni.add_cell(cell260)
biguni.add_cell(cell261)
biguni.add_cell(cell262)
biguni.add_cell(cell263)
# rod number (9,16)
x=  0.000000
y=  1.930000
cyl264 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl265 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl266 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl267 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell264 = openmc.Cell(fill=matfuel01)
cell264.region = -cyl264 & +bndw
fuel_cell_list.append(cell264.id)
cell265 = openmc.Cell(fill=matifba)
cell265.region = +cyl264 & -cyl265 & +bndw
cell266 = openmc.Cell(fill=matair)
cell266.region = +cyl265 & -cyl266 & +bndw
cell267 = openmc.Cell(fill=matclad)
cell267.region = +cyl266 & -cyl267 & +bndw
cell268 = openmc.Cell(fill=matcool)
cell268.region = +cyl267 & +bndw & -px1 & -py7 & +py8
biguni.add_cell(cell264)
biguni.add_cell(cell265)
biguni.add_cell(cell266)
biguni.add_cell(cell267)
biguni.add_cell(cell268)
# rod number (10,16)
x=  1.260000
y=  1.930000
cyl269 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl270 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl271 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell269 = openmc.Cell(fill=matfuel01)
cell269.region = -cyl269
fuel_cell_list.append(cell269.id)
cell270 = openmc.Cell(fill=matair)
cell270.region = +cyl269 & -cyl270
cell271 = openmc.Cell(fill=matclad)
cell271.region = +cyl270 & -cyl271
cell272 = openmc.Cell(fill=matcool)
cell272.region = +cyl271 & +px1 & -px2 & -py7 & +py8
biguni.add_cell(cell269)
biguni.add_cell(cell270)
biguni.add_cell(cell271)
biguni.add_cell(cell272)
# rod number (11,16)
x=  2.520000
y=  1.930000
cyl273 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl274 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl275 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell273 = openmc.Cell(fill=matfuel01)
cell273.region = -cyl273
fuel_cell_list.append(cell273.id)
cell274 = openmc.Cell(fill=matair)
cell274.region = +cyl273 & -cyl274
cell275 = openmc.Cell(fill=matclad)
cell275.region = +cyl274 & -cyl275
cell276 = openmc.Cell(fill=matcool)
cell276.region = +cyl275 & +px2 & -px3 & -py7 & +py8
biguni.add_cell(cell273)
biguni.add_cell(cell274)
biguni.add_cell(cell275)
biguni.add_cell(cell276)
# rod number (12,16)
x=  3.780000
y=  1.930000
cyl277 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl278 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl279 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl280 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell277 = openmc.Cell(fill=matfuel01)
cell277.region = -cyl277
fuel_cell_list.append(cell277.id)
cell278 = openmc.Cell(fill=matifba)
cell278.region = +cyl277 & -cyl278
cell279 = openmc.Cell(fill=matair)
cell279.region = +cyl278 & -cyl279
cell280 = openmc.Cell(fill=matclad)
cell280.region = +cyl279 & -cyl280
cell281 = openmc.Cell(fill=matcool)
cell281.region = +cyl280 & +px3 & -px4 & -py7 & +py8
biguni.add_cell(cell277)
biguni.add_cell(cell278)
biguni.add_cell(cell279)
biguni.add_cell(cell280)
biguni.add_cell(cell281)
# rod number (13,16)
x=  5.040000
y=  1.930000
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
cell285.region = +cyl284 & +px4 & -px5 & -py7 & +py8
biguni.add_cell(cell282)
biguni.add_cell(cell283)
biguni.add_cell(cell284)
biguni.add_cell(cell285)
# rod number (14,16)
x=  6.300000
y=  1.930000
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
cell289.region = +cyl288 & +px5 & -px6 & -py7 & +py8
biguni.add_cell(cell286)
biguni.add_cell(cell287)
biguni.add_cell(cell288)
biguni.add_cell(cell289)
# rod number (15,16)
x=  7.560000
y=  1.930000
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
cell293.region = +cyl292 & +px6 & -px7 & -py7 & +py8
biguni.add_cell(cell290)
biguni.add_cell(cell291)
biguni.add_cell(cell292)
biguni.add_cell(cell293)
# rod number (16,16)
x=  8.820000
y=  1.930000
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
cell297.region = +cyl296 & +px7 & -px8 & -py7 & +py8
biguni.add_cell(cell294)
biguni.add_cell(cell295)
biguni.add_cell(cell296)
biguni.add_cell(cell297)
# rod number (17,16)
x= 10.080000
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
cell301.region = +cyl300 & +px8 & -bnde & -py7 & +py8
biguni.add_cell(cell298)
biguni.add_cell(cell299)
biguni.add_cell(cell300)
biguni.add_cell(cell301)
# rod number (9,17)
x=  0.000000
y=  0.670000
cyl302 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl303 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl304 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell302 = openmc.Cell(fill=matfuel01)
cell302.region = -cyl302 & +bndw
fuel_cell_list.append(cell302.id)
cell303 = openmc.Cell(fill=matair)
cell303.region = +cyl302 & -cyl303 & +bndw
cell304 = openmc.Cell(fill=matclad)
cell304.region = +cyl303 & -cyl304 & +bndw
cell305 = openmc.Cell(fill=matcool)
cell305.region = +cyl304 & +bndw & -px1 & -py8 & +bnds
biguni.add_cell(cell302)
biguni.add_cell(cell303)
biguni.add_cell(cell304)
biguni.add_cell(cell305)
# rod number (10,17)
x=  1.260000
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
cell309.region = +cyl308 & +px1 & -px2 & -py8 & +bnds
biguni.add_cell(cell306)
biguni.add_cell(cell307)
biguni.add_cell(cell308)
biguni.add_cell(cell309)
# rod number (11,17)
x=  2.520000
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
cell313.region = +cyl312 & +px2 & -px3 & -py8 & +bnds
biguni.add_cell(cell310)
biguni.add_cell(cell311)
biguni.add_cell(cell312)
biguni.add_cell(cell313)
# rod number (12,17)
x=  3.780000
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
cell317.region = +cyl316 & +px3 & -px4 & -py8 & +bnds
biguni.add_cell(cell314)
biguni.add_cell(cell315)
biguni.add_cell(cell316)
biguni.add_cell(cell317)
# rod number (13,17)
x=  5.040000
y=  0.670000
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
cell321.region = +cyl320 & +px4 & -px5 & -py8 & +bnds
biguni.add_cell(cell318)
biguni.add_cell(cell319)
biguni.add_cell(cell320)
biguni.add_cell(cell321)
# rod number (14,17)
x=  6.300000
y=  0.670000
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
cell325.region = +cyl324 & +px5 & -px6 & -py8 & +bnds
biguni.add_cell(cell322)
biguni.add_cell(cell323)
biguni.add_cell(cell324)
biguni.add_cell(cell325)
# rod number (15,17)
x=  7.560000
y=  0.670000
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
cell329.region = +cyl328 & +px6 & -px7 & -py8 & +bnds
biguni.add_cell(cell326)
biguni.add_cell(cell327)
biguni.add_cell(cell328)
biguni.add_cell(cell329)
# rod number (16,17)
x=  8.820000
y=  0.670000
cyl330 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl331 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl332 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell330 = openmc.Cell(fill=matfuel01)
cell330.region = -cyl330
fuel_cell_list.append(cell330.id)
cell331 = openmc.Cell(fill=matair)
cell331.region = +cyl330 & -cyl331
cell332 = openmc.Cell(fill=matclad)
cell332.region = +cyl331 & -cyl332
cell333 = openmc.Cell(fill=matcool)
cell333.region = +cyl332 & +px7 & -px8 & -py8 & +bnds
biguni.add_cell(cell330)
biguni.add_cell(cell331)
biguni.add_cell(cell332)
biguni.add_cell(cell333)
# rod number (17,17)
x= 10.080000
y=  0.670000
cyl334 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl335 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl336 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl337 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell334 = openmc.Cell(fill=matfuel01)
cell334.region = -cyl334
fuel_cell_list.append(cell334.id)
cell335 = openmc.Cell(fill=matifba)
cell335.region = +cyl334 & -cyl335
cell336 = openmc.Cell(fill=matair)
cell336.region = +cyl335 & -cyl336
cell337 = openmc.Cell(fill=matclad)
cell337.region = +cyl336 & -cyl337
cell338 = openmc.Cell(fill=matcool)
cell338.region = +cyl337 & +px8 & -bnde & -py8 & +bnds
biguni.add_cell(cell334)
biguni.add_cell(cell335)
biguni.add_cell(cell336)
biguni.add_cell(cell337)
biguni.add_cell(cell338)

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
