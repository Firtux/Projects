import pandas as pd
import numpy as np
import scipy.stats as stats

# функция поиска выбросов по методу квантилей
def quant_outlier(data):
    quant = []
    outliers = []
    for k in data.keys():
        arr = data.get(k)
        quant25 = np.quantile(arr, 0.25)
        quant75 = np.quantile(arr, 0.75)
        quant_scope = quant75 - quant25
        for d in arr:
            if d<(quant25-1.5*quant_scope) or d>(quant75+1.5*quant_scope):
                outliers.append(d)
                quant.append(k)
            else:
                continue
    if len(quant) and len(outliers) != 0:
        quant_df = print (f'По методу квантилей выбросы в таблице:\n{pd.DataFrame({"Выборки": quant, "Выбросы": outliers})}')
    else:
        quant_df = print ('По методу квантилей выбросов нет')
        
    return quant_df

def grubbs_test(data):
    def grubbs_stat(y):
        std_dev = np.std(y)
        avg_y = np.mean(y)
        abs_val_minus_avg = abs(y - avg_y)
        max_of_deviations = max(abs_val_minus_avg)
        max_ind = np.argmax(abs_val_minus_avg)
        Gcal = max_of_deviations / std_dev
        return Gcal, max_ind

    def calculate_critical_value(size, alpha):
        t_dist = stats.t.ppf(1 - alpha / (2 * size), size - 2)
        numerator = (size - 1) * np.sqrt(np.square(t_dist))
        denominator = np.sqrt(size) * np.sqrt(size - 2 + np.square(t_dist))
        critical_value = numerator / denominator
        return critical_value

    def check_G_values(Gs, Gc, inp, max_index):
        if Gs > Gc:
            return inp[max_index]
        else:
             return None

    grubbs_outliers = pd.DataFrame()
    grubbs_not_outliers = []
    grubbs_low = []
   
    for k in data.keys():
        arr = data.get(k) # перебор столбцов Series в data

        if len(arr)<7: # условие применимости теста Граббса
             grubbs_low.append(k)
        else:
            g = 1
            while g == 1: # цикл поиска выбросов с удалением выброса из выборки
                Gcritical = calculate_critical_value(len(arr), 0.05)
                Gstat, max_index = grubbs_stat(arr)
                if Gstat>Gcritical:
                    grubbs_outliers = pd.concat([grubbs_outliers, pd.DataFrame({'Выборки': [k], 'Выбросы': [arr[max_index]]})])
                    arr = arr.drop([max_index])
                else:
                    g = 0
         
    print('Результаты теста Граббса:')

    if not len(grubbs_low) == 0:
        print(f'Для следующих выборок тест неприменим (количество элементов <7): {grubbs_low}')

    if not grubbs_outliers.empty:
        print(f'Выбросы в таблице:\n{grubbs_outliers}')
    else:
        print('Выбросов нет')
    
    if not len(grubbs_not_outliers) == 0:
        print(f'В этих выборках выбросов нет: {grubbs_not_outliers}')