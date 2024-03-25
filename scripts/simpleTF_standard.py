from simpletransformers.classification import ClassificationModel, ClassificationArgs
from sklearn.metrics import accuracy_score, matthews_corrcoef, f1_score
import pandas as pd
import logging
import sys

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

train_folder = sys.argv[1]
fold = sys.argv[2]

train_df = pd.read_csv(f'{train_folder}/training.txt', sep='\t', header=None)
train_df.columns = ["labels", "text"]
train_df.labels.replace([f'standard.{fold}', f'dialect.{fold}'], [0, 1], inplace=True)

# Create a ClassificationModel

model_args = ClassificationArgs(train_batch_size=4, num_train_epochs=5, learning_rate = 1e-4, output_dir=sys.argv[2])

model = ClassificationModel(
    'bert',
    '/TurkuNLP/bert-base-finnish-cased-v1/',
#    'svmall/outputs/checkpoint-386744-epoch-2/',
    num_labels=2,
    args=model_args
)

model.train_model(train_df)
