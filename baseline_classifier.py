# -*- coding: utf-8 -*-
"""Baseline_Classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y1v3056THWLMGe7HWv-JM0Nzbg0sZ6vE
"""

from google.colab import drive
drive.mount('/content/drive')

import os
os.chdir("/content/drive/My Drive/MLGroupProject/Dataset/")

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

"""# Not reqd

"""

os.listdir()

total_samples = 0
for file in os.listdir("/content/drive/My Drive/MLGroupProject/Dataset/ipl_stats/"):
    if file[-1:]!='v':
        continue
    df = pd.read_csv("/content/drive/My Drive/MLGroupProject/Dataset/ipl_stats/"+file)
    print(df.columns)
    print(df.shape)
    total_samples += df.shape[0]
total_samples

"""# Start"""

matches=pd.read_csv('./kaggle_data/matches.csv')

matches.columns

matches.shape

matches = matches.drop(['umpire3', 'umpire1', 'umpire2', 'city'], axis=1)

deliveries = pd.read_csv('./kaggle_data/deliveries.csv')

deliveries.shape

# deliveries.groupby('total_runs').count()['match_id'].plot(kind="bar", title="Runs scored per delivery")

matches_copy = matches.copy()

# matches = matches_copy.copy()

set(matches['team1'].to_list())

team_dict = {'Mumbai Indians':'0','Kolkata Knight Riders': '1','Royal Challengers Bangalore': '2','Deccan Chargers': '3','Chennai Super Kings': '4',
                 'Rajasthan Royals': '5','Delhi Daredevils': '6','Gujarat Lions': '7','Kings XI Punjab': '8',
                 'Sunrisers Hyderabad': '9','Rising Pune Supergiants':'10','Kochi Tuskers Kerala': '11','Pune Warriors': '12','Rising Pune Supergiant': '10','Delhi Capitals':'6'}

matches['team1'] = matches['team1'].map(team_dict)
print(matches.shape)
matches['team2'] = matches['team2'].map(team_dict)
print(matches.shape)

matches['toss_winner'] = matches['toss_winner'].map(team_dict)
print(matches.shape)

matches['winner'] = matches['winner'].map(team_dict)
print(matches.shape)

toss_decision = {'field': 0, 'bat': 1}
matches['toss_decision'] = matches['toss_decision'].map(toss_decision)
print(matches.shape)

matches.isna().sum()
matches = matches.dropna()

print(matches.shape)

matches['team1'] = pd.to_numeric(matches['team1'])
matches['team2'] = pd.to_numeric(matches['team2'])
matches['toss_winner'] = pd.to_numeric(matches['toss_winner'])
matches['toss_decision'] = pd.to_numeric(matches['toss_decision'])
matches['winner'] = pd.to_numeric(matches['winner'])

matches.shape

matches.dtypes

matches['season'] = matches['season']-2008

# matches.sample(5)

matches.loc[matches['team1'] == matches['winner'], 'label'] = 1
matches.loc[matches['team1'] != matches['winner'], 'label'] = 0

matches.shape

data = matches[['team1', 'team2','toss_winner', 'toss_decision', 'dl_applied', 'season', 'label']]

# data = data.dropna()

data.shape

X = data[['team1', 'team2','toss_winner', 'toss_decision', 'dl_applied', 'season']].to_numpy()

# matches[['id','team1', 'team2','toss_winner', 'toss_decision', 'dl_applied', 'season','winner','win_by_runs']].corr()

X.shape

y = data['label'].to_numpy()

y.shape

"""###Logistic Regression"""

from sklearn.model_selection import train_test_split

from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support
from sklearn.model_selection import GridSearchCV

kf = KFold(n_splits=5)
kf.get_n_splits(X)
acc_test = []
acc_train = [] 
precision = []
recall = []
f1score = []
for train_index, test_index in kf.split(X):
    # print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    gridlr = GridSearchCV(LogisticRegression(),{"penalty":["l1","l2"],"C":[0.1,1,10,100]})
    gridlr.fit(X_train,y_train)
    print("best LR params:",gridlr.best_params_)

    y_pred = clf.predict(X_test)
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    print(tn, fp, fn, tp)
    pr = tp / (tp+fp)
    rec = tp/ (tp+fn)
    f1 = 2*pr*rec/(pr+rec)
    
    precision.append(pr)
    recall.append(rec)
    f1score.append(f1)

    print("pr", tp / (tp+fp))
    print('rec', tp/ (tp+fn))
    acc_train.append(clf.score(X_train, y_train))
    acc_test.append(clf.score(X_test, y_test))
    # print(precision_recall_fscore_support(y_test, y_pred))
    # print(classification_report(y_test, y_pred))

