# You are the "computer expert" of a local Athletic Association (C.A.A.). Many teams of runners come to compete. Each time you get a string of all race results of every team who has run. For example here is a string showing the individual results of a team of 5 runners:

# "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"

# Each part of the string is of the form: h|m|s where h, m, s (h for hour, m for minutes, s for seconds) are positive or null integer (represented as strings) with one or two digits. Substrings in the input string are separated by ,  or ,.

# To compare the results of the teams you are asked for giving three statistics; range, average and median.

# Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.

# Mean or Average : To calculate mean, add together all of the numbers and then divide the sum by the total count of numbers.

# Median : In statistics, the median is the number separating the higher half of a data sample from the lower half. The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations. If there is an even number of observations, then there is no single middle value; the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

# Your task is to return a string giving these 3 values. For the example given above, the string result will be

# "Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"

# of the form: "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`

# where hh, mm, ss are integers (represented by strings) with each 2 digits.

# Remarks:
# if a result in seconds is ab.xy... it will be given truncated as ab.
# if the given string is "" you will return ""


# Function to convert the data to the format that the problem says
def convertDataToFmt():
    dataList=[]
    athletes=int(input('How many athletes are in the team?: '))
    for i in range(athletes):
        # Get the data from the user
        data=input('Enter the data in the format hh|mm|ss: ')
        # Split the data
        data=data.split('|')
        # print(type(aloneData))
        # Convert the data to seconds
        data=int(data[0])*3600+int(data[1])*60+int(data[2])
        # Add the data to the list
        dataList.append(data)
    data=dataList
    return data

# Average 
def dataAverage(data):
    averageList=0
    add=0
    lenData=len(data)
    # Run through the array and add up each number
    for i in data:
        add+=i
    # Get the average
    averageList=add/lenData
    return averageList

# Range
def dataRange(data):
    data.sort()
    range=data[-1]-data[0]
    return range

#Median
def dataMedian(data):
    lenData=len(data)
    median=0
    posMedian=(lenData+1)/2
    if posMedian.is_integer():
        median=data[int(posMedian-1)]
    else:
        numrounded=round(posMedian)
        median=(data[numrounded-1]+data[numrounded-2])/2
    return median


# Converted data
converted_data=convertDataToFmt()

# Average
# average_data=dataAverage(converted_data)
# print('The average is:', average_data)

# #Range
# range_data=dataRange(converted_data)
# print('The range is:', range_data)

# # Median
# median_data=dataMedian(converted_data)
# print('The median is:', median_data) 

# RESULT
def convertResultToFmt(converted_data):
    average=dataAverage(converted_data)
    range=dataRange(converted_data)
    median=dataMedian(converted_data)

    # Convert the data to the format that the problem says
    # Average
    # The // operator is the integer division operator. It returns the integer part of the quotient.
    averageHours=average//3600
    averageMinutes=(average%3600)//60
    averageSeconds=(average%3600)%60

    # Range
    rangeHours=range//3600
    rangeMinutes=(range%3600)//60
    rangeSeconds=(range%3600)%60

    # Median
    medianHours=median//3600
    medianMinutes=(median%3600)//60
    medianSeconds=(median%3600)%60

    # Print the result
    print('Range: {}|{}|{} Average: {}|{}|{} Median: {}|{}|{}'.format(rangeHours, rangeMinutes, rangeSeconds, int(averageHours), int(averageMinutes), int(averageSeconds), int(medianHours), int(medianMinutes), int(medianSeconds)))


convertResultToFmt(converted_data)