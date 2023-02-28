def study_schedule(permanence_period: list[tuple], target_time):
    counter = 0
    try:
        for login, logout in permanence_period:
            if login <= target_time <= logout:
                counter += 1
        return counter
    except TypeError:
        return None
