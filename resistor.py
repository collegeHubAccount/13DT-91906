def bandToValue(order) -> None:
    multi = 10**int(str(order)[-1])
    ans = int(str(order)[0:-1])*multi
    return int(ans)