sum(acc_train) / len(acc_train)

print("Logistic Regression: ")
print("Accuracy:",sum(acc_test) / len(acc_test),"Precision:",sum(precision)/len(precision),"Recall:",sum(recall)/len(recall),"F1 Score:",sum(f1score)/len(f1score))

"""### Decision Tree"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support

kf = KFold(n_splits=5)
kf.get_n_splits(X)
acc_test = []
acc_train = [] 
precision = []
recall = []
f1score = []
for train_index, test_index in kf.split(X):
    # print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    griddt = GridSearchCV(DecisionTreeClassifier(),{"criterion":["gini", "entropy"],"splitter":["best","random"],"max_depth":[1,10,100,1000]})
    griddt.fit(X_train,y_train)
    print("Best DT params:",griddt.best_params_)

    y_pred = clf.predict(X_test)
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    print(tn, fp, fn, tp)
    pr = tp / (tp+fp)
    rec = tp/ (tp+fn)
    f1 = 2*pr*rec/(pr+rec)
    
    precision.append(pr)
    recall.append(rec)
    f1score.append(f1)

    print("pr", tp / (tp+fp))
    print('rec', tp/ (tp+fn))
    acc_train.append(clf.score(X_train, y_train))
    acc_test.append(clf.score(X_test, y_test))
    # print(precision_recall_fscore_support(y_test, y_pred))
    # print(classification_report(y_test, y_pred))

sum(acc_train) / len(acc_train)

print("Decision Tree")
print("Accuracy:",sum(acc_test) / len(acc_test),"Precision:",sum(precision)/len(precision),"Recall:",sum(recall)/len(recall),"F1 Score:",sum(f1score)/len(f1score))

"""### SVM"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

from sklearn.model_selection import KFold
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support

kf = KFold(n_splits=5)
kf.get_n_splits(X)
acc_test = []
acc_train = [] 
precision = []
recall = []
f1score = []
for train_index, test_index in kf.split(X):
    # print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    clf = SVC()
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    print(tn, fp, fn, tp)
    pr = tp / (tp+fp)
    rec = tp/ (tp+fn)
    f1 = 2*pr*rec/(pr+rec)
    
    precision.append(pr)
    recall.append(rec)
    f1score.append(f1)

    print("pr", tp / (tp+fp))
    print('rec', tp/ (tp+fn))
    acc_train.append(clf.score(X_train, y_train))
    acc_test.append(clf.score(X_test, y_test))
    # print(precision_recall_fscore_support(y_test, y_pred))
    # print(classification_report(y_test, y_pred))

sum(acc_train) / len(acc_train)

print("SVM")
print("Accuracy:",sum(acc_test) / len(acc_test),"Precision:",sum(precision)/len(precision),"Recall:",sum(recall)/len(recall),"F1 Score:",sum(f1score)/len(f1score))

"""### Random Forest"""

from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support

kf = KFold(n_splits=5)
kf.get_n_splits(X)
acc_test = []
acc_train = [] 
precision = []
recall = []
f1score = []
for train_index, test_index in kf.split(X):
    # print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    
    gridrf = GridSearchCV(RandomForestClassifier(),{"n_estimators" :[1,10,20,30,40,100],"criterion":["gini", "entropy"],"max_depth":[1,2,3,4,5,10]},cv=(X_test,y_test))
    gridrf.fit(X_train,y_train)
    print("Best RF params:",gridrf.best_params_)
    # clf = RandomForestClassifier(gridrf.best_params_)
    # clf.fit(X_train, y_train)
    y_pred = gridrf.predict(X_test)

    # y_pred = clf.predict(X_test)
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    print(tn, fp, fn, tp)
    pr = tp / (tp+fp)
    rec = tp/ (tp+fn)
    f1 = 2*pr*rec/(pr+rec)
    
    precision.append(pr)
    recall.append(rec)
    f1score.append(f1)

    print("pr", tp / (tp+fp))
    print('rec', tp/ (tp+fn))
    acc_train.append(gridrf.score(X_train, y_train))
    acc_test.append(gridrf.score(X_test, y_test))
    # print(precision_recall_fscore_support(y_test, y_pred))
    # print(classification_report(y_test, y_pred))

sum(acc_train) / len(acc_train)

