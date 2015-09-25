import csv
import math #need of square root
import copy
import sys

'Define the normalize function. We can move this to wherever.'
def normalize(minimum, maximum, value):
	return ((value - minimum)/(maximum - minimum))

def dist(sampleList, testList):
	result = 0
	for x, row in enumerate(sampleList):
		result += abs((sampleList[x] - testList[x+2]) ** 2)
	result = math.sqrt(result)
	return result

def average(values, classes):
	avgList = [[0] * len(iterator) for i in classes]
	totalList = [[0] * len(iterator) for i in classes]
	countList = [0] * len(classes)

	for i, item in enumerate(values):
		for j in iterator:
			totalList[int(values[i][1])][j-2] += values[i][j]		
		countList[int(values[i][1])] += 1	

	for i, subList in enumerate(totalList):
		for j in iterator:
			avgList[i][j-2] = (totalList[i][j-2] / countList[i])
	
	return avgList

def output(values, count, classes, numWrong, guess):
	for i,name in enumerate(classes):
		print('class ' + str(i) + ' (' + name + '): ' + str(count[i]) + ' samples, ' + str(round((((count[i] - numWrong[i]) / count[i]) * 100),1)) + '% accuracy')
		fout.write('class ' + str(i) + ' (' + name + '): ' + str(count[i]) + ' samples, ' + str(round((((count[i] - numWrong[i]) / count[i]) * 100),1)) + '% accuracy\n')	

	print('overall: ' + str(len(values)) + ' samples, ' + str(round(((len(values) - sum(numWrong)) / len(values) * 100),1)) + '% accuracy')
	fout.write('overall: ' + str(len(values)) + ' samples, ' + str(round(((len(values) - sum(numWrong)) / len(values) * 100),1)) + '% accuracy\n\n')

	fout.write('Sample,Class,Predicted\n')

	for k,row in enumerate(values):
		fout.write(str(int(row[0])) + ',' + str(int(row[1])) + ',' + str(guess[k]))
		if(guess[k] != row[1]):
			fout.write(',*')
		fout.write('\n')

'Try to open input file otherwise print error and exit'
try:
	fin = open(sys.argv[1], 'r')
except:
	print(sys.argv[1] + " failed to open")
	sys.exit(1)	

'Split the input file on . so we can get the output .cv file'
argSplit = sys.argv[1].split(sep='.')
fileOutput = argSplit[0] + '.cv'

'Try to open output file otherwise print error and exit'
try:
	fout = open(fileOutput, 'w')
except:
	print(fileOutput + " failed to open")
	sys.exit(1)

'Create a csv reader to iterate through file'
reader = csv.reader(fin)

header = reader.__next__()

'An iterator that we will use to get all the classifications in the header'
iterHeader = iter(header)

'''Get the first value in the header since it is the database and
write it to the output file'''
database = next(iterHeader)
fout.write(database + '\n')

'A list to hold the different classes'
classes = list()

'Take all the classes and put the name in a string list'
for classification in iterHeader:	
	seperated = classification.split(sep='=')
	classes.append(seperated[1])

'Get the features on line 2 into a list'
features = reader.__next__()

'''This will be used as an iterator to go through all of the feature
columns (skipping the number column and class column) so we don't have
to type this out all the time'''
iterator = range(2, len(features))

'''*Should* give us a list of zeroes equal to the number of labels-2
Since we don't need the sample number or class for normalizing'''


'Iterator to go through each column so we can get min/max values'

'Get all the values'
valuesReader = csv.reader(fin)

values = list()


'Convert all the values from strings to floats'
for temp in valuesReader:
	temp = [ float(i) for i in temp]
	values.append(temp)

'A list that will get the total number of rows associated with each class'
count = [0] * len(classes)
'A list to hold the guess we make for each row'
guess = [0] * len(values)

for k, row in enumerate(values):
	
	count[int(row[1])] += 1	
	
	'test is the row that we will use for testing against the sample data'
	test = values.pop(k)
	
	'''normalTest and normalList will hold the normalized values of test
	and values respectively'''
	normalTest = copy.deepcopy(test)
	normalList = copy.deepcopy(values)
	
	'''Since we are iterating through min and max we need to initialize
	them to 0'''
	minimum = [0] * (len(iterator))
	maximum = [0] * (len(iterator))
	
	'Set the minimum and maximum arrays with the first row'
	for j in iterator:
		minimum[j - 2] = values[0][j]
		maximum[j - 2] = values[0][j]


	'''Go through the rest of the file to find the minimum and
	maximum values for each column'''
	for row in normalList:
		for i in iterator:
			if row[i] < minimum[i - 2]:
				minimum [i - 2] = row[i]
			if row[i] > maximum[i - 2]:
				maximum [i - 2] = row[i]

	'Go through the whole list again and normalize the values'	
	for i, rowValues in enumerate(normalList):
		for j in iterator:
			normalList[i][j] = normalize(minimum[j-2], maximum[j-2], rowValues[j])	
	for i in iterator:
		normalTest[i] = normalize(minimum[i-2], maximum[i-2], normalTest[i]) 

	'centroid is the a list that contains a list of features for each class'
	centroid = average(normalList, classes)
	
	'''Best will be used to compare vs the values returned
	by the dist function. If it\'s smaller then best it\'s
	the best so far.'''
	best = sys.maxsize
	
	
	for i,classCentroid in enumerate(centroid):
		result = dist(classCentroid, normalTest)	
		if(result < best):
			best = result
			bestGuess = i	
	
	guess[k] = bestGuess

	bestGuess = 0
	
	'Re-insert test back into values'
	values.insert(k,test)

'''numWrong is a list that will get the number of wrong
guesses for each class'''
numWrong = [0] * len(classes)

'Compare our guess vs the actual class'
for k, row in enumerate(values):
	if(guess[k] != row[1]):
		numWrong[int(row[1])] += 1	

output(values, count, classes, numWrong, guess)

fin.close()
fout.close()
#4) Modulize our code?
