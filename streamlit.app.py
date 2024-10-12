import streamlit as st
import pandas as pd
import joblib

# Load the dataset
def load_data():
    try:
        df = pd.read_excel(r"C:\Users\ugrkr\OneDrive\Masaüstü\Finals Model.xlsx")
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {str(e)}")
        st.stop()  # Stop execution if the dataset cannot be loaded

# Load the model and preprocessor
def load_model():
    try:
        model = joblib.load("sehirhatlarılightgbm_model.joblib")
        preprocessor = joblib.load("sehirhatlarıpreprocessor.joblib")
        return model, preprocessor
    except Exception as e:
        st.error(f"Error loading model or preprocessor: {str(e)}")
        st.stop()  # Stop execution if loading fails

# Extract unique values for user input
def get_unique_values(df):
    unique_yolcu_hatti = df['yolcu_hattı'].unique().tolist()
    unique_hafta_gunu = df['hafta_gunu_isim'].unique().tolist()
    unique_ay = df['ay'].unique().tolist()
    unique_kalkis_saat_kategori = df['kalkis_saat_kategori'].unique().tolist()
    return unique_yolcu_hatti, unique_hafta_gunu, unique_ay, unique_kalkis_saat_kategori

# Define user input features
def user_input_features(unique_yolcu_hatti, unique_hafta_gunu, unique_ay, unique_kalkis_saat_kategori):
    toplam_ucret = st.number_input("Toplam Ücret", min_value=210.0, step=0.01)
    yolcusayisi = st.number_input("Yolcu Sayısı", min_value=0, step=1)
    kalkis_saat_kategori = st.selectbox("Kalkış Saat Kategori", unique_kalkis_saat_kategori)
    hafta_gunu_isim = st.selectbox("Hafta Günü", unique_hafta_gunu)
    ay = st.selectbox("Ay", unique_ay)
    yolculuksuresi_dk = st.number_input("Yolculuk Süresi (dk)", min_value=0, step=1)
    yolcu_hatti = st.selectbox("Yolcu Hattı", unique_yolcu_hatti)
    gun_sefer_sayisi = st.number_input("Günlük Sefer Sayısı", min_value=0, step=1)

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

    return pd.DataFrame(data)

# Main app function
def main():
    # Streamlit app title
    st.title("Kar/Zarar Oranı Tahmini Uygulaması")

    # Load data and model
    df = load_data()
    model, preprocessor = load_model()

    # Extract unique values
    unique_yolcu_hatti, unique_hafta_gunu, unique_ay, unique_kalkis_saat_kategori = get_unique_values(df)

    # Get user input
    input_df = user_input_features(unique_yolcu_hatti, unique_hafta_gunu, unique_ay, unique_kalkis_saat_kategori)

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
        return

    # Make predictions if preprocessing was successful
    try:
        prediction = model.predict(input_processed)
        st.subheader("Tahmin Edilen Kar/Zarar Oranı (%):")
        st.write(prediction[0])
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")

# Run the app
if __name__ == "__main__":
    main()
