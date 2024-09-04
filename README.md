# Model Klasifikasi Prediksi Bangkrut

### 1. Project Overview
Tujuan dari proyek ini adalah untuk membuat model klasifikasi yang dapat memprediksi apakah suatu usaha akan bangkrut berdasarkan data finansial yang diberikan. Model ini bertujuan mengurangi kerugian dari bank dengan meminimalisir pinjaman kepada usaha yang diprediksi akan bangkrut.
Deployment: [Deployment](https://huggingface.co/spaces/vincar12/bankrupt_predict)

---

### 2. Project Structure
```bash
├── deployment/                     # Berisi file untuk deployment
├── P1M2_Vincar.ipynb               # Jupyter notebook untuk analisis dan pembuatan model
├── P1M2_Vincar_Inference.ipynb     # Jupyter notebook untuk inferensi model
├── data.csv                        # Dataset asli
├── data_inf.csv                    # Dataset inferensi
├── data_inf_target.csv             # Dataset inferensi dengan target
├── model.pkl                       # Penyimpanan model
├── README.md                       # Project README file
├── README_eng.md                   # Project README file english
```

---

### 3. Workflow

1. **Data Loading & Cleaning**:
   - Data asli dimuat dari csv dan dibersihkan nama kolomnya.
   
2. **Exploratory Data Analysis (EDA)**:
   - Eksplorasi data dengan tujuan memahami dataset lebih lanjut

4. **Feature Engineering**: Feature Engineering adalah proses dengan tujuan modifikasi data agar dapat diproses oleh model
   - **Cardinality**: Cek kardinalitas atau nilai unik dari dataset, kardinalitas rendah biasanya menandakan data kategorikal alih-alih numerik
   - **Split Data**: Membagi data menjadi data inferensi, target, train, dan test.
   - **Handling Outlier**: Handling data *outlier* dengan menghitung skew dan menggunakan *Z-Score* atau *Tukey's Rule*; lalu dilakukan *capping* dengan *winsorizer*
   - **Feature Selection**: Seleksi fitur-fitur yang digunakan untuk model menggunakan basis analisis korelasi. Jika data bersifat nominal akan menggunakan analisis korelasi *chi squared*, sedangkan pada data numerik akan menggunakan analisis *spearman*.
   - **Balancing, Scaling, Dimension Reduction**: *Balancing* diperlukan agar data tidak hanya mempelajari data mayoritas namun juga minoritas. Sedangkan *scaling* berfungsi menyetarakan angka-angka dalam data agar berada dalam sat skala yang sama. Lalu reduksi dimensi atau PCA digunakan agar model menggunakan fitur yang tidak terlalu banyak untuk mengurangi kemungkinan overfitting.

5. **Model Definition**:
   - Penggunaan model dalam dataset ini dibagi menjadi 4 untuk menemukan model apa yang terbaik untuk memprediksi apakah usaha akan bangkrut. Model-model tersebut adalah: SVM, K-Nearest Neighbors, Decision Tree, Random Forest.

6. **Hyperparameter Tuning**:
   - Tuning hyperparameter bertujuan untuk meningkatkan performa model dengan melihat parameter apa yang paling baik untuk model tersebut.

7. **Model Evaluation**:
   - Evaluasi model bertujuan untuk mengetahui tingkat kesalahan dan keberhasilan model dalam memprediksi nilai target setelah dilatih dalam model training.
   - Evaluasi dilakukan dengan melihat nilai *Recall* karena ingin memperkecil kemungkinan model memprediksi sebuah usaha untuk tidak bangkrut namun kenyataannya bangkrut.

8. **Model Saving**:
   - Menyimpan model dengan pickle agar dapat digunakan pada data inference.
     
9. **Kesimpulan & Rekomendasi**:
   - Berisi kesimpulan dari proyek ini serta rekomendasi bisnis berdasarkan model yang dibuat.

10. **Inference**:
   - Dilakukan dalam notebook yang terpisah untuk mengurangi kemungkinan kebocoran data.

---

### 4. Hasil dan Kesimpulan
Dapat disimpulkan beberapa hal:
1. Berdasarkan dataset finansial usaha-usaha taiwan, dapat disimpulkan bahwa kebangkrutan suatu perusahaan dipengaruhi oleh faktor-faktor finansial.
2. Prediksi kebangkrutan suatu usaha dapat dilakukan dengan cara mempelajari data tersebut menggunakan model machine learning.
3. Setelah dilakukan pelatihan model serta tuning dan boosting untuk menemukan model dengan performa terbaik; ditemukan bahwa model SVM setelah tuning merupakan model terbaik.
4. Pemilihan model terbaik didasarkan nilai recall, karena sebagai usaha perbankan tentunya ingin memperkecil kemungkinan salah melakukan pinjaman kepada usaha yang ternyata akan bangkrut.
5. Meski nilai recall dari model sudah cukup bagus(89%), namun nilai precision model masih buruk(17%). Ini menandakan model memilliki kekuatan yang baik untuk menyaring data yang akan bangkrut. Namun masih sering memprediksi usaha akan bangkrut walaupun pada aslinya tidak.
6. Ketidakstabilan nilai tersebut dapat dikarenakan data yang kurang seimbang karena data usaha bangkrut hanyalah 3% maka model kurang optimal dalam mempelajari data.
7. Peningkatan kinerja model kedepannya dapat dilakukan dengan menambahkan data berisikan usaha-usaha yang bangkrut agar model dapat belajar lebih baik; serta lebih fokus lagi kepada metrik aset, hutang, dan uang tunai untuk lebih menguatkan prediksi kebangkrutan.

Maka rekomendasi bisnis penggunaan model sebaiknya digunakan untuk filter awal. Dimana model akan menandai usaha-usaha yang terlihat adanya tanda-tanda finansial yang konsisten dengan usaha-usaha bangkrut. Lalu dapat dilakukan penelusuran finansial lebih dalam lagi secara manual pada usaha-usaha yang ditandai oleh model. Sehingga kemungkinan pinjaman pada usaha-usaha yang akan bangkrut akan mengecil.

---

### 5. References
- Dataset: [Taiwanese Bankruptcy Prediction](https://archive.ics.uci.edu/dataset/572/taiwanese+bankruptcy+prediction)
- Tools: Python, Pandas, NumPy, Seaborn, Matplotlib, Scikit-Learn, IMB-Learn, Streamlit.
