import numpy as np
import cv2
import streamlit as st

def neglect_white(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Define a threshold for white pixels (adjust as needed)
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    
    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)
    
    return result

# Creating title for Streamlit app
st.title("Fabric Defect Detection with OpenCV")

# Uploading file for processing
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded image using OpenCV
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)

    # Neglect white parts in the non-defective images
    image = neglect_white(image)

    img = image.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.blur(gray, (10, 10))

    dst = cv2.fastNlMeansDenoising(blur, None, 10, 7, 21)

    _, binary = cv2.threshold(dst, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel = np.ones((5, 5), np.uint8)

    erosion = cv2.erode(binary, kernel, iterations=1)
    dilation = cv2.dilate(binary, kernel, iterations=1)

    is_defective = False  # Flag to track if fabric is defective

    if (dilation == 0).sum() > 1:
        contours, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for i in contours:
            if cv2.contourArea(i) < 261121.0:
                cv2.drawContours(img, i, -1, (0, 0, 255), 3)
                cv2.putText(img, "Defective fabric", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                is_defective = True
    else:
        cv2.putText(img, "Good fabric", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    st.image(image, caption="Original image with white parts neglected", channels="BGR")
    st.image(blur, caption="Blur")
    st.image(binary, caption="Binary")
    st.image(erosion, caption="Erosion")
    st.image(dilation, caption="Dilation")
    st.image(img, caption="Defected area", channels="BGR")

    # Display acknowledgment message to the user
    if is_defective:
        st.info("The fabric is defective.")
    else:
        st.success("The fabric is good.")
