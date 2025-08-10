import matplotlib

import openmc
import openmc.mgxs as mgxs
import openmc.data          # need for hdf5

#  To run:
#  >python3 mini2o_gad12.omc
#
#  OpenMC model of LWR reactor assembly
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
#  1  1  1  
#  1  1  1  
#  1  1  1  
# 
# FUEMAP
#  1  1  1
#  1  2  1
#  1  1  1
# 
biguni = openmc.Universe(name="biguni")
# boundary planes
bndn = openmc.YPlane(y0=  3.820000, boundary_type='reflective')
bnds = openmc.YPlane(y0=  0.000000, boundary_type='reflective')
bnde = openmc.XPlane(x0=  3.820000, boundary_type='reflective')
bndw = openmc.XPlane(x0=  0.000000, boundary_type='reflective')

# build up cells for coolant region
regcool = +bndw & -bnde & +bnds & -bndn

# rod number (1,1)
x=  0.650000
y=  3.170000
cyl1 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl2 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl3 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell1 = openmc.Cell(fill=matfuel01)
cell1.region = -cyl1
cell2 = openmc.Cell(fill=matair)
cell2.region = +cyl1 & -cyl2
cell3 = openmc.Cell(fill=matclad)
cell3.region = +cyl2 & -cyl3
biguni.add_cell(cell1)
biguni.add_cell(cell2)
biguni.add_cell(cell3)
regcool = regcool & +cyl3
# rod number (2,1)
x=  1.910000
y=  3.170000
cyl4 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl5 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl6 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell4 = openmc.Cell(fill=matfuel01)
cell4.region = -cyl4
cell5 = openmc.Cell(fill=matair)
cell5.region = +cyl4 & -cyl5
cell6 = openmc.Cell(fill=matclad)
cell6.region = +cyl5 & -cyl6
biguni.add_cell(cell4)
biguni.add_cell(cell5)
biguni.add_cell(cell6)
regcool = regcool & +cyl6
# rod number (3,1)
x=  3.170000
y=  3.170000
cyl7 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl8 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl9 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell7 = openmc.Cell(fill=matfuel01)
cell7.region = -cyl7
cell8 = openmc.Cell(fill=matair)
cell8.region = +cyl7 & -cyl8
cell9 = openmc.Cell(fill=matclad)
cell9.region = +cyl8 & -cyl9
biguni.add_cell(cell7)
biguni.add_cell(cell8)
biguni.add_cell(cell9)
regcool = regcool & +cyl9
# rod number (1,2)
x=  0.650000
y=  1.910000
cyl10 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl11 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl12 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell10 = openmc.Cell(fill=matfuel01)
cell10.region = -cyl10
cell11 = openmc.Cell(fill=matair)
cell11.region = +cyl10 & -cyl11
cell12 = openmc.Cell(fill=matclad)
cell12.region = +cyl11 & -cyl12
biguni.add_cell(cell10)
biguni.add_cell(cell11)
biguni.add_cell(cell12)
regcool = regcool & +cyl12
# rod number (2,2)
x=  1.910000
y=  1.910000
cyl13 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL02
cyl14 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl15 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cellgad = openmc.Cell(fill=matfuel02)
cellgad.region = -cyl13
cell14 = openmc.Cell(fill=matair)
cell14.region = +cyl13 & -cyl14
cell15 = openmc.Cell(fill=matclad)
cell15.region = +cyl14 & -cyl15
biguni.add_cell(cellgad)
biguni.add_cell(cell14)
biguni.add_cell(cell15)
regcool = regcool & +cyl15
# rod number (3,2)
x=  3.170000
y=  1.910000
cyl16 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl17 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl18 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell16 = openmc.Cell(fill=matfuel01)
cell16.region = -cyl16
cell17 = openmc.Cell(fill=matair)
cell17.region = +cyl16 & -cyl17
cell18 = openmc.Cell(fill=matclad)
cell18.region = +cyl17 & -cyl18
biguni.add_cell(cell16)
biguni.add_cell(cell17)
biguni.add_cell(cell18)
regcool = regcool & +cyl18
# rod number (1,3)
x=  0.650000
y=  0.650000
cyl19 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl20 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl21 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell19 = openmc.Cell(fill=matfuel01)
cell19.region = -cyl19
cell20 = openmc.Cell(fill=matair)
cell20.region = +cyl19 & -cyl20
cell21 = openmc.Cell(fill=matclad)
cell21.region = +cyl20 & -cyl21
biguni.add_cell(cell19)
biguni.add_cell(cell20)
biguni.add_cell(cell21)
regcool = regcool & +cyl21
# rod number (2,3)
x=  1.910000
y=  0.650000
cyl22 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl23 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl24 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell22 = openmc.Cell(fill=matfuel01)
cell22.region = -cyl22
cell23 = openmc.Cell(fill=matair)
cell23.region = +cyl22 & -cyl23
cell24 = openmc.Cell(fill=matclad)
cell24.region = +cyl23 & -cyl24
biguni.add_cell(cell22)
biguni.add_cell(cell23)
biguni.add_cell(cell24)
regcool = regcool & +cyl24
# rod number (3,3)
x=  3.170000
y=  0.650000
cyl25 = openmc.ZCylinder(x0=x, y0=y, r= 0.40960)  # FUEL01
cyl26 = openmc.ZCylinder(x0=x, y0=y, r= 0.41800)  # AIR
cyl27 = openmc.ZCylinder(x0=x, y0=y, r= 0.47500)  # CLAD
cell25 = openmc.Cell(fill=matfuel01)
cell25.region = -cyl25
cell26 = openmc.Cell(fill=matair)
cell26.region = +cyl25 & -cyl26
cell27 = openmc.Cell(fill=matclad)
cell27.region = +cyl26 & -cyl27
biguni.add_cell(cell25)
biguni.add_cell(cell26)
biguni.add_cell(cell27)
regcool = regcool & +cyl27
# coolant cell
cellcool = openmc.Cell(fill=matcool, region=regcool)
biguni.add_cell(cellcool)
# export geometry
model.geometry = openmc.Geometry(biguni)

