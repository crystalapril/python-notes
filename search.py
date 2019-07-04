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
  pass

search_by_serial(sfw, 381) == {'date': '2018-02', 'serial': 381, 'other': '...'}
search_by_serial(sfw, 368) == {'date': '2017-01', 'serial': 368, 'other': '...'}
search_by_serial(sfw, 800) == None

def search_by_date(books, date):
  pass

search_by_date(sfw, '2018-02') == {'date': '2018-02', 'serial': 381, 'other': '...'}
search_by_date(sfw, '2017-01') == {'date': '2017-01', 'serial': 368, 'other': '...'}
search_by_date(sfw, '1970-01') == None
search_by_date(sfw, '201802')  == None
