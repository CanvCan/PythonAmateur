def kuvvet(taban, us):
    if us == 0:  # temel durum
        return 1
    else:  # özyineleme adimi
        return taban * kuvvet(taban, us - 1)
