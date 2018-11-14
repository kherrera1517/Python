#
# hw11pr1.py
#
# name:
#

# First, the class definition
# Below, we define several useful objects of type Date
#  +++ keep those and/or add your own! +++
# DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date(object):
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """Construct a Date with the given month, day, and year."""
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        s = "{:02d}/{:02d}/{:04d}".format(self.month, self.day, self.year)
        return s


    # Here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False







#
# be sure to add code for the Date class ABOVE--inside the class definition
#
    def copy(self):
        """Returns a new object with the same month, day, year
           as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """Decides if self and d2 represent the same calendar date,
           whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month \
          and self.day == d2.day:
            return True
        else:
            return False

    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
            in history as ==.  This way , we don't need to use the awkward
            d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month \
          and self.day == d2.day:
            return True
        else:
            return False

    #Self-Defined
    # def isBefore(self, d2):
    #     if self.year < d2.year:
    #         return True
    #     elif self.year > d2.year:
    #         return False
    #     else:
    #         if self.month < d2.month:
    #             return True
    #         elif self.month > d2.month:
    #             return False
    #         else:
    #             if self.day < d2.day:
    #                 return True
    #             else:
    #                 return False

    def __lt__(self, d2):
        if self.year < d2.year:
            return True
        elif self.year > d2.year:
            return False
        else:
            if self.month < d2.month:
                return True
            elif self.month > d2.month:
                return False
            else:
                if self.day < d2.day:
                    return True
                else:
                    return False

    def isBefore(self, d2):
        return self < d2

    def __gt__(self, d2):
        if self.year > d2.year:
            return True
        elif self.year < d2.year:
            return False
        else:
            if self.month > d2.month:
                return True
            elif self.month < d2.month:
                return False
            else:
                if self.day > d2.day:
                    return True
                else:
                    return False

    def isAfter(self, d2):
        return self > d2

    def tomorrow(self):
        if self.isLeapYear():
            fdays = 29
        else:
            fdays = 28

        DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        self.day += 1
        if self.day > DIM[self.month]:
            self.day = 1
            self.month += 1

            if self.month > 12:
                self.month = 1
                self.year += 1

    def yesterday(self):
        if self.isLeapYear():
            fdays = 29
        else:
            fdays = 28

        DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        self.day -= 1
        if self.day == 0:
            self.month -= 1
            if self.month == 0:
                self.month = 12
                self.year -= 1
            self.day = DIM[self.month]

    # def addNDays(self, N):
    #     print(self)
    #     while N > 0:
    #         self.tomorrow()
    #         N -= 1
    #         print(self)

    # def subNDays(self, N):
    #     print(self)
    #     while N > 0:
    #         self.yesterday()
    #         N -= 1
    #         print(self)

    def __iadd__(self, N):
        print(self)
        while N > 0:
            self.tomorrow()
            N -= 1
            print(self)
        return self

    def __isub__(self, N):
        print(self)
        while N > 0:
            self.yesterday()
            N -= 1
            print(self)
        return self

    def addNDays(self, N):
        self += N

    def subNDays(self, N):
        self += N

    def __sub__(self, d2):
        d2_copy = d2.copy()
        count = 0

        if self < d2_copy:
            while self < d2_copy:
                d2_copy.yesterday()
                count -= 1
        elif self > d2_copy:
            while self > d2_copy:
                d2_copy.tomorrow()
                count += 1
        return count


    def diff(self, d2):
        return self - d2

    def dow(self):
        sunday = Date(10,10,2010)
        day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        difference = (self - sunday)
        if self.isBefore(sunday):
            return day[-abs(difference)%7]
        else:
            return day[difference%7]

#
# lots of dates to work with...
#
# The nice this about putting them here is that they get redefined with each run
#   of the software (and this is needed for testing!)
#

d1 = Date(11, 13, 2018)    # Today?
winter_break = Date(12, 21, 2018)   # winter break
ny = Date(1, 1, 2018)   # new year
nd = Date(1, 1, 2020)   # new decade
nc = Date(1, 1, 2100)   # new century
graduation = Date(5, 15, 2022)   # alter to suit!
vacation = Date(5, 17, 2019)     # ditto ~ summer break!
sm1 = Date(10, 28, 1929)    # stock market crash
sn2 = Date(10, 19, 1987)    # another s.m. crash: Mondays in Oct. are risky...