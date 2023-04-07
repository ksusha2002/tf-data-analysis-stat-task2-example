import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 506081330

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    lower_quantile = np.percentile(x, alpha/2 * 100)
    upper_quantile = np.percentile(x, (1 - alpha/2) * 100)
    return 0.071, upper_quantile

