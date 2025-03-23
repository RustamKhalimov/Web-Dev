def alarm_clock(day, is_vacation):
    if is_vacation:
        return "10:00" if 1 <= day <= 5 else "off"
    else:
        return "7:00" if 1 <= day <= 5 else "10:00"