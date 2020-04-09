#!/usr/bin/python3


def find_peak(list_):
    """Return a peak in a list of unsorted integers."""
    if list_ == []:
        return

    size = len(list_)
    if size <= 2:
        return max(list_)

    mid = int(size / 2)
    peak = list_[mid]
    if peak > list_[mid - 1] and peak > list_[mid + 1]:
        return peak
    elif peak < list_[mid - 1]:
        return find_peak(list_[:mid])
    else:
        return find_peak(list_[mid + 1:])
