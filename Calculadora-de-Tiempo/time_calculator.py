def add_time(start, duration, day_of_week=False):

    days_of_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
    days_of_week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    duration_tuple = duration.partition(":")
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    start_tuple = start.partition(":")
    start_minutes_tuple = start_tuple[2].partition(" ")
    start_hours = int(start_tuple[0])
    start_minutes = int(start_minutes_tuple[0])
    am_or_pm = start_minutes_tuple[2]

    days_added = int(duration_hours / 24)

    final_minutes = start_minutes + duration_minutes
    if final_minutes >= 60:
        start_hours += 1
        final_minutes = final_minutes % 60

    am_or_pm_switch = {"AM": "PM", "PM": "AM"}
    am_or_pm_changes = int((start_hours + duration_hours) / 12)
    final_hours = (start_hours + duration_hours) % 12

    final_minutes = final_minutes if final_minutes > 9 else "0" + str(final_minutes)
    final_hours = 12 if final_hours == 0 else final_hours

    if am_or_pm == "PM" and start_hours + (duration_hours % 12) >= 12:
        days_added += 1

    am_or_pm = am_or_pm_switch[am_or_pm] if am_or_pm_changes % 2 == 1 else am_or_pm

    return_time = str(final_hours) + ":" + str(final_minutes) + " " + am_or_pm

    if day_of_week:
        day_of_week = day_of_week.lower()
        index = int((days_of_week_index[day_of_week] + days_added) % 7)
        new_day = days_of_week_list[index]
        return_time += ", " + new_day

    if days_added == 1:
        return return_time + " (next day)"
    elif days_added > 1:
        return return_time + " (" + str(days_added) + " days later)"

    return return_time