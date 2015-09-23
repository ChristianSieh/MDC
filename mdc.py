import csv
import math #need of square root

'Need to change this to accept an arguemnt'
fin = open('iris.csv', 'r')
fout = open('iris.cv', 'w')

reader = csv.reader(fin)

'header is the first line in the file'
header = reader.__next__()
print('Header: ', header)

'An iterator that we will use to get all the classificationsi in the header'
iterHeader = iter(header)

'Get the first value in the header since it is the database'
database = next(iterHeader)

'A list to hold the different classification'
classNames = list()

'Take all the classes and put the name in a string list'
for classification in iterHeader:	
	seperated = classification.split(sep='=')
	classNames.append(seperated[1])

print('classNames: ', classNames)

'Get the labels into a list'
labels = reader.__next__()
print('Labels: ', labels)

'''*Should* give us a list of zeroes equal to the number of labels-2
Since we don't need the sample number or class for normalizing'''
minimum = [0] * (len(labels) - 2)
maximum = [0] * (len(labels) - 2)

'Iterator to go through each column so we can get min/max values'
iterator = range(2, len(labels))

'Get all the values'
valuesReader = csv.reader(fin)

values = list()

'Convert all the values from strings to floats'
for temp in valuesReader:
	temp = [ float(i) for i in temp]
	values.append(temp)

'''Initialize the minimum and maximum arrays with
the first row'''
for i in iterator:
	minimum[i - 2] = values[0][i]
	maximum[i - 2] = values[0][i]

'''Go through the rest of the file to find the minimum and
maximum values for each column'''
for labelValues in values:
	for i in iterator:
		if labelValues[i] < minimum[i - 2]:
			minimum [i - 2] = labelValues[i]
		if labelValues[i] > maximum[i - 2]:
			maximum [i - 2] = labelValues[i]

'Define the normalize function. We can move this to wherever.'
def normalize(minimum, maximum, value):
	return ((value - minimum)/(maximum - minimum))

def dist(dim, coordPlist, coordQlist):
        result = 0
        for x in coordPlist and y in coordQlist:
                result += (x - y) ** 2
        result = math.sqrt(result)
        return result

def average(values):
	total = 0
	avglst = []
	
	for j in iterator:
		for i,item in enumerate(values):
			total += values[i][j]			
		avglst.append(total / len(iterator))
		total = 0

	return avglst

'Go through the whole list again and normalize the values'	
for i, rowValues in enumerate(values):
	for j in iterator: #not sure but is iterator a global?
		values[i][j] = normalize(minimum[j-2], maximum[j-2], rowValues[j])	

'''print('Values: ', values)'''
print(average(values)) #awesome

fin.close()
fout.close()
#1) We need to discuss how to get the value of each class (split each class out)
#2) We need to put this in a loop
#3) is the iterator variable a global? but maybe this is OK.  Think it might be OK, yeah probably is OK
#4) Modulize our code?
