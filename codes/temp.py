from sklearn.datasets import fetch_openml
import pandas as pd
import numpy as np

# mnist = fetch_openml('mnist_784')
mnist = pd.read_csv('datasets\mnist_784.csv')

# x, y = mnist["data"], mnist["target"]


x = mnist.loc[:,'pixel1':'pixel784']
y = mnist.loc[:,'class']

x.shape
# 784 here depicts the 28*28 pixels used for each image

