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
    cities = ['chicago', 'new york city', 'washington']

    while True:
        city = input('Which city do you want to analyze, "Chicago", "New York City" or "Washington"?: ').lower()
        if city not in cities:
            print('Oops! Invalid input! Please, check your answer.')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    while True:
        month = input('Filter by month("January" - "June"), or "all"?: ').lower()
        if month not in months:
            print('Oops! Invalid input! Please, check your answer.')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday']

    while True:
        day = input('Filter by day of week("Monday" - "Sunday"), or "all"?: ').lower()
        if day not in days:
            print('Oops! Invalid input! Please, check your answer.')
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month: {}".format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week: {}".format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common start hour: {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start = df['Start Station'].value_counts()
    n = 0
    while start[n] == start.max():
        n += 1
    print("Start Station that is most commonly used: {}".format(start[:n]))

    # TO DO: display most commonly used end station
    end = df['End Station'].value_counts()
    n = 0
    while end[n] == end.max():
        n += 1
    print("\nEnd Station that is most commonly used: {}".format(end[:n]))

    # TO DO: display most frequent combination of start station and end station trip
    j = df.groupby(['Start Station'])['End Station'].value_counts().sort_values(ascending=False)
    n = 0
    while j[n] == j.max():
        n += 1

    print("\nMost frequent combination of start station and end station trip:")
    print()
    print(j[:n])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time: {} sec".format(total_travel))

    import datetime
    total_td = datetime.timedelta(seconds=int(total_travel))
    print("  = {}".format(total_td))

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time: {} sec".format(mean_travel))
    mean_td = datetime.timedelta(seconds=int(mean_travel))
    print("  = {}".format(mean_td))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("Counts of user types: \n", user_type)
    print()

    # TO DO: Display counts of gender
    if city != "washington":
        gender = df['Gender'].dropna().value_counts()
        print("Counts of gender: \n", gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if city != "washington":
        birth = df['Birth Year'].dropna()
        earliest = birth.min()
        recent = birth.max()
        common_year = birth.mode()[0]

        print("\nEarliest year of birth: {}".format(earliest))
        print("Most recent year of birth: {}".format(recent))
        print("Most common year of birth: {}".format(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    l = 0
    p = 5
    o = p-5
    while l == 0:
        print(df.iloc[o:p])
        que = input('Do you want to see raw data more? Type "yes" or "no" :\n')
        if que == 'yes':
            p += 5
            o += 5
        else:
            l += 1


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
