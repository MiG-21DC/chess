import time
import csv

def judgelist(listset):
    for i in listset:
        if listset.count(i) != 1:
            return False
    return True


def process(listset):
    listrow = listset[0]
    listcol = listset[1]
    listleft = listset[2]
    listright = listset[3]
    listcounter = 7
    for element in listcol[::-1]:
        if element == 7:
            element = 0
            listcol[listcounter] = element
            listcounter = listcounter - 1
            continue
        else:
            element = element + 1
            listcol[listcounter] = element
            break
    else:
        print 'end'
        return 'end'
    for i in range(8):
        row = listrow[i]
        col = listcol[i]
        listleft[i] = row + col
        listright[i] = row - col
    newlist = [listrow, listcol, listleft, listright]
    return newlist

#
def get_point_set(listset):
    corx = listset[0]
    cory = listset[1]
    pointset = []
    for i in range(8):
        pointset.append([corx[i], cory[i]])
    return pointset

# main function
def main():
    time_start = time.time()
    filename = 'chess_result_'+str(int(time_start))+'.csv'
    print 'Calculation starts, usually it takes more than 1 minute.'
    csvfile = file(filename, 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['Number', 'Point A', 'Point B', 'Point C', 'Point D', 'Point E', 'Point F', 'Point G', 'Point H'])
    # pos = {}
    # col = 0
    point = {}
    # listrow = []
    # listcol = []
    # listleft = []
    # listright = []
    listcount = [[],[],[],[]]
    unsuccess_approarh = 0
    success_data = 0
    for row in range(8):
        point[row] = [row,0, row-0,row+0]
    for count in range(8):
        poi = point[count]
        listcount[0].append(poi[0])
        listcount[1].append(poi[1])
        listcount[2].append(poi[2])
        listcount[3].append(poi[3])

    end_flag = False
    while True:
        flag = True
        for listset in listcount:
            res = judgelist(listset)

            if res == False:
                flag = False
                break

        if flag == True:
            print '***********************'
            pointset = get_point_set(listcount)
            print pointset
            success_data = success_data + 1
            pointset.insert(0, success_data)
            writer.writerow(pointset)

            listcount = process(listcount)
        else:
            unsuccess_approarh = unsuccess_approarh + 1
            listcount = process(listcount)
        if listcount == 'end':
            break

    print 'Calculation end, success %d, failed %d' % (success_data, unsuccess_approarh)
    print 'The result is stored in %s' % filename
    time_end = time.time()
    print 'Used %f seconds' % (time_end - time_start)
    csvfile.close()


if __name__ == '__main__':
    main()






