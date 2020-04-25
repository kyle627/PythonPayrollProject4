"""
CSC-226 Chapter 12/weeks 11-12 Topics OOP - Inheritance
Language: Python
Programmer: A. Wright
Date:       4/19/2020
Description: RestaurantPayroll.py
Inheritance/Polymorphism Programming Project

 MODIFIED BY:   KYLE EVANGELISTO
 DATE: 4/22/2020 -> 4/23/2020 (it is very late at night)
 *
"""
from RestaurantWorker import WaitStaff
from RestaurantWorker import KitchenStaff
from RestaurantWorker import HourlyWorker


def main():
    # Employees

    bussBoy = HourlyWorker("Sean McKay", "202-555-0102", "D", 20)
    waiterA = WaitStaff("Steve Zoyac", "202-555-0103", "B", 30, 150, 25)
    waiterB = WaitStaff("David Witte", "202-555-0104", "D", 30, 140, 25)
    waiterC = WaitStaff("Robert MacAuley", "202-555-0105", "L", 30, 145, 25)
    chefA = KitchenStaff("Kyle Evangelisto", "202-555-0106", "D", 40)
    chefB = KitchenStaff("Angel Avelar", "202-555-0107", "L", 50)
    chefC = KitchenStaff("Aidan Murphey", "202-555-0108", "D", 40)
    chefD = KitchenStaff("Enrico Duller", "202-555-0109", "B", 55)

    list = [bussBoy, waiterA, waiterB, waiterC, chefA, chefB, chefC, chefD]  # Employees in a list called list

    # For every worker , print out their paycheck

    for element in list:
        element.generatePayCheck()


main()
