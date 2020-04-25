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


class RestaurantPayroll:

    def main(self):
        list = {  # Employees
            HourlyWorker("Sean McKay", "202-555-0102", "D", 20),
            WaitStaff("Steve Zoyac", "202-555-0103", "B", 30, 150, 25),
            WaitStaff("David Witte", "202-555-0104", "D", 30, 140, 25),
            WaitStaff("Robert MacAuley", "202-555-0105", "L", 30, 145, 25),
            KitchenStaff("Kyle Evangelisto", "202-555-0106", "D", 40),
            KitchenStaff("Angel Avelar", "202-555-0107", "L", 50),
            KitchenStaff("Aidan Murphey", "202-555-0108", "D", 40),
            KitchenStaff("Enrico Duller", "202-555-0109", "B", 55)
        }
        for element in list:  # For every worker , print out their paycheck
            element.generatePayCheck()


startup = RestaurantPayroll
startup.main(startup)
