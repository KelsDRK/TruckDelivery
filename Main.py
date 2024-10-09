# Kelston Burgess
# Student ID: 010614346

import csv
import datetime

from HashTable import HashTable
from Package import Package
from Truck import Truck

# Initialize hash table for storing packages
myHash = HashTable()

# Load distance, address, and package data
def load_csv_data(file_name):
    """Load data from a CSV file and return it as a list."""
    with open(file_name) as csvfile:
        return list(csv.reader(csvfile))

# Load CSV data into respective variables for distances, addresses, and packages
CSV_Distance = load_csv_data("CSVDistances.csv") # Load distances between locations from the CSV file
CSV_Address = load_csv_data("CSVAddresses.csv") # Load addresses from the CSV file
CSV_Package = load_csv_data("CSVPackages.csv") # Load package details from the CSV file


# Opening file and reading contents is O(n)
# Inserting Package into hash table is O(1)
def load_package_data(file_name, hashtable):
    """Load package data from CSV and insert it into hash table."""

    # Open the CSV file containing package data
    with open(file_name) as packages:
        package_data = csv.reader(packages) # Read the CSV file using the csv.reader
        next(package_data)  # Skip the header row of the CSV file
        for package in package_data:
            pID = int(package[0])
            paddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline_time = package[5]
            pWeight = package[6]
            pStatus = package[3]

            # Create a package object using the extracted attributes
            p = Package(pID, paddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus)

            # Add the package object to the provided hash table using the package ID as the key
            hashtable.add(pID, p)


# Iterating over rows in CSV_Address is O(n)
def extract_address(address, csv_address):
    """Extract the package ID associated with a given address from the CSV data."""

    # Iterate through each row in the CSV address data
    for row in csv_address:
        # Check if the specified address is found in the relevant column (index 2)
        if address in row[2]: # Adjust index if necessary
            return int(row[0]) # Return the package ID as an integer if a match is found
    return None  # Return None if address is not found

# Two index range checks (X and Y) are both done in constant time O(1)
def distance_between(x, y):
    """
    Retrieve the distance between two points from the CSV_Distance structure.

    Parameters:
    x_index (int): The index of the first point.
    y_index (int): The index of the second point.

    Returns:
    float: The distance between the two points.

    Raises:
    IndexError: If x_index or y_index is out of range.
    ValueError: If the distance cannot be converted to a float.
    """
    try:
        # Check if indices are within the valid range
        if x < 0 or y >= len(CSV_Distance):
            raise IndexError("x_index is out of range.")
        if y < 0 or y >= len(CSV_Distance[0]):
            raise IndexError("y_index is out of range.")

        # Get the distance from the 2D list
        distance = CSV_Distance[x][y]

        if distance == '':
            # If the distance is an empty string, check the inverse
            distance = CSV_Distance[y][x]

        if distance is None or distance == '':
            raise ValueError("Distance not found for the provided indices.")

        return float(distance)
    except IndexError as e:
        raise IndexError(f"Index out of range: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid distance value: {e}")

# Initialize trucks with package lists and starting locations
truck1 = Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East", datetime.time(hour=8))
truck2 = Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0, "4001 South 700 East", datetime.time(hour=10, minute=20))
truck3 = Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East", datetime.time(hour=9, minute=5))

package_hash = HashTable()
load_package_data('CSVPackages.csv', package_hash)

