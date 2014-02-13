#-*-coding:utf-8-*-
#define variable cars as a integer
cars=100
#define variable space_in_a_car as a float
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven * space_in_a_car
average_passengers_per_car=passengers/cars_driven

#print the counts of cars
print "There are",cars,"cars available."
#print the counts of drivers available
print "There are only",drivers,"drivers available."
#print the counts of cars_not_driven
print "There will be",cars_not_driven,"empty cars today."
#print the counts that we can transport
print "We can transport",carpool_capacity,"people today."
#print the counts of passengers today
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car"