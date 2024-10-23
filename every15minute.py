
TOTAL_MINUTES_DAY = 1440
total_minutes = 0
while total_minutes != TOTAL_MINUTES_DAY:
  hours = total_minutes // 60
  minutes = total_minutes % 60
  if total_minutes / 720 < 1:
    period = 'AM'
  else:
    period = 'PM'
  if hours == 0:
    hours = 12
  if hours > 12:
    hours -= 12
  print(f'{hours}:{minutes:0>2d}{period}')
  total_minutes += 15