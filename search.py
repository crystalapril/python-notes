# pip install python-dateutil

# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# [{'serial': 381 - x,
#   'date'  : (datetime(2018, 2, 1) - relativedelta(months = x)).isoformat()[:7],
#   'other' : '...'}
#  for x in range(14)]

sfw = [
  {'date': '2018-02', 'serial': 381, 'other': '...'},
  {'date': '2018-01', 'serial': 380, 'other': '...'},
  {'date': '2017-12', 'serial': 379, 'other': '...'},
  {'date': '2017-11', 'serial': 378, 'other': '...'},
  {'date': '2017-10', 'serial': 377, 'other': '...'},
  {'date': '2017-09', 'serial': 376, 'other': '...'},
  {'date': '2017-08', 'serial': 375, 'other': '...'},
  {'date': '2017-07', 'serial': 374, 'other': '...'},
  {'date': '2017-06', 'serial': 373, 'other': '...'},
  {'date': '2017-05', 'serial': 372, 'other': '...'},
  {'date': '2017-04', 'serial': 371, 'other': '...'},
  {'date': '2017-03', 'serial': 370, 'other': '...'},
  {'date': '2017-02', 'serial': 369, 'other': '...'},
  {'date': '2017-01', 'serial': 368, 'other': '...'},
]

def search_by_serial(books, serial):
    for x in books:
        if x['serial']==serial:
            return x
    return None

search_by_serial(sfw, 381) == {'date': '2018-02', 'serial': 381, 'other': '...'}
search_by_serial(sfw, 368) == {'date': '2017-01', 'serial': 368, 'other': '...'}
search_by_serial(sfw, 800) == None

def search_by_date(books, date):
    for x in books:
        if x['date']==date:
            return x
    return None

search_by_date(sfw, '2018-02') == {'date': '2018-02', 'serial': 381, 'other': '...'}
search_by_date(sfw, '2017-01') == {'date': '2017-01', 'serial': 368, 'other': '...'}
search_by_date(sfw, '1970-01') == None
search_by_date(sfw, '201802')  == None


# https://en.wikipedia.org/wiki/List_of_chemical_elements

