import csv

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
values = csv.reader(fin)

'rowValues1(terrible name) is the first row of data for the data set'
rowValues1 = values.__next__()

'''Initialize the minimum and maximum arrays with
the first row'''
for i in range(2, len(labels)):
	minimum[i - 2] = rowValues1[i]
	maximum[i - 2] = rowValues1[i]	

print(minimum)
print(maximum)

'''Go through the rest of the file to find the minimum and
maximum values for each column'''
for labelValues in values:
	for i in range(2, len(labels)):
		if labelValues[i] < minimum[i - 2]:
			minimum [i - 2] = labelValues[i]
		if labelValues[i] > maximum[i - 2]:
			maximum [i - 2] = labelValues[i]
		
print(minimum)
print(maximum)
