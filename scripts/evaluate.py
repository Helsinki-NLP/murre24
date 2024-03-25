import sys
import re
import pandas as pd
import statistics as stats
from sklearn.metrics import recall_score, precision_score, f1_score

folds = ['a', 'b', 'c']
systems = ['fast', 'FB', 'Heli', 'NB', 'svm']
data = ['S24', 'S24Web', 'S24WebSKN']

precisions = {}
recalls = {}
f1_scores = {}
    
for fold in folds:
    precisions = {}
    recalls = {}
    f1_scores = {}
    
    with open(f'<truefile>') as truefile:
        y_true = [line.rstrip() for line in truefile]
        
    for system in systems:
        ensemble = []
        for instance in data:
            with open(f'{system}.{instance}_{fold}.pred') as predfile:
                y_pred = [line.rstrip() for line in predfile]
            predictions = []
            for item in y_pred:
                new_item = re.sub('\.[abc]', '', item)
                predictions.append(new_item)
            nameofsystem = f'{system}_{instance}'
            precisions[nameofsystem] = precision_score(y_true, predictions, average='macro')
            recalls[nameofsystem] = recall_score(y_true, predictions, average='macro')
            f1_scores[nameofsystem] = f1_score(y_true, predictions, average='macro')
            
            ensemble.append(predictions)
                
        votes=zip(*ensemble)
        ensemble_pred = []
        for vote in votes:
            ensemble_pred.append(stats.mode(list(vote)))
        nameofsystem = f'ensemble_{system}'
        precisions[nameofsystem] = precision_score(y_true, ensemble_pred, average='macro')
        recalls[nameofsystem] = recall_score(y_true, ensemble_pred, average='macro')
        f1_scores[nameofsystem] = f1_score(y_true, ensemble_pred, average='macro')
        
        precision_df = pd.DataFrame.from_dict(precisions, orient='index')
        recall_df = pd.DataFrame.from_dict(recalls, orient='index')
        f1_score_df = pd.DataFrame.from_dict(f1_scores, orient='index')
        
    if fold == 'a':
        precisions_all = precision_df
        recalls_all = recall_df
        f1s_all = f1_score_df
    else:
        precisions_all = precisions_all.merge(precision_df, left_index=True, right_index=True)
        recalls_all = recalls_all.merge(recall_df, left_index=True, right_index=True)
        f1s_all = f1s_all.merge(f1_score_df, left_index=True, right_index=True)

precisions_all.columns = ['a', 'b', 'c']
precisions_all['Mean'] = precisions_all.mean(axis=1)
precisions_all['SD'] = precisions_all.std(axis=1)
precisions_all.to_csv('precisions.csv', sep='\t')

recalls_all.columns = ['a', 'b', 'c']
recalls_all['Mean'] = recalls_all.mean(axis=1)
recalls_all['SD'] = recalls_all.std(axis=1)
recalls_all.to_csv('recalls.csv', sep='\t')

f1s_all.columns = ['a', 'b', 'c']
f1s_all['Mean'] = f1s_all.mean(axis=1)
f1s_all['SD'] = f1s_all.std(axis=1)
f1s_all.to_csv('f1s.csv', sep='\t')

means = pd.concat([precisions_all['Mean'], recalls_all['Mean'], f1s_all['Mean']], axis=1, keys=['Precision', 'Recall', 'F1-score'])
sds = pd.concat([precisions_all['SD'], recalls_all['SD'], f1s_all['SD']], axis=1, keys=['Precision', 'Recall', 'F1-score'])

means.to_csv('means.csv', sep='\t')
sds.to_csv('sds.csv', sep='\t')
