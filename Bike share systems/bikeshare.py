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
    while True:
        city = str( input('Would you like to see data for Chicago, New York city, or Washington?').lower())
        if city in CITY_DATA.keys():
            break
        else:
            print("\nInvelid input. Please try again.\n")
            continue
            
    
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('''Which month would you like to explore?  Enter 'all',
'january', 'february', 'march', 'april', 'may', or 'june': ''').lower()
        
        if month == 'all':
            print('\n let\'s get the data for all months.')
            break
        elif month in months:
            print('\nLet\'s get data for {}.'.format(month.title()))
            break
        else:
            print('\nInvalid Input. Please enter the month, between January to June.\n')
            
    week = ['saturday', 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday','all']    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?').lower()
        #week = ['saturday', 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday','all']
        #if day == 'all':
          ## break
        if day in week:
            print('\nLet\'s get data for {}s.'.format(day.title()))
            break
        else:
            print('\nInvalid Input. please try again.\n')
            continue
 

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
    #load data from csv file.
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour
    
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        # in case we need filter by index or numbers 
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        month=months.index(month)+1
         # filter by month to create the new df
        df = df[df['Month']==month] 

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day']==day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['Month'].value_counts().idxmax()
    print('The Most Common Month: ',popular_month)


    # TO DO: display the most common day of week
    popular_day = df['Day'].mode()[0]
    print('The Most Common Day of Week: ',popular_day)


    # TO DO: display the most common start hour
    popular_start_hour = df['Hour'].mode()[0]
    print('The Most Common Start Hour: ',popular_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The Most commonly Used Start Station: ',popular_start_station)
    

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The Most commonly Used End Station: ',popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    group_station = df.groupby(['Start Station','End Station'])
    popular_trip = group_station.size().sort_values(ascending=False).head().idxmax()
    print('The Most Frequent Combination Trip: {} to {}'.format(popular_trip[0],popular_trip[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Trip Duration: ', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average Trip Duration: ', mean_travel_time)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print ('The Counts of User Types: ',user_types)

    # TO DO: Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print('The Counts of Gender: ',counts_of_gender)
    except:
        print('\nSorry! This City has no Gender Informations')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()
        print('\nThe Oldest User\'s yrar of Birth: ', int(earliest_year_of_birth))
        print('\nThe Youngest User\'s yrar of Birth: ', int(most_recent_year_of_birth))
        print('\nThe Most common User\'s yrar of Birth: ', int( most_common_year_of_birth))
        
    except:
        print('\nSorry! This City has no Birth Year Informations')
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    #if view_data != 'no' or view_data != 'yes':
      #  print('\nPlease answer yes or no only.')
    
    
    start_loc = 0
    end_loc =  5
   
    while (view_data == "yes" ):
        print(df.iloc[start_loc:end_loc])
        start_loc += 5
        end_loc = start_loc + 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == "no":
            break
  
       


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

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
