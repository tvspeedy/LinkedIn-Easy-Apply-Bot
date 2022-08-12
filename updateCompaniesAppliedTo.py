from csv import reader

'''
The purpose of this script is to read in all company names from res/output.csv and res/CompaniesAppliedTo.txt, removing
duplicate values, and re-writing to CompaniesAppliedTo.txt, in order to not apply to the same company more than once.
'''
def read_in_output(filePath)-> list:

    companies = []

    with open(filePath, "r") as my_file:
        file_reader = reader(my_file)
        # do this for all the rows
        for entry in file_reader:
            # print the rows
            if len(entry) == 6 and entry[5] == 'True':
                companies.append(entry[3])
            elif len(entry) == 1:
                companies.append(entry[0])

    return companies

def write_to_file(companies):
    lst =  list(dict.fromkeys(companies))
    lst.sort()
    f = open('res/CompaniesAppliedTo.txt', 'a')
    f.truncate(0)
    f.writelines("%s\n" % i for i in lst)
    f.close()



companiesAppliedTo = list(read_in_output("res/output.csv"))
companiesAppliedTo.extend(read_in_output("res/CompaniesAppliedTo.txt"))

write_to_file(companiesAppliedTo)

print("CompaniesAppliedTo updated")
