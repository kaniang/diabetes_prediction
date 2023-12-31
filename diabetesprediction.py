# -*- coding: utf-8 -*-
"""DiabetesPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q3IFCZUI_MFpuIohVuwmWXuQ8R84YmNO
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

"""#Load Data"""

from google.colab import drive
drive.mount('/content/drive')

data = pd.read_csv('/content/drive/MyDrive/machineLearningTerapan/diabetes_prediction_dataset.csv')

data.shape

data.head()

"""# Eksploratory Data Analysis"""

data.info()

data.describe()

"""##Cleaning Data

membersihkan data dari data null, duplikat dan data pencilan

### check missing value
"""

data_null = data.isnull().sum()
print(data_null)

"""### handling duplicated"""

data_duplicated = data[data.duplicated()]
data_duplicated

data = data.drop_duplicates()

data.shape

"""### check outlier setiap kolom"""

sns.boxplot(x=data.age)

sns.boxplot(x=data.bmi)

"""data outlier pada data BMI bisa disebabkan karena banyakknya orang yang mengalami obesitas"""

sns.boxplot(x=data.HbA1c_level)

sns.boxplot(x=data.blood_glucose_level)

"""##Univariate Analysis

menganalisis data pada bagian kolom tunggal untuk mendapat insight dari data
"""

numerical_features = ['age','bmi','HbA1c_level','blood_glucose_level']
categorical_features = ['gender','hypertension','heart_disease','smoking_history']

"""###Categorical features"""

