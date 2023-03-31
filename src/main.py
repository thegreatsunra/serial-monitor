#!/usr/bin/env python3
"""
Main module docstring
"""
import serial
from datetime import datetime

def hello_world():
    """Returns 'Hello World'"""
    return "Hello World"


def main():
    """Main entry point of the app"""
    while True:
        try:
            logfile = "/home/ribbon/log.txt"
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            ser.reset_input_buffer()
            while True:
                try:
                    if ser.in_waiting > 0:
                        line = ser.readline().decode('utf-8').rstrip()
                        print(str(datetime.now()) + " " + line)
                        with open(logfile, "a") as file:
                            file.write(str(datetime.now()) + " " + line + "\n")
                            file.close()
                except (Exception) as exception:
                    print("Exception: \n", exception)
                    raise
        except (Exception) as exception:
            print("Exception: \n", exception)
            continue


if __name__ == "__main__":
    ## This is executed when run from the command line
    main()
