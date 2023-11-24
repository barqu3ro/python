import datetime

def add_business_days(start_date, num_days):
    current_date = start_date
    while num_days > 0:
        current_date += datetime.timedelta(days=1)
        if current_date.weekday() < 5:  # Monday to Friday
            num_days -= 1
    return current_date

# Example usage
start_date = datetime.date(2017, 6, 15)
num_days = 451
result_date = add_business_days(start_date, num_days)
print(result_date)



