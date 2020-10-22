import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city' , 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    city = input("would you like to see data for chicago, new york or washington ? : ")
    while city not in cities:
        city = input("Enter a city from chicago, new york city or washington : ")

    # TO DO: get user input for month (all, january, february, ... , june)
    month, day = "all", "all"
    filter = input("Would you like to filter the data by month, day, all or not at all : ")
    if filter == "month" or filter == "all":
        month = input("Which month -January, February, March, April, May, or June? : ")
        while month not in months :
            month = input("enter a month in between january to june : ")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if filter =="day" or filter =="all":
        day = input("Which day -Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? : ")
        while day not in days:
            day = input("enter a valid day : ")              
                      

    print('-'*40)
    return city, month, day


                          
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
   
                          
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
                      
                          
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("the most common month is {}".format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("the most common day is {}".format(popular_day))
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]                     
    print("the most common hour is {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print("most start station is {}".format(most_start_station))

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print("most end station is {}".format(most_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_start_end = df[["Start Station", "End Station"]].mode().iloc[0,:]
    print ("most start an end combination is {}".format(most_start_end))                      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("total travel time is {}".format(total_travel_time))
    # TO DO: display mean travel time
    average_travel_time = df["Trip Duration"].mean()
    print("average travel time is {}".format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    counts_user_types = df["User Type"].value_counts()
    print("counts of user types is : {}".format(counts_user_types)) 
    # TO DO: Display counts of gender
    try:                      
        counts_gender = df["Gender"].value_counts()
        print("counts of genders is : {}".format(counts_gender)) 
    except:
        print("only available for NYC and Chicago")                  
    # TO DO: Display earliest, most recent, and most common year of birth
    try:                      
        earliest = df["Birth Year"].min()
        most_recent = df["Birth Year"].max()
        most_common = df["Birth Year"].mode()[0]
        print("earliest year of birth is {}, most recent year of birth is {}, most common is {}".format(earliest, most_recent, most_common))                 
    except:
        print("only available for NYC and Chicago")                      
                          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
