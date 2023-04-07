import pandas as pd
import numpy as np
from scipy.stats import t
chat_id = 506081330
def solution(p: float, x: np.array) -> tuple:
  n = len(x)
  alpha = 1 - p
  x_mean = np.mean(x)
  s = np.sqrt(np.var(x, ddof=1))
  b_hat = x_mean + (x_mean - 0.071) / (n - 1)
  t_alpha_2 = t.ppf(1 - alpha / 2, n - 1)
  left = b_hat - t_alpha_2 * s / np.sqrt(n - 1)
  right = b_hat + t_alpha_2 * s / np.sqrt(n - 1)
  return (left, right)

