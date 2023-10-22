import cv2
import easyocr
import numpy as np

# Load the image and perform OCR
def process_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)
    if result:
        return result[0][-2]
    else:
        return "License Plate not found."

# Streamlit app
st.title("License Plate Reader")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)

    if st.button("Read License Plate"):
        license_plate = process_image(image)
        col1, col2 = st.columns(2)  # Create two columns
        with col1:
            st.markdown("<p style='font-size:36px; font-weight: bold;'>License Plate: </p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<p style='font-size:36px; font-weight: bold;'>{license_plate}</p>", unsafe_allow_html=True)
