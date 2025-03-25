#!/usr/bin/env python3
"""
Main module docstring
"""
from datetime import datetime
import time
import serial
import serial.tools.list_ports
import logging
import os


def find_serial_port():
    """
    Searches for a device whose port name starts with '/dev/ttyACM'.
    """
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if port.device.startswith("/dev/ttyACM"):
            return port.device
    return None


def open_serial_connection(baudrate=9600, timeout=1):
    """
    Attempts to open a serial connection to the device.
    """
    port = find_serial_port()
    if port:
        try:
            logging.info(f"Connecting to {port}")
            return serial.Serial(port, baudrate=baudrate, timeout=timeout)
        except serial.SerialException as e:
            logging.error(f"Failed to open port {port}: {e}")
    else:
        logging.info("No serial device found.")
    return None


def log_serial_data(ser, log_file):
    """
    Reads from the serial port and writes output to the log file.
    """
    while True:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode("utf-8").rstrip()
                timestamped_line = f"{datetime.now()} {line}"
                logging.info(f"Received: {timestamped_line}")
                with open(log_file, mode="a", encoding="utf-8") as file:
                    file.write(timestamped_line + "\n")
            else:
                time.sleep(0.1)  # Reduce CPU usage if there's no data
        except (serial.SerialException, UnicodeDecodeError) as e:
            logging.error(f"Error reading from serial port: {e}")
            ser.close()
            break  # Exit to attempt reconnection


def read_serial_and_write_to_log():
    """
    Manages connection and reconnection to the serial device.
    """
    # Use the current user's home directory for portability
    home_dir = os.path.expanduser("~")
    log_file = os.path.join(home_dir, "stuff", "logs", "serial_log.txt")

    while True:
        ser = open_serial_connection()
        if ser is None:
            logging.info("Retrying connection in 2 seconds...")
            time.sleep(2)
            continue

        log_serial_data(ser, log_file)
        logging.info(
            "Device disconnected or error occurred. Attempting reconnection in 2 seconds..."
        )
        time.sleep(2)


def main():
    """
    Main entry point of the app.
    """
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s"
    )
    read_serial_and_write_to_log()


if __name__ == "__main__":
    main()
