

import json
import os
import os.path
from os import path


def Average(lst):
    return sum(lst) / len(lst)

# Opening JSON file
f = open(r'H:\Thesis 400\1.Dataset_Creation\Final\results\culane\original-culane_acc.json')
mean_accuracy = json.load(f)
f = open(r'H:\Thesis 400\1.Dataset_Creation\Final\results\culane\original-culane_f1.json')
mean_f1 = json.load(f)
f = open(r'H:\Thesis 400\1.Dataset_Creation\Final\results\culane\original-culane_fn.json')
mean_fn = json.load(f)
# print(mean_fn)
f = open(r'H:\Thesis 400\1.Dataset_Creation\Final\results\culane\original-culane_prec.json')
mean_precision = json.load(f)
f = open(r'H:\Thesis 400\1.Dataset_Creation\Final\results\culane\original-culane_acc_calc.json')
mean_accuracy_calc = json.load(f)
# print(data)


acc_mean=Average(mean_accuracy)
f1_mean=Average(mean_f1)
fn=Average(mean_fn)
prec_mean=Average(mean_precision)
acc_calc_mean=Average(mean_accuracy_calc)

recall= f1_mean*prec_mean/(2*prec_mean-f1_mean)
tp=fn*recall/(1-recall)
fn_mean=fn/(tp+fn)
result= {
    'accuracy':acc_mean,
    'f1':f1_mean,
    'fn':fn_mean,
    'prec_mean':prec_mean,
    'acc_calc':acc_calc_mean
}
with open(r'H:\Thesis 400\1.Dataset_Creation\Final\results\culane\result.json', 'w') as outfile:
    outfile.write(json.dumps(result))