# filename = './data/iris/iris.trn'
# dataset = load_csv(filename)
# for i in range(len(dataset[0])-1):
#     str_column_to_float(dataset, i)
# print(dataset)
# # convert class column to integers
# str_column_to_int(dataset, len(dataset[0])-1)
# # evaluate algorithm
# n_folds = 5
# num_neighbors = 3
# scores = evaluate_algorithm(dataset, k_nearest_neighbors, n_folds, num_neighbors)
# print('Scores: %s' % scores)
# print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

a = [1,2,3,4]
print(a.count)