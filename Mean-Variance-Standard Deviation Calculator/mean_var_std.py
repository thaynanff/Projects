import numpy as np

def calculate(list):
  try:
    arr = np.array(list)
    arr = np.reshape(arr, (3, 3))
    
    calculations = {}
  
    mean, variance, standard_deviation, max, min, sum = [], [], [], [], [], []
  
    for x in range(3):
      if x < 2:
        mean.append(np.mean(arr, axis=x).tolist())
        variance.append(np.var(arr, axis=x).tolist())
        standard_deviation.append(np.std(arr, axis=x).tolist())
        max.append(np.max(arr, axis=x).tolist())
        min.append(np.min(arr, axis=x).tolist())
        sum.append(np.sum(arr, axis=x).tolist())
  
      else:
        mean.append(np.mean(arr).tolist())
        variance.append(np.var(arr).tolist())
        standard_deviation.append(np.std(arr).tolist())
        max.append(np.max(arr).tolist())
        min.append(np.min(arr).tolist())
        sum.append(np.sum(arr).tolist())
        
      calculations['mean'] = mean
      calculations['variance'] = variance
      calculations['standard deviation'] = standard_deviation
      calculations['max'] = max
      calculations['min'] = min
      calculations['sum'] = sum

    return calculations

  except:
    return "List must contain nine numbers."