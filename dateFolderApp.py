import os
import calendar
import datetime

# REQUIRES - user fill out rootFolderPath.txt
# asks user to input year and month numerically
# generates folder for that month e.g: Apr 2023
# generates folders for each day of month in format 01042023, 02042023 

numToMonth = {
    1 : "Jan",
    2 : "Feb",
    3 : "Mar",
    4 : "Apr",
    5 : "May",
    6 : "Jun",
    7 : "Jul",
    8 : "Aug",
    9 : "Sep",
    10 : "Oct",
    11 : "Nov",
    12 : "Dec",

}


def getDaysInMonthYear(month, year):
    num_days = calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days + 1)]
    
    return days

def buildMonthFolder(month, year):

    return

def main():
    # 1. open root folder
    with open("rootFolderPath.txt", "r") as file:
        rootFolderName = file.readline()

    # 2. ask for year and month
    year = int(input("What year to input for? (1 - 9999)"))
    month = int(input("What month to input for? (1 - 12)"))

    # 3. get all the days in that month of that year
    days = getDaysInMonthYear(month, year)

    # 4. create new month folder inside of root folder
    directory = numToMonth[month] + " " + str(year)
    path = os.path.join(rootFolderName, directory)
    os.mkdir(path)
    print("New month folder created in " + path)


    # 5. create day folders inside of month folder
    for monthDay in days:
        formatMonthDay = str(monthDay).split("-")
        year = formatMonthDay[0]
        month = formatMonthDay[1]
        day = formatMonthDay[2]
        dayMonthYear = day + month + year
        
        dayPath = os.path.join(rootFolderName, directory, dayMonthYear)
        os.mkdir(dayPath)
    input()
    return
    


if __name__ == "__main__":
    
    main()
    input()
    while True:
        pass



