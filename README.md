Proyek Analisis Data 
# Bike Sharing System
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
🔗Dashboard dapat dilihat dalam tautan berikut ini [Streamlit Dashboard](
```
python -m streamlit run proyek_bikeSharing.py
# or
streamlit run proyek_bikeSharing.py
```
