import numpy as np
import scipy.optimize as opt
"""
Correct coefficients from minimize function
Need to translate into stem
"""


def SSE(fn):
    sse = 0
    x = np.array([0.05, 0.11, 0.15, 0.31, 0.46, 0.52, 0.70, 0.74, 0.82, 0.98, 1.17])
    y = np.array([0.956, 1.09, 1.332, 0.717, 0.771, 0.539, 0.378, 0.370, 0.306, 0.242, 0.104])
    iterable = (fn(i) for i in x)
    yhat = np.fromiter(iterable, float)
    sse = np.sum((y-yhat)**2)
    return sse


def OptimizeFit(a):
        # a[0], a[1], a[2] = a  # this line is redundent
        return SSE(lambda xval: (a[0]+a[1]*np.exp(a[2]*xval)))

vals = opt.minimize(OptimizeFit, np.array([0, 0, 0]), method='Nelder-Mead')
print(vals.x)
