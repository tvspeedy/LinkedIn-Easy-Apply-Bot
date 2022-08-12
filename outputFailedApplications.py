from _csv import reader

'''
Failures will typically occur when the Easy Apply answers are blank. 
Occassionally run this, get the jobIDs, and apply to the job. 
Answering those questions will lead to fewer failures
'''
def read_in_failures(filePath)-> list:

    failureJobIds = []

    with open(filePath, "r") as my_file:
        file_reader = reader(my_file)
        # do this for all the rows
        for entry in file_reader:
            # print the rows
            if len(entry) > 2 and entry[5] == 'False':
                failureJobIds.append(entry[1])

    return failureJobIds

def write_to_file(failures):
    failureJobIds =  list(dict.fromkeys(failures))
    #Don't REALLY need to sort
    failureJobIds.sort()
    f = open('res/failedApplications.txt', 'a')
    f.truncate(0)
    f.writelines("%s\n" % i for i in failureJobIds)
    f.close()

failedApplications = list(read_in_failures("res/output.csv"))

write_to_file(failedApplications)

print("Failed Applications updated")