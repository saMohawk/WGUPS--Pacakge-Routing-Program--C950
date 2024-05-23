import csv
import datetime
from package import packageHashTable
from package import Package
from hash_table import HashTable

class Truck:

    def __init__(self, packages, speed, mileage, address, departureTime, truckID):
        self.packages = packages
        self.speed = speed
        self.mileage = mileage
        self.address = address
        self.departureTime = departureTime
        self.time = departureTime
        self.truckID = truckID

    def __str__(self):
        return f'{self.packages}, {self.speed}, {self.mileage}, {self.address}, {self.departureTime}, {self.time}'

# read distance csv
with open("CSV/distance_file.csv") as distance_file:
    distance = csv.reader(distance_file)
    distance = list(distance)


# get addresses from csv
def getAddress(address):
    addressList = []
    with open('CSV/Address_File.csv') as address_file:
        addresses = csv.reader(address_file)
        for row in addresses:
            addressList.append(row[2])  # assign values
    return addressList
addressList = getAddress('Address_File.csv')

def distanceBetween(x, y):
    I = addressList.index(x)
    J = addressList.index(y)

    distance_from = distance[I][J]
    if distance_from == '':
        distance_from = distance[J][I]
    return float(distance_from)

# create truck objects, 'manually' loading packages in each truck
# Truck 1 will leave first, 8:00 AM local time.
truck1 = Truck([1, 13, 14, 15, 16, 19, 20, 21, 29, 30, 34, 40], 18, 0, "4001 South 700 East", datetime.timedelta(hours=8),1)

# truck 2 depart @ 10:20 AM. After 9's corrected address, all remaining EOD packages
truck2 = Truck([3, 8, 9, 12, 17, 18, 22, 23, 24, 27, 35, 36, 38, 39], 18, 0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20),2)

# truck 3 depart @ 9:05 AM, after late items arrive
truck3 = Truck([2, 4, 5, 6, 7, 10, 11, 25, 26, 28, 31, 32, 33, 37], 18, 0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5),3)

# debug check
# key = 3
# value = packageHashTable.getValue(key)
# # print(f'package info for {key}: {value}')


def deliverPackages(truck):
    notDelivered = []
    for pID in truck.packages:
        package = packageHashTable.getValue(pID) # find packages in hashtable
        package.truckID = truck.truckID #assign truckID to package
        package.departureTime = truck.departureTime
        notDelivered.append(package)   # place packages in notDelivered array

    truck.packages.clear()  # clear list, allow algorithm to reorganize package list

    while len(notDelivered) > 0:  # until all packages are delivered
        nextStop = 1000  # initialize variables
        nextPackage = None

        # begin algorithm
        for package in notDelivered:
            distanceNextStop = distanceBetween(truck.address, package.deliveryAddress) # find distance between two addresses
            if distanceNextStop < nextStop: # assigns the smallest distance to next stop
                nextStop = distanceNextStop
                nextPackage = package
                # package.finalAddress = package.deliveryAddress # updates delivery address

        if nextPackage is not None:
            nextPackage.deliveryTime = truck.time # records time when package is delivered
            nextPackage.departureTime = truck.departureTime

            if nextPackage.ID == "9":   # Check time for updated address for #9
                nextPackage.updateAddress(nextPackage.ID, truck.departureTime)

            truck.packages.append(nextPackage.ID)  # add package next to be delivered

            notDelivered.remove(nextPackage)  # remove from notDelivered array
            package.finalAddress = package.deliveryAddress
            truck.address = nextPackage.deliveryAddress  # update truck address
            truck.mileage += nextStop  # update mileage
            truck.time += datetime.timedelta(minutes=nextStop)

deliverPackages(truck1)
deliverPackages(truck3)
deliverPackages(truck2)  # will not depart until 10:20, truck3 will return by 9:37 so driver will be available

def getTruckAssignedToPackage(package_id):
    for truck in [truck1, truck2, truck3]:
        if package_id in truck.packages:
            return truck
    return None





# val = 13
# test = packageHashTable.getValue(val)
# print(test)