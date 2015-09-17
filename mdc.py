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
Since we don't need the sample number of class for normalizing'''
minimum = [0] * (len(labels) - 2)
maximum = [0] * (len(lables) - 2)

'Iterator to go through each column so we can get min/max values'
iterator = range(3, len(labels))

'Get all the values'
values = csv.reader(fin)

for labelValues in values:
	print(labelValues)
