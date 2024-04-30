import datetime
from package import packageHashTable
from truck import truck1, truck2, truck3


# C950 - Sara Mohammed
# Student ID: 006868543


print("****************************************************")
print("Western Governors University Parcel Service (WGUPS)")
print("****************************************************")
# print("The mileage for the route is:")
# print(truck1.mileage + truck2.mileage + truck3.mileage)
print("*************")

# option 1: print all package data at a given time
def checkAllPackageStatus(time):
    for id in range(1,41):
        package = packageHashTable.getValue(id)
        package.currentStatus(time)

        print("ID: ", package.ID, ", Current Status: ", package.status)


# option 2: print data for certain ID at a give time
def checkOnePackageStatus(packageID, time):
    package = packageHashTable.getValue(packageID)
    if package is None:
        print("No package found with ID: ", packageID)
        return

    package.currentStatus(time)
    print(f"ID: {package.ID}, Current Status: {package.status}")
    # package.currentStatus(time)
    # print(package)

# prompt for user to input time
print("Welcome to the WGUPS package status check interface.")
input_time = input("Please enter the time (HH:MM:SS format): ")
hour, minute, second = input_time.split(":")
time_entered = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))

# simple if statement that calls opt. 1 or 2
branch_input = input("Would you like to view the status of an individual package? (y/n): ")
if branch_input == "y":
    try:
        id_input = int(input("Please enter the package ID: "))
        package = packageHashTable.getValue(id_input)
        checkOnePackageStatus(id_input, time_entered)
       # print("ID: ", package.ID, ", Current Status: ", package.status)
    except ValueError:
        print("Please enter a valid package ID.")
        #exit()

elif branch_input == "n":
    try:
        print("Current status of all packages at ", time_entered, ":")
        checkAllPackageStatus(time_entered)
    except ValueError:
        print("invalid input :( please try again.")
        exit()

else:
    exit()


print("*************")
print("The mileage for the route is:")
print(truck1.mileage + truck2.mileage + truck3.mileage)
print("*************")
print("truck 1 completed delivery at: ", truck1.time)
print("truck 3 completed delivery at: ", truck3.time)
print("truck 2 completed delivery at: ", truck2.time)












