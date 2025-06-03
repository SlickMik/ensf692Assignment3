# school_data.py
# Ibrahiim Khan
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022


# Declare any global variables needed to store the data here

# ***REFERENCE ONLY***
# The shape of the array are [10,20,3]
# Structure of the array is [years, school, grade]

#Variable that stores data from imported arrays
data = np.array([
    year_2013,
    year_2014,
    year_2015,
    year_2016,
    year_2017,
    year_2018,
    year_2019,
    year_2020,
    year_2021,
    year_2022
])


# Data store the reshaped array
data = np.array([year.reshape(20, 3) for year in data])


#List of schools 
schools = {
    1224: "Centennial High School",
    1679: "Robert Thirsk School",
    9626: "Louise Dean School",
    9806: "Queen Elizabeth High School",
    9813: "Forest Lawn High School",
    9815: "Crescent Heights High School",
    9816: "Western Canada High School",
    9823: "Central Memorial High School",
    9825: "James Fowler High School",
    9826: "Ernest Manning High School",
    9829: "William Aberhart High School",
    9830: "National Sport School",
    9836: "Henry Wise Wood High School",
    9847: "Bowness High School",
    9850: "Lord Beaverbrook High School",
    9856: "Jack James High School",
    9857: "Sir Winston Churchill High School",
    9858: "Dr. E. P. Scarlett High School",
    9860: "John G Diefenbaker High School",
    9865: "Lester B. Pearson High School"
}


schoolsalt = {
    "Centennial High School": 1224,
    "Robert Thirsk School": 1679,
    "Louise Dean School": 9626,
    "Queen Elizabeth High School": 9806,
    "Forest Lawn High School": 9813,
    "Crescent Heights High School": 9815,
    "Western Canada High School": 9816,
    "Central Memorial High School": 9823,
    "James Fowler High School": 9825,
    "Ernest Manning High School": 9826,
    "William Aberhart High School": 9829,
    "National Sport School": 9830,
    "Henry Wise Wood High School": 9836,
    "Bowness High School": 9847,
    "Lord Beaverbrook High School": 9850,
    "Jack James High School": 9856,
    "Sir Winston Churchill High School": 9857,
    "Dr. E. P. Scarlett High School": 9858,
    "John G Diefenbaker High School": 9860,
    "Lester B. Pearson High School": 9865
}




# Function that returns the index of the school as entered by the user. The 
# method parses through the list of schools and returns the index of the match.
# if code is of type "int" then return index from schools dictionary 
# if code is of type "string" then return index from schoolalt dictionary
def get_school_index(code):
    if isinstance(code, int):
        school_list = list(schools.keys())
        return school_list.index(code)
    else:
        code = schoolsalt[code]
        school_list = list(schools.keys())
        return school_list.index(code)


 


#main function
def main():
    print("ENSF 692 School Enrollment Statistics")

    
    # Print Stage 1 requirements here
    print("Shape of the full data array: ", data.shape)
    print("Dumestions of the full data array:", data.ndim)

    
   
    selection = input("Please enter a highschool name or code:")


    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    #Ensures that user enters valid input
    try:
        key = int(selection)
        if key not in schools:
            raise ValueError
    except ValueError:
        if selection not in schools.values():
            print("You must enter a valid school name or code.")
            return
        key = selection
        
    school_data = data[:,get_school_index(key),:]

    # Print the school name and code
    if isinstance(key, int):
        school_name = schools[key]
        school_code = key
    else:
        school_name = key
        school_code = schoolsalt[key]


    print("School Name:", school_name)
    print("School Code: ", school_code)

    mean = np.nanmean(school_data, axis=0)
    highest = np.max(school_data)
    lowest = np.min(school_data)
    total_year = np.sum(school_data, axis = 1)

    print("Mean enrolment for Grade 10", mean[0])
    print("Mean enrolment for Grade 11", mean[1])
    print("Mean enrolment for Grade 12", mean[2])
    print("Highest enrolment for a single grade", int(highest))
    print("Lowest enrolment for a single grade", int(lowest))
    
    for i in range(10):
        year = 2013+i   
        print("Total enrollment for", year, ": is", int(total_year[i]))
    

    print("Total ten year enrollment: ", int(np.sum(total_year)))
    print("Mean total enrollment over 10 years",int(np.mean(total_year)) )

    all_enrolments_over_500 = school_data[school_data > 500]
    print("For all enrollments over 500, the median value was:  ", int(np.median(all_enrolments_over_500)))




    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
 

    #nan Ufunc's are used to eliminate any null values
    print("Mean enrollment in 2013:", int(np.nanmean(data[0])))
    print("Mean enrollment in 2022:", int(np.nanmean(data[9])))
    print("Total 2022 graduates:", int(np.nansum(data[9,:,2])))
    print("Highest enrolment for a single grade", int(np.nanmax(data)))
    print("Lowest enrolment for a single grade", int(np.nanmin(data)))


if __name__ == '__main__':
    main()

