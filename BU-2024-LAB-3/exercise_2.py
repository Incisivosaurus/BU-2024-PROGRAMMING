def fix_odometer(odometer_reading, skipped_by):
    remainder = odometer_reading // skipped_by

    return odometer_reading - remainder


if __name__ == "__main__":
    print(fix_odometer(1680648, 5))
