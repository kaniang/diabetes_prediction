# Laporan Proyek Machine Learning - Muhammad Zaki

## Domain Proyek

Penyakit Diabetes atau penyakit gula merupakan penyakit kronis yang harus diwaspadai oleh semua orang. Gejala utamanya adalah kadar gula darah yang melebihi nilai normal. Diabetes terjadi ketika tubuh tidak lagi mampu mengambil glukosa ke dalam sel dan menggunakannya sebagai energi, yang menyebabkan gula berlebihan dalam aliran darah. 

Proyek ini bertujuan untuk membangun model Machine Learning yang dapat memprediksi risiko seseorang untuk terkena diabetes dengan menggunakan data klinis dan informasi tentang faktor risiko seperti BMI, kadar gula darah, dan riwayat merokok. Model ini akan membantu mengidentifikasi individu yang berisiko tinggi untuk terkena diabetes, sehingga mereka dapat menerima perawatan atau segera diinstruksikan untuk merubah pola hidup menjadi lebih sehat.

## Business Understanding

Memahami implikasi bisnis dari proyek ini menunjukkan bahwa prediksi diabetes menggunakan machine learning tidak hanya dapat membantu pencegahan penyakit, namun juga bisa meningkatkan kesehatan masyarakat, mengurangi biaya pengobatan, dan memberikan peluang bisnis potensial di sektor kesehatan.

Bagian laporan ini mencakup:

### Problem Statements
- Pengaruh gender, riwayat kesehatan dan gaya hidup terhadap potensi terkena diabetes
- Membuat model machine learning yang bisa digunakan untuk memprediksi resiko diabetes

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Menurut kesimpulan yang didapat dari visualisasi data, pria memiliki resiko lebih besar dari wanita. Pria memiliki resiko 0.1% sedangkan wanita 0.08%.

  riwayat kesehatan seperti penyakit jantung, darah tinggi memiliki resiko 0.27% - 0.32% terkena diabetes.

  gaya hidup tidak sehat seperti merokok juga bisa meningkatkan resiko terkena diabetes, seperti mamtan perokok memiliki resiko 0.17%.

- untuk mendapat kan hasil sebaik mungkin, maka akan digunakan tiga model machine learning yaitu KNN, Random Forest dan boosting algorithm.
  dari tiga model tersebut, random forest memiliki nilai mse terkecil 

## Data Understanding

Data yang digunakan berasal dari kaggle [Diabetes prediction dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset).
Data tersebut merupakan kumpulan data medis dan demografi pasien berserta status diabetesnya(0 dan 1), data ini berisikan fitur-fitur seperti usia, jenis kelamin, indeks massa tubuh (BMI), hipertensi, penyakit jantung, riwayat merokok, kadar HbA1c, dan kadar glukosa darah.

### Variabel-variabel pada Diabetes prediction dataset adalah sebagai berikut:
- Age : umur yang ada pada dataset
- Gender : jenis kelamin yang ada pada dataset
- Body Mass Index (BMI) : sebuah pengukuran yang digunakan untuk mengevaluasi berat badan seseorang berdasarkan tinggi badan mereka
- Hypertension : pernah atau tidaknya terkana tekanan darah tinggi
- Heart Disease : pernah atau tidaknya terkena penyakit jantung
- Smoking History : riwayat merokok
- HbA1c Level : ukuran seberapa banyak glukosa yang terikat pada hemoglobin dalam sel darah merah selama sekitar 2-3 bulan terakhir. 
- Blood Glucose Level : kadar gula darah terbaru

### Exploratory Data Analysis
- jumlah dataset wanita labih banyak dari pria, namun tingkat resiko pria terkena diabetes lebih tinggi dari wanita sebanyak 0.02%.
- pernah terkena tekanan darah tinggi memiliki resiko hampir 20% lebih tinggi dari yang tidak memiliki riwayat tekanan darah tinggi
- pernah terkena penyakit jantung memiliki resiko lebih dari 25% lebih tinggi dari yang tidak memiliki riwayat penyakit jantung
- mantan perokok dan perokok memiliki resiko terkena diabetees sebesar 17% dan 10%
- HbA1c Level dan glukosa menjadi fitur yang memiliki resiko terkena diabetes yang tinggi sebesar 41%-42%

