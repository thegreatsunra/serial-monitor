#!/usr/bin/env python3
"""
Main module docstring
"""
from datetime import datetime
import serial


def hello_world():
    """
    Returns 'Hello World'
    """
    return "Hello World"


def read_serial_and_write_to_log():
    """
    Reads from serial port and writes output to log file
    """
    log_file = "/home/folk/stuff/logs/sump_log.txt"
    serial_port = "/dev/ttyACM0"
    while True:
        try:
            ser = serial.Serial(port=serial_port, baudrate=9600, timeout=1)
            ser.reset_input_buffer()
            while True:
                try:
                    if ser.in_waiting > 0:
                        line = ser.readline().decode("utf-8").rstrip()
                        print(str(datetime.now()) + " " + line)
                        with open(log_file, mode="a", encoding="utf-8") as file:
                            file.write(str(datetime.now()) + " " + line + "\n")
                            file.close()
                except (Exception) as exception:
                    print("Exception: \n", exception)
                    raise
        except (Exception) as exception:
            print("Exception: \n", exception)
            continue


def main():
    """
    Main entry point of the app
    """
    read_serial_and_write_to_log()


if __name__ == "__main__":
    ## This is executed when run from the command line
    main()
