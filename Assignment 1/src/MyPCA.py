import numpy as np
import sys

class MyPCA:
    def __init__(self, n_components=None, whitening=True):
        self.n_components = n_components
        self.whitening = whitening
        self.data = None

    def fit(self, X, y=None):
        if self.whitening is True:
            self.data = X
            
        
        else:
            print("False")


