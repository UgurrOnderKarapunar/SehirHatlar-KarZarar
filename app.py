import pandas as pd
import joblib
import streamlit as st

# Load the dataset to get unique passenger line values and unique days of the week
df = pd.read_excel(r"C:\Users\ugrkr\OneDrive\Masaüstü\Finals Model.xlsx")

# Load the saved LightGBM model and preprocessor
model = joblib.load("lightgbm_model.joblib")
preprocessor = joblib.load("preprocessor.joblib")

# Extract unique passenger lines from the dataset
unique_yolcu_hatti = df['yolcu_hattı'].unique().tolist()

# Extract unique days of the week from the dataset
unique_hafta_gunu = df['hafta_gunu_isim'].unique().tolist()

# Extract unique months from the dataset (assuming the column name is 'ay')
unique_ay = df['ay'].unique().tolist()

# Extract unique departure time categories from the dataset (assuming this column exists)
unique_kalkis_saat_kategori = df['kalkis_saat_kategori'].unique().tolist()

# Define the input fields for the user to enter values
def user_input_features():
    toplam_ucret = st.number_input("Toplam Ücret", min_value=210.0, step=0.01)
    yolcusayisi = st.number_input("Yolcu Sayısı", min_value=0, step=1)
    
    # Use dynamically populated options for Kalkış Saat Kategori
    kalkis_saat_kategori = st.selectbox("Kalkış Saat Kategori", unique_kalkis_saat_kategori)

    hafta_gunu_isim = st.selectbox("Hafta Günü", unique_hafta_gunu)  # Dynamically populated options
    ay = st.selectbox("Ay", unique_ay)  # Dynamically populated options for months
    yolculuksuresi_dk = st.number_input("Yolculuk Süresi (dk)", min_value=0, step=1)
    yolcu_hatti = st.selectbox("Yolcu Hattı", unique_yolcu_hatti)  # Dynamically populated options
    gun_sefer_sayisi = st.number_input("Günlük Sefer Sayısı", min_value=0, step=1)

    # Store user input as a dataframe
    data = {
        'toplamucret': [toplam_ucret],
        'yolcusayisi': [yolcusayisi],
        'kalkis_saat_kategori': [kalkis_saat_kategori],
        'hafta_gunu_isim': [hafta_gunu_isim],
        'ay': [ay],
        'yolculuksuresi(dk)': [yolculuksuresi_dk],
        'yolcu_hattı': [yolcu_hatti],
        'gun_sefer_sayisi': [gun_sefer_sayisi]
    }

    features = pd.DataFrame(data)
    return features

# Streamlit app title
st.title("Kar/Zarar Oranı Tahmini Uygulaması")

# Get user input
input_df = user_input_features()

# Display the input DataFrame for debugging
st.write("Input DataFrame:")
st.dataframe(input_df)
st.write("Input DataFrame Data Types:")
st.write(input_df.dtypes)

# Preprocess the input
try:
    input_processed = preprocessor.transform(input_df)
except Exception as e:
    st.error(f"Error during preprocessing: {str(e)}")

# Make predictions if preprocessing was successful
if 'input_processed' in locals():
    try:
        prediction = model.predict(input_processed)
        # Display the results
        st.subheader("Tahmin Edilen Kar/Zarar Oranı (%):")
        st.write(prediction[0])
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")

# To run the app, execute this command in your terminal:
# streamlit run app.py
