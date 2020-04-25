"""
CSC-226 Chapter 12/weeks 11-12 Topics OOP - Inheritance
Sample Program:  RestaurantPayroll
Sample Language: Python
Programmer: A. Wright
Date:       4/19/2020
Description: RestaurantWorker.py
Inheritance/Polymorphism Programming Project
 *
 * super class RestaurantWorker has a self.__name, phone, netPay and a shift  these
 * are common properties of all workers at the Blue Moon Cafe
 * set and get methods are provided and there is a
 * polymorphic generatePayCheck() method that is meant to be overridden in
 * sub classes
 * NOTE the enum type is not supported by Python 3 so Shift is represented as a Set

 MODIFIED BY:   KYLE EVANGELISTO
 DATE: 4/22/2020 -> 4/23/2020 (it is very late at night)
 *
"""


class RestaurantWorker:
    allShifts = {'B', 'L', 'D', 'S'}
    '''
    * INITIALIZER (like a CONVERSION constructor that builds a RestaurantWorker object)
    * accepts inputs for: self.__name, phone, shift  
    *
    '''

    def __init__(self, name, phone, shift):

        self.__name = name  # __name is 'hidden' (by name mangling) no direct
        self.__phone = phone  # access from outside class, app uses
        self._shift = shift  # @property getter and @setter
        self._netPay = 0
        self._HealthInsuranceCOST = 68.50

    # Python style of set/get methods are like C# fields - uses properties

    @property  # can take the place of a getName() *READ-ONLY* attribute
    def name(self):  # Coded in C# style of protecting object 'fields'
        """ Return the name."""
        return self.__name

    @name.setter  # can take the place of a setName()
    def name(self, name):
        """ Set the name """
        self.__name = name

    '''
     * Mutator: setPhone()        coded like Java
     * Sets self.__phone to the provided input phone number
     *  
     '''

    def setPhone(self, phone):
        self.__phone = phone

    '''
     * Mutator: setShift()
     *          verify valid input (member of set allShifts
     '''

    def setShift(self, shift):
        if shift in RestaurantWorker.allShifts:
            self._shift = shift

    '''
     * Accessor: getPhone()
     *     returns a copy of the object's phone number
     '''

    def getPhone(self):
        return self.__phone

    '''
     * Accessor: getShift()
     *     returns a copy of the object's shift Breakfast, Lunch, Dinner, or Swing
     '''

    def getShift(self):
        if self._shift == 'B':
            shift = 'Breakfast'
        elif self._shift == 'L':
            shift = 'Lunch'
        elif self._shift == 'D':
            shift = 'Dinner'
        else:
            shift = 'Swing'
        return shift

    '''
     * Accessor: getPay()
     *     returns a copy of the object's pay
     '''

    def getPay(self):
        return self._netPay

    '''
    * Accessor getHealthInsuranceCOST()
    *   returns a copy of the Health Insurance Cost
    '''

    def getHealthInsuranceCost(self):
        return self._HealthInsuranceCOST

    '''
      * Mutator: generatePayCheck()
      * specific to each RestaurantWorker
      * 
    '''

    def generatePayCheck(self):

        print(" ******************NON-NEGOTIABLE***********")
        print('\tName: ' + self.__name)
        print(" ---------------DO NOT CASH----------------")
        print(f'\n\t ****$ {self._netPay:.2f}')
        print('\n*******************************************')

    '''
     * Accessor: __str__() -- Python's toString()
     * 
     * produces a String version of the object
    '''

    def __str__(self):
        out = "\tBlue Moon Cafe Employee Information\n"
        out += " " + self.__name + "\t" + self.__phone + "\tShift: " + self.getShift() + "\n"

        return out


class HourlyWorker(RestaurantWorker):
    hourlyRate = 15

    def __init__(self, name, phone, shift, hours):
        super().__init__(name, phone, shift)

        self._hours = hours

    @property  # can take the place of a gethours()
    def hours(self):  # can be called by using its identifier
        """ returns the number of hours worked """
        return self._hours

    @hours.setter  # can take the place of a setHours()
    def hours(self, hours):
        """ Set the hours """
        self._hours = hours

    def calculatePay(self):  # Calculates Hourly worker pay
        self._netPay = (self._hours * self.hourlyRate) - self._HealthInsuranceCOST
        return self._netPay

    def generatePayCheck(self):  # generates pay check by using calcpay method and calling super generatepaycheck
        _netPay = self.calculatePay()
        super().generatePayCheck()

    def __str__(self):  # to string
        out = super().__str__()
        out += 'HourlyWorker Pay Rate:$ {:,.2f}'.format(self.hourlyRate)
        return out


class WaitStaff(HourlyWorker):

    def __init__(self, name, phone, shift, hours, gratuities, uniformAllowance):
        super().__init__(name, phone, shift, hours)
        self._gratuities = gratuities
        self._uniformAllowance = uniformAllowance

    '''
        * Accessor getGratuities()
        *   returns Gratuities
        '''

    @property
    def getGratuities(self):
        return self.gratuities

    '''
    * Mutator setGratuities()
    *   returns Gratuities
    '''

    def setGratuities(self, gratuities):
        return

    '''
    * Accessor getUniformAllowance()
    *   returns UniformAllowance
     '''

    @property
    def getUniformAllowance(self):
        return self.uniformAllowance

    def calculatePay(self):  # Calculates wait staff pay
        pay = (self.hours * self.hourlyRate) + self._gratuities - self.getHealthInsuranceCost()
        return pay

    def generatePayCheck(self):  # generates pay check by using calcpay method and calling super generatepaycheck
        self._netPay = self.calculatePay()
        super().generatePayCheck()

    def __str__(self):  # to string
        out = super.__str__()
        out += '\nEmployee Gratuities: $ {:,.2f}'.format(self.getGratuities)
        out += '\nEmployee Uniform Allowance $ {:,.2f}'.format(self.getUniformAllowance)
        return out


class KitchenStaff(HourlyWorker):
    overTimeRate = 1.5

    def __init__(self, name, phone, shift, hours):
        super().__init__(name, phone, shift, hours)

    '''
    * Mutator getOverTimeRate()
    *   returns OverTimeRate
    '''

    def getOverTimeRate(self):
        return self.overTimeRate

    def calculatePay(self):  # conditional statement to check and see if kitchen staff has more than 40 hours.
        # Calculates their pay and returns it
        if self.hours > 40:
            pay = ((self.hourlyRate * 40) + ((self.hourlyRate * self.overTimeRate) * (self.hours - 40))) \
                      - self.getHealthInsuranceCost()
            return pay
        else:
            pay = (self.hourlyRate * self.hours) - self.getHealthInsuranceCost()
            return pay

    def generatePayCheck(self):  # generates pay check by using calcpay method and calling super generatepaycheck
        self._netPay = self.calculatePay()
        super().generatePayCheck()

    def __str__(self):
        out = super.__str__()
        out += "\nEmployee's hours of overtime: " + self.hours - 40
        return out
