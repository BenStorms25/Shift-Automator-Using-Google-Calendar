# this is a program that will take a pdf of a course syllabus, find the final date, and write that to Google Calendar.

import quickstart

class Shift:
    def __init__(self, date, start, end):
        self.date = date
        self.start = start
        self.end = end


def main():


    #creates service for google calendar to be written to.
    service = quickstart.createService()

    #beginning message
    print("Hello, this is to help you stay organized with your shift throughout the week.")

    #creates list of shifts that will be written to.
    listofShifts = []
    shiftInfoString = input("Enter the shift in the form: yyyy-mm-dd Start End, with spaces in between: ")
    listofShifts.append(shiftInfoString)

    while(shiftInfoString != ''):

        shiftInfoString = input("Enter the shift: ")
        listofShifts.append(shiftInfoString)

    #remove last element of listOfShifts (should be '')
    listofShifts.pop()

    listOfShiftObj = []

    for shift in listofShifts:
        shiftList = shift.split()
        thisShift = Shift(shiftList[0], shiftList[1], shiftList[2])
        listOfShiftObj.append(thisShift)
    
    print(listOfShiftObj)

    listOfShiftObj = quickstart.formatTime(listOfShiftObj)
    for shift in listOfShiftObj:
        print(shift.start)


    calID = quickstart.createCalendar(service, "Work Shifts")
    
    for shiftObj in listOfShiftObj:
        quickstart.insertEvent(service = service, calendarId = calID, startDate = shiftObj.date, endDate = shiftObj.date, startTime = shiftObj.start, endTime = shiftObj.end)

main()





