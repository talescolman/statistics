import statistics

# List of functions

# mean() returns the average of data.

data1 = [1, 8 , 9.74, 22, 22, 38, 39.9]
statistics.mean(data1)

# fmean() This runs faster than the mean() function and it always returns a float.

data2 = [2.5, 3.5, 8.25]
statistics.fmean(data2)

# geometric_mean() The geometric mean indicates the central tendency or typical value of the data using the product of the values (as opposed to the arithmetic mean which uses their sum).

data3 = [17, 20, 34, 56, 57, 58, 77]
statistics.geometric_mean(data3)

# harmonic_mean() a measure of the central location of the data. It is often appropriate when averaging rates or ratios, for example speeds.
# If one of the values is zero, the result will be zero.

data4 = [1, 26, 54]
statistics.harmonic_mean(data4)

# median() Median (middle value) of data.

data5 = [89, 93, 97, 101]
statistics.median(data5)

# median_low() Return the low median of numeric data. 

data6 = [1, 3, 5, 7]
statistics.median_low(data6)

# median_high() Return the high median of data.

data6 = [1, 3, 5, 7]
statistics.median_hich(data6)

# median_grouped() Return the median of grouped continuous data, calculated as the 50th percentile, using interpolation.

data7 = [72, 74, 75, 76, 77]
statistics.median_grouped(data7)

statistics.median_goruped(data7, interval=2) # Optional argument interval represents the class interval

# mode() Single mode (most common value) of discrete or nominal data.

data8 = [1, 1, 2, 3, 3, 3, 3, 4]
statistics.mode(data8)

# mode() can also be used with other data types
data9 = ["CA", "TX", "FL", "CA", "NY", "FL", "CA", "CA"]
statistics.mode(data9)

# multimode() Return a list of the most frequently occurring values in the order they were first encountered in the data.

statistics.multimode(data9)

# deviation

# pstdev() Return the population standard deviation (the square root of the population variance).

data10 = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
statistics.pstdev(data10)

# pvariance() Population standard deviation of data.

statistics.pvariance(data10)

statistics.pvaciance(data10, mu) # use MU if you already calculate the mean

# stdev() Sample standard deviation of data.
# A large variance indicates that the data is spread out; a small variance indicates it is clustered closely around the mean

statistics.stdev(data10)

statistics.stdev(data10, m) # If you already calculate the mean

# variance() Sample variance of data.

statistics.variance(data10)

statistics.variance(data10, m) # If you already calculate the mean
