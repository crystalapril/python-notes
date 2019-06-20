# https://en.wikipedia.org/wiki/Melting_point
# https://en.wikipedia.org/wiki/Triple_point
# https://en.wikipedia.org/wiki/List_of_chemical_elements

melting_point = [
  ('C'  , 3800   ),
  ('Al' ,  933.47),
  ('Fe' , 1811   ),
  ('Cu' , 1357.77),
  # ('Ag' , 1234.93),
  ('W'  , 3695   ),
  ('Pt' , 2041.4 ),
  # ('Au' , 1337.33),
  # ('Hg' ,  234.43),
]

def get_symbol(xs):
    l=[]
    for x in xs:
        l.append(x[0])
    return l

def get_symbol(xs):
    return list(map(lambda x:x[0],xs))
  

def get_melting_point(xs):
    l=[]
    for x in xs:
        l.append(x[1])
    return l

def get_melting_point(xs):
    return list(map(lambda x:x[1],xs))

get_symbol       (melting_point) == ['C' , 'Al'  , 'Fe', 'Cu'   , 'W' , 'Pt'  ]
get_melting_point(melting_point) == [3800, 933.47, 1811, 1357.77, 3695, 2041.4]


def to_celsius(xs):
    l=[]
    for x in xs:
        l.append(x[0],x[1]-273.15)
    return l

def to_celsius(xs):
    return list(map(lambda x:(x[0],x[1]-273.15),xs))

to_celsius(melting_point) == [
  ('C' , 3526.85),
  ('Al',  660.32),
  ('Fe', 1537.85),
  ('Cu', 1084.62),
  # ('Ag',  961.78),
  ('W',  3421.85),
  ('Pt', 1768.25),
  # ('Au', 1064.18),
  # ('Hg',  -38.72),
]

def below(xs, y):
  pass

def above(xs, y):
  pass

def between(xs, y, z):
  pass

below(melting_point, 1000) == [('Al', 933.47)]
below(melting_point, 1500) == [('Al', 933.47), ('Cu', 1357.77)]
below(melting_point, 2000) == [('Al', 933.47), ('Fe', 1811), ('Cu', 1357.77)]

above(melting_point, 3000) == [('C', 3800), ('W', 3695)]
above(melting_point, 2000) == [('C', 3800), ('W', 3695), ('Pt', 2041.4)]
above(melting_point, 1500) == [('C', 3800), ('Fe', 1811), ('W', 3695), ('Pt', 2041.4)]

between(melting_point, 1000, 1500) == [('Cu', 1357.77)]
between(melting_point, 1500, 2000) == [('Fe', 1811)]
between(melting_point, 2000, 3000) == [('Pt', 2041.4)]
