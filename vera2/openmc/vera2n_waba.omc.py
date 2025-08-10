import matplotlib

import openmc
import openmc.mgxs as mgxs
import openmc.data          # need for hdf5

#  To run:
#  >python3 vera2n_waba.omc
#
# OpenMC Input created by BUNBLD on 08/09/2025 11:48:06
#  VERA Benchmark #2 - Single Assembly
#  Uniform PWR Assembly
#  November 15, 2012
#  Number densities from KENO run
#  VERA Benchmark 2N - like 2A + 104 IFBA pins + 20 WABA
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

# material 7 WABA
matwaba = openmc.Material(name='waba')
matwaba.add_nuclide('B10',  2.985530E-03)
matwaba.add_nuclide('B11',  1.211920E-02)
matwaba.add_nuclide('C0',  3.770010E-03)
matwaba.add_nuclide('O16',  5.855630E-02)
matwaba.add_nuclide('Al27',  3.902230E-02)
matwaba.set_density('g/cm3',  3.65000)
matwaba.temperature=  600.000

# Material mixtures

# Instantiate a Materials collection
model.materials = openmc.Materials([matfuel01,matclad,matcool,matmod,matair,matifba,matwaba])
#
# ------------- Geometry ------------------------
#
# PINMAP
#  3  8  8  4  8  8  4  8  1  
#  8  1  1  8  1  1  8  1  1  
#  8  1  1  8  1  1  8  1  1  
#  4  8  8  2  8  8  4  8  1  
#  8  1  1  8  1  8  8  1  1  
#  8  1  1  8  8  4  8  1  1  
#  4  8  8  4  8  8  1  1  1  
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
cyl14 = openmc.ZCylinder(x0=x, y0=y, r= 0.28600)  # MOD
cyl15 = openmc.ZCylinder(x0=x, y0=y, r= 0.33900)  # CLAD
cyl16 = openmc.ZCylinder(x0=x, y0=y, r= 0.35300)  # AIR
cyl17 = openmc.ZCylinder(x0=x, y0=y, r= 0.40400)  # WABA
cyl18 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl19 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # CLAD
cyl20 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl21 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell14 = openmc.Cell(fill=matmod)
cell14.region = -cyl14 & -bndn
cell15 = openmc.Cell(fill=matclad)
cell15.region = +cyl14 & -cyl15 & -bndn
cell16 = openmc.Cell(fill=matair)
cell16.region = +cyl15 & -cyl16 & -bndn
cell17 = openmc.Cell(fill=matwaba)
cell17.region = +cyl16 & -cyl17 & -bndn
cell18 = openmc.Cell(fill=matair)
cell18.region = +cyl17 & -cyl18 & -bndn
cell19 = openmc.Cell(fill=matclad)
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
cyl24 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl25 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl26 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell23 = openmc.Cell(fill=matfuel01)
cell23.region = -cyl23 & -bndn
fuel_cell_list.append(cell23.id)
cell24 = openmc.Cell(fill=matifba)
cell24.region = +cyl23 & -cyl24 & -bndn
cell25 = openmc.Cell(fill=matair)
cell25.region = +cyl24 & -cyl25 & -bndn
cell26 = openmc.Cell(fill=matclad)
cell26.region = +cyl25 & -cyl26 & -bndn
cell27 = openmc.Cell(fill=matcool)
cell27.region = +cyl26 & +px4 & -px5 & -bndn & +py1
biguni.add_cell(cell23)
biguni.add_cell(cell24)
biguni.add_cell(cell25)
biguni.add_cell(cell26)
biguni.add_cell(cell27)
# rod number (14,9)
x=  6.300000
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
cell32.region = +cyl31 & +px5 & -px6 & -bndn & +py1
biguni.add_cell(cell28)
biguni.add_cell(cell29)
biguni.add_cell(cell30)
biguni.add_cell(cell31)
biguni.add_cell(cell32)
# rod number (15,9)
x=  7.560000
y= 10.750000
cyl33 = openmc.ZCylinder(x0=x, y0=y, r= 0.28600)  # MOD
cyl34 = openmc.ZCylinder(x0=x, y0=y, r= 0.33900)  # CLAD
cyl35 = openmc.ZCylinder(x0=x, y0=y, r= 0.35300)  # AIR
cyl36 = openmc.ZCylinder(x0=x, y0=y, r= 0.40400)  # WABA
cyl37 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl38 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # CLAD
cyl39 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl40 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell33 = openmc.Cell(fill=matmod)
cell33.region = -cyl33 & -bndn
cell34 = openmc.Cell(fill=matclad)
cell34.region = +cyl33 & -cyl34 & -bndn
cell35 = openmc.Cell(fill=matair)
cell35.region = +cyl34 & -cyl35 & -bndn
cell36 = openmc.Cell(fill=matwaba)
cell36.region = +cyl35 & -cyl36 & -bndn
cell37 = openmc.Cell(fill=matair)
cell37.region = +cyl36 & -cyl37 & -bndn
cell38 = openmc.Cell(fill=matclad)
cell38.region = +cyl37 & -cyl38 & -bndn
cell39 = openmc.Cell(fill=matmod)
cell39.region = +cyl38 & -cyl39 & -bndn
cell40 = openmc.Cell(fill=matclad)
cell40.region = +cyl39 & -cyl40 & -bndn
cell41 = openmc.Cell(fill=matcool)
cell41.region = +cyl40 & +px6 & -px7 & -bndn & +py1
biguni.add_cell(cell33)
biguni.add_cell(cell34)
biguni.add_cell(cell35)
biguni.add_cell(cell36)
biguni.add_cell(cell37)
biguni.add_cell(cell38)
biguni.add_cell(cell39)
biguni.add_cell(cell40)
biguni.add_cell(cell41)
# rod number (16,9)
x=  8.820000
y= 10.750000
cyl42 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl43 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl44 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl45 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell42 = openmc.Cell(fill=matfuel01)
cell42.region = -cyl42 & -bndn
fuel_cell_list.append(cell42.id)
cell43 = openmc.Cell(fill=matifba)
cell43.region = +cyl42 & -cyl43 & -bndn
cell44 = openmc.Cell(fill=matair)
cell44.region = +cyl43 & -cyl44 & -bndn
cell45 = openmc.Cell(fill=matclad)
cell45.region = +cyl44 & -cyl45 & -bndn
cell46 = openmc.Cell(fill=matcool)
cell46.region = +cyl45 & +px7 & -px8 & -bndn & +py1
biguni.add_cell(cell42)
biguni.add_cell(cell43)
biguni.add_cell(cell44)
biguni.add_cell(cell45)
biguni.add_cell(cell46)
# rod number (17,9)
x= 10.080000
y= 10.750000
cyl47 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl48 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl49 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell47 = openmc.Cell(fill=matfuel01)
cell47.region = -cyl47 & -bndn
fuel_cell_list.append(cell47.id)
cell48 = openmc.Cell(fill=matair)
cell48.region = +cyl47 & -cyl48 & -bndn
cell49 = openmc.Cell(fill=matclad)
cell49.region = +cyl48 & -cyl49 & -bndn
cell50 = openmc.Cell(fill=matcool)
cell50.region = +cyl49 & +px8 & -bnde & -bndn & +py1
biguni.add_cell(cell47)
biguni.add_cell(cell48)
biguni.add_cell(cell49)
biguni.add_cell(cell50)
# rod number (9,10)
x=  0.000000
y=  9.490000
cyl51 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl52 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl53 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl54 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell51 = openmc.Cell(fill=matfuel01)
cell51.region = -cyl51 & +bndw
fuel_cell_list.append(cell51.id)
cell52 = openmc.Cell(fill=matifba)
cell52.region = +cyl51 & -cyl52 & +bndw
cell53 = openmc.Cell(fill=matair)
cell53.region = +cyl52 & -cyl53 & +bndw
cell54 = openmc.Cell(fill=matclad)
cell54.region = +cyl53 & -cyl54 & +bndw
cell55 = openmc.Cell(fill=matcool)
cell55.region = +cyl54 & +bndw & -px1 & -py1 & +py2
biguni.add_cell(cell51)
biguni.add_cell(cell52)
biguni.add_cell(cell53)
biguni.add_cell(cell54)
biguni.add_cell(cell55)
# rod number (10,10)
x=  1.260000
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
cell59.region = +cyl58 & +px1 & -px2 & -py1 & +py2
biguni.add_cell(cell56)
biguni.add_cell(cell57)
biguni.add_cell(cell58)
biguni.add_cell(cell59)
# rod number (11,10)
x=  2.520000
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
cell63.region = +cyl62 & +px2 & -px3 & -py1 & +py2
biguni.add_cell(cell60)
biguni.add_cell(cell61)
biguni.add_cell(cell62)
biguni.add_cell(cell63)
# rod number (12,10)
x=  3.780000
y=  9.490000
cyl64 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl65 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl66 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl67 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell64 = openmc.Cell(fill=matfuel01)
cell64.region = -cyl64
fuel_cell_list.append(cell64.id)
cell65 = openmc.Cell(fill=matifba)
cell65.region = +cyl64 & -cyl65
cell66 = openmc.Cell(fill=matair)
cell66.region = +cyl65 & -cyl66
cell67 = openmc.Cell(fill=matclad)
cell67.region = +cyl66 & -cyl67
cell68 = openmc.Cell(fill=matcool)
cell68.region = +cyl67 & +px3 & -px4 & -py1 & +py2
biguni.add_cell(cell64)
biguni.add_cell(cell65)
biguni.add_cell(cell66)
biguni.add_cell(cell67)
biguni.add_cell(cell68)
# rod number (13,10)
x=  5.040000
y=  9.490000
cyl69 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl70 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl71 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell69 = openmc.Cell(fill=matfuel01)
cell69.region = -cyl69
fuel_cell_list.append(cell69.id)
cell70 = openmc.Cell(fill=matair)
cell70.region = +cyl69 & -cyl70
cell71 = openmc.Cell(fill=matclad)
cell71.region = +cyl70 & -cyl71
cell72 = openmc.Cell(fill=matcool)
cell72.region = +cyl71 & +px4 & -px5 & -py1 & +py2
biguni.add_cell(cell69)
biguni.add_cell(cell70)
biguni.add_cell(cell71)
biguni.add_cell(cell72)
# rod number (14,10)
x=  6.300000
y=  9.490000
cyl73 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl74 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl75 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell73 = openmc.Cell(fill=matfuel01)
cell73.region = -cyl73
fuel_cell_list.append(cell73.id)
cell74 = openmc.Cell(fill=matair)
cell74.region = +cyl73 & -cyl74
cell75 = openmc.Cell(fill=matclad)
cell75.region = +cyl74 & -cyl75
cell76 = openmc.Cell(fill=matcool)
cell76.region = +cyl75 & +px5 & -px6 & -py1 & +py2
biguni.add_cell(cell73)
biguni.add_cell(cell74)
biguni.add_cell(cell75)
biguni.add_cell(cell76)
# rod number (15,10)
x=  7.560000
y=  9.490000
cyl77 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl78 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl79 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl80 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell77 = openmc.Cell(fill=matfuel01)
cell77.region = -cyl77
fuel_cell_list.append(cell77.id)
cell78 = openmc.Cell(fill=matifba)
cell78.region = +cyl77 & -cyl78
cell79 = openmc.Cell(fill=matair)
cell79.region = +cyl78 & -cyl79
cell80 = openmc.Cell(fill=matclad)
cell80.region = +cyl79 & -cyl80
cell81 = openmc.Cell(fill=matcool)
cell81.region = +cyl80 & +px6 & -px7 & -py1 & +py2
biguni.add_cell(cell77)
biguni.add_cell(cell78)
biguni.add_cell(cell79)
biguni.add_cell(cell80)
biguni.add_cell(cell81)
# rod number (16,10)
x=  8.820000
y=  9.490000
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
cell85.region = +cyl84 & +px7 & -px8 & -py1 & +py2
biguni.add_cell(cell82)
biguni.add_cell(cell83)
biguni.add_cell(cell84)
biguni.add_cell(cell85)
# rod number (17,10)
x= 10.080000
y=  9.490000
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
cell89.region = +cyl88 & +px8 & -bnde & -py1 & +py2
biguni.add_cell(cell86)
biguni.add_cell(cell87)
biguni.add_cell(cell88)
biguni.add_cell(cell89)
# rod number (9,11)
x=  0.000000
y=  8.230000
cyl90 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl91 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl92 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl93 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell90 = openmc.Cell(fill=matfuel01)
cell90.region = -cyl90 & +bndw
fuel_cell_list.append(cell90.id)
cell91 = openmc.Cell(fill=matifba)
cell91.region = +cyl90 & -cyl91 & +bndw
cell92 = openmc.Cell(fill=matair)
cell92.region = +cyl91 & -cyl92 & +bndw
cell93 = openmc.Cell(fill=matclad)
cell93.region = +cyl92 & -cyl93 & +bndw
cell94 = openmc.Cell(fill=matcool)
cell94.region = +cyl93 & +bndw & -px1 & -py2 & +py3
biguni.add_cell(cell90)
biguni.add_cell(cell91)
biguni.add_cell(cell92)
biguni.add_cell(cell93)
biguni.add_cell(cell94)
# rod number (10,11)
x=  1.260000
y=  8.230000
cyl95 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl96 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl97 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell95 = openmc.Cell(fill=matfuel01)
cell95.region = -cyl95
fuel_cell_list.append(cell95.id)
cell96 = openmc.Cell(fill=matair)
cell96.region = +cyl95 & -cyl96
cell97 = openmc.Cell(fill=matclad)
cell97.region = +cyl96 & -cyl97
cell98 = openmc.Cell(fill=matcool)
cell98.region = +cyl97 & +px1 & -px2 & -py2 & +py3
biguni.add_cell(cell95)
biguni.add_cell(cell96)
biguni.add_cell(cell97)
biguni.add_cell(cell98)
# rod number (11,11)
x=  2.520000
y=  8.230000
cyl99 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl100 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl101 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell99 = openmc.Cell(fill=matfuel01)
cell99.region = -cyl99
fuel_cell_list.append(cell99.id)
cell100 = openmc.Cell(fill=matair)
cell100.region = +cyl99 & -cyl100
cell101 = openmc.Cell(fill=matclad)
cell101.region = +cyl100 & -cyl101
cell102 = openmc.Cell(fill=matcool)
cell102.region = +cyl101 & +px2 & -px3 & -py2 & +py3
biguni.add_cell(cell99)
biguni.add_cell(cell100)
biguni.add_cell(cell101)
biguni.add_cell(cell102)
# rod number (12,11)
x=  3.780000
y=  8.230000
cyl103 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl104 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl105 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl106 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell103 = openmc.Cell(fill=matfuel01)
cell103.region = -cyl103
fuel_cell_list.append(cell103.id)
cell104 = openmc.Cell(fill=matifba)
cell104.region = +cyl103 & -cyl104
cell105 = openmc.Cell(fill=matair)
cell105.region = +cyl104 & -cyl105
cell106 = openmc.Cell(fill=matclad)
cell106.region = +cyl105 & -cyl106
cell107 = openmc.Cell(fill=matcool)
cell107.region = +cyl106 & +px3 & -px4 & -py2 & +py3
biguni.add_cell(cell103)
biguni.add_cell(cell104)
biguni.add_cell(cell105)
biguni.add_cell(cell106)
biguni.add_cell(cell107)
# rod number (13,11)
x=  5.040000
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
cell111.region = +cyl110 & +px4 & -px5 & -py2 & +py3
biguni.add_cell(cell108)
biguni.add_cell(cell109)
biguni.add_cell(cell110)
biguni.add_cell(cell111)
# rod number (14,11)
x=  6.300000
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
cell115.region = +cyl114 & +px5 & -px6 & -py2 & +py3
biguni.add_cell(cell112)
biguni.add_cell(cell113)
biguni.add_cell(cell114)
biguni.add_cell(cell115)
# rod number (15,11)
x=  7.560000
y=  8.230000
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
cell120.region = +cyl119 & +px6 & -px7 & -py2 & +py3
biguni.add_cell(cell116)
biguni.add_cell(cell117)
biguni.add_cell(cell118)
biguni.add_cell(cell119)
biguni.add_cell(cell120)
# rod number (16,11)
x=  8.820000
y=  8.230000
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
cell124.region = +cyl123 & +px7 & -px8 & -py2 & +py3
biguni.add_cell(cell121)
biguni.add_cell(cell122)
biguni.add_cell(cell123)
biguni.add_cell(cell124)
# rod number (17,11)
x= 10.080000
y=  8.230000
cyl125 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl126 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl127 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell125 = openmc.Cell(fill=matfuel01)
cell125.region = -cyl125
fuel_cell_list.append(cell125.id)
cell126 = openmc.Cell(fill=matair)
cell126.region = +cyl125 & -cyl126
cell127 = openmc.Cell(fill=matclad)
cell127.region = +cyl126 & -cyl127
cell128 = openmc.Cell(fill=matcool)
cell128.region = +cyl127 & +px8 & -bnde & -py2 & +py3
biguni.add_cell(cell125)
biguni.add_cell(cell126)
biguni.add_cell(cell127)
biguni.add_cell(cell128)
# rod number (9,12)
x=  0.000000
y=  6.970000
cyl129 = openmc.ZCylinder(x0=x, y0=y, r= 0.28600)  # MOD
cyl130 = openmc.ZCylinder(x0=x, y0=y, r= 0.33900)  # CLAD
cyl131 = openmc.ZCylinder(x0=x, y0=y, r= 0.35300)  # AIR
cyl132 = openmc.ZCylinder(x0=x, y0=y, r= 0.40400)  # WABA
cyl133 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl134 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # CLAD
cyl135 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl136 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell129 = openmc.Cell(fill=matmod)
cell129.region = -cyl129 & +bndw
cell130 = openmc.Cell(fill=matclad)
cell130.region = +cyl129 & -cyl130 & +bndw
cell131 = openmc.Cell(fill=matair)
cell131.region = +cyl130 & -cyl131 & +bndw
cell132 = openmc.Cell(fill=matwaba)
cell132.region = +cyl131 & -cyl132 & +bndw
cell133 = openmc.Cell(fill=matair)
cell133.region = +cyl132 & -cyl133 & +bndw
cell134 = openmc.Cell(fill=matclad)
cell134.region = +cyl133 & -cyl134 & +bndw
cell135 = openmc.Cell(fill=matmod)
cell135.region = +cyl134 & -cyl135 & +bndw
cell136 = openmc.Cell(fill=matclad)
cell136.region = +cyl135 & -cyl136 & +bndw
cell137 = openmc.Cell(fill=matcool)
cell137.region = +cyl136 & +bndw & -px1 & -py3 & +py4
biguni.add_cell(cell129)
biguni.add_cell(cell130)
biguni.add_cell(cell131)
biguni.add_cell(cell132)
biguni.add_cell(cell133)
biguni.add_cell(cell134)
biguni.add_cell(cell135)
biguni.add_cell(cell136)
biguni.add_cell(cell137)
# rod number (10,12)
x=  1.260000
y=  6.970000
cyl138 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl139 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl140 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl141 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell138 = openmc.Cell(fill=matfuel01)
cell138.region = -cyl138
fuel_cell_list.append(cell138.id)
cell139 = openmc.Cell(fill=matifba)
cell139.region = +cyl138 & -cyl139
cell140 = openmc.Cell(fill=matair)
cell140.region = +cyl139 & -cyl140
cell141 = openmc.Cell(fill=matclad)
cell141.region = +cyl140 & -cyl141
cell142 = openmc.Cell(fill=matcool)
cell142.region = +cyl141 & +px1 & -px2 & -py3 & +py4
biguni.add_cell(cell138)
biguni.add_cell(cell139)
biguni.add_cell(cell140)
biguni.add_cell(cell141)
biguni.add_cell(cell142)
# rod number (11,12)
x=  2.520000
y=  6.970000
cyl143 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl144 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl145 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl146 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell143 = openmc.Cell(fill=matfuel01)
cell143.region = -cyl143
fuel_cell_list.append(cell143.id)
cell144 = openmc.Cell(fill=matifba)
cell144.region = +cyl143 & -cyl144
cell145 = openmc.Cell(fill=matair)
cell145.region = +cyl144 & -cyl145
cell146 = openmc.Cell(fill=matclad)
cell146.region = +cyl145 & -cyl146
cell147 = openmc.Cell(fill=matcool)
cell147.region = +cyl146 & +px2 & -px3 & -py3 & +py4
biguni.add_cell(cell143)
biguni.add_cell(cell144)
biguni.add_cell(cell145)
biguni.add_cell(cell146)
biguni.add_cell(cell147)
# rod number (12,12)
x=  3.780000
y=  6.970000
cyl148 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl149 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell148 = openmc.Cell(fill=matmod)
cell148.region = -cyl148
cell149 = openmc.Cell(fill=matclad)
cell149.region = +cyl148 & -cyl149
cell150 = openmc.Cell(fill=matcool)
cell150.region = +cyl149 & +px3 & -px4 & -py3 & +py4
biguni.add_cell(cell148)
biguni.add_cell(cell149)
biguni.add_cell(cell150)
# rod number (13,12)
x=  5.040000
y=  6.970000
cyl151 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl152 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl153 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl154 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell151 = openmc.Cell(fill=matfuel01)
cell151.region = -cyl151
fuel_cell_list.append(cell151.id)
cell152 = openmc.Cell(fill=matifba)
cell152.region = +cyl151 & -cyl152
cell153 = openmc.Cell(fill=matair)
cell153.region = +cyl152 & -cyl153
cell154 = openmc.Cell(fill=matclad)
cell154.region = +cyl153 & -cyl154
cell155 = openmc.Cell(fill=matcool)
cell155.region = +cyl154 & +px4 & -px5 & -py3 & +py4
biguni.add_cell(cell151)
biguni.add_cell(cell152)
biguni.add_cell(cell153)
biguni.add_cell(cell154)
biguni.add_cell(cell155)
# rod number (14,12)
x=  6.300000
y=  6.970000
cyl156 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl157 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl158 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl159 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell156 = openmc.Cell(fill=matfuel01)
cell156.region = -cyl156
fuel_cell_list.append(cell156.id)
cell157 = openmc.Cell(fill=matifba)
cell157.region = +cyl156 & -cyl157
cell158 = openmc.Cell(fill=matair)
cell158.region = +cyl157 & -cyl158
cell159 = openmc.Cell(fill=matclad)
cell159.region = +cyl158 & -cyl159
cell160 = openmc.Cell(fill=matcool)
cell160.region = +cyl159 & +px5 & -px6 & -py3 & +py4
biguni.add_cell(cell156)
biguni.add_cell(cell157)
biguni.add_cell(cell158)
biguni.add_cell(cell159)
biguni.add_cell(cell160)
# rod number (15,12)
x=  7.560000
y=  6.970000
cyl161 = openmc.ZCylinder(x0=x, y0=y, r= 0.28600)  # MOD
cyl162 = openmc.ZCylinder(x0=x, y0=y, r= 0.33900)  # CLAD
cyl163 = openmc.ZCylinder(x0=x, y0=y, r= 0.35300)  # AIR
cyl164 = openmc.ZCylinder(x0=x, y0=y, r= 0.40400)  # WABA
cyl165 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl166 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # CLAD
cyl167 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl168 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell161 = openmc.Cell(fill=matmod)
cell161.region = -cyl161
cell162 = openmc.Cell(fill=matclad)
cell162.region = +cyl161 & -cyl162
cell163 = openmc.Cell(fill=matair)
cell163.region = +cyl162 & -cyl163
cell164 = openmc.Cell(fill=matwaba)
cell164.region = +cyl163 & -cyl164
cell165 = openmc.Cell(fill=matair)
cell165.region = +cyl164 & -cyl165
cell166 = openmc.Cell(fill=matclad)
cell166.region = +cyl165 & -cyl166
cell167 = openmc.Cell(fill=matmod)
cell167.region = +cyl166 & -cyl167
cell168 = openmc.Cell(fill=matclad)
cell168.region = +cyl167 & -cyl168
cell169 = openmc.Cell(fill=matcool)
cell169.region = +cyl168 & +px6 & -px7 & -py3 & +py4
biguni.add_cell(cell161)
biguni.add_cell(cell162)
biguni.add_cell(cell163)
biguni.add_cell(cell164)
biguni.add_cell(cell165)
biguni.add_cell(cell166)
biguni.add_cell(cell167)
biguni.add_cell(cell168)
biguni.add_cell(cell169)
# rod number (16,12)
x=  8.820000
y=  6.970000
cyl170 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl171 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl172 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl173 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell170 = openmc.Cell(fill=matfuel01)
cell170.region = -cyl170
fuel_cell_list.append(cell170.id)
cell171 = openmc.Cell(fill=matifba)
cell171.region = +cyl170 & -cyl171
cell172 = openmc.Cell(fill=matair)
cell172.region = +cyl171 & -cyl172
cell173 = openmc.Cell(fill=matclad)
cell173.region = +cyl172 & -cyl173
cell174 = openmc.Cell(fill=matcool)
cell174.region = +cyl173 & +px7 & -px8 & -py3 & +py4
biguni.add_cell(cell170)
biguni.add_cell(cell171)
biguni.add_cell(cell172)
biguni.add_cell(cell173)
biguni.add_cell(cell174)
# rod number (17,12)
x= 10.080000
y=  6.970000
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
cell178.region = +cyl177 & +px8 & -bnde & -py3 & +py4
biguni.add_cell(cell175)
biguni.add_cell(cell176)
biguni.add_cell(cell177)
biguni.add_cell(cell178)
# rod number (9,13)
x=  0.000000
y=  5.710000
cyl179 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl180 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl181 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl182 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell179 = openmc.Cell(fill=matfuel01)
cell179.region = -cyl179 & +bndw
fuel_cell_list.append(cell179.id)
cell180 = openmc.Cell(fill=matifba)
cell180.region = +cyl179 & -cyl180 & +bndw
cell181 = openmc.Cell(fill=matair)
cell181.region = +cyl180 & -cyl181 & +bndw
cell182 = openmc.Cell(fill=matclad)
cell182.region = +cyl181 & -cyl182 & +bndw
cell183 = openmc.Cell(fill=matcool)
cell183.region = +cyl182 & +bndw & -px1 & -py4 & +py5
biguni.add_cell(cell179)
biguni.add_cell(cell180)
biguni.add_cell(cell181)
biguni.add_cell(cell182)
biguni.add_cell(cell183)
# rod number (10,13)
x=  1.260000
y=  5.710000
cyl184 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl185 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl186 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell184 = openmc.Cell(fill=matfuel01)
cell184.region = -cyl184
fuel_cell_list.append(cell184.id)
cell185 = openmc.Cell(fill=matair)
cell185.region = +cyl184 & -cyl185
cell186 = openmc.Cell(fill=matclad)
cell186.region = +cyl185 & -cyl186
cell187 = openmc.Cell(fill=matcool)
cell187.region = +cyl186 & +px1 & -px2 & -py4 & +py5
biguni.add_cell(cell184)
biguni.add_cell(cell185)
biguni.add_cell(cell186)
biguni.add_cell(cell187)
# rod number (11,13)
x=  2.520000
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
cell191.region = +cyl190 & +px2 & -px3 & -py4 & +py5
biguni.add_cell(cell188)
biguni.add_cell(cell189)
biguni.add_cell(cell190)
biguni.add_cell(cell191)
# rod number (12,13)
x=  3.780000
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
cell196.region = +cyl195 & +px3 & -px4 & -py4 & +py5
biguni.add_cell(cell192)
biguni.add_cell(cell193)
biguni.add_cell(cell194)
biguni.add_cell(cell195)
biguni.add_cell(cell196)
# rod number (13,13)
x=  5.040000
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
cell200.region = +cyl199 & +px4 & -px5 & -py4 & +py5
biguni.add_cell(cell197)
biguni.add_cell(cell198)
biguni.add_cell(cell199)
biguni.add_cell(cell200)
# rod number (14,13)
x=  6.300000
y=  5.710000
cyl201 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl202 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl203 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl204 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell201 = openmc.Cell(fill=matfuel01)
cell201.region = -cyl201
fuel_cell_list.append(cell201.id)
cell202 = openmc.Cell(fill=matifba)
cell202.region = +cyl201 & -cyl202
cell203 = openmc.Cell(fill=matair)
cell203.region = +cyl202 & -cyl203
cell204 = openmc.Cell(fill=matclad)
cell204.region = +cyl203 & -cyl204
cell205 = openmc.Cell(fill=matcool)
cell205.region = +cyl204 & +px5 & -px6 & -py4 & +py5
biguni.add_cell(cell201)
biguni.add_cell(cell202)
biguni.add_cell(cell203)
biguni.add_cell(cell204)
biguni.add_cell(cell205)
# rod number (15,13)
x=  7.560000
y=  5.710000
cyl206 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl207 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl208 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl209 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell206 = openmc.Cell(fill=matfuel01)
cell206.region = -cyl206
fuel_cell_list.append(cell206.id)
cell207 = openmc.Cell(fill=matifba)
cell207.region = +cyl206 & -cyl207
cell208 = openmc.Cell(fill=matair)
cell208.region = +cyl207 & -cyl208
cell209 = openmc.Cell(fill=matclad)
cell209.region = +cyl208 & -cyl209
cell210 = openmc.Cell(fill=matcool)
cell210.region = +cyl209 & +px6 & -px7 & -py4 & +py5
biguni.add_cell(cell206)
biguni.add_cell(cell207)
biguni.add_cell(cell208)
biguni.add_cell(cell209)
biguni.add_cell(cell210)
# rod number (16,13)
x=  8.820000
y=  5.710000
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
cell214.region = +cyl213 & +px7 & -px8 & -py4 & +py5
biguni.add_cell(cell211)
biguni.add_cell(cell212)
biguni.add_cell(cell213)
biguni.add_cell(cell214)
# rod number (17,13)
x= 10.080000
y=  5.710000
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
cell218.region = +cyl217 & +px8 & -bnde & -py4 & +py5
biguni.add_cell(cell215)
biguni.add_cell(cell216)
biguni.add_cell(cell217)
biguni.add_cell(cell218)
# rod number (9,14)
x=  0.000000
y=  4.450000
cyl219 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl220 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl221 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl222 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell219 = openmc.Cell(fill=matfuel01)
cell219.region = -cyl219 & +bndw
fuel_cell_list.append(cell219.id)
cell220 = openmc.Cell(fill=matifba)
cell220.region = +cyl219 & -cyl220 & +bndw
cell221 = openmc.Cell(fill=matair)
cell221.region = +cyl220 & -cyl221 & +bndw
cell222 = openmc.Cell(fill=matclad)
cell222.region = +cyl221 & -cyl222 & +bndw
cell223 = openmc.Cell(fill=matcool)
cell223.region = +cyl222 & +bndw & -px1 & -py5 & +py6
biguni.add_cell(cell219)
biguni.add_cell(cell220)
biguni.add_cell(cell221)
biguni.add_cell(cell222)
biguni.add_cell(cell223)
# rod number (10,14)
x=  1.260000
y=  4.450000
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
cell227.region = +cyl226 & +px1 & -px2 & -py5 & +py6
biguni.add_cell(cell224)
biguni.add_cell(cell225)
biguni.add_cell(cell226)
biguni.add_cell(cell227)
# rod number (11,14)
x=  2.520000
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
cell231.region = +cyl230 & +px2 & -px3 & -py5 & +py6
biguni.add_cell(cell228)
biguni.add_cell(cell229)
biguni.add_cell(cell230)
biguni.add_cell(cell231)
# rod number (12,14)
x=  3.780000
y=  4.450000
cyl232 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl233 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl234 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl235 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell232 = openmc.Cell(fill=matfuel01)
cell232.region = -cyl232
fuel_cell_list.append(cell232.id)
cell233 = openmc.Cell(fill=matifba)
cell233.region = +cyl232 & -cyl233
cell234 = openmc.Cell(fill=matair)
cell234.region = +cyl233 & -cyl234
cell235 = openmc.Cell(fill=matclad)
cell235.region = +cyl234 & -cyl235
cell236 = openmc.Cell(fill=matcool)
cell236.region = +cyl235 & +px3 & -px4 & -py5 & +py6
biguni.add_cell(cell232)
biguni.add_cell(cell233)
biguni.add_cell(cell234)
biguni.add_cell(cell235)
biguni.add_cell(cell236)
# rod number (13,14)
x=  5.040000
y=  4.450000
cyl237 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl238 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl239 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl240 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell237 = openmc.Cell(fill=matfuel01)
cell237.region = -cyl237
fuel_cell_list.append(cell237.id)
cell238 = openmc.Cell(fill=matifba)
cell238.region = +cyl237 & -cyl238
cell239 = openmc.Cell(fill=matair)
cell239.region = +cyl238 & -cyl239
cell240 = openmc.Cell(fill=matclad)
cell240.region = +cyl239 & -cyl240
cell241 = openmc.Cell(fill=matcool)
cell241.region = +cyl240 & +px4 & -px5 & -py5 & +py6
biguni.add_cell(cell237)
biguni.add_cell(cell238)
biguni.add_cell(cell239)
biguni.add_cell(cell240)
biguni.add_cell(cell241)
# rod number (14,14)
x=  6.300000
y=  4.450000
cyl242 = openmc.ZCylinder(x0=x, y0=y, r= 0.28600)  # MOD
cyl243 = openmc.ZCylinder(x0=x, y0=y, r= 0.33900)  # CLAD
cyl244 = openmc.ZCylinder(x0=x, y0=y, r= 0.35300)  # AIR
cyl245 = openmc.ZCylinder(x0=x, y0=y, r= 0.40400)  # WABA
cyl246 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl247 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # CLAD
cyl248 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl249 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell242 = openmc.Cell(fill=matmod)
cell242.region = -cyl242
cell243 = openmc.Cell(fill=matclad)
cell243.region = +cyl242 & -cyl243
cell244 = openmc.Cell(fill=matair)
cell244.region = +cyl243 & -cyl244
cell245 = openmc.Cell(fill=matwaba)
cell245.region = +cyl244 & -cyl245
cell246 = openmc.Cell(fill=matair)
cell246.region = +cyl245 & -cyl246
cell247 = openmc.Cell(fill=matclad)
cell247.region = +cyl246 & -cyl247
cell248 = openmc.Cell(fill=matmod)
cell248.region = +cyl247 & -cyl248
cell249 = openmc.Cell(fill=matclad)
cell249.region = +cyl248 & -cyl249
cell250 = openmc.Cell(fill=matcool)
cell250.region = +cyl249 & +px5 & -px6 & -py5 & +py6
biguni.add_cell(cell242)
biguni.add_cell(cell243)
biguni.add_cell(cell244)
biguni.add_cell(cell245)
biguni.add_cell(cell246)
biguni.add_cell(cell247)
biguni.add_cell(cell248)
biguni.add_cell(cell249)
biguni.add_cell(cell250)
# rod number (15,14)
x=  7.560000
y=  4.450000
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
cell255.region = +cyl254 & +px6 & -px7 & -py5 & +py6
biguni.add_cell(cell251)
biguni.add_cell(cell252)
biguni.add_cell(cell253)
biguni.add_cell(cell254)
biguni.add_cell(cell255)
# rod number (16,14)
x=  8.820000
y=  4.450000
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
cell259.region = +cyl258 & +px7 & -px8 & -py5 & +py6
biguni.add_cell(cell256)
biguni.add_cell(cell257)
biguni.add_cell(cell258)
biguni.add_cell(cell259)
# rod number (17,14)
x= 10.080000
y=  4.450000
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
cell263.region = +cyl262 & +px8 & -bnde & -py5 & +py6
biguni.add_cell(cell260)
biguni.add_cell(cell261)
biguni.add_cell(cell262)
biguni.add_cell(cell263)
# rod number (9,15)
x=  0.000000
y=  3.190000
cyl264 = openmc.ZCylinder(x0=x, y0=y, r= 0.28600)  # MOD
cyl265 = openmc.ZCylinder(x0=x, y0=y, r= 0.33900)  # CLAD
cyl266 = openmc.ZCylinder(x0=x, y0=y, r= 0.35300)  # AIR
cyl267 = openmc.ZCylinder(x0=x, y0=y, r= 0.40400)  # WABA
cyl268 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl269 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # CLAD
cyl270 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl271 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell264 = openmc.Cell(fill=matmod)
cell264.region = -cyl264 & +bndw
cell265 = openmc.Cell(fill=matclad)
cell265.region = +cyl264 & -cyl265 & +bndw
cell266 = openmc.Cell(fill=matair)
cell266.region = +cyl265 & -cyl266 & +bndw
cell267 = openmc.Cell(fill=matwaba)
cell267.region = +cyl266 & -cyl267 & +bndw
cell268 = openmc.Cell(fill=matair)
cell268.region = +cyl267 & -cyl268 & +bndw
cell269 = openmc.Cell(fill=matclad)
cell269.region = +cyl268 & -cyl269 & +bndw
cell270 = openmc.Cell(fill=matmod)
cell270.region = +cyl269 & -cyl270 & +bndw
cell271 = openmc.Cell(fill=matclad)
cell271.region = +cyl270 & -cyl271 & +bndw
cell272 = openmc.Cell(fill=matcool)
cell272.region = +cyl271 & +bndw & -px1 & -py6 & +py7
biguni.add_cell(cell264)
biguni.add_cell(cell265)
biguni.add_cell(cell266)
biguni.add_cell(cell267)
biguni.add_cell(cell268)
biguni.add_cell(cell269)
biguni.add_cell(cell270)
biguni.add_cell(cell271)
biguni.add_cell(cell272)
# rod number (10,15)
x=  1.260000
y=  3.190000
cyl273 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl274 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl275 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl276 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell273 = openmc.Cell(fill=matfuel01)
cell273.region = -cyl273
fuel_cell_list.append(cell273.id)
cell274 = openmc.Cell(fill=matifba)
cell274.region = +cyl273 & -cyl274
cell275 = openmc.Cell(fill=matair)
cell275.region = +cyl274 & -cyl275
cell276 = openmc.Cell(fill=matclad)
cell276.region = +cyl275 & -cyl276
cell277 = openmc.Cell(fill=matcool)
cell277.region = +cyl276 & +px1 & -px2 & -py6 & +py7
biguni.add_cell(cell273)
biguni.add_cell(cell274)
biguni.add_cell(cell275)
biguni.add_cell(cell276)
biguni.add_cell(cell277)
# rod number (11,15)
x=  2.520000
y=  3.190000
cyl278 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl279 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl280 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl281 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell278 = openmc.Cell(fill=matfuel01)
cell278.region = -cyl278
fuel_cell_list.append(cell278.id)
cell279 = openmc.Cell(fill=matifba)
cell279.region = +cyl278 & -cyl279
cell280 = openmc.Cell(fill=matair)
cell280.region = +cyl279 & -cyl280
cell281 = openmc.Cell(fill=matclad)
cell281.region = +cyl280 & -cyl281
cell282 = openmc.Cell(fill=matcool)
cell282.region = +cyl281 & +px2 & -px3 & -py6 & +py7
biguni.add_cell(cell278)
biguni.add_cell(cell279)
biguni.add_cell(cell280)
biguni.add_cell(cell281)
biguni.add_cell(cell282)
# rod number (12,15)
x=  3.780000
y=  3.190000
cyl283 = openmc.ZCylinder(x0=x, y0=y, r= 0.28600)  # MOD
cyl284 = openmc.ZCylinder(x0=x, y0=y, r= 0.33900)  # CLAD
cyl285 = openmc.ZCylinder(x0=x, y0=y, r= 0.35300)  # AIR
cyl286 = openmc.ZCylinder(x0=x, y0=y, r= 0.40400)  # WABA
cyl287 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl288 = openmc.ZCylinder(x0=x, y0=y, r= 0.48400)  # CLAD
cyl289 = openmc.ZCylinder(x0=x, y0=y, r= 0.56100)  # MOD
cyl290 = openmc.ZCylinder(x0=x, y0=y, r= 0.60200)  # CLAD
cell283 = openmc.Cell(fill=matmod)
cell283.region = -cyl283
cell284 = openmc.Cell(fill=matclad)
cell284.region = +cyl283 & -cyl284
cell285 = openmc.Cell(fill=matair)
cell285.region = +cyl284 & -cyl285
cell286 = openmc.Cell(fill=matwaba)
cell286.region = +cyl285 & -cyl286
cell287 = openmc.Cell(fill=matair)
cell287.region = +cyl286 & -cyl287
cell288 = openmc.Cell(fill=matclad)
cell288.region = +cyl287 & -cyl288
cell289 = openmc.Cell(fill=matmod)
cell289.region = +cyl288 & -cyl289
cell290 = openmc.Cell(fill=matclad)
cell290.region = +cyl289 & -cyl290
cell291 = openmc.Cell(fill=matcool)
cell291.region = +cyl290 & +px3 & -px4 & -py6 & +py7
biguni.add_cell(cell283)
biguni.add_cell(cell284)
biguni.add_cell(cell285)
biguni.add_cell(cell286)
biguni.add_cell(cell287)
biguni.add_cell(cell288)
biguni.add_cell(cell289)
biguni.add_cell(cell290)
biguni.add_cell(cell291)
# rod number (13,15)
x=  5.040000
y=  3.190000
cyl292 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl293 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl294 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl295 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell292 = openmc.Cell(fill=matfuel01)
cell292.region = -cyl292
fuel_cell_list.append(cell292.id)
cell293 = openmc.Cell(fill=matifba)
cell293.region = +cyl292 & -cyl293
cell294 = openmc.Cell(fill=matair)
cell294.region = +cyl293 & -cyl294
cell295 = openmc.Cell(fill=matclad)
cell295.region = +cyl294 & -cyl295
cell296 = openmc.Cell(fill=matcool)
cell296.region = +cyl295 & +px4 & -px5 & -py6 & +py7
biguni.add_cell(cell292)
biguni.add_cell(cell293)
biguni.add_cell(cell294)
biguni.add_cell(cell295)
biguni.add_cell(cell296)
# rod number (14,15)
x=  6.300000
y=  3.190000
cyl297 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl298 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl299 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl300 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell297 = openmc.Cell(fill=matfuel01)
cell297.region = -cyl297
fuel_cell_list.append(cell297.id)
cell298 = openmc.Cell(fill=matifba)
cell298.region = +cyl297 & -cyl298
cell299 = openmc.Cell(fill=matair)
cell299.region = +cyl298 & -cyl299
cell300 = openmc.Cell(fill=matclad)
cell300.region = +cyl299 & -cyl300
cell301 = openmc.Cell(fill=matcool)
cell301.region = +cyl300 & +px5 & -px6 & -py6 & +py7
biguni.add_cell(cell297)
biguni.add_cell(cell298)
biguni.add_cell(cell299)
biguni.add_cell(cell300)
biguni.add_cell(cell301)
# rod number (15,15)
x=  7.560000
y=  3.190000
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
cell305.region = +cyl304 & +px6 & -px7 & -py6 & +py7
biguni.add_cell(cell302)
biguni.add_cell(cell303)
biguni.add_cell(cell304)
biguni.add_cell(cell305)
# rod number (16,15)
x=  8.820000
y=  3.190000
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
cell309.region = +cyl308 & +px7 & -px8 & -py6 & +py7
biguni.add_cell(cell306)
biguni.add_cell(cell307)
biguni.add_cell(cell308)
biguni.add_cell(cell309)
# rod number (17,15)
x= 10.080000
y=  3.190000
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
cell313.region = +cyl312 & +px8 & -bnde & -py6 & +py7
biguni.add_cell(cell310)
biguni.add_cell(cell311)
biguni.add_cell(cell312)
biguni.add_cell(cell313)
# rod number (9,16)
x=  0.000000
y=  1.930000
cyl314 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl315 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl316 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl317 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell314 = openmc.Cell(fill=matfuel01)
cell314.region = -cyl314 & +bndw
fuel_cell_list.append(cell314.id)
cell315 = openmc.Cell(fill=matifba)
cell315.region = +cyl314 & -cyl315 & +bndw
cell316 = openmc.Cell(fill=matair)
cell316.region = +cyl315 & -cyl316 & +bndw
cell317 = openmc.Cell(fill=matclad)
cell317.region = +cyl316 & -cyl317 & +bndw
cell318 = openmc.Cell(fill=matcool)
cell318.region = +cyl317 & +bndw & -px1 & -py7 & +py8
biguni.add_cell(cell314)
biguni.add_cell(cell315)
biguni.add_cell(cell316)
biguni.add_cell(cell317)
biguni.add_cell(cell318)
# rod number (10,16)
x=  1.260000
y=  1.930000
cyl319 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl320 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl321 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell319 = openmc.Cell(fill=matfuel01)
cell319.region = -cyl319
fuel_cell_list.append(cell319.id)
cell320 = openmc.Cell(fill=matair)
cell320.region = +cyl319 & -cyl320
cell321 = openmc.Cell(fill=matclad)
cell321.region = +cyl320 & -cyl321
cell322 = openmc.Cell(fill=matcool)
cell322.region = +cyl321 & +px1 & -px2 & -py7 & +py8
biguni.add_cell(cell319)
biguni.add_cell(cell320)
biguni.add_cell(cell321)
biguni.add_cell(cell322)
# rod number (11,16)
x=  2.520000
y=  1.930000
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
cell326.region = +cyl325 & +px2 & -px3 & -py7 & +py8
biguni.add_cell(cell323)
biguni.add_cell(cell324)
biguni.add_cell(cell325)
biguni.add_cell(cell326)
# rod number (12,16)
x=  3.780000
y=  1.930000
cyl327 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl328 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl329 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl330 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell327 = openmc.Cell(fill=matfuel01)
cell327.region = -cyl327
fuel_cell_list.append(cell327.id)
cell328 = openmc.Cell(fill=matifba)
cell328.region = +cyl327 & -cyl328
cell329 = openmc.Cell(fill=matair)
cell329.region = +cyl328 & -cyl329
cell330 = openmc.Cell(fill=matclad)
cell330.region = +cyl329 & -cyl330
cell331 = openmc.Cell(fill=matcool)
cell331.region = +cyl330 & +px3 & -px4 & -py7 & +py8
biguni.add_cell(cell327)
biguni.add_cell(cell328)
biguni.add_cell(cell329)
biguni.add_cell(cell330)
biguni.add_cell(cell331)
# rod number (13,16)
x=  5.040000
y=  1.930000
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
cell335.region = +cyl334 & +px4 & -px5 & -py7 & +py8
biguni.add_cell(cell332)
biguni.add_cell(cell333)
biguni.add_cell(cell334)
biguni.add_cell(cell335)
# rod number (14,16)
x=  6.300000
y=  1.930000
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
cell339.region = +cyl338 & +px5 & -px6 & -py7 & +py8
biguni.add_cell(cell336)
biguni.add_cell(cell337)
biguni.add_cell(cell338)
biguni.add_cell(cell339)
# rod number (15,16)
x=  7.560000
y=  1.930000
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
cell343.region = +cyl342 & +px6 & -px7 & -py7 & +py8
biguni.add_cell(cell340)
biguni.add_cell(cell341)
biguni.add_cell(cell342)
biguni.add_cell(cell343)
# rod number (16,16)
x=  8.820000
y=  1.930000
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
cell347.region = +cyl346 & +px7 & -px8 & -py7 & +py8
biguni.add_cell(cell344)
biguni.add_cell(cell345)
biguni.add_cell(cell346)
biguni.add_cell(cell347)
# rod number (17,16)
x= 10.080000
y=  1.930000
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
cell351.region = +cyl350 & +px8 & -bnde & -py7 & +py8
biguni.add_cell(cell348)
biguni.add_cell(cell349)
biguni.add_cell(cell350)
biguni.add_cell(cell351)
# rod number (9,17)
x=  0.000000
y=  0.670000
cyl352 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl353 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl354 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell352 = openmc.Cell(fill=matfuel01)
cell352.region = -cyl352 & +bndw
fuel_cell_list.append(cell352.id)
cell353 = openmc.Cell(fill=matair)
cell353.region = +cyl352 & -cyl353 & +bndw
cell354 = openmc.Cell(fill=matclad)
cell354.region = +cyl353 & -cyl354 & +bndw
cell355 = openmc.Cell(fill=matcool)
cell355.region = +cyl354 & +bndw & -px1 & -py8 & +bnds
biguni.add_cell(cell352)
biguni.add_cell(cell353)
biguni.add_cell(cell354)
biguni.add_cell(cell355)
# rod number (10,17)
x=  1.260000
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
cell359.region = +cyl358 & +px1 & -px2 & -py8 & +bnds
biguni.add_cell(cell356)
biguni.add_cell(cell357)
biguni.add_cell(cell358)
biguni.add_cell(cell359)
# rod number (11,17)
x=  2.520000
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
cell363.region = +cyl362 & +px2 & -px3 & -py8 & +bnds
biguni.add_cell(cell360)
biguni.add_cell(cell361)
biguni.add_cell(cell362)
biguni.add_cell(cell363)
# rod number (12,17)
x=  3.780000
y=  0.670000
cyl364 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl365 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl366 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell364 = openmc.Cell(fill=matfuel01)
cell364.region = -cyl364
fuel_cell_list.append(cell364.id)
cell365 = openmc.Cell(fill=matair)
cell365.region = +cyl364 & -cyl365
cell366 = openmc.Cell(fill=matclad)
cell366.region = +cyl365 & -cyl366
cell367 = openmc.Cell(fill=matcool)
cell367.region = +cyl366 & +px3 & -px4 & -py8 & +bnds
biguni.add_cell(cell364)
biguni.add_cell(cell365)
biguni.add_cell(cell366)
biguni.add_cell(cell367)
# rod number (13,17)
x=  5.040000
y=  0.670000
cyl368 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl369 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl370 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell368 = openmc.Cell(fill=matfuel01)
cell368.region = -cyl368
fuel_cell_list.append(cell368.id)
cell369 = openmc.Cell(fill=matair)
cell369.region = +cyl368 & -cyl369
cell370 = openmc.Cell(fill=matclad)
cell370.region = +cyl369 & -cyl370
cell371 = openmc.Cell(fill=matcool)
cell371.region = +cyl370 & +px4 & -px5 & -py8 & +bnds
biguni.add_cell(cell368)
biguni.add_cell(cell369)
biguni.add_cell(cell370)
biguni.add_cell(cell371)
# rod number (14,17)
x=  6.300000
y=  0.670000
cyl372 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl373 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl374 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell372 = openmc.Cell(fill=matfuel01)
cell372.region = -cyl372
fuel_cell_list.append(cell372.id)
cell373 = openmc.Cell(fill=matair)
cell373.region = +cyl372 & -cyl373
cell374 = openmc.Cell(fill=matclad)
cell374.region = +cyl373 & -cyl374
cell375 = openmc.Cell(fill=matcool)
cell375.region = +cyl374 & +px5 & -px6 & -py8 & +bnds
biguni.add_cell(cell372)
biguni.add_cell(cell373)
biguni.add_cell(cell374)
biguni.add_cell(cell375)
# rod number (15,17)
x=  7.560000
y=  0.670000
cyl376 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl377 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl378 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell376 = openmc.Cell(fill=matfuel01)
cell376.region = -cyl376
fuel_cell_list.append(cell376.id)
cell377 = openmc.Cell(fill=matair)
cell377.region = +cyl376 & -cyl377
cell378 = openmc.Cell(fill=matclad)
cell378.region = +cyl377 & -cyl378
cell379 = openmc.Cell(fill=matcool)
cell379.region = +cyl378 & +px6 & -px7 & -py8 & +bnds
biguni.add_cell(cell376)
biguni.add_cell(cell377)
biguni.add_cell(cell378)
biguni.add_cell(cell379)
# rod number (16,17)
x=  8.820000
y=  0.670000
cyl380 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl381 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl382 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell380 = openmc.Cell(fill=matfuel01)
cell380.region = -cyl380
fuel_cell_list.append(cell380.id)
cell381 = openmc.Cell(fill=matair)
cell381.region = +cyl380 & -cyl381
cell382 = openmc.Cell(fill=matclad)
cell382.region = +cyl381 & -cyl382
cell383 = openmc.Cell(fill=matcool)
cell383.region = +cyl382 & +px7 & -px8 & -py8 & +bnds
biguni.add_cell(cell380)
biguni.add_cell(cell381)
biguni.add_cell(cell382)
biguni.add_cell(cell383)
# rod number (17,17)
x= 10.080000
y=  0.670000
cyl384 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl385 = openmc.ZCylinder(x0=x, y0=y, r= 0.41060)  # IFBA
cyl386 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl387 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell384 = openmc.Cell(fill=matfuel01)
cell384.region = -cyl384
fuel_cell_list.append(cell384.id)
cell385 = openmc.Cell(fill=matifba)
cell385.region = +cyl384 & -cyl385
cell386 = openmc.Cell(fill=matair)
cell386.region = +cyl385 & -cyl386
cell387 = openmc.Cell(fill=matclad)
cell387.region = +cyl386 & -cyl387
cell388 = openmc.Cell(fill=matcool)
cell388.region = +cyl387 & +px8 & -bnde & -py8 & +bnds
biguni.add_cell(cell384)
biguni.add_cell(cell385)
biguni.add_cell(cell386)
biguni.add_cell(cell387)
biguni.add_cell(cell388)

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
