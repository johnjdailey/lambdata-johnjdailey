# mlfeat.py


# Assign a target for predictive modeling
target = 'High'


# Arrange data into X features matrix and y target vector
X_train = train.drop(columns=target)
y_train = train[target]
X_test = test.drop(columns=target)
y_test = test[target]
