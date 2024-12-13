import streamlit as st
from inference.predict import predict

st.title("BCCD Object Detection Web App")
st.write("Upload an image of blood cells to detect RBC, WBC, and Platelets.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image, predictions = predict(uploaded_file)
    st.image(image, caption="Detected Objects", use_column_width=True)
    st.write("Detection Results:")
    st.write(predictions)
