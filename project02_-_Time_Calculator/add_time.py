def add_time(start, duration, day=None):

  day_week = ('monday', 'tuesday', 'wednesday', 
              'thursday', 'friday', 'saturday', 'sunday')

  st = start.split()
  clock_format = st[1].lower()

  hora = st[0].split(':')
  temp = duration.split(':')
  
  hora_float = [float(hora[0]), float(hora[1])]
  if clock_format == 'pm':
    hora_float[0] += 12.0
  temp_float = [float(temp[0]), float(temp[1])]
  
  result = []
  for index in range(2):
    soma = hora_float[index] + temp_float[index]
    result.append(soma)

  hour = result[0]
  minute = result[1]

  if minute >= 60:
    hour += 1
    minute -= 60

  hour_div = hour / 24
  hour_str = str(hour_div).split('.')
  n_days = round(float(hour_str[0]))

  while hour > 24:
    hour -= 24
  
  if hour == 24.0:
    hour = 12.0
    clock = 'AM'
  elif hour == 12.0:
    hour = 12.0
    clock = 'PM'
  elif hour > 12.0:
    clock = 'PM'
    hour -= 12
  elif hour < 12.0:
    clock = 'AM'

  if day:
    index = day_week.index(day.lower())
    new_index = (index + n_days) % 7
    new_day = day_week[new_index].capitalize()
    weekday = f', {new_day}'
  else:
    weekday = ""

  if n_days > 1:
    new_time = f'{hour:.0f}:{minute:02.0f} {clock}' + weekday + f' ({n_days:.0f} days later)'
  elif n_days == 1:
    new_time = f'{hour:.0f}:{minute:02.0f} {clock}' + weekday + f' (next day)'
  elif n_days < 1:
    new_time = f'{hour:.0f}:{minute:02.0f} {clock}' + weekday

  print(new_time)

  return new_time

if __name__ == '__main__':
    add_time('10:25 AM', '150:10')