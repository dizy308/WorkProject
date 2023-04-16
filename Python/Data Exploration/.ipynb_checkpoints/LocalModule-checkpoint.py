import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def check_central_tendency(col_name, data_frame):
    _min = data_frame[col_name].min()
    _max = data_frame[col_name].max()
    _mean = data_frame[col_name].mean()
    _median = data_frame[col_name].median()
    _mode = data_frame[col_name].mode()[0]
    _range = _max - _min
    print(f'Variable: {col_name}, Min: {_min}, Max: {_max}, Mean: {round(_mean, 3)}, Median: {_median}, Mode: {_mode}, Range: {_range}')
def check_dispersion(col_name, data_frame):
    Q1 = data_frame[col_name].quantile(0.25)
    Q3 = data_frame[col_name].quantile(0.75)
    IQR = Q3 - Q1
    var = data_frame[col_name].var()
    std = data_frame[col_name].std()
    skew = data_frame[col_name].skew()
    kutosis = data_frame[col_name].kurtosis()
    print(f'Variable: {col_name}, Q1: {Q1}, Q3: {Q3}, IQR: {IQR}, Variance: {round(var, 3)}, \
    Std: {round(std,3)}, Skew: {round(skew,3)}, Kutosis: {round(kutosis, 3)}')
def visualize_numrical_variable(col_name, data_frame):
    plt.figure(figsize=(8,6))
    plt.subplot(1,2,1)
    plt.hist(data_frame[col_name])
    plt.title(f'Hist plot of {col_name}')
    plt.subplot(1,2,2)
    plt.boxplot(data_frame[col_name].dropna())
    plt.title(f'Box plot of {col_name}')
    plt.show()

def visualize_numrical_variable(col_name, data_frame):
    plt.figure(figsize=(8,6))
    plt.subplot(1,2,1)
    plt.hist(data_frame[col_name])
    plt.title(f'Hist plot of {col_name}')
    plt.subplot(1,2,2)
    plt.boxplot(data_frame[col_name].dropna())
    plt.title(f'Box plot of {col_name}')
    plt.show()
    
def analyze_category_variable(col_name,data_frame):
    count_percent = data_frame[col_name].value_counts(normalize = True)
    count_value = data_frame[col_name].value_counts()
    print(f'Count_values: {count_value}')
    print(f'Count_percent: {count_percent}')
    print('=======')
    count_value.plot.bar()
    plt.show()

    
if __name__ == '__main__':
    main()