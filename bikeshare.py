#Bike Share project
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv' }
"""
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
"""


print('Hello! Let\'s explore some US bikeshare data!')
print()


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

            #Getting User input for city,day,month
    while True:
            user_city = input('Which city would you like to see data for Chicago/New York City/Washington\nAns:').title()
            cities = ['Chicago','New York City','Washington']
            if user_city in cities:
                break
            else:
                print('Invalid City entered!!\n Please try again')
    while True:
            month = input("Which month would you like to filter from January to June\nAns:").title()
            months= ['January', 'February', 'March', 'April', 'May', 'June']
            if month in months:
                break
            else:
                print('Invalid month entered\nPlease try again')
    while True:
            day = input("Which day of the week would you like to filter\nAns:").title()
            days=  ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']
            if day in days:
                break
            else:
                print('Invalid day of week entered!!!\nPlease try again ')

    print('-'*40)
    return user_city, month, day

def load_data(user_city, month, day):
            """
            Loads data for the specified city and filters by month and day if applicable.
            Args:
                (str) city - name of the city to analyze
                (str) month - name of the month to filter by, or "all" to apply no month filter
                (str) day - name of the day of week to filter by, or "all" to apply no day filter
            Returns:
                df - Pandas DataFrame containing city data filtered by month and day
            """
            df = pd.read_csv(CITY_DATA[user_city])  # loadingdata file into a dataframe
            df['Start Time'] = pd.to_datetime(df['Start Time'])# converting the Start Time column to datetime

            # extract month and day of week and hour from Start Time to create new columns
            df['month'] = df['Start Time'].dt.month
            df['day_of_week'] = df['Start Time'].dt.day_name()
            df['hour'] = df['Start Time'].dt.hour

            # filtering by month if applicable
            if month != 'all':
                months = ['January', 'February', 'March', 'April', 'May', 'June'] # filtering by month to create the new datafram
                month = months.index(month) + 1
            # filtering by day of week if applicable
            if day != 'all':
                df = df[ df['day_of_week'] == day.title()]  # filtering by day of week to create the new datafram

            return df

def time_stats(df):
            """Displays statistics on the most frequent times of travel."""
            while True:
                stats = input('Do you want to see statistics on the most frequent times of travel for the day and month chosen(yes/no) \nAns:').lower()
                if stats == 'yes':
                    start_time = time.time()
                    # display the most common month
                    most_common_month = df['month'].mode()[0]
                    # display the most common day of week
                    most_common_day_of_week = df['day_of_week'].mode()[0]
                    print("The most common month and day of week are {} and {} :" .format(most_common_month,most_common_day_of_week))
                    # display the most common start hour
                    def hr_func(ts):
                        return ts.hour
                    df.insert(2,'time_hour', df['Start Time'].apply(hr_func))
                    popular_hour = df['time_hour'].mode()[0]
                    print("The most common start hour is :", popular_hour)
                    print("\nThis took %s seconds." % (time.time() - start_time))
                    print('-'*40)

                    break
                else:
                    break

def station_stats(df):
            """Displays statistics on the most popular stations and trip."""
            print('Still displying more statistis..........................\n')
            while True:
                station_stats = input('Would you like to see the most popular stations and trip for the month and day chosen(yes/no) \nAns:').lower()
                if station_stats == 'yes':
                    start_time = time.time()
                    #displaying  most commonly used start station
                    most_used_start_station = df['Start Station'].mode()[0]
                    print("The most commonly used start station :\n\n", most_used_start_station)
                    #displaying most commonly used end station
                    most_used_end_station = df['End Station'].mode()[0]
                    #displaying the  most frequent combination of start station and end station trip
                    print("The most commonly used start station and end station are : {}, {}".format(most_used_start_station,most_used_end_station))
                    print("\nThis took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                    break
                else:
                    break

def trip_duration_stats(df):
            """Displays statistics on the total and average trip duration."""
            trip_stast = input('Will you want to see statistics on the total and average trip duration(yes/no) \nAns:').lower()
            while True:
                if trip_stast == 'yes':
                    start_time = time.time()
                    #displaying the  total travel time
                    total_travel = df['Trip Duration'].sum()
                    print("The total travel time  is :", total_travel)
                    #displaying the mean travel time
                    mean_travel = df['Trip Duration'].mean()
                    print("The mean travel time is {}\n Total time taken was {}:".format(mean_travel,time.time() - start_time))
                    print('-'*40)
                    break
                else:
                    break
def user_stats(df,user_city):
            """Displays statistics on bikeshare users."""
            user_stat = input('Do you want to also see the statistics on the bikeshare users(yes/no) \nAns:').lower()
            start_time = time.time()
            while True:
                if user_stat == 'yes' and user_city == 'Washington':
                    print('Here you go!!!!!!\n')
                    #Displaying the counts of user types
                    print()
                    user_counts = df['User Type'].value_counts()
                    print("The counts of user types in the chosen city is:",user_counts)
                    print("\nThis took %s seconds." % (time.time() - start_time))
                    break

                if user_stat == 'yes' and user_city != "Chicago":

                    #Displaying the  counts of gender
                    print('Here you go!!!!!!\n')
                    user_counts = df['User Type'].value_counts()
                    print("The counts of user types in the chosen city is:",user_counts)
                    gender_counts = df['Gender'].value_counts()
                    print("Counts of gender:\n",gender_counts)
                    #Displaying earliest, most recent, and most common year of birth
                    #Calculating for the most erliest year
                    earliest_year = df['Birth Year'].min()
                    print("The most earliest birth year is:", earliest_year)
                    #Calulating for the recent year
                    recent_year = df['Birth Year'].max()
                    print("The most recent birth year is:", recent_year)
                    #Calculating for the most common year
                    most_birthyear = df['Birth Year'].mode()[0]
                    print("The most common birth year is:",most_birthyear)
                    print("\nThis took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                    break

                else:
                    break


def display_data(df):
                """
                Displays the raw data file as requested by the user.
                """
                #Asking for user input
                data_choice = input("Would you like to see the raw data for the city chosen(yes/no) \nAns: ").lower()
                start_num= 0
                end_num = 5
                if data_choice == 'yes':
                #Loop to  continue displaying data upon user's request
                    while end_num <= df.shape[0] - 1:
                        print(df.iloc[start_num:end_num,:])
                        start_num += 5
                        end_num += 5
                        data_end = input("Would you like to continue(yes/no) \n Ans:").lower()
                        if data_end == 'no':
                            break


def main():
    while True:
        user_city, month, day = get_filters()
        df = load_data(user_city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,user_city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'yes':
            continue
        else:
            print('Thanks for your service!!!Bye')
            break


if __name__ == "__main__":
    main()
