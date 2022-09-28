import datetime
while True:
    try:
        birthdate = input("Please enter your exact Date of Birth(eg.               March 6 2004):")
        birthday = datetime.datetime.strptime(birthdate, '%B %d %Y')
        break
    except:
        print("Please put in the Format 'Month Day Year' without any initial space")

today = datetime.datetime.today()
timedelta = (today - birthday).total_seconds()
print("You have been alive for:",timedelta,"seconds")
