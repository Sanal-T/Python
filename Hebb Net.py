import numpy as np

class HebbNet:
    def __init__(self, input_size):
        self.weights = np.zeros(input_size)

    def train(self, X, Y):
        """
        Train the network using Hebbian learning rule
        X: Input data (NxM) where N = number of samples, M = number of features
        Y: Output labels (-1 or 1)
        """
        for i in range(len(X)):  
            self.weights += X[i] * Y[i]

    def predict(self, X):
        """
        Predict output based on trained weights
        """
        return np.sign(np.dot(X, self.weights))  # Activation function: sign(w·x)

X = np.array([
    [1, 1], 
    [1, -1], 
    [-1, 1], 
    [-1, -1]
])

Y = np.array([1, -1, -1, -1])  

hebb_net = HebbNet(input_size=2)
hebb_net.train(X, Y)

test_input = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
predictions = hebb_net.predict(test_input)

print("Trained Weights:", hebb_net.weights)
print("Predictions:", predictions)