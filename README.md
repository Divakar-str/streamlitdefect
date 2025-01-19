# Fabric Defect Detection with OpenCV

## Description
This project uses OpenCV and Streamlit to detect defects in fabric images. The application allows users to upload an image of fabric, and the system will analyze it to identify defective areas. It performs image processing techniques such as grayscale conversion, blurring, denoising, binary thresholding, and morphological operations (erosion and dilation) to detect defects.

The application then marks defective regions and provides feedback to the user on whether the fabric is defective or good.

## Features
- Upload images of fabric.
- Neglect white parts of the fabric (assumed to be non-defective).
- Process images using OpenCV techniques.
- Identify defective areas using contour detection.
- Display processed images with feedback on whether the fabric is defective or good.

## Technologies Used
- **Python**: For backend logic and processing.
- **OpenCV**: For image processing techniques.
- **Streamlit**: For creating an interactive web application.
- **NumPy**: For handling arrays and matrix operations.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Divakar-str/streamlitdefect.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Live Demo
Check out the live demo at [Fabric Defect Detection](#).

## Future Enhancements
- Improve defect detection accuracy by fine-tuning parameters.
- Implement a machine learning model to detect defects automatically.
- Add support for batch image processing.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
