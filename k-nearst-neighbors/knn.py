from math import sqrt
from csv import reader

# train_set= [
#     [ 0.376000, 0.488000, 0],
#     [ 0.312000, 0.544000, 0],
#     [ 0.298000, 0.624000, 0],
#     [ 0.394000, 0.600000, 0],
#     [ 0.506000, 0.512000, 0],
#     [ 0.488000, 0.334000, 1],
#     [ 0.478000, 0.398000, 1],
#     [ 0.606000, 0.366000, 1],
#     [ 0.428000, 0.294000, 1],
#     [ 0.542000, 0.252000, 1],
# ]

# class_data = (row[len(data_set[0])-1] for row in data_set)
# for clss in class_data:
# 	print(clss)
#get class in dataset


# test_set = [
#     [ 0.550000, 0.364000],
#     [ 0.558000, 0.470000],
#     [ 0.456000, 0.450000],
#     [ 0.450000, 0.570000],
# ]

def load_file(file_name):
	data_set = list()
	with open(file_name,'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			data_set.append(row)
	return data_set

def str_to_float(data_set, col):
	for row in data_set:
		row[col] = float(row[col].strip())


def str_to_int(data_set, col):
    # class_values = [row[column] for row in dataset]
    # unique = set(class_values)
    # lookup = dict()
    # for i, value in enumerate(unique):
    #     lookup[value] = i
    # for row in dataset:
    #     row[column] = lookup[row[column]]
    # return lookup
    for row in data_set:
    	row[col] = int(row[col].strip())

def euclid_distance(test_row, train_row):
	distance = 0
	for i in range(len(train_row)-1):
		distance += (test_row[i] - train_row[i])**2
	return sqrt(distance)

# test_set = [
# 		[5.6, 2.9, 3.6, 1.3, 1], 
# 		[6.4, 3.2, 4.5, 1.5, 1], 
# 		[5.1, 3.8, 1.9, 0.4, 0], 
# 		[4.6, 3.2, 1.4, 0.2, 0]]
# train_set = [
# 	[7.7, 3.8, 6.7, 2.2, 2],
# 	[5.0, 3.4, 1.6, 0.4, 0], 
# 	[6.7, 3.0, 5.0, 1.7, 1], 
# 	[5.9, 3.0, 4.2, 1.5, 1],
# 	[6.6, 2.9, 4.6, 1.3, 1], 
# 	[5.1, 3.3, 1.7, 0.5, 0], 
# 	[5.7, 2.8, 4.1, 1.3, 1]
# ]
def minkowski_distance(test_row, train_row, q):
	distance = 0.0
	for i in range(len(train_row)-1):
		#print(test_row[i],' x ', train_row[i])
		distance += (test_row[i] - train_row[i])**q
	value = (distance)**(1/q)
	return value
# for row in train_set:
# 	d = minkowski_distance(test_set[0], row, 4)
# 	print(d)

def find_neighbors(train_set, test_row, num_neighbor, q):
	distances = list()
	neighbors = list()
	for train_row in train_set:
		d = minkowski_distance(test_row, train_row, q)
		distances.append((train_row,d))
	distances.sort(key = lambda tup: tup[1])
	#print(distances[0])
	for i in range(num_neighbor):
		neighbors.append(distances[i][0])
	#print(neighbors)
	return neighbors

def classify(train_set, test_row, num_neighbor,q):
	neighbors = find_neighbors(train_set, test_row, num_neighbor,q)
	#print(neighbors)
	classified_values = [neighbor[-1] for neighbor in neighbors];
	#print(classified_values)
	prediction = max(set(classified_values),key =classified_values.count)
	return prediction

#print(classify(train_set, test_set[1], 2))

def knn(train_set, test_set, num_neighbor,q):
	predictions = list()
	for test_row in test_set:
		prediction = classify(train_set, test_row, num_neighbor,q)
		predictions.append(prediction)
	return predictions

train_file_path = './data/leukemia/ALLAML.trn'
test_file_path = './data/leukemia/ALLAML.tst'
data_set = load_file(train_file_path)
test_set = load_file(test_file_path)

for i in range(len(data_set[0])-1):
	str_to_float(data_set, i)

for i in range(len(test_set[0])-1):
	str_to_float(test_set, i)


str_to_int(data_set, len(data_set[0])-1)

str_to_int(test_set, len(test_set[0])-1)


num_neighbor = 3
dim = len(data_set[0])-1
result = knn(data_set,test_set,num_neighbor,dim)
print(result)
