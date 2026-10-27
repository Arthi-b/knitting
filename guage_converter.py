
#objects:

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
    def __init__(self, sts, rows, length):
        self.sts = sts
        self.rows = rows if rows is not None else 0
        self.length = length

pattern_gauge = (Gauge(19, 25, 4))
my_gauge = (Gauge(18, 24, 4))
desired_dim = 37

#SAME STS + ROWS, DIFF LENGTH
# converts the gauge and selects from an existing size in the pattern. 
def gauge_convert_length(pattern_gauge, my_gauge, desired_dim, pattern):
    #conversion factor
    cf = pattern_gauge.length / my_gauge.length
    print("The conversion factor is: ", cf)

    converted_dim = desired_dim * cf
    print ("The converted dimension is: ", converted_dim, ", The pattern sizes are: ", pattern.dimensions)

    if converted_dim in pattern.dimensions:
        print("The converted dimension is an exact match in the pattern. Select size", converted_dim)
    else:
        closest_size = min(
        pattern.dimensions,
        key=lambda size: abs(size - converted_dim)
    )
    if closest_size > converted_dim:
        second_closest_size = (pattern.dimensions[pattern.dimensions.index(closest_size) - 1])
    elif closest_size < converted_dim:
        second_closest_size = (pattern.dimensions[pattern.dimensions.index(closest_size) + 1])

    print("The closest size(s) is/are: ", closest_size, "and", second_closest_size)

    dim_smaller = patttern.dimensions[]


gauge_convert_length(pattern_gauge, my_gauge2, desired_dim, pattern1)


#SAME LENGTH, DIFF STS + ROWS
# converts the gauge and selects from an existing size in the pattern. 
def gauge_convert_sts(pattern_gauge, my_gauge, desired_dim, pattern):
    #conversion factor
    cf = pattern_gauge.length / my_gauge.length
    print("The conversion factor is: ", cf)

    converted_dim = desired_dim * cf
    print ("The converted dimension is: ", converted_dim, ", The pattern sizes are: ", pattern.dimensions)

    if converted_dim in pattern.dimensions:
        print("The converted dimension is an exact match in the pattern. Select size", converted_dim)
    else:
        closest_size = min(
        pattern.dimensions,
        key=lambda size: abs(size - converted_dim)
    )
    if closest_size > converted_dim:
        second_closest_size = (pattern.dimensions[pattern.dimensions.index(closest_size) - 1])
    elif closest_size < converted_dim:
        second_closest_size = (pattern.dimensions[pattern.dimensions.index(closest_size) + 1])

    print("The closest size(s) is/are: ", closest_size, "and", second_closest_size)
