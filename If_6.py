age = int(input('what year were you born? '))

if age <= 1924:
    print('The greatest Generation')
elif 1925 <= age <= 1945:
    print('The Slient Generation')
elif 1946 <= age <= 1964:
    print('baby boomer')
elif 1965 <= age <= 1980:
    print('Generation X')
elif 1981 <= age <= 1996:
    print('millennial')
elif 1997 <= age:
    print('Generation Z')
    
