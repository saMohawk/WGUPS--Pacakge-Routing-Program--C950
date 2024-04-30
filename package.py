import csv
from hash_table import HashTable

# package object information
class Package:
    def __init__(self, ID, deliveryAddress, city, state, Zip, deadline, weight, notes, status):
        self.ID = ID
        self.deliveryAddress = deliveryAddress
        self.city = city
        self.state = state
        self.Zip = Zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.deliveryTime = None
        self.departureTime = None

    def __str__(self):
        return (f'ID: {self.ID}, address: {self.deliveryAddress}, '
                f'city: {self.city}, state: {self.state}, zip: {self.Zip},'
                f' deadline: {self.deadline}, weight: {self.weight}, notes: {self.notes}, status: {self.status}')


    def currentStatus(self, time_entered): # find status of package at any give time
        if self.deliveryTime < time_entered:
            self.status = "Delivered"
        elif self.departureTime > time_entered:
            self.status = "at hub"
        else:
            self.status = "out for delivery"

# create hash table
packageHashTable = HashTable()

 # create and load package data from csv
def createPackage(file):
    with open(file) as packages:
       data =  csv.reader(packages, delimiter=',')
      #  next(data) # skip header
       for packages in data:
           # print("test",  packages)
           pID = int(packages[0])
           pdeliveryAddress = packages[1]
           pcity = packages[2]
           pstate = packages[3]
           pZip = packages[4]
           pdeadline = packages[5]
           pweight = packages[6]
           pnotes = packages[7]
           pstatus = "@ Hub"  # call current status function

           p = Package(pID, pdeliveryAddress, pcity, pstate, pZip, pdeadline, pweight, pnotes, pstatus)

           packageHashTable.insert(pID, p)

file_path = 'packageCSV.csv'
createPackage(file_path)

# test
# key = '1'
# value = packageHashTable.getValue(key)
# print(f'package info for {key}: {value}')
















