# MESSAGE "WELCOME"

# Repeat until quit:
# 	PROMPT "Select an option"
# 			"[1] Most occuring name"
# 			"[2] Min Year"
# 			"[3] Max Year"
# 			"[9] Quit"

# 	INPUT option

# 	Do option calculations

# 	Display Data Result

# MESSAGE "Goodbye"

# DATA
# name STRING
# year STRING
# city STRING
# event STRING
DATA_FILENAME = "data_subset.csv"

names = []
years = []
cities = []
events = []

def show_entries_with_name(name):
    print(f"Entries with name '{name}':")
    for i in range(len(names)):
        if names[i] == name:
            print(f"Year: {years[i]}, City: {cities[i]}, Event: {events[i]}")

def load_data():
    with open(DATA_FILENAME, "r") as file:
        for line in file:
            name, year, city, event = line.strip().split(",")
            names.append(name)
            years.append(year)
            cities.append(city)
            events.append(event)

def calculate_most_occurring_name():
    max_count_name = None
    name_counts = {}
    for name in names:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

        if max_count_name is None or name_counts[name] > name_counts[max_count_name]:
            max_count_name = name

    most_occurring_name = max_count_name
    print(f"The most occurring name is: {most_occurring_name} with {name_counts[most_occurring_name]} occurrences.")
    return most_occurring_name

def main():
    print("WELCOME")
    print("Loading data...")
    load_data()

    option = "0"
    while option != "9":
        print("Select an option")
        print("[1] Most occuring name")
        print("[2] Min Year")
        print("[3] Max Year")
        print("[9] Quit")

        option = input("Enter your option: ")

        if option == "1":
            print("Calculating most occurring name...")
            name = calculate_most_occurring_name()
            show_entries_with_name(name)

        elif option == "2":
            print("Calculating minimum year...")
            # Add code to calculate and display the minimum year
        elif option == "3":
            print("Calculating maximum year...")
            # Add code to calculate and display the maximum year
        elif option == "9":
            print("Quitting...")
        else:
            print("Invalid option. Please try again.")

    print("Goodbye")

if __name__ == "__main__":
    main()



