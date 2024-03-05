Proyek Analisis Data 
# Bike Sharing System 🚲
## Pertanyaan Bisnis?
1. Bagaimana peforma Bike Sharing System dalam beberapa tahun terakhir?
2. Musim apa yang memiliki nilai pengguna rental sepeda paling tinggi pada Bike Sharing System?
3. Apakah ada pengaruh suhu terhadap rental sepeda pada Bike Sharing System?
## Insight
1. Banyaknya peminat Bike Sharing System meningkat pada tahun 2012 dari tahun 2011. Pada kedua tahun tersebut puncak peminat memiliki pola yang sama yaitu meningkat pada pertengahan tahun.
2. Musim yang memiliki nilai pengguna rental sepeda paling tinggi yaitu pada musim gugur (fall)
3. Suhu berpengaruh dan korelasi kuat terhadap total rental sepeda
## Setup Environtment
```
# using conda
conda create --name main-ds python=3.9
conda activate main-ds
# using pip
pip install numpy pandas matplotlib seaborn jupyter streamlit babel
```
## Streamlit Dashboard
### Streamlit Cloud
🔗Dashboard dapat dilihat dalam tautan berikut ini [Streamlit Dashboard](https://nemxjzy8iqwmeteoqbr42a.streamlit.app/)
Pada Dashboard menunjukkan Perhitungan Users, Distribusi Data Total Users dan Temperatur serta Plot Regresi Temperature
![image](https://github.com/AnomBangkit/Proyek-Analisis-Data/assets/160373142/d48f9e6a-3070-453c-8e96-8af035cd042e)
### Streamlit Local
#### Menginstal library yang dibutuhkan
Untuk menginstal semua library, buka terminal/command prompt/conda prompt, navigasi pada path project folder, dan jalankan dengan kode berikut :
```
pip install -r requirements.txt
```
#### Run Streamlit
```
cd Dashboard
python -m streamlit run dashboard.py
# or
streamlit run dashboard.py
```
Terima Kasih sudah berkunjung 🌈
