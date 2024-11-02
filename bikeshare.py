import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
def get_filters():    
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # adding to documentation branch
    # adding to documentation branch(2)
    while True:
        city =input('ENTER THE CITY(Chicago, New York City,or Washington): ').lower()
        if city in cities:
            break
        else:
            print('Please enter valid city.')

    # get user input for month (all, january, february, ... , june)    
    while True:
        month = input('ENTER MONTH(all,january, february, ... , june) : ').lower()
        if month in months:
            break
        else:
          print('Please enter valid month.')  
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('ENTER DAY(all, monday, tuesday, ... sunday) : ').lower()
        if day in days:
            break
        else:
          print('Please enter valid day.') 

    print('-'*40)
    return city, month, day


def load_data(city, month, day):     
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month

    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]
    # extract day from Start Time into new column called month    
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: ", df['month'].value_counts().idxmax())

    # display the most common day of week
    print("The most common day is: ", df['day_of_week'].value_counts().idxmax())

    # display the most common start hour
    print("The most common hour is: ", df['Start Time'].dt.hour.value_counts().idxmax())
    # display the most common seconds
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station is: ", df ['Start Station'].value_counts().idxmax())

    # display most commonly used end station
    print("The most common end station is: ", df['End Station'].value_counts().idxmax())

    # display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip")
    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum() / 3600.0
    print("total travel time in hours is: ", total_duration)

    # display mean travel time
    mean_duration = df['Trip Duration'].mean() / 3600.0
    print("mean travel time in hours is: ", mean_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User Type count: ",df['User Type'].value_counts())
   
    # Display counts of gender
    try:        
        print("Gender count: ",df['Gender'].value_counts())
    except:
        print('Counts of Each User Gender:\nSorry, no gender data available for {}'.format(city.title()))       
    

    # Display earliest, most recent, and most common year of birth
    try:
        print("The earliest year of birth is:",int(df['Birth Year'].min()),
            ", most recent one is:",int(df['Birth Year'].max()),
            "and the most common one is: ",int(df['Birth Year'].value_counts().idxmax()))
    except:
        print('Counts of User Birth Year:\nSorry, no birth year data available for {}'.format(city.title()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data (df):
    """Displays the data due filteration.
    5 rows will added in each press"""
    print('press enter to see row data, press no to skip')   
    x = 0
    while (input()!= 'no'):       
        x = x+5
        print(df.head(x))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
