def interpolate(t, value):
    if len(t) < 2:
        raise ValueError("calibration table should have at least two points")

    inpt = sorted(t)

    if value < inpt[0]:
        low = inpt[0]
        high = inpt[1]

    elif value > inpt[-1]:
        low = inpt[-2]
        high = inpt[-1]
    else:
        for low, high in zip(inpt[:-1], inpt[1:]):
            if low <= value <= high:
                break

    dx = high - low
    dy = t[high] - t[low]
    slope = dy / dx
    estimate = t[low] + slope * (value - low)

    return estimate
