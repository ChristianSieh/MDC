'''Functions to be used with mdc.py. 
Includes:
	normalize(minimum, maximum, value) Christian Sieh
	dist(sampleList, testList) Ben Kaiser
	average(values, classes, iterator) Ben Kaiser and Christian Sieh
	output(values, count, classes, numWrong, guess, fout) Ben Kaiser and Christian Sieh

	9/24/2015
'''
import math

def normalize(minimum, maximum, value):
	'''Normalizes values to a number between 0 and 1 unless
	values is larger/smaller then maximum/minimum'''
	return ((value - minimum)/(maximum - minimum))

def dist(sampleList, testList):
	'''Computes euclidian distance between sampleList and testList'''
	result = 0
	for x, row in enumerate(sampleList):
		result += abs((sampleList[x] - testList[x+2]) ** 2)
	result = math.sqrt(result)
	return result

def average(values, classes, iterator):
	'''Goes through columns of the range in iterator
	and averages each column together for each class
	in values'''
	avgList = [[0] * len(iterator) for i in classes]
	totalList = [[0] * len(iterator) for i in classes]
	countList = [0] * len(classes)

	'Get the sum for each column in each class'
	for i, item in enumerate(values):
		for j in iterator:
			totalList[int(values[i][1])][j-2] += values[i][j]		
		countList[int(values[i][1])] += 1	

	'Get the average for each column in each class'
	for i, subList in enumerate(totalList):
		for j in iterator:
			avgList[i][j-2] = (totalList[i][j-2] / countList[i])
	
	return avgList

def output(values, count, classes, numWrong, guess, fout):
	'''Prints out the formatted information from the input file along
	with the accuracy of our program correctly guessing the class'''

	'Gets the accuracy for each class and prints it out'
	for i,name in enumerate(classes):
		classAccuracy = str(round((((count[i] - numWrong[i]) / count[i]) * 100),1))
		print('class ' + str(i) + ' (' + name + '): ' + str(count[i]) + ' samples, ' + classAccuracy + '% accuracy')
		fout.write('class ' + str(i) + ' (' + name + '): ' + str(count[i]) + ' samples, ' + classAccuracy + '% accuracy\n')	

	'Gets the total accuracy for the whole data set and prints it out'
	overallAccuracy = str(round(((len(values) - sum(numWrong)) / len(values) * 100),1)) 
	print('overall: ' + str(len(values)) + ' samples, ' + overallAccuracy + '% accuracy')
	fout.write('overall: ' + str(len(values)) + ' samples, ' + overallAccuracy  + '% accuracy\n\n')



	'Prints out Sample,Class,Predicted and a * if our guess was wrong, for each row'
	fout.write('Sample,Class,Predicted\n')

	for k,row in enumerate(values):
		fout.write(str(int(row[0])) + ',' + str(int(row[1])) + ',' + str(guess[k]))
		if(guess[k] != row[1]):
			fout.write(',*')
		fout.write('\n')