print("Random Forest")
print("Accuracy:",sum(acc_test) / len(acc_test),"Precision:",sum(precision)/len(precision),"Recall:",sum(recall)/len(recall),"F1 Score:",sum(f1score)/len(f1score))



"""### All Together"""

from sklearn.model_selection import train_test_split


from sklearn.utils import shuffle
X, y = shuffle(X, y, random_state=3)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
clf = LogisticRegression(random_state=0)
clf.fit(X_train, y_train)
gridlr = GridSearchCV(LogisticRegression(),{"penalty":["l1","l2"],"C":[0.1,1,10,100]})
gridlr.fit(X_train,y_train)
print("best LR params:",gridlr.best_params_)

rf = RandomForestClassifier()
rf.fit(X_train,y_train)
gridrf = GridSearchCV(RandomForestClassifier(),{"n_estimators" :[1,10,100,1000],"criterion":["gini", "entropy"],"max_depth":[1,2,3,4,5,10]})
gridrf.fit(X_train,y_train)
print("Best RF params:",gridrf.best_params_)

dt = DecisionTreeClassifier()
dt.fit(X_train,y_train)
griddt = GridSearchCV(DecisionTreeClassifier(),{"criterion":["gini", "entropy"],"splitter":["best","random"],"max_depth":[1,2,3,4,5,10]})
griddt.fit(X_train,y_train)
print("Best DT params:",griddt.best_params_)

svcpred = SVC()
svcpred.fit(X_train,y_train)
gridsvc = GridSearchCV(SVC(),{"C":[0.1,1,10,100],"kernel":["linear", "poly", "rbf", ],"gamma":["scale","auto"]})
gridsvc.fit(X_train,y_train)
print("Best SVC params:",gridsvc.best_params_)

y_pred_logreg = gridlr.predict(X_test)
y_pred_svc = gridsvc.predict(X_test)
y_pred_rf = gridrf.predict(X_test)
y_pred_dt = griddt.predict(X_test)

from sklearn.metrics import classification_report,accuracy_score

print("Logistic Regression: ")
print(classification_report(y_test, y_pred_logreg))

print("Decision Tree: ")
print(classification_report(y_test, y_pred_dt))

print("SVM: ")
print(classification_report(y_test, y_pred_svc))

print("Random Forest: ")
print(classification_report(y_test, y_pred_rf))

print("SVM accuracy: ",accuracy_score(y_test,y_pred_svc))
print("DT accuracy: ",accuracy_score(y_test,y_pred_dt))
print("RF accuracy: ",accuracy_score(y_test,y_pred_rf))
print("LR accuracy: ",accuracy_score(y_test,y_pred_logreg))

"""# Regression """

match_score = deliveries.groupby(['match_id','inning','batting_team'])['total_runs'].sum().reset_index()

matches = matches.rename(columns={"id": "match_id"})

merged_df = pd.merge(matches,match_score, on="match_id")

merged_df = merged_df[['team1', 'team2','toss_winner', 'toss_decision', 'dl_applied', 'season', 'batting_team', 'inning', 'total_runs']]

merged_df.shape

merged_df.isnull().sum()

# ['team1', 'team2','toss_winner', 'toss_decision', 'batting_team']
# ['team1', 'team2','toss_winner', 'toss_decision', 'batting_team']

team_dict = {'Mumbai Indians':'0','Kolkata Knight Riders': '1','Royal Challengers Bangalore': '2','Deccan Chargers': '3','Chennai Super Kings': '4',
                 'Rajasthan Royals': '5','Delhi Daredevils': '6','Gujarat Lions': '7','Kings XI Punjab': '8',
                 'Sunrisers Hyderabad': '9','Rising Pune Supergiants':'10','Kochi Tuskers Kerala': '11','Pune Warriors': '12','Rising Pune Supergiant': '13'}

merged_df['team1'] = merged_df['team1'].map(team_dict)
merged_df['team2'] = merged_df['team2'].map(team_dict)
merged_df['batting_team'] = merged_df['batting_team'].map(team_dict)
merged_df['toss_winner'] = merged_df['toss_winner'].map(team_dict)
# merged_df['winner'] = merged_df['winner'].map(team_dict)
toss_decision = {'field': 0, 'bat': 1}
merged_df['toss_decision'] = merged_df['toss_decision'].map(toss_decision)
merged_df['team1'] = pd.to_numeric(merged_df['team1'])
merged_df['team2'] = pd.to_numeric(merged_df['team2'])
merged_df['toss_winner'] = pd.to_numeric(merged_df['toss_winner'])
merged_df['toss_decision'] = pd.to_numeric(merged_df['toss_decision'])
merged_df['batting_team'] = pd.to_numeric(merged_df['batting_team'])

