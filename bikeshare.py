import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze. Makes sure to get valuable information.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('\nHello! Great you want to learn more about bikeshare data. \nHope you enjoy the experience, otherwise go in contact with Maria Stecher. \nLet\'s get started with some simple questions:\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input("Please decide for one of the following cities: \nChicago, Washington or New York City |" )).lower()
            if city == "chicago" or city == 'washington' or city == 'new york city':
                break
            else: 
                print("You did not decide for one of the mentioned cities, please try again!")
        except ValueError: 
           print("Unfortunately your decision does not fit the requirements, please try again. Take care to use the excepted wording")
        finally:
           print("Let\'s move on to the next question!\n")
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        try: 
            month = int(input("Which month you are interested in?\nPlease enter the number of the month (for information about the whole year enter 0): ")) 
            if 0 <= month <= 6: 
                break
            elif 7<= month <=12:
                print('\nThe database does not contain any information on that particular month, please choose another one.\nHint: July till December are not included in the database')
            else:
                print("This is not a valid input for a month, please try again!")
        except Exception as e: 
           print("Unfortunately your decision does not fit the requirements, please try again. \nTake care to use the excepted input: {}".format(e))
        finally:
           print("Let\'s move on to the next question!\n")
                        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        try: 
            day = int(input("Which day of the week you are interested in? \nPlease enter the number of the day within the week, starting with 1 for monday\n(for information about the whole week enter 0): "))
            if 0 <= day <= 6: 
                break
            elif day == 7:
                print('\nThe database does not contain any information on that particular day, please choose another one.')
            else: 
                print("This is not a valid input for a day of the week, please try again!")
        except Exception as e: 
           print("Unfortunately your decision does not fit the requirements, please try again. Take care to use the excepted input:                         {}".format(e))
        finally:
           print("Let\'s move on to the next question!\n")

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
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    if not month == 0:
         df = df[df['Start Time'].dt.month == month]
    
    if not day == 0:
         df = df[df['Start Time'].dt.dayofweek == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month

    ## find the most popular hour
    common_month = df['month'].mode()[0]
    print('Most common month: ', common_month)

    # TO DO: display the most common day of week
    df['weekday'] = df['Start Time'].dt.dayofweek
    common_weekday = df['weekday'].mode()[0]
    print('Most common day of the week: ', common_weekday)
    
    # TO DO: display the most common start hour
    df['start hour'] = df['Start Time'].dt.hour
    common_start_hour = df['start hour'].mode()[0]
    print('Most common start hour: ', common_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_start_end'] = df['Start Station'] + ' and ending at '+ df['End Station']
    common_start_end_station = df['combination_start_end'].mode()[0]
    print('Most common combination of start station and end station: Starting at ', common_start_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    total_trip_duration = dt.timedelta(minutes = int(total_trip_duration))
    print('Total travel time is (xxx days, hh:mm:ss): {}'.format(total_trip_duration))

    # TO DO: display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    mean_trip_duration = round(mean_trip_duration,0)
    mean_trip_duration = dt.timedelta(minutes = mean_trip_duration)
    print('Mean travel time is (hh:mm:ss): {}'.format(mean_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCounts of user types:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if "Gender" in df:
        print('\nCounts of gender:')
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        common_birth_year = df['Birth Year'].mode()[0]
        min_birth_year = df['Birth Year'].min()
        max_birth_year = df['Birth Year'].max()
        print('\nEarliest year of birth: {}'.format(int(min_birth_year)))
        print('Most recent year of birth: {}'.format(int(max_birth_year)))
        print('Most common year of birth: {}'.format(int(common_birth_year)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def details(df): 
    """
    Asks the user whether detailed information on the list is wished.
    Prints 5 rows of the list and asks again for the decision. 
    Continues with the following rows if answered again with yes. 
    Stops whenever the user answers with "no" or the list was fully shown.
    
    (str) decision_details - decision of the user whether to get (another) 5 rows of details. 
    """
    row_count = 0    
    all_rows = len(df)
    
    while row_count < all_rows:
        decision_details = input("\nWould you like to get some details? Enter yes or no.\n").lower()
        if decision_details == "no": 
            break
        elif decision_details == "yes": 
            print(df.iloc[row_count : row_count+5,])
            row_count = row_count + 5
        else: 
            print('\nThis is not a valid input to the question, please try again.')
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        details(df)

        
        while True:
            try: 
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() == 'yes':
                     break
                elif restart.lower() == 'no':
                    print('You are welcome, see you later again!')
                    break
                else: 
                    print('Your answer does not correspond to the expected value. Please enter yes or no.\n')
            except Exception as e: 
                print("Unfortunately your decision does not fit the requirements, please try again. \nTake care to use the excepted input: {}".format(e))
        
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
