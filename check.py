import csv

def generateGroups(fileName):
    resGroups = {}
    resKeys = []
    with open(fileName, 'r') as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            row = row[0]
            resKeys.append(str(row))
            resGroups[str(row)] = []
            resGroups[str(row)+'_n'] = []
    return (resGroups, resKeys)

def fillGroup(resGroups, fileName, index_b, index_e, mode):
    with open(fileName, 'r') as f:
        csvReader = csv.reader(f)
        next(csvReader, None)
        for row in csvReader:
            building = row[index_b].lower()
            email = row[index_e]
            if mode == 0:
                resGroups[building].append(email)
            else:
                resGroups[building+'_n'].append(email)

def check(resGroups, old_info, new_info, out):
    re, keys = resGroups
    fillGroup(re, new_info[0], new_info[1], new_info[2], new_info[4])
    fillGroup(re, old_info[0], old_info[1], old_info[2], old_info[4])

    old_out = old_info[3]
    new_out = new_info[3]

    for aKey in keys:
        list_old = re[str(aKey)]
        list_new = re[str(aKey)+"_n"]
        for i in range(len(list_new)):
            if str(list_new[i]) not in list_old:
                with open(new_out, 'a') as n:
                    csvWriter = csv.writer(n)
                    csvWriter.writerow([str(aKey), str(list_new[i])])

        for i in range(len(list_old)):
            if str(list_old[i]) not in list_new:
                with open(old_out, 'a') as n:
                    csvWriter = csv.writer(n)
                    csvWriter.writerow([str(aKey), str(list_old[i])])

        with open(old_out, 'a') as o:
            csvWriter = csv.writer



if __name__ == "__main__":
    re = generateGroups("resGroup.csv")
    check(re, ['old.csv', 4, 6, 'old_o.csv', 0], ['new.csv', 3, 5, 'new_o.csv', 1], re[0])

    #print(re)
