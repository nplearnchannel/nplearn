day = 'Sunday'
year = 2021

# Method 1: % sign
print('Today is a %s of %s' % (day,year))

# Method 2: format
print('Today is a {} of {}'.format(day,year))
print('Today is a {date_name} of {year}, and last {date_name} is also in {year} as well'.format(date_name=day,year=year))

# Method 3: fstring
print(f'Today is a {day} of {year}')

my_dict = {'day':'Sunday','year':2021}
print(f"Today is a {my_dict['day']} of {my_dict['year']}")

# ====================================== Multiple lines print ======================================
# using ( )
my_message = (
    f"Today is a {day} "
    f"of {year}"
)
print(my_message)

# fstring with \
my_message = f"""Today is a {day} \
of {year}
"""
print(my_message)

# fstring without \
my_message = f"""Today is a {day} 
of {year}
"""
print(my_message)