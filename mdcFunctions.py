import math

def normalize(minimum, maximum, value):
	return ((value - minimum)/(maximum - minimum))

def dist(sampleList, testList):
	result = 0
	for x, row in enumerate(sampleList):
		result += abs((sampleList[x] - testList[x+2]) ** 2)
	result = math.sqrt(result)
	return result

def average(values, classes, iterator):
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

def output(values, count, classes, numWrong, guess, fout):
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

