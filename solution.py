import pandas as pd
import numpy as np
from scipy.stats import uniform

chat_id = 123456

def solution(p: float, x: np.array) -> tuple:
    # Вычисляем параметры равномерного распределения
    a = 0.071
    b = np.max(x)
    
    # Вычисляем уровень значимости alpha на основе уровня доверия p
    alpha = 1 - p
    
    # Находим квантиль порядка 1-alpha для равномерного распределения на отрезке [0,1]
    quantile = uniform.ppf(1 - alpha, loc=a, scale=b-a)
    
    # Вычисляем границы доверительного интервала для параметра b
    lower_bound = quantile
    upper_bound = b
    
    # Возвращаем границы доверительного интервала в виде кортежа
    return lower_bound, upper_bound


