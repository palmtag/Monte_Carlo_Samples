import matplotlib

import openmc
import openmc.mgxs as mgxs
import openmc.data          # need for hdf5

#  To run:
#  >python3 vera2o_gad12.omc
#
# OpenMC Input created by BUNBLD on 08/09/2025 11:48:06
#  VERA Benchmark #2 - Single Assembly
#  Uniform PWR Assembly
#  November 15, 2012
#  Number densities from KENO run
#  VERA Benchmark 2O - like 2A + 12 gad pins
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

# material 2 FUEL02
matfuel02 = openmc.Material(name='fuel02')
matfuel02.add_nuclide('O16',  4.537050E-02)
matfuel02.add_nuclide('Gd152',  3.359600E-06)
matfuel02.add_nuclide('Gd154',  3.661900E-05)
matfuel02.add_nuclide('Gd155',  2.486060E-04)
matfuel02.add_nuclide('Gd156',  3.438490E-04)
matfuel02.add_nuclide('Gd157',  2.628840E-04)
matfuel02.add_nuclide('Gd158',  4.172550E-04)
matfuel02.add_nuclide('Gd160',  3.671980E-04)
matfuel02.add_nuclide('U234',  3.180960E-06)
matfuel02.add_nuclide('U235',  3.905000E-04)
matfuel02.add_nuclide('U236',  1.793000E-06)
matfuel02.add_nuclide('U238',  2.102990E-02)
matfuel02.set_density('g/cm3', 10.11099)
matfuel02.temperature=  600.000

# material 3 CLAD
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

# material 4 COOL
matcool = openmc.Material(name='cool')
matcool.add_nuclide('H1',  4.962240E-02)
matcool.add_nuclide('O16',  2.481120E-02)
matcool.add_nuclide('B10',  1.070700E-05)
matcool.add_nuclide('B11',  4.309710E-05)
matcool.set_density('g/cm3',  0.74300)
matcool.temperature=  600.000
matcool.add_s_alpha_beta('c_H_in_H2O')

# material 5 MOD
matmod = openmc.Material(name='mod')
matmod.add_nuclide('H1',  4.962240E-02)
matmod.add_nuclide('O16',  2.481120E-02)
matmod.add_nuclide('B10',  1.070700E-05)
matmod.add_nuclide('B11',  4.309710E-05)
matmod.set_density('g/cm3',  0.74300)
matmod.temperature=  600.000
matmod.add_s_alpha_beta('c_H_in_H2O')

# material 6 AIR
matair = openmc.Material(name='air')
matair.add_nuclide('He4',  2.687140E-05)
matair.set_density('g/cm3',  0.00018)
matair.temperature=  600.000

# Material mixtures