# -------------- Plot ------------

model.export_to_xml()
plot1 = openmc.Plot()
plot1.basis = 'xy'
plot1.origin = (  1.920,  1.920, 0)
plot1.width = (  3.820,  3.820)
plot1.pixels = (400,400)
plot1.color_by = 'material'

plots = openmc.Plots([plot1])
plots.export_to_xml()
openmc.plot_geometry()

# OpenMC simulation parameters

lower_left  = [   0.0000,   0.0000,-20]
upper_right = [   3.8199,   3.8199, 20]
uniform_dist = openmc.stats.Box(lower_left, upper_right, only_fissionable=True)
src = openmc.Source(space=uniform_dist)

settings = openmc.Settings()
settings.source = src
settings.batches = 1000
settings.inactive = 100
settings.particles = 200000
settings.output = {'tallies': True}

model.settings = settings
#==================== Set up cross sections =======================

# Instantiate a "coarse" 2-group EnergyGroups object
coarse_groups = mgxs.EnergyGroups([0., 0.625, 20.0e6])

# Instantiate a "fine" 8-group EnergyGroups object
fine_groups = mgxs.EnergyGroups([0., 0.058, 0.14, 0.28,
                                 0.625, 4.0, 5.53e3, 821.0e3, 20.0e6])

# Initialize a 2-group MGXS Library for OpenMOC
mgxs_lib = openmc.mgxs.Library(model.geometry)
mgxs_lib.energy_groups = fine_groups

# Types of cross sections available:
#   TotalXS ("total")
#   TransportXS ("transport" or "nu-transport with nu set to True)
#   AbsorptionXS ("absorption")
#   CaptureXS ("capture")
#   FissionXS ("fission" or "nu-fission" with nu set to True)
#   KappaFissionXS ("kappa-fission")
#   ScatterXS ("scatter" or "nu-scatter" with nu set to True)
#   ScatterMatrixXS ("scatter matrix" or "nu-scatter matrix" with nu set to True)
#   Chi ("chi")
#   ChiPrompt ("chi prompt")
#   InverseVelocity ("inverse-velocity")
#   PromptNuFissionXS ("prompt-nu-fission")
#   DelayedNuFissionXS ("delayed-nu-fission")
#   ChiDelayed ("chi-delayed")
#   Beta ("beta")

# Specify multi-group cross section types to compute
mgxs_lib.mgxs_types = ['transport', 'total', 'capture', 'absorption', 'nu-fission', 'fission', 'kappa-fission', 'scatter matrix', 'chi']

# Specify a "cell" domain type for the cross section tally filters
mgxs_lib.domain_type = 'cell'

# Specify the cell domains over which to compute multi-group cross sections
# **** Note: users need to manually modify this list of cells they want edited
# **** Note: or call all cells
# mgxs_lib.domains = model.geometry.get_all_material_cells().values()
mgxs_lib.domains = [cellgad, cell16, cell17, cell18, cellcool]

for cell in mgxs_lib.domains:
    print ("generate cross sections for cell: ", cell.id, cell.name)

# Compute cross sections on a nuclide-by-nuclide basis  (not used here)
## mgxs_lib.by_nuclide = True

# Construct all tallies needed for the multi-group cross section library
mgxs_lib.build_library()

# Create a "tallies.xml" file for the MGXS Library  - "merge" to reduce number of tallies
tallies = openmc.Tallies()
mgxs_lib.add_to_tallies_file(tallies) # , merge=True)

model.tallies = tallies

#======================= Run ==========================

statepoint_file = model.run()
# ====================== Tallies ======================

# Load the last statepoint file
sp = openmc.StatePoint(statepoint_file)

# Retrieve OpenMC's k-effective value (used for edit at the end)
openmc_keff = sp.keff.nominal_value

# Initialize MGXS Library with OpenMC statepoint data
mgxs_lib.load_from_statepoint(sp)

# Store the cross section data in an "mgxs/mgxs.h5" HDF5 binary file
print ("creating HDF cross section file")
mgxs_lib.build_hdf5_store(filename='mgxs.h5')   # , directory='mgxs')

# finished
print ("OpenMC keff ", openmc_keff)
print ("done")
