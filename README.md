README.md# Laporan Proyek Machine Learning - Muhammad Zaki

## Domain Proyek

Penyakit Diabetes atau penyakit gula merupakan penyakit kronis yang harus diwaspadai oleh semua orang. Gejala utamanya adalah kadar gula darah yang melebihi nilai normal. Diabetes terjadi ketika tubuh tidak lagi mampu mengambil _glukosa_ ke dalam sel dan menggunakannya sebagai energi, yang menyebabkan gula berlebihan dalam aliran darah. 

Proyek ini bertujuan untuk membangun model _Machine Learning_ yang dapat memprediksi risiko seseorang untuk terkena diabetes dengan menggunakan data klinis dan informasi tentang faktor risiko seperti BMI, kadar gula darah, dan riwayat merokok. Model ini akan membantu mengidentifikasi individu yang berisiko tinggi untuk terkena diabetes, sehingga mereka dapat menerima perawatan atau segera diinstruksikan untuk merubah pola hidup menjadi lebih sehat.

## _Business Understanding_

Memahami implikasi bisnis dari proyek ini menunjukkan bahwa prediksi diabetes menggunakan machine learning tidak hanya dapat membantu pencegahan penyakit, namun juga bisa meningkatkan kesehatan masyarakat, mengurangi biaya pengobatan, dan memberikan peluang bisnis potensial di sektor kesehatan.

### _Problem Statements_
- Pengaruh _gender_, riwayat kesehatan dan gaya hidup terhadap potensi terkena diabetes
- Membuat model _machine learning_ yang bisa digunakan untuk memprediksi resiko diabetes

### Tujuan

Menjelaskan tujuan dari pernyataan masalah:
- Dilihat dari hasil visualisasi data, pria memiliki resiko lebih besar dari wanita. Pria memiliki resiko 0.1% sedangkan wanita 0.08%.

  riwayat kesehatan seperti penyakit jantung, darah tinggi memiliki resiko 0.27% - 0.32% terkena diabetes.

  gaya hidup tidak sehat seperti merokok juga bisa meningkatkan resiko terkena diabetes, seperti mamtan perokok memiliki resiko 0.17%.

- untuk mendapat kan hasil sebaik mungkin, maka akan digunakan tiga model machine learning yaitu KNN, Random Forest dan boosting algorithm.
  dari tiga model tersebut, random forest memiliki nilai mse terkecil 

## _Data Understanding_

![data](/img/data_raw.jpg)
Data yang digunakan berasal dari kaggle [Diabetes prediction dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset).
Data tersebut merupakan kumpulan data medis dan demografi pasien berserta status diabetesnya(0 dan 1), data ini berisikan fitur-fitur seperti usia, jenis kelamin, indeks massa tubuh (BMI), hipertensi, penyakit jantung, riwayat merokok, kadar HbA1c, dan kadar glukosa darah.

### Variabel-variabel pada Diabetes prediction dataset adalah sebagai berikut:
- Age : umur yang ada pada dataset
- _Gender_ : jenis kelamin yang ada pada dataset
- _Body Mass Index_ (BMI) : sebuah pengukuran yang digunakan untuk mengevaluasi berat badan seseorang berdasarkan tinggi badan mereka
- _Hypertension_ : pernah atau tidaknya terkana tekanan darah tinggi
- _Heart Disease_ : pernah atau tidaknya terkena penyakit jantung
- _Smoking History_ : riwayat merokok
- _HbA1c Level_ : ukuran seberapa banyak glukosa yang terikat pada hemoglobin dalam sel darah merah selama sekitar 2-3 bulan terakhir. 
- _Blood Glucose Level_ : kadar gula darah terbaru

### _Exploratory Data Analysis_
Korelasi antara variabel dengan resiko terkena diabetes:
- jumlah data wanita labih banyak dari pria, namun tingkat resiko pria terkena diabetes lebih tinggi dari wanita sebanyak 0.02%.
![gender](/img/gender.png)  
- pernah terkena tekanan darah tinggi memiliki resiko hampir 20% lebih tinggi dari yang tidak memiliki riwayat tekanan darah tinggi.
![hypertension](/img/hypertension.png) 
- pernah terkena penyakit jantung memiliki resiko lebih dari 25% lebih tinggi dari yang tidak memiliki riwayat penyakit jantung.
![hearth_disease](/img/hearth_disease.png) 
- mantan perokok dan perokok memiliki resiko terkena diabetees sebesar 17% dan 10%
![smoking_history](/img/smoking_history.png)
- HbA1c Level dan glukosa menjadi fitur yang memiliki resiko terkena diabetes yang tinggi sebesar 41%-42%.
![correlation](/img/correlation.png)

