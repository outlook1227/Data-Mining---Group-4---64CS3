# Import the library and sckit-learn
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 14
import seaborn as sns
import pandas as pd
from imblearn.over_sampling import SMOTE, RandomOverSampler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics

bank_dataset = pd.read_csv("Data Mining Project - 64CS2/bank-additional-full.csv", sep = ';')
bank_dataset

def model_eval(model, x_train, y_train, x_test, y_test, colors):
  from sklearn.metrics import accuracy_score, roc_curve, confusion_matrix, roc_auc_score, recall_score, precision_score, classification_report

  model.fit(x_train, y_train.values.ravel())
  y_prediction = model.predict(x_test)
  y_score = model.predict_proba(x_test)[:,1]

  # Print accuracy, AUC and Recall Score
  print("Overall Test Accuracy:", accuracy_score(y_test, y_prediction))
  print("Test AUC Score:", roc_auc_score(y_test, y_score))
  print("Overall Test Recall:", recall_score(y_test, y_prediction))

  # Classification report for the dataset
  print("_" * 60)
  print('Classification Report of Test:\n', classification_report(y_test, y_prediction))

  cm = confusion_matrix(y_test, y_prediction)
  df_cm = pd.DataFrame(cm, range(2),
                    range(2))

  plt.figure(figsize = (15.5, 7))
  plt.subplot(1, 2, 1)
  cm_plot = sns.heatmap(df_cm, annot=True, fmt='n', annot_kws={"size": 14.35},
                        xticklabels = ['no', 'yes'], 
                        yticklabels = ['no', 'yes'], cmap = "Blues")
  plt.xlabel("Predicted Label")
  plt.ylabel("True Label")
  plt.title("Confusion Matrix", fontsize = 14.5)

  false_positive_rate, true_positive_rate, threshold = roc_curve(y_test, y_score)
  plt.subplot(1, 2, 2)
  plt.plot([0, 1], [0, 1], color="navy", lw = 1.5, linestyle = "--")

  plt.xlim([0.0, 1.0])
  plt.ylim([0.0, 1.05])
  plt.plot(false_positive_rate, true_positive_rate, linewidth = 2.5, 
          label="ROC curve (area = %0.2f)" % roc_auc_score(y_test, y_score), color = colors)
  plt.title("ROC Curve", fontsize = 14.5)
  plt.xlabel("False Positive Rate - FPR")
  plt.ylabel("True Positive Rate - TPR")
  plt.grid()
  plt.legend()
  plt.show()
