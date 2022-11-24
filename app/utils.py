from datetime import datetime

def get_time_delta(frequency, date):
  date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
  _, _frequency, _type = frequency.split(' ')

  diff = datetime.now() - date

  if _type == 'hours':
    return int(_frequency) * 3600 - (diff.seconds + (diff.days * 60 * 60 * 24))
  elif _type == 'minutes':
    return int(_frequency) * 60 - (diff.seconds + (diff.days * 60 * 60 * 24))