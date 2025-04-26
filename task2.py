import pandas as pd

df = pd.read_csv("Dataset .csv")
df.dropna(inplace=True)
df.drop('Switch to order menu', axis=1, inplace=True)
df.loc[:, 'Cuisines'] = df['Cuisines'].str.split(', ')
df = df.explode('Cuisines')

def reset_to_main():
    global df1
    df1 = df.copy()
    print("\nGoing back to the main menu...\n")
    currency(df1)

def cuisine(df1, city):
    city_filtered_df = df1[df1['City'] == city]
    if city_filtered_df.empty:
        print(f"\nNo restaurants available in {city}.")
    else:
        unique_cuisines = city_filtered_df['Cuisines'].unique()
        print(f"\nUnique Cuisines available in {city}:")
        for i, cuisine in enumerate(unique_cuisines, start=1):
            print(f"{i}. {cuisine}")
        print("0. Go back to the main menu.")
        try:
            cuisine_choice = int(input("\nEnter the number corresponding to your preferred cuisine: "))
            if cuisine_choice == 0:
                reset_to_main()
                return
            if cuisine_choice < 1 or cuisine_choice > len(unique_cuisines):
                print("Invalid choice. Please select a valid number.")
                return
            user_cuisine = unique_cuisines[cuisine_choice - 1]
            print(f"You selected: {user_cuisine}")
            cuisine_filtered_df = city_filtered_df[city_filtered_df['Cuisines'] == user_cuisine]
            if cuisine_filtered_df.empty:
                print(f"\nNo restaurants available for {user_cuisine} cuisine in {city}.")
            else:
                cuisine_filtered_df_sorted = cuisine_filtered_df.sort_values(by=['Aggregate rating', 'Average Cost for two'], ascending=[False, True])
                print(f"\nRestaurants serving {user_cuisine} cuisine in {city} (Sorted by Aggregate rating and Average Cost for Two):")
                print(cuisine_filtered_df_sorted[['Restaurant Name', 'Address', 'Aggregate rating', 'Average Cost for two', 'Has Table booking', 'Has Online delivery', 'Is delivering now']].head(10))
        except ValueError:
            print("Invalid input. Please enter a number.")

def city(df1, currency):
    filtered_df = df1[df1['Currency'] == currency]
    if filtered_df.empty:
        print("No restaurants available for the selected currency.")
        return
    else:
        unique_cities = filtered_df['City'].unique()
        print("\nAvailable Cities for the selected currency:")
        for i, city in enumerate(unique_cities, start=1):
            print(f"{i}. {city}")
        print("0. Go back to the main menu.")
    try:
        city_choice = int(input("\nEnter the number corresponding to your preferred city: "))
        if city_choice == 0:
            reset_to_main()
            return
        if city_choice < 1 or city_choice > len(unique_cities):
            print("Invalid choice. Please select a valid number.")
            return
        user_city = unique_cities[city_choice - 1]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    city_filtered_df = filtered_df[filtered_df['City'] == user_city]
    if city_filtered_df.empty:
        print("\n\n\tNo restaurants available for the selected city.")
    else:
        cuisine(df1, user_city)

def currency(df1):
    unique_currencies = df1['Currency'].unique()
    print("Available Currencies:")
    for i, currency in enumerate(unique_currencies, start=1):
        print(f"{i}. {currency}")
    print("0. Exit")
    user_choice = input("\nSelect the currency based on the country: ")
    try:
        user_choice = int(user_choice)
        if user_choice == 0:
            print("Exiting...")
            return
        if user_choice < 1 or user_choice > len(unique_currencies):
            raise IndexError
        user_currency = unique_currencies[user_choice - 1]
        print(f"You selected: {user_currency}")
        city(df1, user_currency)
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number from the list.")

df1 = df.copy()
currency(df1)


"""
Task 2 completed :
To Create a restaurant recommendation
system based on user preferences.
"""