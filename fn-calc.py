

import json
import os
import os.path
from os import path



filename = 'result.json'

f = open(r'H:\Thesis 400\1.Dataset_Creation\Final\results\\'+filename)
result = json.load(f)

acc_mean = result['accuracy']
f1_mean = result['f1']
fn = result['fn']
prec_mean = result['prec_mean']

recall = f1_mean*prec_mean/(2*prec_mean-f1_mean)
tp = fn*recall/(1-recall)
fn_mean = fn/(tp+fn)
result = {
    'accuracy': acc_mean,
    'f1': f1_mean,
    'fn': fn_mean,
    'prec_mean': prec_mean,
}

print(result)
