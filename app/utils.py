from datetime import datetime

def get_time_delta(frequency, date):
  date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
  parsed_frequency = frequency.split(' ')
  if parsed_frequency[2] == 'hours':
    print(int(parsed_frequency[1]) * 3600 - (datetime.now() - date).seconds)
    return int(parsed_frequency[1]) * 3600 - (datetime.now() - date).seconds
  elif parsed_frequency[2] == 'minutes':
    print(int(parsed_frequency[1]) * 60 - (datetime.now() - date).seconds)
    return int(parsed_frequency[1]) * 60 - (datetime.now() - date).seconds