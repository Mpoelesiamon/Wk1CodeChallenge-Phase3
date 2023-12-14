def convert_to_24_hour(hour, minute, period):
    if period == 'am':
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    time_24_hour = f"{hour:02d}{minute:02d}"
    print(f"The 24-hour time is: {time_24_hour}")
    return time_24_hour

# Example usage
convert_to_24_hour(8, 30, 'am')