element = [
  (1, 'H', 'Hydrogen'),
  (2, 'He', 'Helium'),
  (3, 'Li', 'Lithium'),
  (4, 'Be', 'Beryllium'),
  (5, 'B', 'Boron'),
  (6, 'C', 'Carbon'),
  (7, 'N', 'Nitrogen'),
  (8, 'O', 'Oxygen'),
  (9, 'F', 'Fluorine'),
  (10, 'Ne', 'Neon'),
  (11, 'Na', 'Sodium'),
  (12, 'Mg', 'Magnesium'),
  (13, 'Al', 'Aluminium'),
  (14, 'Si', 'Silicon'),
  (15, 'P', 'Phosphorus'),
  (16, 'S', 'Sulfur'),
  (17, 'Cl', 'Chlorine'),
  (18, 'Ar', 'Argon'),
  (19, 'K', 'Potassium'),
  (20, 'Ca', 'Calcium'),
  (21, 'Sc', 'Scandium'),
  (22, 'Ti', 'Titanium'),
  (23, 'V', 'Vanadium'),
  (24, 'Cr', 'Chromium'),
  (25, 'Mn', 'Manganese'),
  (26, 'Fe', 'Iron'),
  (27, 'Co', 'Cobalt'),
  (28, 'Ni', 'Nickel'),
  (29, 'Cu', 'Copper'),
  (30, 'Zn', 'Zinc'),
  (31, 'Ga', 'Gallium'),
  (32, 'Ge', 'Germanium'),
  (33, 'As', 'Arsenic'),
  (34, 'Se', 'Selenium'),
  (35, 'Br', 'Bromine'),
  (36, 'Kr', 'Krypton'),
  (37, 'Rb', 'Rubidium'),
  (38, 'Sr', 'Strontium'),
  (39, 'Y', 'Yttrium'),
  (40, 'Zr', 'Zirconium'),
  (41, 'Nb', 'Niobium'),
  (42, 'Mo', 'Molybdenum'),
  (43, 'Tc', 'Technetium'),
  (44, 'Ru', 'Ruthenium'),
  (45, 'Rh', 'Rhodium'),
  (46, 'Pd', 'Palladium'),
  (47, 'Ag', 'Silver'),
  (48, 'Cd', 'Cadmium'),
  (49, 'In', 'Indium'),
  (50, 'Sn', 'Tin'),
  (51, 'Sb', 'Antimony'),
  (52, 'Te', 'Tellurium'),
  (53, 'I', 'Iodine'),
  (54, 'Xe', 'Xenon'),
  (55, 'Cs', 'Caesium'),
  (56, 'Ba', 'Barium'),
  (57, 'La', 'Lanthanum'),
  (58, 'Ce', 'Cerium'),
  (59, 'Pr', 'Praseodymium'),
  (60, 'Nd', 'Neodymium'),
  (61, 'Pm', 'Promethium'),
  (62, 'Sm', 'Samarium'),
  (63, 'Eu', 'Europium'),
  (64, 'Gd', 'Gadolinium'),
  (65, 'Tb', 'Terbium'),
  (66, 'Dy', 'Dysprosium'),
  (67, 'Ho', 'Holmium'),
  (68, 'Er', 'Erbium'),
  (69, 'Tm', 'Thulium'),
  (70, 'Yb', 'Ytterbium'),
  (71, 'Lu', 'Lutetium'),
  (72, 'Hf', 'Hafnium'),
  (73, 'Ta', 'Tantalum'),
  (74, 'W', 'Tungsten'),
  (75, 'Re', 'Rhenium'),
  (76, 'Os', 'Osmium'),
  (77, 'Ir', 'Iridium'),
  (78, 'Pt', 'Platinum'),
  (79, 'Au', 'Gold'),
  (80, 'Hg', 'Mercury'),
  (81, 'Tl', 'Thallium'),
  (82, 'Pb', 'Lead'),
  (83, 'Bi', 'Bismuth'),
  (84, 'Po', 'Polonium'),
  (85, 'At', 'Astatine'),
  (86, 'Rn', 'Radon'),
  (87, 'Fr', 'Francium'),
  (88, 'Ra', 'Radium'),
  (89, 'Ac', 'Actinium'),
  (90, 'Th', 'Thorium'),
  (91, 'Pa', 'Protactinium'),
  (92, 'U', 'Uranium'),
  (93, 'Np', 'Neptunium'),
  (94, 'Pu', 'Plutonium'),
  (95, 'Am', 'Americium'),
  (96, 'Cm', 'Curium'),
  (97, 'Bk', 'Berkelium'),
  (98, 'Cf', 'Californium'),
  (99, 'Es', 'Einsteinium'),
  (100, 'Fm', 'Fermium'),
  (101, 'Md', 'Mendelevium'),
  (102, 'No', 'Nobelium'),
  (103, 'Lr', 'Lawrencium'),
  (104, 'Rf', 'Rutherfordium'),
  (105, 'Db', 'Dubnium'),
  (106, 'Sg', 'Seaborgium'),
  (107, 'Bh', 'Bohrium'),
  (108, 'Hs', 'Hassium'),
  (109, 'Mt', 'Meitnerium'),
  (110, 'Ds', 'Darmstadtium'),
  (111, 'Rg', 'Roentgenium'),
  (112, 'Cn', 'Copernicium'),
  (113, 'Nh', 'Nihonium'),
  (114, 'Fl', 'Flerovium'),
  (115, 'Mc', 'Moscovium'),
  (116, 'Lv', 'Livermorium'),
  (117, 'Ts', 'Tennessine'),
  (118, 'Og', 'Oganesson'),
]

def search_by_atomic_number(element, Z):
    for x in element:
        if x[0]==Z:
            return x
    return None

search_by_atomic_number(element, 1) == (1, 'H', 'Hydrogen')
search_by_atomic_number(element, 6) == (6, 'C', 'Carbon')
search_by_atomic_number(element, 8) == (8, 'O', 'Oxygen')
search_by_atomic_number(element, 0) == None

def search_by_symbol(element, x):
    for y in element:
        if y[1]==x:
            return y
    return None

search_by_symbol(element, 'H') == (1, 'H', 'Hydrogen')
search_by_symbol(element, 'C') == (6, 'C', 'Carbon')
search_by_symbol(element, 'O') == (8, 'O', 'Oxygen')
search_by_symbol(element, '')  == None

def search_by_name(element, x):
    for y in element:
        if y[2]==x:
            return y
    return None

search_by_name(element, 'Hydrogen') == (1, 'H', 'Hydrogen')
search_by_name(element, 'Carbon')   == (6, 'C', 'Carbon')
search_by_name(element, 'Oxygen')   == (8, 'O', 'Oxygen')
search_by_name(element, '')         == None
