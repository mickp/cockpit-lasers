## This module defines the interface for a laser that can be controlled
# by cockpit.devices.laserpower.
import abc
import Pyro4
import serial
import socket
import threading
import time

# The name of the config section for this device
CONFIG_NAME = 'dummyLaser'
# The name of the class that provides the interface specified below.
CLASS_NAME = 'Laser'


## This is a prototype for a class to be used with laser_server.
class Laser(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, serialPort, baudRate, timeout):
        ## Should connect to the physical device here and set self.connection
        # to a type with read, readline and write methods (e.g. serial.Serial).
        self.connection = None


    ## Simple passthrough.
    @abc.abstractmethod
    def read(self, numChars):
        return self.connection.read(numChars)


    ## Simple passthrough.
    @abc.abstractmethod
    def readline(self):
        return self.connection.readline().strip()


    ## Send a command.
    @abc.abstractmethod
    def write(self, command):
        # Override if a specific format is required.
        response = self.connection.write(command + '\r\n')
        return response

    
    ## Query and return the laser status.
    @abc.abstractmethod
    def getStatus(self):
        result = []
        # ...
        return result


    ## Turn the laser ON. Return True if we succeeded, False otherwise.
    @abc.abstractmethod
    def enable(self):
        pass


    ## Turn the laser OFF.
    @abc.abstractmethod
    def disable(self):
        pass


    ## Return True if the laser is currently able to produce light. We assume this is equivalent
    # to the laser being in S2 mode.
    @abc.abstractmethod
    def getIsOn(self):
        pass


    ## Set the laser power in native units.
    @abc.abstractmethod
    def setPower(self, level):
        pass


    ## Return the max. power in mW.
    @abc.abstractmethod
    def getMaxPower_mW(self):
        pass


    ## Return the current power in native units.
    @abc.abstractmethod
    def getPower(self):
        pass


    ## Return the current power in mW.
    @abc.abstractmethod
    def getPower_mW(self):
        pass


    ## Set the power from an argument in mW.
    @abc.abstractmethod
    def setPower_mW(self, mW):
        pass