# Instantiate a Materials collection
model.materials = openmc.Materials([matfuel01,matfuel02,matclad,matcool,matmod,matair])
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
#  1  1  1  1  2  1  1  1  1
#  0  1  1  0  1  1  0  1  1
#  1  1  2  1  1  1  1  1  1
#  1  1  1  1  1  0  1  1  1
#  0  1  1  0  1  1  2  1  1
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
cyl12 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl13 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell12 = openmc.Cell(fill=matmod)
cell12.region = -cyl12 & -bndn
cell13 = openmc.Cell(fill=matclad)
cell13.region = +cyl12 & -cyl13 & -bndn
cell14 = openmc.Cell(fill=matcool)
cell14.region = +cyl13 & +px3 & -px4 & -bndn & +py1
biguni.add_cell(cell12)
biguni.add_cell(cell13)
biguni.add_cell(cell14)
# rod number (13,9)
x=  5.040000
y= 10.750000
cyl15 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl16 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl17 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell15 = openmc.Cell(fill=matfuel01)
cell15.region = -cyl15 & -bndn
fuel_cell_list.append(cell15.id)
cell16 = openmc.Cell(fill=matair)
cell16.region = +cyl15 & -cyl16 & -bndn
cell17 = openmc.Cell(fill=matclad)
cell17.region = +cyl16 & -cyl17 & -bndn
cell18 = openmc.Cell(fill=matcool)
cell18.region = +cyl17 & +px4 & -px5 & -bndn & +py1
biguni.add_cell(cell15)
biguni.add_cell(cell16)
biguni.add_cell(cell17)
biguni.add_cell(cell18)
# rod number (14,9)
x=  6.300000
y= 10.750000
cyl19 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl20 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl21 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell19 = openmc.Cell(fill=matfuel01)
cell19.region = -cyl19 & -bndn
fuel_cell_list.append(cell19.id)
cell20 = openmc.Cell(fill=matair)
cell20.region = +cyl19 & -cyl20 & -bndn
cell21 = openmc.Cell(fill=matclad)
cell21.region = +cyl20 & -cyl21 & -bndn
cell22 = openmc.Cell(fill=matcool)
cell22.region = +cyl21 & +px5 & -px6 & -bndn & +py1
biguni.add_cell(cell19)
biguni.add_cell(cell20)
biguni.add_cell(cell21)
biguni.add_cell(cell22)
# rod number (15,9)
x=  7.560000
y= 10.750000
cyl23 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl24 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell23 = openmc.Cell(fill=matmod)
cell23.region = -cyl23 & -bndn
cell24 = openmc.Cell(fill=matclad)
cell24.region = +cyl23 & -cyl24 & -bndn
cell25 = openmc.Cell(fill=matcool)
cell25.region = +cyl24 & +px6 & -px7 & -bndn & +py1
biguni.add_cell(cell23)
biguni.add_cell(cell24)
biguni.add_cell(cell25)
# rod number (16,9)
x=  8.820000
y= 10.750000
cyl26 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl27 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl28 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell26 = openmc.Cell(fill=matfuel01)
cell26.region = -cyl26 & -bndn
fuel_cell_list.append(cell26.id)
cell27 = openmc.Cell(fill=matair)
cell27.region = +cyl26 & -cyl27 & -bndn
cell28 = openmc.Cell(fill=matclad)
cell28.region = +cyl27 & -cyl28 & -bndn
cell29 = openmc.Cell(fill=matcool)
cell29.region = +cyl28 & +px7 & -px8 & -bndn & +py1
biguni.add_cell(cell26)
biguni.add_cell(cell27)
biguni.add_cell(cell28)
biguni.add_cell(cell29)
# rod number (17,9)
x= 10.080000
y= 10.750000
cyl30 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl31 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl32 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell30 = openmc.Cell(fill=matfuel01)
cell30.region = -cyl30 & -bndn
fuel_cell_list.append(cell30.id)
cell31 = openmc.Cell(fill=matair)
cell31.region = +cyl30 & -cyl31 & -bndn
cell32 = openmc.Cell(fill=matclad)
cell32.region = +cyl31 & -cyl32 & -bndn
cell33 = openmc.Cell(fill=matcool)
cell33.region = +cyl32 & +px8 & -bnde & -bndn & +py1
biguni.add_cell(cell30)
biguni.add_cell(cell31)
biguni.add_cell(cell32)
biguni.add_cell(cell33)
# rod number (9,10)
x=  0.000000
y=  9.490000
cyl34 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl35 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl36 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell34 = openmc.Cell(fill=matfuel01)
cell34.region = -cyl34 & +bndw
fuel_cell_list.append(cell34.id)
cell35 = openmc.Cell(fill=matair)
cell35.region = +cyl34 & -cyl35 & +bndw
cell36 = openmc.Cell(fill=matclad)
cell36.region = +cyl35 & -cyl36 & +bndw
cell37 = openmc.Cell(fill=matcool)
cell37.region = +cyl36 & +bndw & -px1 & -py1 & +py2
biguni.add_cell(cell34)
biguni.add_cell(cell35)
biguni.add_cell(cell36)
biguni.add_cell(cell37)
# rod number (10,10)
x=  1.260000
y=  9.490000
cyl38 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl39 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl40 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell38 = openmc.Cell(fill=matfuel01)
cell38.region = -cyl38
fuel_cell_list.append(cell38.id)
cell39 = openmc.Cell(fill=matair)
cell39.region = +cyl38 & -cyl39
cell40 = openmc.Cell(fill=matclad)
cell40.region = +cyl39 & -cyl40
cell41 = openmc.Cell(fill=matcool)
cell41.region = +cyl40 & +px1 & -px2 & -py1 & +py2
biguni.add_cell(cell38)
biguni.add_cell(cell39)
biguni.add_cell(cell40)
biguni.add_cell(cell41)
# rod number (11,10)
x=  2.520000
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
cell45.region = +cyl44 & +px2 & -px3 & -py1 & +py2
biguni.add_cell(cell42)
biguni.add_cell(cell43)
biguni.add_cell(cell44)
biguni.add_cell(cell45)
# rod number (12,10)
x=  3.780000
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
cell49.region = +cyl48 & +px3 & -px4 & -py1 & +py2
biguni.add_cell(cell46)
biguni.add_cell(cell47)
biguni.add_cell(cell48)
biguni.add_cell(cell49)
# rod number (13,10)
x=  5.040000
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
cell53.region = +cyl52 & +px4 & -px5 & -py1 & +py2
biguni.add_cell(cell50)
biguni.add_cell(cell51)
biguni.add_cell(cell52)
biguni.add_cell(cell53)
# rod number (14,10)
x=  6.300000
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
cell57.region = +cyl56 & +px5 & -px6 & -py1 & +py2
biguni.add_cell(cell54)
biguni.add_cell(cell55)
biguni.add_cell(cell56)
biguni.add_cell(cell57)
# rod number (15,10)
x=  7.560000
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
cell61.region = +cyl60 & +px6 & -px7 & -py1 & +py2
biguni.add_cell(cell58)
biguni.add_cell(cell59)
biguni.add_cell(cell60)
biguni.add_cell(cell61)
# rod number (16,10)
x=  8.820000
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
cell65.region = +cyl64 & +px7 & -px8 & -py1 & +py2
biguni.add_cell(cell62)
biguni.add_cell(cell63)
biguni.add_cell(cell64)
biguni.add_cell(cell65)
# rod number (17,10)
x= 10.080000
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
cell69.region = +cyl68 & +px8 & -bnde & -py1 & +py2
biguni.add_cell(cell66)
biguni.add_cell(cell67)
biguni.add_cell(cell68)
biguni.add_cell(cell69)
# rod number (9,11)
x=  0.000000
y=  8.230000
cyl70 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl71 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl72 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell70 = openmc.Cell(fill=matfuel01)
cell70.region = -cyl70 & +bndw
fuel_cell_list.append(cell70.id)
cell71 = openmc.Cell(fill=matair)
cell71.region = +cyl70 & -cyl71 & +bndw
cell72 = openmc.Cell(fill=matclad)
cell72.region = +cyl71 & -cyl72 & +bndw
cell73 = openmc.Cell(fill=matcool)
cell73.region = +cyl72 & +bndw & -px1 & -py2 & +py3
biguni.add_cell(cell70)
biguni.add_cell(cell71)
biguni.add_cell(cell72)
biguni.add_cell(cell73)
# rod number (10,11)
x=  1.260000
y=  8.230000
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
cell77.region = +cyl76 & +px1 & -px2 & -py2 & +py3
biguni.add_cell(cell74)
biguni.add_cell(cell75)
biguni.add_cell(cell76)
biguni.add_cell(cell77)
# rod number (11,11)
x=  2.520000
y=  8.230000
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
cell81.region = +cyl80 & +px2 & -px3 & -py2 & +py3
biguni.add_cell(cell78)
biguni.add_cell(cell79)
biguni.add_cell(cell80)
biguni.add_cell(cell81)
# rod number (12,11)
x=  3.780000
y=  8.230000
cyl82 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl83 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl84 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell82 = openmc.Cell(fill=matfuel01)
cell82.region = -cyl82
fuel_cell_list.append(cell82.id)
cell83 = openmc.Cell(fill=matair)
cell83.region = +cyl82 & -cyl83
cell84 = openmc.Cell(fill=matclad)
cell84.region = +cyl83 & -cyl84
cell85 = openmc.Cell(fill=matcool)
cell85.region = +cyl84 & +px3 & -px4 & -py2 & +py3
biguni.add_cell(cell82)
biguni.add_cell(cell83)
biguni.add_cell(cell84)
biguni.add_cell(cell85)
# rod number (13,11)
x=  5.040000
y=  8.230000
cyl86 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL02
cyl87 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl88 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell86 = openmc.Cell(fill=matfuel02)
cell86.region = -cyl86
fuel_cell_list.append(cell86.id)
cell87 = openmc.Cell(fill=matair)
cell87.region = +cyl86 & -cyl87
cell88 = openmc.Cell(fill=matclad)
cell88.region = +cyl87 & -cyl88
cell89 = openmc.Cell(fill=matcool)
cell89.region = +cyl88 & +px4 & -px5 & -py2 & +py3
biguni.add_cell(cell86)
biguni.add_cell(cell87)
biguni.add_cell(cell88)
biguni.add_cell(cell89)
# rod number (14,11)
x=  6.300000
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
cell93.region = +cyl92 & +px5 & -px6 & -py2 & +py3
biguni.add_cell(cell90)
biguni.add_cell(cell91)
biguni.add_cell(cell92)
biguni.add_cell(cell93)
# rod number (15,11)
x=  7.560000
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
cell97.region = +cyl96 & +px6 & -px7 & -py2 & +py3
biguni.add_cell(cell94)
biguni.add_cell(cell95)
biguni.add_cell(cell96)
biguni.add_cell(cell97)
# rod number (16,11)
x=  8.820000
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
cell101.region = +cyl100 & +px7 & -px8 & -py2 & +py3
biguni.add_cell(cell98)
biguni.add_cell(cell99)
biguni.add_cell(cell100)
biguni.add_cell(cell101)
# rod number (17,11)
x= 10.080000
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
cell105.region = +cyl104 & +px8 & -bnde & -py2 & +py3
biguni.add_cell(cell102)
biguni.add_cell(cell103)
biguni.add_cell(cell104)
biguni.add_cell(cell105)
# rod number (9,12)
x=  0.000000
y=  6.970000
cyl106 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl107 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell106 = openmc.Cell(fill=matmod)
cell106.region = -cyl106 & +bndw
cell107 = openmc.Cell(fill=matclad)
cell107.region = +cyl106 & -cyl107 & +bndw
cell108 = openmc.Cell(fill=matcool)
cell108.region = +cyl107 & +bndw & -px1 & -py3 & +py4
biguni.add_cell(cell106)
biguni.add_cell(cell107)
biguni.add_cell(cell108)
# rod number (10,12)
x=  1.260000
y=  6.970000
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
cell112.region = +cyl111 & +px1 & -px2 & -py3 & +py4
biguni.add_cell(cell109)
biguni.add_cell(cell110)
biguni.add_cell(cell111)
biguni.add_cell(cell112)
# rod number (11,12)
x=  2.520000
y=  6.970000
cyl113 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl114 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl115 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell113 = openmc.Cell(fill=matfuel01)
cell113.region = -cyl113
fuel_cell_list.append(cell113.id)
cell114 = openmc.Cell(fill=matair)
cell114.region = +cyl113 & -cyl114
cell115 = openmc.Cell(fill=matclad)
cell115.region = +cyl114 & -cyl115
cell116 = openmc.Cell(fill=matcool)
cell116.region = +cyl115 & +px2 & -px3 & -py3 & +py4
biguni.add_cell(cell113)
biguni.add_cell(cell114)
biguni.add_cell(cell115)
biguni.add_cell(cell116)
# rod number (12,12)
x=  3.780000
y=  6.970000
cyl117 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl118 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell117 = openmc.Cell(fill=matmod)
cell117.region = -cyl117
cell118 = openmc.Cell(fill=matclad)
cell118.region = +cyl117 & -cyl118
cell119 = openmc.Cell(fill=matcool)
cell119.region = +cyl118 & +px3 & -px4 & -py3 & +py4
biguni.add_cell(cell117)
biguni.add_cell(cell118)
biguni.add_cell(cell119)
# rod number (13,12)
x=  5.040000
y=  6.970000
cyl120 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl121 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl122 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell120 = openmc.Cell(fill=matfuel01)
cell120.region = -cyl120
fuel_cell_list.append(cell120.id)
cell121 = openmc.Cell(fill=matair)
cell121.region = +cyl120 & -cyl121
cell122 = openmc.Cell(fill=matclad)
cell122.region = +cyl121 & -cyl122
cell123 = openmc.Cell(fill=matcool)
cell123.region = +cyl122 & +px4 & -px5 & -py3 & +py4
biguni.add_cell(cell120)
biguni.add_cell(cell121)
biguni.add_cell(cell122)
biguni.add_cell(cell123)
# rod number (14,12)
x=  6.300000
y=  6.970000
cyl124 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl125 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl126 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell124 = openmc.Cell(fill=matfuel01)
cell124.region = -cyl124
fuel_cell_list.append(cell124.id)
cell125 = openmc.Cell(fill=matair)
cell125.region = +cyl124 & -cyl125
cell126 = openmc.Cell(fill=matclad)
cell126.region = +cyl125 & -cyl126
cell127 = openmc.Cell(fill=matcool)
cell127.region = +cyl126 & +px5 & -px6 & -py3 & +py4
biguni.add_cell(cell124)
biguni.add_cell(cell125)
biguni.add_cell(cell126)
biguni.add_cell(cell127)
# rod number (15,12)
x=  7.560000
y=  6.970000
cyl128 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl129 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell128 = openmc.Cell(fill=matmod)
cell128.region = -cyl128
cell129 = openmc.Cell(fill=matclad)
cell129.region = +cyl128 & -cyl129
cell130 = openmc.Cell(fill=matcool)
cell130.region = +cyl129 & +px6 & -px7 & -py3 & +py4
biguni.add_cell(cell128)
biguni.add_cell(cell129)
biguni.add_cell(cell130)
# rod number (16,12)
x=  8.820000
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
cell134.region = +cyl133 & +px7 & -px8 & -py3 & +py4
biguni.add_cell(cell131)
biguni.add_cell(cell132)
biguni.add_cell(cell133)
biguni.add_cell(cell134)
# rod number (17,12)
x= 10.080000
y=  6.970000
cyl135 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl136 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl137 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell135 = openmc.Cell(fill=matfuel01)
cell135.region = -cyl135
fuel_cell_list.append(cell135.id)
cell136 = openmc.Cell(fill=matair)
cell136.region = +cyl135 & -cyl136
cell137 = openmc.Cell(fill=matclad)
cell137.region = +cyl136 & -cyl137
cell138 = openmc.Cell(fill=matcool)
cell138.region = +cyl137 & +px8 & -bnde & -py3 & +py4
biguni.add_cell(cell135)
biguni.add_cell(cell136)
biguni.add_cell(cell137)
biguni.add_cell(cell138)
# rod number (9,13)
x=  0.000000
y=  5.710000
cyl139 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl140 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl141 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell139 = openmc.Cell(fill=matfuel01)
cell139.region = -cyl139 & +bndw
fuel_cell_list.append(cell139.id)
cell140 = openmc.Cell(fill=matair)
cell140.region = +cyl139 & -cyl140 & +bndw
cell141 = openmc.Cell(fill=matclad)
cell141.region = +cyl140 & -cyl141 & +bndw
cell142 = openmc.Cell(fill=matcool)
cell142.region = +cyl141 & +bndw & -px1 & -py4 & +py5
biguni.add_cell(cell139)
biguni.add_cell(cell140)
biguni.add_cell(cell141)
biguni.add_cell(cell142)
# rod number (10,13)
x=  1.260000
y=  5.710000
cyl143 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl144 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl145 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell143 = openmc.Cell(fill=matfuel01)
cell143.region = -cyl143
fuel_cell_list.append(cell143.id)
cell144 = openmc.Cell(fill=matair)
cell144.region = +cyl143 & -cyl144
cell145 = openmc.Cell(fill=matclad)
cell145.region = +cyl144 & -cyl145
cell146 = openmc.Cell(fill=matcool)
cell146.region = +cyl145 & +px1 & -px2 & -py4 & +py5
biguni.add_cell(cell143)
biguni.add_cell(cell144)
biguni.add_cell(cell145)
biguni.add_cell(cell146)
# rod number (11,13)
x=  2.520000
y=  5.710000
cyl147 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL02
cyl148 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl149 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell147 = openmc.Cell(fill=matfuel02)
cell147.region = -cyl147
fuel_cell_list.append(cell147.id)
cell148 = openmc.Cell(fill=matair)
cell148.region = +cyl147 & -cyl148
cell149 = openmc.Cell(fill=matclad)
cell149.region = +cyl148 & -cyl149
cell150 = openmc.Cell(fill=matcool)
cell150.region = +cyl149 & +px2 & -px3 & -py4 & +py5
biguni.add_cell(cell147)
biguni.add_cell(cell148)
biguni.add_cell(cell149)
biguni.add_cell(cell150)
# rod number (12,13)
x=  3.780000
y=  5.710000
cyl151 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl152 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl153 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell151 = openmc.Cell(fill=matfuel01)
cell151.region = -cyl151
fuel_cell_list.append(cell151.id)
cell152 = openmc.Cell(fill=matair)
cell152.region = +cyl151 & -cyl152
cell153 = openmc.Cell(fill=matclad)
cell153.region = +cyl152 & -cyl153
cell154 = openmc.Cell(fill=matcool)
cell154.region = +cyl153 & +px3 & -px4 & -py4 & +py5
biguni.add_cell(cell151)
biguni.add_cell(cell152)
biguni.add_cell(cell153)
biguni.add_cell(cell154)
# rod number (13,13)
x=  5.040000
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
cell158.region = +cyl157 & +px4 & -px5 & -py4 & +py5
biguni.add_cell(cell155)
biguni.add_cell(cell156)
biguni.add_cell(cell157)
biguni.add_cell(cell158)
# rod number (14,13)
x=  6.300000
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
cell162.region = +cyl161 & +px5 & -px6 & -py4 & +py5
biguni.add_cell(cell159)
biguni.add_cell(cell160)
biguni.add_cell(cell161)
biguni.add_cell(cell162)
# rod number (15,13)
x=  7.560000
y=  5.710000
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
cell166.region = +cyl165 & +px6 & -px7 & -py4 & +py5
biguni.add_cell(cell163)
biguni.add_cell(cell164)
biguni.add_cell(cell165)
biguni.add_cell(cell166)
# rod number (16,13)
x=  8.820000
y=  5.710000
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
cell170.region = +cyl169 & +px7 & -px8 & -py4 & +py5
biguni.add_cell(cell167)
biguni.add_cell(cell168)
biguni.add_cell(cell169)
biguni.add_cell(cell170)
# rod number (17,13)
x= 10.080000
y=  5.710000
cyl171 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl172 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl173 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell171 = openmc.Cell(fill=matfuel01)
cell171.region = -cyl171
fuel_cell_list.append(cell171.id)
cell172 = openmc.Cell(fill=matair)
cell172.region = +cyl171 & -cyl172
cell173 = openmc.Cell(fill=matclad)
cell173.region = +cyl172 & -cyl173
cell174 = openmc.Cell(fill=matcool)
cell174.region = +cyl173 & +px8 & -bnde & -py4 & +py5
biguni.add_cell(cell171)
biguni.add_cell(cell172)
biguni.add_cell(cell173)
biguni.add_cell(cell174)
# rod number (9,14)
x=  0.000000
y=  4.450000
cyl175 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl176 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl177 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell175 = openmc.Cell(fill=matfuel01)
cell175.region = -cyl175 & +bndw
fuel_cell_list.append(cell175.id)
cell176 = openmc.Cell(fill=matair)
cell176.region = +cyl175 & -cyl176 & +bndw
cell177 = openmc.Cell(fill=matclad)
cell177.region = +cyl176 & -cyl177 & +bndw
cell178 = openmc.Cell(fill=matcool)
cell178.region = +cyl177 & +bndw & -px1 & -py5 & +py6
biguni.add_cell(cell175)
biguni.add_cell(cell176)
biguni.add_cell(cell177)
biguni.add_cell(cell178)
# rod number (10,14)
x=  1.260000
y=  4.450000
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
cell182.region = +cyl181 & +px1 & -px2 & -py5 & +py6
biguni.add_cell(cell179)
biguni.add_cell(cell180)
biguni.add_cell(cell181)
biguni.add_cell(cell182)
# rod number (11,14)
x=  2.520000
y=  4.450000
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
cell186.region = +cyl185 & +px2 & -px3 & -py5 & +py6
biguni.add_cell(cell183)
biguni.add_cell(cell184)
biguni.add_cell(cell185)
biguni.add_cell(cell186)
# rod number (12,14)
x=  3.780000
y=  4.450000
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
cell190.region = +cyl189 & +px3 & -px4 & -py5 & +py6
biguni.add_cell(cell187)
biguni.add_cell(cell188)
biguni.add_cell(cell189)
biguni.add_cell(cell190)
# rod number (13,14)
x=  5.040000
y=  4.450000
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
cell194.region = +cyl193 & +px4 & -px5 & -py5 & +py6
biguni.add_cell(cell191)
biguni.add_cell(cell192)
biguni.add_cell(cell193)
biguni.add_cell(cell194)
# rod number (14,14)
x=  6.300000
y=  4.450000
cyl195 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl196 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell195 = openmc.Cell(fill=matmod)
cell195.region = -cyl195
cell196 = openmc.Cell(fill=matclad)
cell196.region = +cyl195 & -cyl196
cell197 = openmc.Cell(fill=matcool)
cell197.region = +cyl196 & +px5 & -px6 & -py5 & +py6
biguni.add_cell(cell195)
biguni.add_cell(cell196)
biguni.add_cell(cell197)
# rod number (15,14)
x=  7.560000
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
cell201.region = +cyl200 & +px6 & -px7 & -py5 & +py6
biguni.add_cell(cell198)
biguni.add_cell(cell199)
biguni.add_cell(cell200)
biguni.add_cell(cell201)
# rod number (16,14)
x=  8.820000
y=  4.450000
cyl202 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl203 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl204 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell202 = openmc.Cell(fill=matfuel01)
cell202.region = -cyl202
fuel_cell_list.append(cell202.id)
cell203 = openmc.Cell(fill=matair)
cell203.region = +cyl202 & -cyl203
cell204 = openmc.Cell(fill=matclad)
cell204.region = +cyl203 & -cyl204
cell205 = openmc.Cell(fill=matcool)
cell205.region = +cyl204 & +px7 & -px8 & -py5 & +py6
biguni.add_cell(cell202)
biguni.add_cell(cell203)
biguni.add_cell(cell204)
biguni.add_cell(cell205)
# rod number (17,14)
x= 10.080000
y=  4.450000
cyl206 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl207 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl208 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell206 = openmc.Cell(fill=matfuel01)
cell206.region = -cyl206
fuel_cell_list.append(cell206.id)
cell207 = openmc.Cell(fill=matair)
cell207.region = +cyl206 & -cyl207
cell208 = openmc.Cell(fill=matclad)
cell208.region = +cyl207 & -cyl208
cell209 = openmc.Cell(fill=matcool)
cell209.region = +cyl208 & +px8 & -bnde & -py5 & +py6
biguni.add_cell(cell206)
biguni.add_cell(cell207)
biguni.add_cell(cell208)
biguni.add_cell(cell209)
# rod number (9,15)
x=  0.000000
y=  3.190000
cyl210 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl211 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell210 = openmc.Cell(fill=matmod)
cell210.region = -cyl210 & +bndw
cell211 = openmc.Cell(fill=matclad)
cell211.region = +cyl210 & -cyl211 & +bndw
cell212 = openmc.Cell(fill=matcool)
cell212.region = +cyl211 & +bndw & -px1 & -py6 & +py7
biguni.add_cell(cell210)
biguni.add_cell(cell211)
biguni.add_cell(cell212)
# rod number (10,15)
x=  1.260000
y=  3.190000
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
cell216.region = +cyl215 & +px1 & -px2 & -py6 & +py7
biguni.add_cell(cell213)
biguni.add_cell(cell214)
biguni.add_cell(cell215)
biguni.add_cell(cell216)
# rod number (11,15)
x=  2.520000
y=  3.190000
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
cell220.region = +cyl219 & +px2 & -px3 & -py6 & +py7
biguni.add_cell(cell217)
biguni.add_cell(cell218)
biguni.add_cell(cell219)
biguni.add_cell(cell220)
# rod number (12,15)
x=  3.780000
y=  3.190000
cyl221 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl222 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell221 = openmc.Cell(fill=matmod)
cell221.region = -cyl221
cell222 = openmc.Cell(fill=matclad)
cell222.region = +cyl221 & -cyl222
cell223 = openmc.Cell(fill=matcool)
cell223.region = +cyl222 & +px3 & -px4 & -py6 & +py7
biguni.add_cell(cell221)
biguni.add_cell(cell222)
biguni.add_cell(cell223)
# rod number (13,15)
x=  5.040000
y=  3.190000
cyl224 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl225 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl226 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell224 = openmc.Cell(fill=matfuel01)
cell224.region = -cyl224
fuel_cell_list.append(cell224.id)
cell225 = openmc.Cell(fill=matair)
cell225.region = +cyl224 & -cyl225
cell226 = openmc.Cell(fill=matclad)
cell226.region = +cyl225 & -cyl226
cell227 = openmc.Cell(fill=matcool)
cell227.region = +cyl226 & +px4 & -px5 & -py6 & +py7
biguni.add_cell(cell224)
biguni.add_cell(cell225)
biguni.add_cell(cell226)
biguni.add_cell(cell227)
# rod number (14,15)
x=  6.300000
y=  3.190000
cyl228 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl229 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl230 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell228 = openmc.Cell(fill=matfuel01)
cell228.region = -cyl228
fuel_cell_list.append(cell228.id)
cell229 = openmc.Cell(fill=matair)
cell229.region = +cyl228 & -cyl229
cell230 = openmc.Cell(fill=matclad)
cell230.region = +cyl229 & -cyl230
cell231 = openmc.Cell(fill=matcool)
cell231.region = +cyl230 & +px5 & -px6 & -py6 & +py7
biguni.add_cell(cell228)
biguni.add_cell(cell229)
biguni.add_cell(cell230)
biguni.add_cell(cell231)
# rod number (15,15)
x=  7.560000
y=  3.190000
cyl232 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL02
cyl233 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl234 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell232 = openmc.Cell(fill=matfuel02)
cell232.region = -cyl232
fuel_cell_list.append(cell232.id)
cell233 = openmc.Cell(fill=matair)
cell233.region = +cyl232 & -cyl233
cell234 = openmc.Cell(fill=matclad)
cell234.region = +cyl233 & -cyl234
cell235 = openmc.Cell(fill=matcool)
cell235.region = +cyl234 & +px6 & -px7 & -py6 & +py7
biguni.add_cell(cell232)
biguni.add_cell(cell233)
biguni.add_cell(cell234)
biguni.add_cell(cell235)
# rod number (16,15)
x=  8.820000
y=  3.190000
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
cell239.region = +cyl238 & +px7 & -px8 & -py6 & +py7
biguni.add_cell(cell236)
biguni.add_cell(cell237)
biguni.add_cell(cell238)
biguni.add_cell(cell239)
# rod number (17,15)
x= 10.080000
y=  3.190000
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
cell243.region = +cyl242 & +px8 & -bnde & -py6 & +py7
biguni.add_cell(cell240)
biguni.add_cell(cell241)
biguni.add_cell(cell242)
biguni.add_cell(cell243)
# rod number (9,16)
x=  0.000000
y=  1.930000
cyl244 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl245 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl246 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell244 = openmc.Cell(fill=matfuel01)
cell244.region = -cyl244 & +bndw
fuel_cell_list.append(cell244.id)
cell245 = openmc.Cell(fill=matair)
cell245.region = +cyl244 & -cyl245 & +bndw
cell246 = openmc.Cell(fill=matclad)
cell246.region = +cyl245 & -cyl246 & +bndw
cell247 = openmc.Cell(fill=matcool)
cell247.region = +cyl246 & +bndw & -px1 & -py7 & +py8
biguni.add_cell(cell244)
biguni.add_cell(cell245)
biguni.add_cell(cell246)
biguni.add_cell(cell247)
# rod number (10,16)
x=  1.260000
y=  1.930000
cyl248 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl249 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl250 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell248 = openmc.Cell(fill=matfuel01)
cell248.region = -cyl248
fuel_cell_list.append(cell248.id)
cell249 = openmc.Cell(fill=matair)
cell249.region = +cyl248 & -cyl249
cell250 = openmc.Cell(fill=matclad)
cell250.region = +cyl249 & -cyl250
cell251 = openmc.Cell(fill=matcool)
cell251.region = +cyl250 & +px1 & -px2 & -py7 & +py8
biguni.add_cell(cell248)
biguni.add_cell(cell249)
biguni.add_cell(cell250)
biguni.add_cell(cell251)
# rod number (11,16)
x=  2.520000
y=  1.930000
cyl252 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl253 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl254 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell252 = openmc.Cell(fill=matfuel01)
cell252.region = -cyl252
fuel_cell_list.append(cell252.id)
cell253 = openmc.Cell(fill=matair)
cell253.region = +cyl252 & -cyl253
cell254 = openmc.Cell(fill=matclad)
cell254.region = +cyl253 & -cyl254
cell255 = openmc.Cell(fill=matcool)
cell255.region = +cyl254 & +px2 & -px3 & -py7 & +py8
biguni.add_cell(cell252)
biguni.add_cell(cell253)
biguni.add_cell(cell254)
biguni.add_cell(cell255)
# rod number (12,16)
x=  3.780000
y=  1.930000
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
cell259.region = +cyl258 & +px3 & -px4 & -py7 & +py8
biguni.add_cell(cell256)
biguni.add_cell(cell257)
biguni.add_cell(cell258)
biguni.add_cell(cell259)
# rod number (13,16)
x=  5.040000
y=  1.930000
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
cell263.region = +cyl262 & +px4 & -px5 & -py7 & +py8
biguni.add_cell(cell260)
biguni.add_cell(cell261)
biguni.add_cell(cell262)
biguni.add_cell(cell263)
# rod number (14,16)
x=  6.300000
y=  1.930000
cyl264 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl265 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl266 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell264 = openmc.Cell(fill=matfuel01)
cell264.region = -cyl264
fuel_cell_list.append(cell264.id)
cell265 = openmc.Cell(fill=matair)
cell265.region = +cyl264 & -cyl265
cell266 = openmc.Cell(fill=matclad)
cell266.region = +cyl265 & -cyl266
cell267 = openmc.Cell(fill=matcool)
cell267.region = +cyl266 & +px5 & -px6 & -py7 & +py8
biguni.add_cell(cell264)
biguni.add_cell(cell265)
biguni.add_cell(cell266)
biguni.add_cell(cell267)
# rod number (15,16)
x=  7.560000
y=  1.930000
cyl268 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl269 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl270 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell268 = openmc.Cell(fill=matfuel01)
cell268.region = -cyl268
fuel_cell_list.append(cell268.id)
cell269 = openmc.Cell(fill=matair)
cell269.region = +cyl268 & -cyl269
cell270 = openmc.Cell(fill=matclad)
cell270.region = +cyl269 & -cyl270
cell271 = openmc.Cell(fill=matcool)
cell271.region = +cyl270 & +px6 & -px7 & -py7 & +py8
biguni.add_cell(cell268)
biguni.add_cell(cell269)
biguni.add_cell(cell270)
biguni.add_cell(cell271)
# rod number (16,16)
x=  8.820000
y=  1.930000
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
cell275.region = +cyl274 & +px7 & -px8 & -py7 & +py8
biguni.add_cell(cell272)
biguni.add_cell(cell273)
biguni.add_cell(cell274)
biguni.add_cell(cell275)
# rod number (17,16)
x= 10.080000
y=  1.930000
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
cell279.region = +cyl278 & +px8 & -bnde & -py7 & +py8
biguni.add_cell(cell276)
biguni.add_cell(cell277)
biguni.add_cell(cell278)
biguni.add_cell(cell279)
# rod number (9,17)
x=  0.000000
y=  0.670000
cyl280 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl281 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl282 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell280 = openmc.Cell(fill=matfuel01)
cell280.region = -cyl280 & +bndw
fuel_cell_list.append(cell280.id)
cell281 = openmc.Cell(fill=matair)
cell281.region = +cyl280 & -cyl281 & +bndw
cell282 = openmc.Cell(fill=matclad)
cell282.region = +cyl281 & -cyl282 & +bndw
cell283 = openmc.Cell(fill=matcool)
cell283.region = +cyl282 & +bndw & -px1 & -py8 & +bnds
biguni.add_cell(cell280)
biguni.add_cell(cell281)
biguni.add_cell(cell282)
biguni.add_cell(cell283)
# rod number (10,17)
x=  1.260000
y=  0.670000
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
cell287.region = +cyl286 & +px1 & -px2 & -py8 & +bnds
biguni.add_cell(cell284)
biguni.add_cell(cell285)
biguni.add_cell(cell286)
biguni.add_cell(cell287)
# rod number (11,17)
x=  2.520000
y=  0.670000
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
cell291.region = +cyl290 & +px2 & -px3 & -py8 & +bnds
biguni.add_cell(cell288)
biguni.add_cell(cell289)
biguni.add_cell(cell290)
biguni.add_cell(cell291)
# rod number (12,17)
x=  3.780000
y=  0.670000
cyl292 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl293 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl294 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell292 = openmc.Cell(fill=matfuel01)
cell292.region = -cyl292
fuel_cell_list.append(cell292.id)
cell293 = openmc.Cell(fill=matair)
cell293.region = +cyl292 & -cyl293
cell294 = openmc.Cell(fill=matclad)
cell294.region = +cyl293 & -cyl294
cell295 = openmc.Cell(fill=matcool)
cell295.region = +cyl294 & +px3 & -px4 & -py8 & +bnds
biguni.add_cell(cell292)
biguni.add_cell(cell293)
biguni.add_cell(cell294)
biguni.add_cell(cell295)
# rod number (13,17)
x=  5.040000
y=  0.670000
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
cell299.region = +cyl298 & +px4 & -px5 & -py8 & +bnds
biguni.add_cell(cell296)
biguni.add_cell(cell297)
biguni.add_cell(cell298)
biguni.add_cell(cell299)
# rod number (14,17)
x=  6.300000
y=  0.670000
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
cell303.region = +cyl302 & +px5 & -px6 & -py8 & +bnds
biguni.add_cell(cell300)
biguni.add_cell(cell301)
biguni.add_cell(cell302)
biguni.add_cell(cell303)
# rod number (15,17)
x=  7.560000
y=  0.670000
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
cell307.region = +cyl306 & +px6 & -px7 & -py8 & +bnds
biguni.add_cell(cell304)
biguni.add_cell(cell305)
biguni.add_cell(cell306)
biguni.add_cell(cell307)
# rod number (16,17)
x=  8.820000
y=  0.670000
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
cell311.region = +cyl310 & +px7 & -px8 & -py8 & +bnds
biguni.add_cell(cell308)
biguni.add_cell(cell309)
biguni.add_cell(cell310)
biguni.add_cell(cell311)
# rod number (17,17)
x= 10.080000
y=  0.670000
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
cell315.region = +cyl314 & +px8 & -bnde & -py8 & +bnds
biguni.add_cell(cell312)
biguni.add_cell(cell313)
biguni.add_cell(cell314)
biguni.add_cell(cell315)

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