## fitur gender
feature = categorical_features[0]
count = data[feature].value_counts()
percent = 100*data[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

data = data[data['gender'] != 'Other']

## fitur gender
feature = categorical_features[0]
count = data[feature].value_counts()
percent = 100*data[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

## fitur hypertension
feature = categorical_features[1]
count = data[feature].value_counts()
percent = 100*data[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

## fitur heart disase
feature = categorical_features[2]
count = data[feature].value_counts()
percent = 100*data[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

## fitur smoking history
feature = categorical_features[3]
count = data[feature].value_counts()
percent = 100*data[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

## diabetes
feature = 'diabetes'
count = data[feature].value_counts()
percent = 100*data[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""### Numerical features"""

data[numerical_features].hist(bins=50, figsize=(20,15))
plt.show()

"""## Multivariate Analysis

melihat hubungan atau korelasi antara variabel yang ada dengan resiko terkena diabetes

### Categorical features
"""

# fungsi untuk melihat korelasi sebuah fitur terhadap target
def plot_stats(feature,label_rotation=False,horizontal_layout=True):
    temp = data[feature].value_counts()
    df1 = pd.DataFrame({feature: temp.index,'Number of contracts': temp.values})

    # Calculate the percentage of diabetes=1 per category value
    cat_perc = data[[feature, 'diabetes']].groupby([feature],as_index=False).mean()
    cat_perc.sort_values(by='diabetes', ascending=False, inplace=True)

    if(horizontal_layout):
        fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,6))
    else:
        fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(12,14))
    sns.set_color_codes("pastel")
    s = sns.barplot(ax=ax1, x = feature, y="Number of contracts",data=df1)
    if(label_rotation):
        s.set_xticklabels(s.get_xticklabels(),rotation=90)

    s = sns.barplot(ax=ax2, x = feature, y='diabetes', order=cat_perc[feature], data=cat_perc)
    if(label_rotation):
        s.set_xticklabels(s.get_xticklabels(),rotation=90)
    plt.ylabel('Percent of diabetes with value 1 [%]', fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show();

plot_stats('gender')

"""pria memiliki resiko terkena diabetes lebih tinggi dari wanita sebesar 0.02%"""

plot_stats('hypertension')

"""tekanan darah tinggi memiliki resiko terkena diabetes lebih dari 20% dari yang tidak mengalami darah tinggi"""

plot_stats('heart_disease')

"""riwayat kesehatan seperti penyakit jantung, darah tinggi memiliki resiko 0.27% - 0.32% terkena diabetes."""

plot_stats('smoking_history')

"""merokok juga bisa meningkatkan resiko terkena diabetes, seperti mamtan perokok memiliki resiko 0.17%

###Numerical features
"""

plt.figure(figsize=(10, 8))
correlation_matrix = data.corr().round(2)

# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""HbA1c_level dan blood_glucose_level memiliki korelasi yang tinggi terhadap resiko diabetes sebanyak 41% - 42%

# data preparation

mempersiapkan data untuk proses train. data kategorikal yang memiliki nilai unik lebih dari 2 akan dilakukan onHotEncoding dan data yang memiliki 2 nilai unik akan dilakuan label encoder

## Encoding Categorical Feature
"""

data.head()

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
data['Gender_encoded'] = label_encoder.fit_transform(data['gender'])

from sklearn.preprocessing import  OneHotEncoder
data = pd.concat([data, pd.get_dummies(data['smoking_history'], prefix='smoking_history')],axis=1)
data.drop(['gender','smoking_history'], axis=1, inplace=True)
data.head()

"""## Train test split

membagi data menjadi train dan test, untuk data test diambila 10% dari keseluruhan data
"""

from sklearn.model_selection import train_test_split

X = data.drop(["diabetes"],axis =1)
y = data["diabetes"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)

print(f'Total sample in whole dataset: {len(X)}')
print(f'Total sample in train dataset: {len(X_train)}')
print(f'Total sample in test dataset: {len(X_test)}')

"""## standarisasi

melakukan scaling data dengan menggunakan standar scalerm dengan tujuan untuk menghemat komputasi dan meninggkatkan peforma model
"""

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()

"""#Modelling

menggunakan 3 model machine learning, KNN Random Forest dan Boosting Algorithm

## K-Nearest Neighbor
"""

# Siapkan dataframe untuk analisis model
models = pd.DataFrame(index=['train_mse', 'test_mse'],
                      columns=['KNN', 'RandomForest', 'Boosting'])

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor(n_neighbors=10)
knn.fit(X_train, y_train)

models.loc['train_mse','knn'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)

"""## random forest"""

# Impor library yang dibutuhkan
from sklearn.ensemble import RandomForestRegressor

# buat model prediksi
RF = RandomForestRegressor(n_estimators=50, max_depth=16, random_state=55, n_jobs=-1)
RF.fit(X_train, y_train)

models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

"""## boosting algorithm"""

from sklearn.ensemble import AdaBoostRegressor

boosting = AdaBoostRegressor(learning_rate=0.05, random_state=55)
boosting.fit(X_train, y_train)
models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

"""#evaluasi model"""

# Lakukan scaling terhadap fitur numerik pada X_test sehingga memiliki rata-rata=0 dan varians=1
X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

"""## matriks evaluasi mse

menghitung peforma model menggunakan mse
"""

# Buat variabel mse yang isinya adalah dataframe nilai mse data train dan test pada masing-masing algoritma
mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])

# Buat dictionary untuk setiap algoritma yang digunakan
model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting}

# Hitung Mean Squared Error masing-masing algoritma pada data train dan test
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3

# Panggil mse
mse

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""## matriks evaluasi roc-auc

menghitung peforma model menggunakan kurfa ROC-AUC
"""

from sklearn.metrics import roc_auc_score, roc_curve

y_pred_knn = knn.predict(X_test)
roc_auc = roc_auc_score(y_test, y_pred_knn)
print(f'KNN AUC-ROC Score: {roc_auc:.4f}')

fpr, tpr, thresholds = roc_curve(y_test, y_pred_knn)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label='ROC Curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) KNN Model')
plt.legend(loc='lower right')
plt.show()

y_pred_RF = RF.predict(X_test)
roc_auc = roc_auc_score(y_test, y_pred_RF)
print(f'RF AUC-ROC Score: {roc_auc:.4f}')

fpr, tpr, thresholds = roc_curve(y_test, y_pred_RF)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label='ROC Curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Random Forest Model')
plt.legend(loc='lower right')
plt.show()

y_pred_boost = boosting.predict(X_test)
roc_auc = roc_auc_score(y_test, y_pred_boost)
print(f'Boost AUC-ROC Score: {roc_auc:.4f}')

fpr, tpr, thresholds = roc_curve(y_test, y_pred_boost)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label='ROC Curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Boosting Model')
plt.legend(loc='lower right')
plt.show()

"""## Tes prediksi"""

prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true':y_test[:1]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)

pd.DataFrame(pred_dict)