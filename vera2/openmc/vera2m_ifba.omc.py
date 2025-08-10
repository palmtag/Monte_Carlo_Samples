import matplotlib

import openmc
import openmc.mgxs as mgxs
import openmc.data          # need for hdf5

#  To run:
#  >python3 vera2m_ifba.omc
#
# OpenMC Input created by BUNBLD on 08/09/2025 11:48:06
#  VERA Benchmark #2 - Single Assembly
#  Uniform PWR Assembly
#  November 15, 2012
#  Number densities from KENO run
#  VERA Benchmark 2M - like 2A + 128 IFBA pins
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
#  3  8  8  2  8  8  2  8  1  
#  8  1  1  8  1  1  8  1  8  
#  8  1  1  8  1  1  8  1  1  
#  2  8  8  2  8  8  2  8  1  
#  8  1  1  8  1  8  8  1  8  
#  8  1  1  8  8  2  8  1  1  
#  2  8  8  2  8  8  1  8  1  
#  8  1  1  8  1  1  8  1  1  
#  1  8  1  1  8  1  1  1  8  
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
cyl10 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl11 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl12 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell9 = openmc.Cell(fill=matfuel01)
cell9.region = -cyl9 & -bndn
fuel_cell_list.append(cell9.id)
cell10 = openmc.Cell(fill=matifba)
cell10.region = +cyl9 & -cyl10 & -bndn
cell11 = openmc.Cell(fill=matair)
cell11.region = +cyl10 & -cyl11 & -bndn
cell12 = openmc.Cell(fill=matclad)
cell12.region = +cyl11 & -cyl12 & -bndn
cell13 = openmc.Cell(fill=matcool)
cell13.region = +cyl12 & +px2 & -px3 & -bndn & +py1
biguni.add_cell(cell9)
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
cyl18 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl19 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl20 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell17 = openmc.Cell(fill=matfuel01)
cell17.region = -cyl17 & -bndn
fuel_cell_list.append(cell17.id)
cell18 = openmc.Cell(fill=matifba)
cell18.region = +cyl17 & -cyl18 & -bndn
cell19 = openmc.Cell(fill=matair)
cell19.region = +cyl18 & -cyl19 & -bndn
cell20 = openmc.Cell(fill=matclad)
cell20.region = +cyl19 & -cyl20 & -bndn
cell21 = openmc.Cell(fill=matcool)
cell21.region = +cyl20 & +px4 & -px5 & -bndn & +py1
biguni.add_cell(cell17)
biguni.add_cell(cell18)
biguni.add_cell(cell19)
biguni.add_cell(cell20)
biguni.add_cell(cell21)
# rod number (14,9)
x=  6.300000
y= 10.750000
cyl22 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl23 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl24 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl25 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell22 = openmc.Cell(fill=matfuel01)
cell22.region = -cyl22 & -bndn
fuel_cell_list.append(cell22.id)
cell23 = openmc.Cell(fill=matifba)
cell23.region = +cyl22 & -cyl23 & -bndn
cell24 = openmc.Cell(fill=matair)
cell24.region = +cyl23 & -cyl24 & -bndn
cell25 = openmc.Cell(fill=matclad)
cell25.region = +cyl24 & -cyl25 & -bndn
cell26 = openmc.Cell(fill=matcool)
cell26.region = +cyl25 & +px5 & -px6 & -bndn & +py1
biguni.add_cell(cell22)
biguni.add_cell(cell23)
biguni.add_cell(cell24)
biguni.add_cell(cell25)
biguni.add_cell(cell26)
# rod number (15,9)
x=  7.560000
y= 10.750000
cyl27 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl28 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell27 = openmc.Cell(fill=matmod)
cell27.region = -cyl27 & -bndn
cell28 = openmc.Cell(fill=matclad)
cell28.region = +cyl27 & -cyl28 & -bndn
cell29 = openmc.Cell(fill=matcool)
cell29.region = +cyl28 & +px6 & -px7 & -bndn & +py1
biguni.add_cell(cell27)
biguni.add_cell(cell28)
biguni.add_cell(cell29)
# rod number (16,9)
x=  8.820000
y= 10.750000
cyl30 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl31 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl32 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl33 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell30 = openmc.Cell(fill=matfuel01)
cell30.region = -cyl30 & -bndn
fuel_cell_list.append(cell30.id)
cell31 = openmc.Cell(fill=matifba)
cell31.region = +cyl30 & -cyl31 & -bndn
cell32 = openmc.Cell(fill=matair)
cell32.region = +cyl31 & -cyl32 & -bndn
cell33 = openmc.Cell(fill=matclad)
cell33.region = +cyl32 & -cyl33 & -bndn
cell34 = openmc.Cell(fill=matcool)
cell34.region = +cyl33 & +px7 & -px8 & -bndn & +py1
biguni.add_cell(cell30)
biguni.add_cell(cell31)
biguni.add_cell(cell32)
biguni.add_cell(cell33)
biguni.add_cell(cell34)
# rod number (17,9)
x= 10.080000
y= 10.750000
cyl35 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl36 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl37 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell35 = openmc.Cell(fill=matfuel01)
cell35.region = -cyl35 & -bndn
fuel_cell_list.append(cell35.id)
cell36 = openmc.Cell(fill=matair)
cell36.region = +cyl35 & -cyl36 & -bndn
cell37 = openmc.Cell(fill=matclad)
cell37.region = +cyl36 & -cyl37 & -bndn
cell38 = openmc.Cell(fill=matcool)
cell38.region = +cyl37 & +px8 & -bnde & -bndn & +py1
biguni.add_cell(cell35)
biguni.add_cell(cell36)
biguni.add_cell(cell37)
biguni.add_cell(cell38)
# rod number (9,10)
x=  0.000000
y=  9.490000
cyl39 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl40 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl41 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl42 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell39 = openmc.Cell(fill=matfuel01)
cell39.region = -cyl39 & +bndw
fuel_cell_list.append(cell39.id)
cell40 = openmc.Cell(fill=matifba)
cell40.region = +cyl39 & -cyl40 & +bndw
cell41 = openmc.Cell(fill=matair)
cell41.region = +cyl40 & -cyl41 & +bndw
cell42 = openmc.Cell(fill=matclad)
cell42.region = +cyl41 & -cyl42 & +bndw
cell43 = openmc.Cell(fill=matcool)
cell43.region = +cyl42 & +bndw & -px1 & -py1 & +py2
biguni.add_cell(cell39)
biguni.add_cell(cell40)
biguni.add_cell(cell41)
biguni.add_cell(cell42)
biguni.add_cell(cell43)
# rod number (10,10)
x=  1.260000
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
cell47.region = +cyl46 & +px1 & -px2 & -py1 & +py2
biguni.add_cell(cell44)
biguni.add_cell(cell45)
biguni.add_cell(cell46)
biguni.add_cell(cell47)
# rod number (11,10)
x=  2.520000
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
cell51.region = +cyl50 & +px2 & -px3 & -py1 & +py2
biguni.add_cell(cell48)
biguni.add_cell(cell49)
biguni.add_cell(cell50)
biguni.add_cell(cell51)
# rod number (12,10)
x=  3.780000
y=  9.490000
cyl52 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl53 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl54 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl55 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell52 = openmc.Cell(fill=matfuel01)
cell52.region = -cyl52
fuel_cell_list.append(cell52.id)
cell53 = openmc.Cell(fill=matifba)
cell53.region = +cyl52 & -cyl53
cell54 = openmc.Cell(fill=matair)
cell54.region = +cyl53 & -cyl54
cell55 = openmc.Cell(fill=matclad)
cell55.region = +cyl54 & -cyl55
cell56 = openmc.Cell(fill=matcool)
cell56.region = +cyl55 & +px3 & -px4 & -py1 & +py2
biguni.add_cell(cell52)
biguni.add_cell(cell53)
biguni.add_cell(cell54)
biguni.add_cell(cell55)
biguni.add_cell(cell56)
# rod number (13,10)
x=  5.040000
y=  9.490000
cyl57 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl58 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl59 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell57 = openmc.Cell(fill=matfuel01)
cell57.region = -cyl57
fuel_cell_list.append(cell57.id)
cell58 = openmc.Cell(fill=matair)
cell58.region = +cyl57 & -cyl58
cell59 = openmc.Cell(fill=matclad)
cell59.region = +cyl58 & -cyl59
cell60 = openmc.Cell(fill=matcool)
cell60.region = +cyl59 & +px4 & -px5 & -py1 & +py2
biguni.add_cell(cell57)
biguni.add_cell(cell58)
biguni.add_cell(cell59)
biguni.add_cell(cell60)
# rod number (14,10)
x=  6.300000
y=  9.490000
cyl61 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl62 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl63 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell61 = openmc.Cell(fill=matfuel01)
cell61.region = -cyl61
fuel_cell_list.append(cell61.id)
cell62 = openmc.Cell(fill=matair)
cell62.region = +cyl61 & -cyl62
cell63 = openmc.Cell(fill=matclad)
cell63.region = +cyl62 & -cyl63
cell64 = openmc.Cell(fill=matcool)
cell64.region = +cyl63 & +px5 & -px6 & -py1 & +py2
biguni.add_cell(cell61)
biguni.add_cell(cell62)
biguni.add_cell(cell63)
biguni.add_cell(cell64)
# rod number (15,10)
x=  7.560000
y=  9.490000
cyl65 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl66 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl67 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl68 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell65 = openmc.Cell(fill=matfuel01)
cell65.region = -cyl65
fuel_cell_list.append(cell65.id)
cell66 = openmc.Cell(fill=matifba)
cell66.region = +cyl65 & -cyl66
cell67 = openmc.Cell(fill=matair)
cell67.region = +cyl66 & -cyl67
cell68 = openmc.Cell(fill=matclad)
cell68.region = +cyl67 & -cyl68
cell69 = openmc.Cell(fill=matcool)
cell69.region = +cyl68 & +px6 & -px7 & -py1 & +py2
biguni.add_cell(cell65)
biguni.add_cell(cell66)
biguni.add_cell(cell67)
biguni.add_cell(cell68)
biguni.add_cell(cell69)
# rod number (16,10)
x=  8.820000
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
cell73.region = +cyl72 & +px7 & -px8 & -py1 & +py2
biguni.add_cell(cell70)
biguni.add_cell(cell71)
biguni.add_cell(cell72)
biguni.add_cell(cell73)
# rod number (17,10)
x= 10.080000
y=  9.490000
cyl74 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl75 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl76 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl77 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell74 = openmc.Cell(fill=matfuel01)
cell74.region = -cyl74
fuel_cell_list.append(cell74.id)
cell75 = openmc.Cell(fill=matifba)
cell75.region = +cyl74 & -cyl75
cell76 = openmc.Cell(fill=matair)
cell76.region = +cyl75 & -cyl76
cell77 = openmc.Cell(fill=matclad)
cell77.region = +cyl76 & -cyl77
cell78 = openmc.Cell(fill=matcool)
cell78.region = +cyl77 & +px8 & -bnde & -py1 & +py2
biguni.add_cell(cell74)
biguni.add_cell(cell75)
biguni.add_cell(cell76)
biguni.add_cell(cell77)
biguni.add_cell(cell78)
# rod number (9,11)
x=  0.000000
y=  8.230000
cyl79 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl80 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl81 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl82 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell79 = openmc.Cell(fill=matfuel01)
cell79.region = -cyl79 & +bndw
fuel_cell_list.append(cell79.id)
cell80 = openmc.Cell(fill=matifba)
cell80.region = +cyl79 & -cyl80 & +bndw
cell81 = openmc.Cell(fill=matair)
cell81.region = +cyl80 & -cyl81 & +bndw
cell82 = openmc.Cell(fill=matclad)
cell82.region = +cyl81 & -cyl82 & +bndw
cell83 = openmc.Cell(fill=matcool)
cell83.region = +cyl82 & +bndw & -px1 & -py2 & +py3
biguni.add_cell(cell79)
biguni.add_cell(cell80)
biguni.add_cell(cell81)
biguni.add_cell(cell82)
biguni.add_cell(cell83)
# rod number (10,11)
x=  1.260000
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
cell87.region = +cyl86 & +px1 & -px2 & -py2 & +py3
biguni.add_cell(cell84)
biguni.add_cell(cell85)
biguni.add_cell(cell86)
biguni.add_cell(cell87)
# rod number (11,11)
x=  2.520000
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
cell91.region = +cyl90 & +px2 & -px3 & -py2 & +py3
biguni.add_cell(cell88)
biguni.add_cell(cell89)
biguni.add_cell(cell90)
biguni.add_cell(cell91)
# rod number (12,11)
x=  3.780000
y=  8.230000
cyl92 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl93 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl94 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl95 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell92 = openmc.Cell(fill=matfuel01)
cell92.region = -cyl92
fuel_cell_list.append(cell92.id)
cell93 = openmc.Cell(fill=matifba)
cell93.region = +cyl92 & -cyl93
cell94 = openmc.Cell(fill=matair)
cell94.region = +cyl93 & -cyl94
cell95 = openmc.Cell(fill=matclad)
cell95.region = +cyl94 & -cyl95
cell96 = openmc.Cell(fill=matcool)
cell96.region = +cyl95 & +px3 & -px4 & -py2 & +py3
biguni.add_cell(cell92)
biguni.add_cell(cell93)
biguni.add_cell(cell94)
biguni.add_cell(cell95)
biguni.add_cell(cell96)
# rod number (13,11)
x=  5.040000
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
cell100.region = +cyl99 & +px4 & -px5 & -py2 & +py3
biguni.add_cell(cell97)
biguni.add_cell(cell98)
biguni.add_cell(cell99)
biguni.add_cell(cell100)
# rod number (14,11)
x=  6.300000
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
cell104.region = +cyl103 & +px5 & -px6 & -py2 & +py3
biguni.add_cell(cell101)
biguni.add_cell(cell102)
biguni.add_cell(cell103)
biguni.add_cell(cell104)
# rod number (15,11)
x=  7.560000
y=  8.230000
cyl105 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl106 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl107 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl108 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell105 = openmc.Cell(fill=matfuel01)
cell105.region = -cyl105
fuel_cell_list.append(cell105.id)
cell106 = openmc.Cell(fill=matifba)
cell106.region = +cyl105 & -cyl106
cell107 = openmc.Cell(fill=matair)
cell107.region = +cyl106 & -cyl107
cell108 = openmc.Cell(fill=matclad)
cell108.region = +cyl107 & -cyl108
cell109 = openmc.Cell(fill=matcool)
cell109.region = +cyl108 & +px6 & -px7 & -py2 & +py3
biguni.add_cell(cell105)
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
cyl118 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl119 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell118 = openmc.Cell(fill=matmod)
cell118.region = -cyl118 & +bndw
cell119 = openmc.Cell(fill=matclad)
cell119.region = +cyl118 & -cyl119 & +bndw
cell120 = openmc.Cell(fill=matcool)
cell120.region = +cyl119 & +bndw & -px1 & -py3 & +py4
biguni.add_cell(cell118)
biguni.add_cell(cell119)
biguni.add_cell(cell120)
# rod number (10,12)
x=  1.260000
y=  6.970000
cyl121 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl122 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl123 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl124 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell121 = openmc.Cell(fill=matfuel01)
cell121.region = -cyl121
fuel_cell_list.append(cell121.id)
cell122 = openmc.Cell(fill=matifba)
cell122.region = +cyl121 & -cyl122
cell123 = openmc.Cell(fill=matair)
cell123.region = +cyl122 & -cyl123
cell124 = openmc.Cell(fill=matclad)
cell124.region = +cyl123 & -cyl124
cell125 = openmc.Cell(fill=matcool)
cell125.region = +cyl124 & +px1 & -px2 & -py3 & +py4
biguni.add_cell(cell121)
biguni.add_cell(cell122)
biguni.add_cell(cell123)
biguni.add_cell(cell124)
biguni.add_cell(cell125)
# rod number (11,12)
x=  2.520000
y=  6.970000
cyl126 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl127 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl128 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl129 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell126 = openmc.Cell(fill=matfuel01)
cell126.region = -cyl126
fuel_cell_list.append(cell126.id)
cell127 = openmc.Cell(fill=matifba)
cell127.region = +cyl126 & -cyl127
cell128 = openmc.Cell(fill=matair)
cell128.region = +cyl127 & -cyl128
cell129 = openmc.Cell(fill=matclad)
cell129.region = +cyl128 & -cyl129
cell130 = openmc.Cell(fill=matcool)
cell130.region = +cyl129 & +px2 & -px3 & -py3 & +py4
biguni.add_cell(cell126)
biguni.add_cell(cell127)
biguni.add_cell(cell128)
biguni.add_cell(cell129)
biguni.add_cell(cell130)
# rod number (12,12)
x=  3.780000
y=  6.970000
cyl131 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl132 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell131 = openmc.Cell(fill=matmod)
cell131.region = -cyl131
cell132 = openmc.Cell(fill=matclad)
cell132.region = +cyl131 & -cyl132
cell133 = openmc.Cell(fill=matcool)
cell133.region = +cyl132 & +px3 & -px4 & -py3 & +py4
biguni.add_cell(cell131)
biguni.add_cell(cell132)
biguni.add_cell(cell133)
# rod number (13,12)
x=  5.040000
y=  6.970000
cyl134 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl135 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl136 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl137 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell134 = openmc.Cell(fill=matfuel01)
cell134.region = -cyl134
fuel_cell_list.append(cell134.id)
cell135 = openmc.Cell(fill=matifba)
cell135.region = +cyl134 & -cyl135
cell136 = openmc.Cell(fill=matair)
cell136.region = +cyl135 & -cyl136
cell137 = openmc.Cell(fill=matclad)
cell137.region = +cyl136 & -cyl137
cell138 = openmc.Cell(fill=matcool)
cell138.region = +cyl137 & +px4 & -px5 & -py3 & +py4
biguni.add_cell(cell134)
biguni.add_cell(cell135)
biguni.add_cell(cell136)
biguni.add_cell(cell137)
biguni.add_cell(cell138)
# rod number (14,12)
x=  6.300000
y=  6.970000
cyl139 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl140 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl141 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl142 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell139 = openmc.Cell(fill=matfuel01)
cell139.region = -cyl139
fuel_cell_list.append(cell139.id)
cell140 = openmc.Cell(fill=matifba)
cell140.region = +cyl139 & -cyl140
cell141 = openmc.Cell(fill=matair)
cell141.region = +cyl140 & -cyl141
cell142 = openmc.Cell(fill=matclad)
cell142.region = +cyl141 & -cyl142
cell143 = openmc.Cell(fill=matcool)
cell143.region = +cyl142 & +px5 & -px6 & -py3 & +py4
biguni.add_cell(cell139)
biguni.add_cell(cell140)
biguni.add_cell(cell141)
biguni.add_cell(cell142)
biguni.add_cell(cell143)
# rod number (15,12)
x=  7.560000
y=  6.970000
cyl144 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl145 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell144 = openmc.Cell(fill=matmod)
cell144.region = -cyl144
cell145 = openmc.Cell(fill=matclad)
cell145.region = +cyl144 & -cyl145
cell146 = openmc.Cell(fill=matcool)
cell146.region = +cyl145 & +px6 & -px7 & -py3 & +py4
biguni.add_cell(cell144)
biguni.add_cell(cell145)
biguni.add_cell(cell146)
# rod number (16,12)
x=  8.820000
y=  6.970000
cyl147 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl148 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl149 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl150 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell147 = openmc.Cell(fill=matfuel01)
cell147.region = -cyl147
fuel_cell_list.append(cell147.id)
cell148 = openmc.Cell(fill=matifba)
cell148.region = +cyl147 & -cyl148
cell149 = openmc.Cell(fill=matair)
cell149.region = +cyl148 & -cyl149
cell150 = openmc.Cell(fill=matclad)
cell150.region = +cyl149 & -cyl150
cell151 = openmc.Cell(fill=matcool)
cell151.region = +cyl150 & +px7 & -px8 & -py3 & +py4
biguni.add_cell(cell147)
biguni.add_cell(cell148)
biguni.add_cell(cell149)
biguni.add_cell(cell150)
biguni.add_cell(cell151)
# rod number (17,12)
x= 10.080000
y=  6.970000
cyl152 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl153 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl154 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell152 = openmc.Cell(fill=matfuel01)
cell152.region = -cyl152
fuel_cell_list.append(cell152.id)
cell153 = openmc.Cell(fill=matair)
cell153.region = +cyl152 & -cyl153
cell154 = openmc.Cell(fill=matclad)
cell154.region = +cyl153 & -cyl154
cell155 = openmc.Cell(fill=matcool)
cell155.region = +cyl154 & +px8 & -bnde & -py3 & +py4
biguni.add_cell(cell152)
biguni.add_cell(cell153)
biguni.add_cell(cell154)
biguni.add_cell(cell155)
# rod number (9,13)
x=  0.000000
y=  5.710000
cyl156 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl157 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl158 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl159 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell156 = openmc.Cell(fill=matfuel01)
cell156.region = -cyl156 & +bndw
fuel_cell_list.append(cell156.id)
cell157 = openmc.Cell(fill=matifba)
cell157.region = +cyl156 & -cyl157 & +bndw
cell158 = openmc.Cell(fill=matair)
cell158.region = +cyl157 & -cyl158 & +bndw
cell159 = openmc.Cell(fill=matclad)
cell159.region = +cyl158 & -cyl159 & +bndw
cell160 = openmc.Cell(fill=matcool)
cell160.region = +cyl159 & +bndw & -px1 & -py4 & +py5
biguni.add_cell(cell156)
biguni.add_cell(cell157)
biguni.add_cell(cell158)
biguni.add_cell(cell159)
biguni.add_cell(cell160)
# rod number (10,13)
x=  1.260000
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
cell164.region = +cyl163 & +px1 & -px2 & -py4 & +py5
biguni.add_cell(cell161)
biguni.add_cell(cell162)
biguni.add_cell(cell163)
biguni.add_cell(cell164)
# rod number (11,13)
x=  2.520000
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
cell168.region = +cyl167 & +px2 & -px3 & -py4 & +py5
biguni.add_cell(cell165)
biguni.add_cell(cell166)
biguni.add_cell(cell167)
biguni.add_cell(cell168)
# rod number (12,13)
x=  3.780000
y=  5.710000
cyl169 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl170 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl171 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl172 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell169 = openmc.Cell(fill=matfuel01)
cell169.region = -cyl169
fuel_cell_list.append(cell169.id)
cell170 = openmc.Cell(fill=matifba)
cell170.region = +cyl169 & -cyl170
cell171 = openmc.Cell(fill=matair)
cell171.region = +cyl170 & -cyl171
cell172 = openmc.Cell(fill=matclad)
cell172.region = +cyl171 & -cyl172
cell173 = openmc.Cell(fill=matcool)
cell173.region = +cyl172 & +px3 & -px4 & -py4 & +py5
biguni.add_cell(cell169)
biguni.add_cell(cell170)
biguni.add_cell(cell171)
biguni.add_cell(cell172)
biguni.add_cell(cell173)
# rod number (13,13)
x=  5.040000
y=  5.710000
cyl174 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl175 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl176 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell174 = openmc.Cell(fill=matfuel01)
cell174.region = -cyl174
fuel_cell_list.append(cell174.id)
cell175 = openmc.Cell(fill=matair)
cell175.region = +cyl174 & -cyl175
cell176 = openmc.Cell(fill=matclad)
cell176.region = +cyl175 & -cyl176
cell177 = openmc.Cell(fill=matcool)
cell177.region = +cyl176 & +px4 & -px5 & -py4 & +py5
biguni.add_cell(cell174)
biguni.add_cell(cell175)
biguni.add_cell(cell176)
biguni.add_cell(cell177)
# rod number (14,13)
x=  6.300000
y=  5.710000
cyl178 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl179 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl180 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl181 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell178 = openmc.Cell(fill=matfuel01)
cell178.region = -cyl178
fuel_cell_list.append(cell178.id)
cell179 = openmc.Cell(fill=matifba)
cell179.region = +cyl178 & -cyl179
cell180 = openmc.Cell(fill=matair)
cell180.region = +cyl179 & -cyl180
cell181 = openmc.Cell(fill=matclad)
cell181.region = +cyl180 & -cyl181
cell182 = openmc.Cell(fill=matcool)
cell182.region = +cyl181 & +px5 & -px6 & -py4 & +py5
biguni.add_cell(cell178)
biguni.add_cell(cell179)
biguni.add_cell(cell180)
biguni.add_cell(cell181)
biguni.add_cell(cell182)
# rod number (15,13)
x=  7.560000
y=  5.710000
cyl183 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl184 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl185 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl186 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell183 = openmc.Cell(fill=matfuel01)
cell183.region = -cyl183
fuel_cell_list.append(cell183.id)
cell184 = openmc.Cell(fill=matifba)
cell184.region = +cyl183 & -cyl184
cell185 = openmc.Cell(fill=matair)
cell185.region = +cyl184 & -cyl185
cell186 = openmc.Cell(fill=matclad)
cell186.region = +cyl185 & -cyl186
cell187 = openmc.Cell(fill=matcool)
cell187.region = +cyl186 & +px6 & -px7 & -py4 & +py5
biguni.add_cell(cell183)
biguni.add_cell(cell184)
biguni.add_cell(cell185)
biguni.add_cell(cell186)
biguni.add_cell(cell187)
# rod number (16,13)
x=  8.820000
y=  5.710000
cyl188 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl189 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl190 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell188 = openmc.Cell(fill=matfuel01)
cell188.region = -cyl188
fuel_cell_list.append(cell188.id)
cell189 = openmc.Cell(fill=matair)
cell189.region = +cyl188 & -cyl189
cell190 = openmc.Cell(fill=matclad)
cell190.region = +cyl189 & -cyl190
cell191 = openmc.Cell(fill=matcool)
cell191.region = +cyl190 & +px7 & -px8 & -py4 & +py5
biguni.add_cell(cell188)
biguni.add_cell(cell189)
biguni.add_cell(cell190)
biguni.add_cell(cell191)
# rod number (17,13)
x= 10.080000
y=  5.710000
cyl192 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl193 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl194 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl195 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell192 = openmc.Cell(fill=matfuel01)
cell192.region = -cyl192
fuel_cell_list.append(cell192.id)
cell193 = openmc.Cell(fill=matifba)
cell193.region = +cyl192 & -cyl193
cell194 = openmc.Cell(fill=matair)
cell194.region = +cyl193 & -cyl194
cell195 = openmc.Cell(fill=matclad)
cell195.region = +cyl194 & -cyl195
cell196 = openmc.Cell(fill=matcool)
cell196.region = +cyl195 & +px8 & -bnde & -py4 & +py5
biguni.add_cell(cell192)
biguni.add_cell(cell193)
biguni.add_cell(cell194)
biguni.add_cell(cell195)
biguni.add_cell(cell196)
# rod number (9,14)
x=  0.000000
y=  4.450000
cyl197 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl198 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl199 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl200 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell197 = openmc.Cell(fill=matfuel01)
cell197.region = -cyl197 & +bndw
fuel_cell_list.append(cell197.id)
cell198 = openmc.Cell(fill=matifba)
cell198.region = +cyl197 & -cyl198 & +bndw
cell199 = openmc.Cell(fill=matair)
cell199.region = +cyl198 & -cyl199 & +bndw
cell200 = openmc.Cell(fill=matclad)
cell200.region = +cyl199 & -cyl200 & +bndw
cell201 = openmc.Cell(fill=matcool)
cell201.region = +cyl200 & +bndw & -px1 & -py5 & +py6
biguni.add_cell(cell197)
biguni.add_cell(cell198)
biguni.add_cell(cell199)
biguni.add_cell(cell200)
biguni.add_cell(cell201)
# rod number (10,14)
x=  1.260000
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
cell205.region = +cyl204 & +px1 & -px2 & -py5 & +py6
biguni.add_cell(cell202)
biguni.add_cell(cell203)
biguni.add_cell(cell204)
biguni.add_cell(cell205)
# rod number (11,14)
x=  2.520000
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
cell209.region = +cyl208 & +px2 & -px3 & -py5 & +py6
biguni.add_cell(cell206)
biguni.add_cell(cell207)
biguni.add_cell(cell208)
biguni.add_cell(cell209)
# rod number (12,14)
x=  3.780000
y=  4.450000
cyl210 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl211 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl212 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl213 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell210 = openmc.Cell(fill=matfuel01)
cell210.region = -cyl210
fuel_cell_list.append(cell210.id)
cell211 = openmc.Cell(fill=matifba)
cell211.region = +cyl210 & -cyl211
cell212 = openmc.Cell(fill=matair)
cell212.region = +cyl211 & -cyl212
cell213 = openmc.Cell(fill=matclad)
cell213.region = +cyl212 & -cyl213
cell214 = openmc.Cell(fill=matcool)
cell214.region = +cyl213 & +px3 & -px4 & -py5 & +py6
biguni.add_cell(cell210)
biguni.add_cell(cell211)
biguni.add_cell(cell212)
biguni.add_cell(cell213)
biguni.add_cell(cell214)
# rod number (13,14)
x=  5.040000
y=  4.450000
cyl215 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl216 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl217 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl218 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell215 = openmc.Cell(fill=matfuel01)
cell215.region = -cyl215
fuel_cell_list.append(cell215.id)
cell216 = openmc.Cell(fill=matifba)
cell216.region = +cyl215 & -cyl216
cell217 = openmc.Cell(fill=matair)
cell217.region = +cyl216 & -cyl217
cell218 = openmc.Cell(fill=matclad)
cell218.region = +cyl217 & -cyl218
cell219 = openmc.Cell(fill=matcool)
cell219.region = +cyl218 & +px4 & -px5 & -py5 & +py6
biguni.add_cell(cell215)
biguni.add_cell(cell216)
biguni.add_cell(cell217)
biguni.add_cell(cell218)
biguni.add_cell(cell219)
# rod number (14,14)
x=  6.300000
y=  4.450000
cyl220 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl221 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell220 = openmc.Cell(fill=matmod)
cell220.region = -cyl220
cell221 = openmc.Cell(fill=matclad)
cell221.region = +cyl220 & -cyl221
cell222 = openmc.Cell(fill=matcool)
cell222.region = +cyl221 & +px5 & -px6 & -py5 & +py6
biguni.add_cell(cell220)
biguni.add_cell(cell221)
biguni.add_cell(cell222)
# rod number (15,14)
x=  7.560000
y=  4.450000
cyl223 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl224 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl225 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl226 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell223 = openmc.Cell(fill=matfuel01)
cell223.region = -cyl223
fuel_cell_list.append(cell223.id)
cell224 = openmc.Cell(fill=matifba)
cell224.region = +cyl223 & -cyl224
cell225 = openmc.Cell(fill=matair)
cell225.region = +cyl224 & -cyl225
cell226 = openmc.Cell(fill=matclad)
cell226.region = +cyl225 & -cyl226
cell227 = openmc.Cell(fill=matcool)
cell227.region = +cyl226 & +px6 & -px7 & -py5 & +py6
biguni.add_cell(cell223)
biguni.add_cell(cell224)
biguni.add_cell(cell225)
biguni.add_cell(cell226)
biguni.add_cell(cell227)
# rod number (16,14)
x=  8.820000
y=  4.450000
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
cell231.region = +cyl230 & +px7 & -px8 & -py5 & +py6
biguni.add_cell(cell228)
biguni.add_cell(cell229)
biguni.add_cell(cell230)
biguni.add_cell(cell231)
# rod number (17,14)
x= 10.080000
y=  4.450000
cyl232 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl233 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl234 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell232 = openmc.Cell(fill=matfuel01)
cell232.region = -cyl232
fuel_cell_list.append(cell232.id)
cell233 = openmc.Cell(fill=matair)
cell233.region = +cyl232 & -cyl233
cell234 = openmc.Cell(fill=matclad)
cell234.region = +cyl233 & -cyl234
cell235 = openmc.Cell(fill=matcool)
cell235.region = +cyl234 & +px8 & -bnde & -py5 & +py6
biguni.add_cell(cell232)
biguni.add_cell(cell233)
biguni.add_cell(cell234)
biguni.add_cell(cell235)
# rod number (9,15)
x=  0.000000
y=  3.190000
cyl236 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl237 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell236 = openmc.Cell(fill=matmod)
cell236.region = -cyl236 & +bndw
cell237 = openmc.Cell(fill=matclad)
cell237.region = +cyl236 & -cyl237 & +bndw
cell238 = openmc.Cell(fill=matcool)
cell238.region = +cyl237 & +bndw & -px1 & -py6 & +py7
biguni.add_cell(cell236)
biguni.add_cell(cell237)
biguni.add_cell(cell238)
# rod number (10,15)
x=  1.260000
y=  3.190000
cyl239 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl240 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl241 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl242 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell239 = openmc.Cell(fill=matfuel01)
cell239.region = -cyl239
fuel_cell_list.append(cell239.id)
cell240 = openmc.Cell(fill=matifba)
cell240.region = +cyl239 & -cyl240
cell241 = openmc.Cell(fill=matair)
cell241.region = +cyl240 & -cyl241
cell242 = openmc.Cell(fill=matclad)
cell242.region = +cyl241 & -cyl242
cell243 = openmc.Cell(fill=matcool)
cell243.region = +cyl242 & +px1 & -px2 & -py6 & +py7
biguni.add_cell(cell239)
biguni.add_cell(cell240)
biguni.add_cell(cell241)
biguni.add_cell(cell242)
biguni.add_cell(cell243)
# rod number (11,15)
x=  2.520000
y=  3.190000
cyl244 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl245 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl246 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl247 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell244 = openmc.Cell(fill=matfuel01)
cell244.region = -cyl244
fuel_cell_list.append(cell244.id)
cell245 = openmc.Cell(fill=matifba)
cell245.region = +cyl244 & -cyl245
cell246 = openmc.Cell(fill=matair)
cell246.region = +cyl245 & -cyl246
cell247 = openmc.Cell(fill=matclad)
cell247.region = +cyl246 & -cyl247
cell248 = openmc.Cell(fill=matcool)
cell248.region = +cyl247 & +px2 & -px3 & -py6 & +py7
biguni.add_cell(cell244)
biguni.add_cell(cell245)
biguni.add_cell(cell246)
biguni.add_cell(cell247)
biguni.add_cell(cell248)
# rod number (12,15)
x=  3.780000
y=  3.190000
cyl249 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl250 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell249 = openmc.Cell(fill=matmod)
cell249.region = -cyl249
cell250 = openmc.Cell(fill=matclad)
cell250.region = +cyl249 & -cyl250
cell251 = openmc.Cell(fill=matcool)
cell251.region = +cyl250 & +px3 & -px4 & -py6 & +py7
biguni.add_cell(cell249)
biguni.add_cell(cell250)
biguni.add_cell(cell251)
# rod number (13,15)
x=  5.040000
y=  3.190000
cyl252 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl253 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl254 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl255 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell252 = openmc.Cell(fill=matfuel01)
cell252.region = -cyl252
fuel_cell_list.append(cell252.id)
cell253 = openmc.Cell(fill=matifba)
cell253.region = +cyl252 & -cyl253
cell254 = openmc.Cell(fill=matair)
cell254.region = +cyl253 & -cyl254
cell255 = openmc.Cell(fill=matclad)
cell255.region = +cyl254 & -cyl255
cell256 = openmc.Cell(fill=matcool)
cell256.region = +cyl255 & +px4 & -px5 & -py6 & +py7
biguni.add_cell(cell252)
biguni.add_cell(cell253)
biguni.add_cell(cell254)
biguni.add_cell(cell255)
biguni.add_cell(cell256)
# rod number (14,15)
x=  6.300000
y=  3.190000
cyl257 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl258 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl259 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl260 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell257 = openmc.Cell(fill=matfuel01)
cell257.region = -cyl257
fuel_cell_list.append(cell257.id)
cell258 = openmc.Cell(fill=matifba)
cell258.region = +cyl257 & -cyl258
cell259 = openmc.Cell(fill=matair)
cell259.region = +cyl258 & -cyl259
cell260 = openmc.Cell(fill=matclad)
cell260.region = +cyl259 & -cyl260
cell261 = openmc.Cell(fill=matcool)
cell261.region = +cyl260 & +px5 & -px6 & -py6 & +py7
biguni.add_cell(cell257)
biguni.add_cell(cell258)
biguni.add_cell(cell259)
biguni.add_cell(cell260)
biguni.add_cell(cell261)
# rod number (15,15)
x=  7.560000
y=  3.190000
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
cell265.region = +cyl264 & +px6 & -px7 & -py6 & +py7
biguni.add_cell(cell262)
biguni.add_cell(cell263)
biguni.add_cell(cell264)
biguni.add_cell(cell265)
# rod number (16,15)
x=  8.820000
y=  3.190000
cyl266 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl267 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl268 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl269 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell266 = openmc.Cell(fill=matfuel01)
cell266.region = -cyl266
fuel_cell_list.append(cell266.id)
cell267 = openmc.Cell(fill=matifba)
cell267.region = +cyl266 & -cyl267
cell268 = openmc.Cell(fill=matair)
cell268.region = +cyl267 & -cyl268
cell269 = openmc.Cell(fill=matclad)
cell269.region = +cyl268 & -cyl269
cell270 = openmc.Cell(fill=matcool)
cell270.region = +cyl269 & +px7 & -px8 & -py6 & +py7
biguni.add_cell(cell266)
biguni.add_cell(cell267)
biguni.add_cell(cell268)
biguni.add_cell(cell269)
biguni.add_cell(cell270)
# rod number (17,15)
x= 10.080000
y=  3.190000
cyl271 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl272 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl273 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell271 = openmc.Cell(fill=matfuel01)
cell271.region = -cyl271
fuel_cell_list.append(cell271.id)
cell272 = openmc.Cell(fill=matair)
cell272.region = +cyl271 & -cyl272
cell273 = openmc.Cell(fill=matclad)
cell273.region = +cyl272 & -cyl273
cell274 = openmc.Cell(fill=matcool)
cell274.region = +cyl273 & +px8 & -bnde & -py6 & +py7
biguni.add_cell(cell271)
biguni.add_cell(cell272)
biguni.add_cell(cell273)
biguni.add_cell(cell274)
# rod number (9,16)
x=  0.000000
y=  1.930000
cyl275 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl276 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl277 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl278 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell275 = openmc.Cell(fill=matfuel01)
cell275.region = -cyl275 & +bndw
fuel_cell_list.append(cell275.id)
cell276 = openmc.Cell(fill=matifba)
cell276.region = +cyl275 & -cyl276 & +bndw
cell277 = openmc.Cell(fill=matair)
cell277.region = +cyl276 & -cyl277 & +bndw
cell278 = openmc.Cell(fill=matclad)
cell278.region = +cyl277 & -cyl278 & +bndw
cell279 = openmc.Cell(fill=matcool)
cell279.region = +cyl278 & +bndw & -px1 & -py7 & +py8
biguni.add_cell(cell275)
biguni.add_cell(cell276)
biguni.add_cell(cell277)
biguni.add_cell(cell278)
biguni.add_cell(cell279)
# rod number (10,16)
x=  1.260000
y=  1.930000
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
cell283.region = +cyl282 & +px1 & -px2 & -py7 & +py8
biguni.add_cell(cell280)
biguni.add_cell(cell281)
biguni.add_cell(cell282)
biguni.add_cell(cell283)
# rod number (11,16)
x=  2.520000
y=  1.930000
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
cell287.region = +cyl286 & +px2 & -px3 & -py7 & +py8
biguni.add_cell(cell284)
biguni.add_cell(cell285)
biguni.add_cell(cell286)
biguni.add_cell(cell287)
# rod number (12,16)
x=  3.780000
y=  1.930000
cyl288 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl289 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl290 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl291 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell288 = openmc.Cell(fill=matfuel01)
cell288.region = -cyl288
fuel_cell_list.append(cell288.id)
cell289 = openmc.Cell(fill=matifba)
cell289.region = +cyl288 & -cyl289
cell290 = openmc.Cell(fill=matair)
cell290.region = +cyl289 & -cyl290
cell291 = openmc.Cell(fill=matclad)
cell291.region = +cyl290 & -cyl291
cell292 = openmc.Cell(fill=matcool)
cell292.region = +cyl291 & +px3 & -px4 & -py7 & +py8
biguni.add_cell(cell288)
biguni.add_cell(cell289)
biguni.add_cell(cell290)
biguni.add_cell(cell291)
biguni.add_cell(cell292)
# rod number (13,16)
x=  5.040000
y=  1.930000
cyl293 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl294 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl295 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell293 = openmc.Cell(fill=matfuel01)
cell293.region = -cyl293
fuel_cell_list.append(cell293.id)
cell294 = openmc.Cell(fill=matair)
cell294.region = +cyl293 & -cyl294
cell295 = openmc.Cell(fill=matclad)
cell295.region = +cyl294 & -cyl295
cell296 = openmc.Cell(fill=matcool)
cell296.region = +cyl295 & +px4 & -px5 & -py7 & +py8
biguni.add_cell(cell293)
biguni.add_cell(cell294)
biguni.add_cell(cell295)
biguni.add_cell(cell296)
# rod number (14,16)
x=  6.300000
y=  1.930000
cyl297 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl298 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl299 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell297 = openmc.Cell(fill=matfuel01)
cell297.region = -cyl297
fuel_cell_list.append(cell297.id)
cell298 = openmc.Cell(fill=matair)
cell298.region = +cyl297 & -cyl298
cell299 = openmc.Cell(fill=matclad)
cell299.region = +cyl298 & -cyl299
cell300 = openmc.Cell(fill=matcool)
cell300.region = +cyl299 & +px5 & -px6 & -py7 & +py8
biguni.add_cell(cell297)
biguni.add_cell(cell298)
biguni.add_cell(cell299)
biguni.add_cell(cell300)
# rod number (15,16)
x=  7.560000
y=  1.930000
cyl301 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl302 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl303 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl304 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell301 = openmc.Cell(fill=matfuel01)
cell301.region = -cyl301
fuel_cell_list.append(cell301.id)
cell302 = openmc.Cell(fill=matifba)
cell302.region = +cyl301 & -cyl302
cell303 = openmc.Cell(fill=matair)
cell303.region = +cyl302 & -cyl303
cell304 = openmc.Cell(fill=matclad)
cell304.region = +cyl303 & -cyl304
cell305 = openmc.Cell(fill=matcool)
cell305.region = +cyl304 & +px6 & -px7 & -py7 & +py8
biguni.add_cell(cell301)
biguni.add_cell(cell302)
biguni.add_cell(cell303)
biguni.add_cell(cell304)
biguni.add_cell(cell305)
# rod number (16,16)
x=  8.820000
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
cell309.region = +cyl308 & +px7 & -px8 & -py7 & +py8
biguni.add_cell(cell306)
biguni.add_cell(cell307)
biguni.add_cell(cell308)
biguni.add_cell(cell309)
# rod number (17,16)
x= 10.080000
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
cell313.region = +cyl312 & +px8 & -bnde & -py7 & +py8
biguni.add_cell(cell310)
biguni.add_cell(cell311)
biguni.add_cell(cell312)
biguni.add_cell(cell313)
# rod number (9,17)
x=  0.000000
y=  0.670000
cyl314 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl315 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl316 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell314 = openmc.Cell(fill=matfuel01)
cell314.region = -cyl314 & +bndw
fuel_cell_list.append(cell314.id)
cell315 = openmc.Cell(fill=matair)
cell315.region = +cyl314 & -cyl315 & +bndw
cell316 = openmc.Cell(fill=matclad)
cell316.region = +cyl315 & -cyl316 & +bndw
cell317 = openmc.Cell(fill=matcool)
cell317.region = +cyl316 & +bndw & -px1 & -py8 & +bnds
biguni.add_cell(cell314)
biguni.add_cell(cell315)
biguni.add_cell(cell316)
biguni.add_cell(cell317)
# rod number (10,17)
x=  1.260000
y=  0.670000
cyl318 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl319 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl320 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl321 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell318 = openmc.Cell(fill=matfuel01)
cell318.region = -cyl318
fuel_cell_list.append(cell318.id)
cell319 = openmc.Cell(fill=matifba)
cell319.region = +cyl318 & -cyl319
cell320 = openmc.Cell(fill=matair)
cell320.region = +cyl319 & -cyl320
cell321 = openmc.Cell(fill=matclad)
cell321.region = +cyl320 & -cyl321
cell322 = openmc.Cell(fill=matcool)
cell322.region = +cyl321 & +px1 & -px2 & -py8 & +bnds
biguni.add_cell(cell318)
biguni.add_cell(cell319)
biguni.add_cell(cell320)
biguni.add_cell(cell321)
biguni.add_cell(cell322)
# rod number (11,17)
x=  2.520000
y=  0.670000
cyl323 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl324 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl325 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell323 = openmc.Cell(fill=matfuel01)
cell323.region = -cyl323
fuel_cell_list.append(cell323.id)
cell324 = openmc.Cell(fill=matair)
cell324.region = +cyl323 & -cyl324
cell325 = openmc.Cell(fill=matclad)
cell325.region = +cyl324 & -cyl325
cell326 = openmc.Cell(fill=matcool)
cell326.region = +cyl325 & +px2 & -px3 & -py8 & +bnds
biguni.add_cell(cell323)
biguni.add_cell(cell324)
biguni.add_cell(cell325)
biguni.add_cell(cell326)
# rod number (12,17)
x=  3.780000
y=  0.670000
cyl327 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl328 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl329 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell327 = openmc.Cell(fill=matfuel01)
cell327.region = -cyl327
fuel_cell_list.append(cell327.id)
cell328 = openmc.Cell(fill=matair)
cell328.region = +cyl327 & -cyl328
cell329 = openmc.Cell(fill=matclad)
cell329.region = +cyl328 & -cyl329
cell330 = openmc.Cell(fill=matcool)
cell330.region = +cyl329 & +px3 & -px4 & -py8 & +bnds
biguni.add_cell(cell327)
biguni.add_cell(cell328)
biguni.add_cell(cell329)
biguni.add_cell(cell330)
# rod number (13,17)
x=  5.040000
y=  0.670000
cyl331 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl332 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl333 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl334 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell331 = openmc.Cell(fill=matfuel01)
cell331.region = -cyl331
fuel_cell_list.append(cell331.id)
cell332 = openmc.Cell(fill=matifba)
cell332.region = +cyl331 & -cyl332
cell333 = openmc.Cell(fill=matair)
cell333.region = +cyl332 & -cyl333
cell334 = openmc.Cell(fill=matclad)
cell334.region = +cyl333 & -cyl334
cell335 = openmc.Cell(fill=matcool)
cell335.region = +cyl334 & +px4 & -px5 & -py8 & +bnds
biguni.add_cell(cell331)
biguni.add_cell(cell332)
biguni.add_cell(cell333)
biguni.add_cell(cell334)
biguni.add_cell(cell335)
# rod number (14,17)
x=  6.300000
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
cell339.region = +cyl338 & +px5 & -px6 & -py8 & +bnds
biguni.add_cell(cell336)
biguni.add_cell(cell337)
biguni.add_cell(cell338)
biguni.add_cell(cell339)
# rod number (15,17)
x=  7.560000
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
cell343.region = +cyl342 & +px6 & -px7 & -py8 & +bnds
biguni.add_cell(cell340)
biguni.add_cell(cell341)
biguni.add_cell(cell342)
biguni.add_cell(cell343)
# rod number (16,17)
x=  8.820000
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
cell347.region = +cyl346 & +px7 & -px8 & -py8 & +bnds
biguni.add_cell(cell344)
biguni.add_cell(cell345)
biguni.add_cell(cell346)
biguni.add_cell(cell347)
# rod number (17,17)
x= 10.080000
y=  0.670000
cyl348 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl349 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl350 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl351 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell348 = openmc.Cell(fill=matfuel01)
cell348.region = -cyl348
fuel_cell_list.append(cell348.id)
cell349 = openmc.Cell(fill=matifba)
cell349.region = +cyl348 & -cyl349
cell350 = openmc.Cell(fill=matair)
cell350.region = +cyl349 & -cyl350
cell351 = openmc.Cell(fill=matclad)
cell351.region = +cyl350 & -cyl351
cell352 = openmc.Cell(fill=matcool)
cell352.region = +cyl351 & +px8 & -bnde & -py8 & +bnds
biguni.add_cell(cell348)
biguni.add_cell(cell349)
biguni.add_cell(cell350)
biguni.add_cell(cell351)
biguni.add_cell(cell352)

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
