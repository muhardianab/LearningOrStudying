def add_time(start, duration, day_name = None):
  
  #Splitting the Format
  add_hours = int(duration.split(':')[0])
  add_minutes = int(duration.split(':')[1])

  initial_hour = int(start.split(':')[0])
  initial_minute = int((start.split(':')[1]).split(' ')[0])
  phase = (start.split(':')[1]).split(' ')[1]
  
  #Calculate the time
  if phase == 'PM':
    total_initial_hour = 12 + initial_hour
  else:
    total_initial_hour = initial_hour

  new_total_hours = total_initial_hour + add_hours
  new_total_minutes = initial_minute + add_minutes

  #New time
  if new_total_minutes >= 60:
    new_total_minutes -= 60
    new_total_hours += 1

  if new_total_hours >= 24:
    total_days = new_total_hours // 24
    new_total_hours = new_total_hours % 24
    if new_total_hours == 0:
      new_phase = 'AM'
      new_total_hours = 12
    elif new_total_hours >= 12:
      new_phase = 'PM'
      new_total_hours -= 12
    else:
      new_phase = 'AM'
  else:
    total_days = 0
    if new_total_hours >= 12:
      new_phase = 'PM'
      new_total_hours -= 12
      if new_total_hours == 0:
        new_total_hours = 12
    else:
      new_phase = 'AM'

  if total_days == 0:
    return_day = f''
  elif total_days <= 1:
    return_day = f'(next day)'
  else:
    return_day = f'({total_days} days later)'

  #Calculate the day
  day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

  if day_name != None:
    if day_name.capitalize() in day_list:
      initial_day_index = day_list.index(day_name.capitalize())
      new_day_index = initial_day_index + total_days
      if new_day_index > 6:
        new_day_index = ((new_day_index) + 1) % 7 - 1
        new_day = day_list[new_day_index]
      else:
        new_day = day_list[new_day_index]

  if total_days == 0:
    if day_name != None:
      final_result = f"{new_total_hours}:{new_total_minutes:02} {new_phase}, {new_day}"
    else:
      final_result = f"{new_total_hours}:{new_total_minutes:02} {new_phase}"

  else:
    if day_name != None:
      final_result = f"{new_total_hours}:{new_total_minutes:02} {new_phase}, {new_day} {return_day}"
    else:
      final_result = f"{new_total_hours}:{new_total_minutes:02} {new_phase} {return_day}"

  return final_result
