import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# Generate synthetic data
np.random.seed(0)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.randn(80) * 0.1

# Split the data into training and testing sets
X_train, X_test = X[:60], X[60:]
y_train, y_test = y[:60], y[60:]

degrees = [1, 4, 15]
colors = ['b', 'g', 'r']

plt.figure(figsize=(14, 5))
for i, degree in enumerate(degrees):
    ax = plt.subplot(1, len(degrees), i + 1)
    plt.setp(ax, xticks=(), yticks=())

    # Create polynomial features
    polynomial_features = PolynomialFeatures(degree=degree)
    X_poly_train = polynomial_features.fit_transform(X_train)
    X_poly_test = polynomial_features.transform(X_test)

    # Fit a polynomial regression model
    model = LinearRegression()
    model.fit(X_poly_train, y_train)

    # Predictions on training and testing data
    y_train_pred = model.predict(X_poly_train)
    y_test_pred = model.predict(X_poly_test)

    # Calculate and display the MSE
    mse_train = mean_squared_error(y_train, y_train_pred)
    mse_test = mean_squared_error(y_test, y_test_pred)

    plt.scatter(X, y, color='gray', s=20, edgecolor='k', label='Data')
    plt.plot(X_test, y_test_pred, color=colors[i], lw=2, label=f'Degree {degree} (MSE: {mse_test:.2f})')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title(f'Degree {degree} Polynomial Regression')
    plt.legend(loc='best')

plt.tight_layout()
plt.show()
