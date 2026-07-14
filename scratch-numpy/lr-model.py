import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.01, iterations=1000, regularization=None, lambda_=0.01):
        self.lr = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        m, n = X.shape

        self.weights = np.zeros(n)
        self.bias = 0.0

        for step in range(Self.iterations):
            y_predicted = np.dot(X, self.weights) + self.bias

            error = y_predicted - y

            