## Data Preparation
- Label Encoder
  pada kolom gender terdapat 3 katergori. katergori ketiga unknown hanya ada 18 data dan tidak sampai sebanyak 0.01% dari keseluruhah data jadi data tersebut di hapus. kemudian 2 kategori male dan female dilakukan label encoder, yaitu mengganti nilai female jadi 0 dan male jadi 1.
- oneHotEncoder
  untuk kolom yang memiliki nilai kategori yang lebih dari 2 akan dilakukan onHotencoding dengan membuat kolom baru berdasarkan setiap nilai dari kolom tersebut.
  - Split data
    melakukan pembagian data untuk proses traing dan testing sebesar 0.9 : 0.1. dari jumlah keseluruhan data 96128 dibagai menjadi 86515 untuk proses train dan 9613 untuk proses test.
- Standarisasi
    untuk data tipe numerikal dilakukan standarisasi agar model bekerja lebih optimal. metode standarisasi yang digunakan adalah standardscaler dengan cara mengubah skala fitur-fitur numerik dalam dataset sehingga memiliki mean nol dan standar deviasi satu.
## Modeling
Terdapat tiga model yang akan digunakan yaitu:
- K-Nearest Network
  
  menggunakan module dari sklearn.neighbors "KNeighborsRegressor" dan parameter "n_neighbors" = 10, setelah itu data train dimasukkan ke model untuk dipelajari
  
  Model KNN memiliki keunggulan pada kesederhanaannya namun memiliki kekurangan pada dataset yang besar dan memiliki data outlier
  
- Random Forest
  
  menggunakan module dari sklearn.ensemble "RandomForestRegressor" dan parameter "n_estimators" = 50, "max_depth" = 16, "random_state" = 55 dan "n_jobs" = -1. setelah itu data dimasukkan ke model untuk dipelajari

  Model Random Forest memiliki keunggulan pada dataset yang class-nya imbalance atau tidak seimbang dan bagus untuk model dengan banyak fitur tetapi memiliki kekurangan bisa menjadi overfitting.
  
- Boosting Algorithm
  menggunakan module dari sklearn.ensemble "AdaBoostRegressor" dan parameter "learning_rate"=0.05 dan "random_state"=55. setelah itu data dimasukkan ke model untuk dipelajari

  model AdaBoostRegressor merupakan model yang bisa mencegah overfitting tetapi memiliki kekurangan pada data yang banyak memiliki oultlier. 

### Pemilihan Model
dari ketiga model tersebut model yang memiki peforma bagus adalah Random Forest, model ini dipilih karena dataset yang imbalance. model Ramdom Forest kuat dalam menangani class imbalamce. dilihat pada matriks evaluasi model ini memiliki skor "mse" yang paling kecil dan nilai ROC-AUC yang paling besar.
  
## Evaluation

Matriks evaluasi yang digunakan untuk melihat peforma model adalah Mean Squared Error (MSE) dan Area Under the Receiver Operating Characteristic Curve (AUC-ROC).
- matriks MSE digunakan untuk melihat kesalahan model denga cara mengukur kesalahan prediksi model dalam bentuk kuadrat kemudian merata-ratakannya untuk memberikan gambaran peforma model. semakin kecil skor semakin baik
- AOC-RUC digunakakan untuk kemampuan model dalam membedakan kelas positif dan negatif dengan memploting True Positive Rate (TPR) terhadap False Positive Rate (FPR) dan menghitung area bawah kurva ROC. semakin besar skor semakin baik
- bedasarkan hasil matriks evaluasi Model Random Forest memiliki peforma terbaik dengan nilai mse train, test berturut-turut 0.000015, 0.000027 dan nilai AUC-ROC score 0.9730


**---END---**