# Method for ordering packages on a given truck using the nearest neighbor algorithm
# Also calculates distance a given truck drives once the packages are sorted
# Time complexity is O(n^2)
def package_delivery_start(truck):
    # Create a list to hold packages that have not yet been delivered
    not_delivered = []
    # Populate the not_delivered list with packages from the truck
    for packageID in truck.packages:
        package = package_hash.get(packageID) # Retrieve package using its ID
        if package:  # Check if the package exists
            not_delivered.append(package) # Add to not_delivered list if found

    # Clear the truck's package list to prepare for new delivery order
    truck.packages.clear()

    # Continue delivering packages until there are none left in not_delivered
    while not_delivered:
        next_address = float('inf')  # Initialize next_address with infinity to find the minimum distance
        next_package = None # Placeholder for the closest package

        # Iterate through the not_delivered list to find the closest package
        for package in not_delivered:
            # Extract indices for the truck's current address and the package's address
            truck_address = extract_address(truck.address, CSV_Address)
            package_address = extract_address(package.address, CSV_Address)
            distance = distance_between(truck_address, package_address)

            # Check if this package is closer than the previously found closest package
            if distance < next_address:
                next_address = distance
                next_package = package

        # If no package is found (shouldn't happen if not_delivered is populated correctly)
        if next_package is None:
            break  # Exit the loop if there are no packages left to deliver

        # Add the closest package to the truck's package list for delivery
        truck.packages.append(next_package.ID)

        # Remove the delivered package from the not_delivered list
        not_delivered.remove(next_package)

        # Update the truck's attributes based on the delivery
        truck.mileage += next_address
        truck.address = next_package.address

        # Convert truck's current time to a datetime object for calculations
        current_time = datetime.datetime.combine(datetime.date.today(), truck.time)

        # Update the truck's time based on the distance traveled
        current_time += datetime.timedelta(hours=next_address / 18)

        # Convert the updated time back to datetime.time format
        truck.time = current_time.time()

        # Set the delivery and departure times for the delivered package
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.depart_time

# Execute package delivery for each truck
package_delivery_start(truck1)
package_delivery_start(truck2)

# Truck 3 does not leave until the first two trucks have finished delivering
truck3.depart_time = min(truck1.time, truck2.time)
package_delivery_start(truck3)


def timedelta_to_time(td):
    """
    Convert a datetime.timedelta to a datetime. Time object.

    Parameters:
    td (datetime.timedelta): The timedelta to convert.

    Returns:
    datetime.time: The corresponding time.
    """
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Ensure hours are within 0-23
    hours = hours % 24

    return datetime.time(hours, minutes, seconds)


class Main:
    # User Interface
    # Upon running the program, the following message will appear.
    print("Western Governors University Parcel Service (WGUPS)")
    print()

    # Display the total mileage for all trucks combined
    print("The mileage for the route is:")
    print(truck1.mileage + truck2.mileage + truck3.mileage)  # Print total mileage for all trucks
    print()

    # Prompt the user to start the process by entering the word "time"
    text = input("To start please type the word 'time' (All else will cause the program to quit): ")

    # If the user enters "time", proceed to request a specific time for checking packages
    if text == "time":
        try:
            # Ask the user to enter a specific time in HH:MM:SS format
            user_time = input("Please enter a time to check status of package(s). Use the following format, HH:MM:SS: ")
            (h, m, s) = user_time.split(":")  # Split the input into hours, minutes, and seconds

            # Convert the time into a timedelta object for easy manipulation
            convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            new_convert_time_delta = timedelta_to_time(convert_timedelta)  # Convert timedelta to time format

            print(convert_timedelta)  # Display the converted timedelta

            # Ask the user if they want to see the status of all packages or just one
            second_input = input("To view the status of an individual package please type 'solo'. For a rundown of all "
                                 "packages please type 'all': ")

            # If the user enters "solo", prompt for a specific package ID
            if second_input == "solo":
                try:
                    # The user will be asked to input a package ID; invalid entry will cause the program to quit
                    solo_input = input("Enter the numeric package ID: ")
                    package = package_hash.get(int(solo_input))  # Retrieve the package using the entered ID

                    # Update the package status based on the provided time
                    package.update_status(new_convert_time_delta)
                    print(str(package))  # Print the package information

                except ValueError:
                    # Handle invalid inputs for package ID
                    print("Entry invalid. Closing program.")
                    exit()

            # If the user types "all", display information for all packages at once
            elif second_input == "all":
                try:
                    for packageID in range(1, 41):  # Loop through package IDs 1 to 40
                        package = package_hash.get(packageID)  # Retrieve each package
                        package.update_status(new_convert_time_delta)  # Update its status
                        print(str(package))  # Print the package information
                except ValueError:
                    # Handle errors during status updates
                    print("Entry invalid. Closing program.")
                    exit()
            else:
                # Exit if an invalid option is chosen
                exit()
        except ValueError:
            # Handle errors during time input conversion
            print("Entry invalid. Closing program.")
            exit()
    else:
        # If the user input is anything other than "time"
        print("Entry invalid. Closing program.")
        exit()