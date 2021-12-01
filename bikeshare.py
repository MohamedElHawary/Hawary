import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    
    while True:
        city = input("\nPlease write the city name you want to view from the below list \nchicago \nnew york \nwasington\n \nCity:").lower()
        if city not in ("new york", "chicago", "washington"):
            print("Ops... you may entered a wrong selection")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month = input("Please select the month you want from the below list or type all, if you want to see the full data \njanuary \nfebruary \nmarch \napril \nmay \njune \n---------------- \nMonth: ").lower()
        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("please write the full month name correctly!")
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = input("Great..\nWhich day do you want??\nplease write the full day name ex:monday \nor get all  get the all days\n---------------- \nDay Name: ").lower()
        if day not in ("saturday", "sunday", "monday", "wednesday", "thursday", "friday", "all"):
            print(":( please make sure that you wrote the day name correctly")
            continue
        else:
            break


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
    df["month"] = df["Start Time"].dt.month
    df["weekday"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour
    
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
    
        df = df[df['month'] == month]
    
    if day != "all":
        df = df[df["weekday"] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    common_month = df['month'].mode()[0]
    print("the common month is:", common_month)


    # TO DO: display the most common day of week
    common_day = df["weekday"].mode()[0]
    print("the most day of week is:", common_day)


    # TO DO: display the most common start hour
    common_hour = df["hour"].mode()[0]
    print("the common hour is:", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Common_start_station = df['Start Station'].value_counts().idxmax()
    print("\nThe Common start station is :", Common_start_station)


    # TO DO: display most commonly used end station
    Last_station = df['End Station'].value_counts().idxmax()
    print("\nThe common last station is :", Last_station)


    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Common_start_station, " & ", Last_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trips_duration = sum(df["Trip Duration"])
    total_trips_duration = total_trips_duration / 86400
    print("Total Trips Durations (by Days) is:", total_trips_duration,"Days")
    total_trips_duration = sum(df["Trip Duration"])
    total_trips_duration = total_trips_duration / 1440
    print("Total Trips Durations (by Hours) is:", total_trips_duration,"Hours")


    # TO DO: display mean travel time
    Minimum_Travel_Time = df["Trip Duration"].mean()
    Minimum_Travel_Time = Minimum_Travel_Time / 60
    print("Minimum Travel Time Was:", Minimum_Travel_Time,"Minutes")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('Count of User Types:\n', counts_of_user_types)


    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Oldest_Year = df['Birth Year'].min()
      print('\nOldest Year:', Oldest_Year)
    except KeyError:
      print("\nOldest Year:\nSorry :( There isn't data can be displayed for this month.")

    try:
      Newest_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Newest_Year)
    except KeyError:
      print("\nThe Newest Year:\nSorry :( There isn't data can be displayed for this month.")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    view_data = input('\nWould you like to explore some of the row data? Enter yes or no\n')
    start_loc = 0
    keep_asking = True
    while (keep_asking):
        print(df.iloc[start_loc:start_loc + 5, :10])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == "no": 
            keep_asking = False
        else:
            print("Sorry :( There is no more data to get")
            break
                     
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