merged_df.dtypes

merged_df.head()

data = merged_df[['team1', 'team2','toss_winner', 'toss_decision', 'dl_applied', 'season', 'batting_team', 'inning', 'total_runs']]

data.shape

data = data.dropna()
data.shape

final_df.dropna()
final_df.shape

final_df.shape

final_df.columns

final_df.shape

data.shape

X_1 = data[['team1', 'team2','toss_winner', 'toss_decision', 'dl_applied', 'season', 'batting_team', 'inning']].to_numpy()

y_1 = data['total_runs'].to_numpy()

np.isnan(X_1)

y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=4)

y_train

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)

y_pred_train = reg.predict(X_train)

import matplotlib.pyplot as plt

y_pred.shape

y_test.shape

from sklearn.metrics import mean_squared_error, mean_absolute_error

plt.figure(figsize=(15,5))
plt.plot(y_pred[:50], label = "Predicted runs")
plt.plot(y_pred_2[:50], label = "Predicted runs_2")
plt.plot(y_test[:50], label = "Real runs")
plt.legend()
plt.show()

mean_absolute_error(y_pred, y_test)

mean_squared_error(y_pred, y_test)

mean_absolute_error(y_pred_train, y_train)

kf = KFold(n_splits=5)
kf.get_n_splits(X)
mae_test = []
mae_train = [] 
for train_index, test_index in kf.split(X):
    # print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    clf =  LinearRegression()
    clf.fit(X_train, y_train)
    y_pred_train = clf.predict(X_train) 
    y_pred = clf.predict(X_test)
    mae_train.append(mean_absolute_error(y_pred_train, y_train))
    mae_test.append(mean_absolute_error(y_pred, y_test))
    # print(classification_report(y_test, y_pred))

sum(mae_train) / len(mae_train)

sum(mae_test) / len(mae_test)

temp = pd.get_dummies(merged_df[['team1', 'team2','toss_winner', 'toss_decision','batting_team']])
# temp = pd.get_dummies(merged_df[['team1', 'team2','toss_winner', 'toss_decision', 'dl_applied', 'season', 'batting_team', 'inning']])

final_df = pd.concat([merged_df, temp], axis=1).drop_duplicates()

to_remove = ['batting_team',
 'team1',
 'team2',
 'toss_winner',
 'toss_decision']

final_df = final_df.drop(to_remove, axis=1)

y_2 = final_df['total_runs'].to_numpy()

final_df = final_df.drop('total_runs', axis=1)

X_2 = final_df.to_numpy()

X_1.shape, X_2.shape

y_1[:50] == y_2[:50]

X_train, X_test, y_train, y_test = train_test_split(X_1, y_1, test_size=0.20, random_state=4)

X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X_2, y_2,test_size=0.20, random_state=4)

np.array_equal(y_1,y_2)

y_test_2[:50] == y_test[:50]

clf =  LinearRegression()
clf.fit(X_train, y_train)

clf_1 =  LinearRegression()
clf_1.fit(X_train_2, y_train_2)

y_pred = clf.predict(X_test)

y_pred_2 = clf_1.predict(X_test_2)

plt.figure(figsize=(15,5))
plt.plot(y_pred[:50], label = "Predicted runs(Label Encoding)")
plt.plot(y_pred_2[:50], label = "Predicted runs (One-hot Encoding)")
plt.plot(y_test[:50], label = "Real runs")
plt.legend()
plt.show()

mean_absolute_error(y_pred, y_test)

from sklearn.utils import shuffle
X, y = shuffle(X, y, random_state=3)

kf = KFold(n_splits=6)
kf.get_n_splits(X)
mae_test = []
mae_train = [] 
for train_index, test_index in kf.split(X):
    # print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    clf =  LinearRegression()
    clf.fit(X_train, y_train)
    y_pred_train = clf.predict(X_train) 
    y_pred = clf.predict(X_test)
    mae_train.append(mean_absolute_error(y_pred_train, y_train))
    mae_test.append(mean_absolute_error(y_pred, y_test))
    print(mean_absolute_error(y_pred, y_test))
    # print(classification_report(y_test, y_pred))

sum(mae_train) / len(mae_train)

sum(mae_test) / len(mae_test)
