from datetime import datetime
from datetime import timedelta


def add(moment: datetime):
    return moment + timedelta(seconds=10**9)