## _Data Preparation_
- _missing value handling_
  tidak dilakukan karena data yang disediakan merupakan data yang telah bersih dari nilai null
- _outlier handling_
  tidak dikakukan dengan alasan memang ada kondisi demikian secara nyata
- _Label Encoder_

  pada kolom gender terdapat 3 katergori, katergori ketiga unknown hanya ada 18 data dan tidak sampai sebanyak 0.01% dari keseluruhah data jadi data tersebut di hapus. kemudian 2 kategori male dan female dilakukan label encoder, yaitu mengganti nilai female jadi 0 dan male jadi 1.
- _oneHotEncoder_
  
  untuk kolom yang memiliki nilai kategori yang lebih dari 2 akan dilakukan onHotencoding dengan membuat kolom baru berdasarkan setiap nilai dari kolom tersebut.
  - Split data
    
    melakukan pembagian data untuk proses traing dan testing sebesar 0.9 : 0.1. dari jumlah keseluruhan data 96128 dibagai menjadi 86515 untuk proses train dan 9613 untuk proses test.
- Standarisasi
  
    untuk data tipe numerikal dilakukan standarisasi agar model bekerja lebih optimal. metode standarisasi yang digunakan adalah standardscaler dengan cara mengubah skala fitur-fitur numerik dalam dataset sehingga memiliki mean nol dan standar deviasi satu.
## Modeling
Terdapat tiga model yang akan digunakan yaitu:
- K-Nearest Network
  
  Algoritma ini bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat.
  menggunakan module dari sklearn.neighbors "KNeighborsRegressor" dan parameter "n_neighbors" = 10, setelah itu data train dimasukkan ke model untuk dipelajari.
  
  Model KNN memiliki keunggulan pada kesederhanaannya namun memiliki kekurangan pada dataset yang besar dan memiliki data outlier
  
- Random Forest

  Algoritma ini bekerja dengan cara memilih sampel acak dari data kemudian membuat _decision tree_ untuk setiap sampel terpilih dan mengambil voting terbanyak dari hasil prediksi untuk menjadi prediksi terakir.
  menggunakan module dari sklearn.ensemble "RandomForestRegressor" dan parameter "n_estimators" = 50, "max_depth" = 16, "random_state" = 55 dan "n_jobs" = -1. setelah itu data dimasukkan ke model untuk dipelajari

  Model Random Forest memiliki keunggulan pada dataset yang class-nya imbalance atau tidak seimbang dan bagus untuk model dengan banyak fitur tetapi memiliki kekurangan bisa menjadi overfitting.
  
- Boosting Algorithm

  Algoritma ini bekerja dengan menggabungkan beberapa model sederhana dan dianggap lemah (weak learners) sehingga membentuk suatu model yang kuat.
  menggunakan module dari sklearn.ensemble "AdaBoostRegressor" dan parameter "learning_rate"=0.05 dan "random_state"=55. setelah itu data dimasukkan ke model untuk dipelajari

  model AdaBoostRegressor merupakan model yang bisa mencegah overfitting tetapi memiliki kekurangan pada data yang banyak memiliki oultlier. 

### Pemilihan Model
Setelah dilakukan pelatihan di tiap-tiap model _machine learning_ bisa dilihat peforma masing-masing model:
- K-Nearest Network
  
![roc_knn](/img/roc_knn.png)
- Random Forest
  
![roc_knn](/img/roc_rf.png)
- Boosting Algorithm
  
![roc_knn](/img/roc_knn.png)
- dengan perbandingan skor mse

![mse](/img/mse.png)

dari ketiga model tersebut model yang memiki peforma bagus adalah Random Forest, model ini dipilih karena dataset yang imbalance. model Ramdom Forest kuat dalam menangani class imbalamce. dilihat pada matriks evaluasi model ini memiliki skor "mse" yang paling kecil dan nilai ROC-AUC yang paling besar.
  
## Evaluation

Matriks evaluasi yang digunakan untuk melihat peforma model adalah Mean Squared Error (MSE) dan Area Under the Receiver Operating Characteristic Curve (AUC-ROC).
- matriks MSE digunakan untuk melihat kesalahan model denga cara mengukur kesalahan prediksi model dalam bentuk kuadrat kemudian merata-ratakannya untuk memberikan gambaran peforma model. semakin kecil skor semakin baik
- AOC-RUC digunakakan untuk kemampuan model dalam membedakan kelas positif dan negatif dengan memploting True Positive Rate (TPR) terhadap False Positive Rate (FPR) dan menghitung area bawah kurva ROC. semakin besar skor semakin baik
- bedasarkan hasil matriks evaluasi Model Random Forest memiliki peforma terbaik dengan nilai mse train, test berturut-turut 0.000015, 0.000027 dan nilai AUC-ROC score 0.9730


**---END---**
