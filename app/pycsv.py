import csv
import copy
l_csv= []
c_csv=[]
def readCSV():
	print "\nReading the csv file ................................................................................[start]"
	global l_csv
	with open('/home/zainul/Desktop/Apriori_Combinations_and_Confidence/assets/dataset1.0.csv', 'rb') as  csvfile:
			spamreader= csv.reader(csvfile, delimiter= ' ', quotechar= '|')
			for row in spamreader:
				#c+= copy.copy([row])
				l_csv+= [row]
	formatCSV()

def formatCSV():
	global c_csv, l_csv
	c_csv= l_csv[0]
	c_csv= c_csv[0:27]
	l_csv[0]= c_csv
	#print len(l)
	print "\nFinished reading and formatting CSV..................................................................[OK]"

def dispCSV():
	for i in l_csv:
		print i
		#print len(i)
		#a= raw_input()
'''def checkker(s, tt):
	for i in range(0, len(s)):
		if(i not in tt):
			s[i]= '1'
	t= range(0,27)
	if(s[t[0]] == '1' and s[t[1]] == '1' and s[t[2]] == '1' and s[t[3]] == '1' and s[t[4]] == '1' and s[t[5]] == '1'\
	 and s[t[6]] == '1' and s[t[7]] == '1' and s[t[8]] == '1' and s[t[9]] == '1'  and s[t[10]] == '1' and s[t[11]] == '1'\
	  and s[t[12]] == '1' and s[t[13]] == '1' and s[t[14]] == '1' and s[t[15]] == '1' and s[t[16]] == '1' and s[t[17]] == '1'\
	and s[t[18]] == '1'and s[t[19]] == '1'and s[t[20]] == '1'and s[t[21]] == '1'and s[t[22]] == '1'and s[t[23]] == '1'and s[t[24]] == '1' \
	and s[t[25]] == '1'and s[t[26]] == '1'):
		return True
	else:
		return False
'''
def checkker(s, tt):
	for i in range(0, len(s)):
		if(i in tt):
			if (s[i] == '1'):
				pass
			else:
				return False
	return True

def workForUnion(t):
	t_copy = copy.copy(t)
	#t.sort()
	#print type(t), t
	global l_csv, count
	count= 0
	l= len(t_copy)
	l_csvC= copy.copy(l_csv[1:])
	for i in l_csvC:
		if(checkker(copy.copy(i),t_copy)):
			count = count +1
	return float(count)


#%matplotlib inline
if __name__ == "__main__":
	readCSV()
	#dispCSV()
	print workForUnion([9, 10, 19, 2, 6, 8])
	print workForUnion([1])
	print workForUnion([3])

#[22,21,25,13,16,14]
#[21,20,24,12,15,13]
#[21,20, 24, 12, 15, 13]
