def getHoursMinutesSeconds(totalSeconds):
    seconds = totalSeconds
    time = []
    hours = 0
    minutes = 0

    while seconds >= 3600:
        seconds -= 3600
        hours += 1

    while seconds >= 60:
        seconds -= 60
        minutes += 1


    if hours > 0:
        time.append(str(hours) + 'h')

    if minutes > 0:
        time.append(str(minutes) + 'm')

    if seconds > 0:
        time.append(str(seconds) + 's')

    if totalSeconds == 0:
        time.append(str(0) + 's')

    return ' '.join(time)


assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
