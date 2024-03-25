from simpletransformers.classification import ClassificationModel, ClassificationArgs
from sklearn.metrics import accuracy_score
import pandas as pd
import logging
import sys
import os

modelfolder = sys.argv[1]
filefolder = sys.argv[2]

for folder in os.listdir(modelfolder):
   if folder.endswith('epoch-5'):
      outputfolder = f"{modelfolder}/{folder}"

model = ClassificationModel(
    'bert',
    outputfolder,
    num_labels=2,
) 

with open(f'{filefolder}/test.txt', 'r') as f:
    text = [line.strip() for line in f]

predictions, raw_outputs = model.predict(text)

eval_df = pd.DataFrame({'text': text, 'labels': predictions})
eval_df.labels.replace([0, 1], ['standard', 'dialect'], inplace=True)
#For dialects:
#eval_df.labels.replace([0, 1, 2, 3, 4, 5, 6, 7, 8], ['savo', 'kaakko', 'lounais', 'häme', 'epj', 'kpj', 'ppj', 'stadi', 'generic'], inplace=True)

eval_df.to_csv(sys.argv[3], sep='\t', index=False, header=False)

