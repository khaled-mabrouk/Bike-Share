import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities_list=['washington','chicago','new york city']
months_list = ['january','february','march','april','may','june']
days_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
   #get user input for city (chicago, new york city, washington)
    
    
    
    city = input('Please choose your favorite city from this list[chicago,new york city,washington]:  ').lower().strip()
    
    #check input :
    while city  not in cities_list:
        city = input('Oops,invalid input ,Please choose your favorite city from this list[chicago-new york city-washington]: ').lower().strip()
        
        if city in cities_list:
             break
                
    # get user input for month (all, january, february, ... , june)
    
    
    
    
    month =input('Please,choose your favorite month or all  (all,january, february,march,april,may,june):  ').lower().strip()
    
    #check input :
    
    while month  not in months_list and month != 'all':
        month = input('Oops,invalid input ,Please choose your favorite  month or all  (all, january, february,march,,april,may,june):  '  ).lower().strip()
        
        if month in months_list or month == 'all':
             break  
                
    #get user input for day of week (all, monday, tuesday, ... sunday)
    
    
    
    
    day =input('Please,choose your favorite day or all (all,sunday,monday, tuesday,wednesday,thursday,friday,saturday):   ').lower().strip()
    
    #check input :
    
    while day not in days_list and day != 'all':
        day = input('Oops,invalid input ,Please choose your favorite  day or all (all,sunday, monday,tuesday,wednesday,thursday,friday,saturday ):  ').lower().strip()
        
        if day in  days_list or day == 'all':
             break            
    
        
           
     




     

    
    print(f'Your choices are {city, month, day}')

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
    #loading data from csv files filterd by city
    df = pd.read_csv(CITY_DATA[city])
    
    #Conveting start time column to datetime format 
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    #filtered dataframe(df) by month and day of week wich choosen by the user :
    if month in months_list:
        month = months_list.index(month) + 1
        df = df[df['month']==month]
    if day in days_list:
        df = df[df['day of week']==day.title()]

    print('-'*40)
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # calculating the most common month 
    frequent_month = df['month'].mode()[0]
    frequent_month = months_list[frequent_month-1] 
    print('The most frequent month is {}\n'.format(frequent_month).title())    

    # calculating the most common day of week
    frequent_day = df['day of week'].mode()[0]
    print('The most frequent day of week is {}\n'.format(frequent_day))  

    #calculating the most common start hour
    frequent_hour= df['hour'].mode()[0]
    print('The most frequent start hour  is {}\n'.format(frequent_hour))  


   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Calculating the most commonly used start station
    frequent_start_station = df['Start Station'].mode()[0]
    
    print('The most frequent start station  is {}\n'.format(frequent_start_station))


    #Calculating most commonly used end station:
    
    frequent_end_station = df['End Station'].mode()[0]
    
    print('The most frequent end station is {}\n'.format(frequent_end_station))

    #Calculating The most frequent combination of start station and end station trip
    
    trip  = 'from '+df['Start Station']+' to '+ df['End Station']
    
    frequent_trip = trip.mode()[0]
    
    print('The most frequent trip is {}\n'.format(frequent_trip))
    
 

   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculating total Trip Duration :
    total_travel_time = df['Trip Duration'].sum()
    
    #converting total_travel_time  to (hour,minutes,seconds):
    
    hour = total_travel_time//3600
    minutes =(total_travel_time-(hour*3600))//60
    seconds = (total_travel_time-(hour*3600))-(minutes*60)

    print(f'total Trip Duration  is "{hour}" Hour and "{minutes}" Minutes and "{seconds}" Seconds\n')

    


    # Calculating mean of Trip Duration:
    
    mean_duration_time = df['Trip Duration'].mean()
    
    #converting mean_duration_time  to (hour,minutes,seconds):
    
    hour = mean_duration_time //3600
    minutes =(mean_duration_time -(hour*3600))//60
    seconds = (mean_duration_time -(hour*3600))-(minutes*60)
    
    print(f'mean of Trip Duration  is "{hour:.0f}" Hour and "{minutes:.0f}" Minutes and "{seconds:.3f}" Seconds\n')
    

    
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # showing counts of user types
    counts_user_types = df['User Type'].value_counts()
    
    print(f'counts of user types are {counts_user_types} \n')
   
    # Display counts of gender
    if city != 'washington':
        counts_gender = df['Gender'].value_counts()
        print(f'counts of gender are {counts_gender} \n')
              
    #calculatin earliest, most recent, and most common year of birth
    if city != 'washington': 
        earliest_year = df['Birth Year'].min()        
        most_recent_year = df['Birth Year'].max()
        most_common_year =  df['Birth Year'].mode()[0] 
    #Displaying  earliest, most recent, and most common year of birth 
                
        print(f'The earliest year of birth is : {earliest_year:.0f} \n ')
                
        print(f'The most recent year of birth is :  {most_recent_year :.0f} \n ')  
                
        print(f'The most common year of birth is : {most_common_year:.0f} \n ')      
    

   
     
   
                


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_raw_data(df):
    """Showing five rows from raw data for user if he wants this"""
                
    #Asking user if he wants raw data
    
    
    Answer = input('Would you like to show you five rows of raw data (yes,no)?  ').lower().strip()
    
    
    
        
    
            
    count=0  
    while Answer == 'yes':
        
        print(df.iloc[count:count+5])
        count+=5
        Answer = input('Would you like to show  you another five rows of raw data (yes,no)?  ').lower().strip()
        if Answer != 'yes':
             break
                
                
                
                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
       
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_raw_data(df)
                
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
        if restart.lower() != 'yes':
           break


if __name__ == "__main__":
	main()
