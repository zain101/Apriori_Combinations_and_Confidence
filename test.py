from  app import pycsv
import copy

def single():
    print pycsv.workForUnion([19,18])
    print pycsv.workForUnion([19])
    print pycsv.workForUnion([19])
    z = [[[19],[5]], [[19],[5]]]
    print z[0][0], pycsv.workForUnion(z[0][0])
    print z[1][0], pycsv.workForUnion(z[1][0])





def listTest(xxx):
    for i in range(0, len(xxx)):
        z = copy.copy(xxx)
        zzz = z[i][0]
        print  zzz, pycsv.workForUnion(copy.copy(zzz))





if __name__ == '__main__':
        pycsv.readCSV()
        print "performin for single element ................"
        single()
        print "performin for single element ends ................"

        print "performing for a list............................"
        a = [
            [[0], [0]],
            [[1,2,3,], [4]],
            [[5,6,7], [8,9]],
            [[19], [8,9]]
            ]
        listTest(a)
