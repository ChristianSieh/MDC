import csv
import math #need of square root

'Need to change this to accept an arguemnt'
fin = open('iris.csv', 'r')

reader = csv.reader(fin)

'header is the first line in the file'
header = reader.__next__()
print(header)

'An iterator that we will use to get all the classificationsi in the header'
iterHeader = iter(header)

'Get the first value in the header since it is the database'
database = next(iterHeader)

'''Take all the classes and put them in a dictionary
Could just use a string array but was learning how dictionaries
work in Python'''
for classification in iterHeader:	
	print(classification)
	seperated = classification.split(sep='=')
	print(seperated)
	print(seperated[0])
	print(seperated[1])
	'''Take the "key" and "value" for each classification and
	turn it into a tuple. This way we can add it to dictionary'''        
	classificationTuple = tuple(seperated)

	'''Might be a better way of doing this but it initializes an
	empty dictionary and then we update it with classificationTuple'''
	myDictionary = {}
	myDictionary.update({classificationTuple})

for x in myDictionary:
	print(x)
	print(myDictionary[x])	

'Get the labels into a list'
labels = reader.__next__()
print(labels)

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

'Go through the whole list again and normalize the values'	
for i, rowValues in enumerate(values):
	for j in iterator:
		values[i][j] = normalize(minimum[j-2], maximum[j-2], rowValues[j])	

'print(values)'
