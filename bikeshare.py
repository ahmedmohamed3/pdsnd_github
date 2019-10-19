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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print('-'*40)
        city=str(input("choose the City : chicago, new york city, washington\n"))
        city=city.lower()
        if (city=="chicago") or(city=="new york city")or(city=="washington"):
            break
        else:
            print("Choose From The Given Options\n")

    # get user input for month (all, january, february, ... , june)
    while True:
        print('-'*40)
        month=input("if you want to filter with Month \n please choose the month :\n  january , february , march , april , may , june  \n and if not choose \"none\"  ")
        month=month.lower()
        if (month=="january") or(month=="february") or(month=="march") or(month=="april") or(month=="may") or(month=="june")or (month=="none"):
            break
        else:
            print("Choose From The Given Options\n")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('-'*40)
        day=input("if you want to filter with Day \n please choose the Day :\n Saturday , Sunday ,Monday ,Tuesday , Wednesday , Thursday ,Friday \n and if not choose \"none\"  ")
        day=day.lower()
        if (day=="saturday") or(day=="sunday") or(day=="monday") or(day=="tuesday") or(day=="Wednesday") or (day=="thursday") or(day=="friday") or(day=="none") :
            break
        else:
            print("Choose From The Given Options\n")

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'none':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]


    if day != 'none':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('The most common month : {}'.format(popular_month))

    # display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print('The most common day : ', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    station_s=df['Start Station'].mode()[0]
    print('The most common start station:', station_s)
    # display most commonly used end station
    station_e=df['End Station'].mode()[0]
    print('The most common end station:', station_e)


    # display most frequent combination of start station and end station trip
    common_station=(df['Start Station'].append(df['End Station'])).mode()[0]
    print('The most frequent combination of start station and end station trip :', common_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration=df['Trip Duration'].sum()
    print(total_duration)
    # display mean travel time
    mean_duration=df['Trip Duration'].mean()
    print(mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    num_types=df['User Type'].groupby(df['User Type']).count()
    print(num_types)

    # Display counts of gender
    num_gender=df['Gender'].groupby(df['Gender']).count()
    print(num_gender)

    # Display earliest, most recent, and most common year of birth
    b_year=df['Birth Year']
    print("earliest year of birth :{}".format(b_year.min()))
    print("most recent year of birth : {}".format(b_year.max()))
    print("most common year of birth : {}".format(b_year.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    while True:
        disp=input("Do you want to see raw data? press (Yes or No)\n")
        disp=disp.lower()
        if disp=="yes":
            print("The Rows From {} to {} is :".format(0,5))
            print(df.iloc[0:5])
            disp_more(df)
            break
        elif disp=="no":
            break
        else:
            print("Please Enter \"yes\" or \"No\" only\n")
def disp_more(df):
    a=5
    while True:
        new_disp=input("do you want to see more 5 lines of raw data? press (Yes or No)\n")
        new_disp=new_disp.lower()
        if new_disp=="yes":
            print("The Rows From {} to {} is :".format(a,a+5))
            print(df.iloc[a:a+5])
            a+=5
        elif new_disp=="no":
            break
        else:
            print("Please Enter \"yes\" or \"No\" only\n")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if city=="washington": #washington does not have gender
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            display_data(df)
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
