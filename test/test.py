from  app import *
import copy

def single():
    print workForUnion([19,18])
    print workForUnion([19])
    print workForUnion([19])
    z = [[[19],[5]], [[19],[5]]]
    print z[0][0], workForUnion(z[0][0])
    print z[1][0], workForUnion(z[1][0])





def listTest(xxx):
    for i in range(0, len(xxx)):
        z = copy.copy(xxx)
        zzz = z[i][0]
        print  zzz, workForUnion(copy.copy(zzz))





if __name__ == '__main__':
        readCSV()
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
