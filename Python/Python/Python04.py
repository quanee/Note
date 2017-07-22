import time


# time 模块
'''
Help on built-in module time:

NAME
    time - This module provides various functions to manipulate time values.

DESCRIPTION
    There are two standard representations of time.  One is the number
    of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
    or a floating point number (to represent fractions of seconds).
    The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
    The actual value can be retrieved by calling gmtime(0).

    The other representation is a tuple of 9 integers giving local time.
    The tuple items are:
      year (including century, e.g. 1998)
      month (1-12)
      day (1-31)
      hours (0-23)
      minutes (0-59)
      seconds (0-59)
      weekday (0-6, Monday is 0)
      Julian day (day in the year, 1-366)
      DST (Daylight Savings Time) flag (-1, 0 or 1)
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.

CLASSES
    builtins.tuple(builtins.object)
        struct_time

    class struct_time(builtins.tuple)
     |  The time value as returned by gmtime(), localtime(), and strptime(), and
     |  accepted by asctime(), mktime() and strftime().  May be considered as a
     |  sequence of 9 integers.
     |
     |  Note that several fields' values are not the same as those defined by
     |  the C language standard for struct tm.  For example, the value of the
     |  field tm_year is the actual year, not year - 1900.  See individual
     |  fields' descriptions for details.
     |
     |  Method resolution order:
     |      struct_time
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __reduce__(...)
     |      helper for pickle
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  tm_gmtoff
     |      offset from UTC in seconds
     |
     |  tm_hour
     |      hours, range [0, 23]
     |
     |  tm_isdst
     |      1 if summer time is in effect, 0 if not, and -1 if unknown
     |
     |  tm_mday
     |      day of month, range [1, 31]
     |
     |  tm_min
     |      minutes, range [0, 59]
     |
     |  tm_mon
     |      month of year, range [1, 12]
     |
     |  tm_sec
     |      seconds, range [0, 61])
     |
     |  tm_wday
     |      day of week, range [0, 6], Monday is 0
     |
     |  tm_yday
     |      day of year, range [1, 366]
     |
     |  tm_year
     |      year, for example, 1993
     |
     |  tm_zone
     |      abbreviation of timezone name
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |