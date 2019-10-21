import pandas as pd
import sklearn 
import random 
import math
yo = pd.read_csv("merged_discharge_with_icds")
yo = yo[yo["CATEGORY"] == 'Discharge summary']
total_subjects = set(yo["SUBJECT_ID"].values)
random_pids = random.sample(total_subjects, len(total_subjects))
train_pids = random_pids[:math.ceil(len(total_subjects)*0.85)]
val_pids = random_pids[math.ceil(len(total_subjects)*0.85):math.ceil(len(total_subjects)*0.9)]
test_pids = random_pids[math.ceil(len(total_subjects)*0.9):]
import pdb; pdb.set_trace()
train = yo[yo["SUBJECT_ID"].isin(train_pids)]
val = yo[yo["SUBJECT_ID"].isin(val_pids)]
test = yo[yo["SUBJECT_ID"].isin(test_pids)]
train.to_csv("mimic_train.csv")
val.to_csv("mimic_val.csv")
test.to_csv("mimic_test.csv")
