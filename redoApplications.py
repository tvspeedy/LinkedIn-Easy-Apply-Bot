'''
Reads in re-appliedFailedApplications.txt, gets the jobID, and updates output.csv to reflect
the successfull application
'''
import csv
from _csv import reader


def re_AppliedJobIDs():
    reAppliedJobIds = []

    with open("res/re-appliedFailedApplications.txt", "r") as my_file:
        file_reader = reader(my_file)
        # do this for all the rows
        for entry in file_reader:
            reAppliedJobIds.append(entry[0])

    return reAppliedJobIds

def outputCSV():
    csvData = []

    with open("res/output.csv", "r") as my_file:
        file_reader = reader(my_file)
        # do this for all the rows
        for entry in file_reader:
            csvData.append(entry)

    return csvData

def updateOutputCSV(reAppliedJobIds, outputCSV):

    updatedJobIds = []
    #attempted to apply to jobs
    for appliedJob in outputCSV:
        #look if the application failed
        if appliedJob != [] and appliedJob[5]== 'False' and appliedJob[1] in reAppliedJobIds:
            appliedJob[5] = 'True'
            updatedJobIds.append(appliedJob[1])

    new_failedApplicationList = [x for x in reAppliedJobIds if (x not in updatedJobIds)]
    # re-write to csv
    with open('res/failedApplications.txt', 'w', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        for row in new_failedApplicationList:
        # write a row to the csv file
            writer.writerow(row)


    #re-write to csv
    with open('res/output.csv', 'w', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        for row in outputCSV:
            # write a row to the csv file
            writer.writerow(row)

re_AppliedJobIDs = re_AppliedJobIDs()

if re_AppliedJobIDs:
    outputCSV = outputCSV()
    updateOutputCSV(reAppliedJobIds=re_AppliedJobIDs, outputCSV=outputCSV)


