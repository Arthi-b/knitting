
#objects:

from ast import pattern


class Pattern:
    #constructor method
    def __init__(self, dimensions, ease):
        self.dimensions = dimensions if dimensions is not None else []
        self.ease = ease

pattern0 = (Pattern([39, 42, 45, 48, 51], 8))
pattern1 = (Pattern([37, 40, 43, 46], 8))

#pattern_gaugue: int sts, int rows, int length
#my_gauge: int sts, int rows, int length
class Gauge:
    #constructor method
    def __init__(self, sts, length, rows=None):
        self.sts = sts
        self.rows = rows 
        self.length = length

pattern_gauge = (Gauge(sts = 19, length = 10))
my_gauge = (Gauge(sts = 19, length = 9, rows = 25))
my_gauge2 = (Gauge(sts = 21, length = 10, rows = 27))
desired_dim = 35

# converts the gauge and selects an existing size from the pattern. 
def gauge_converter(pattern_gauge, my_gauge, desired_dim, pattern):
   # Calculate stitch density
    pattern_st_density = pattern_gauge.sts / pattern_gauge.length
    my_st_density = my_gauge.sts / my_gauge.length

    # Calculate conversion factor
    cf = my_st_density / pattern_st_density
    # Find target pattern measurement
    converted_dim = desired_dim * cf

    print("Conversion factor:", round(cf, 4))
    print("Converted dimension:", round(converted_dim, 2))

    smaller = [
        size for size in pattern.dimensions
        if size < converted_dim
    ]

    larger = [
        size for size in pattern.dimensions
        if size > converted_dim
    ]
    closest_smaller = max(smaller) if smaller else None
    closest_larger = min(larger) if larger else None
    print("More fitted option:", closest_smaller)
    print("More relaxed option:", closest_larger)

gauge_converter(pattern_gauge, my_gauge2, desired_dim, pattern1)