# File test.py

#print(5+5)
#print(10-2)
#print(3*9)
#print(12/3)
#print(6**2)

import numpy as np

arr = np.zeros((2,5))

for i in range(arr.shape[0]):
	for j in range(arr.shape[1]):
		if (i+j) % 2 == 0:
			arr[i][j] = 1

#print(arr)

scores = [[75, 88, 92, 85, 79], [91, 83, 89, 77, 95], [82, 90, 87, 93, 88]]

highest_exam_per_student = np.argmax(scores, axis = 1)
lowest_student_per_exam = np.argmin(scores, axis = 0)
#print(highest_exam_per_student)
