📌 OCR Streamlit Project - OCR-Based Variable Detection

🚀 Project Overview

The CCR Streamlit Project is an innovative web application that integrates an OCR (Optical Character Recognition) model with a Streamlit interface to process live camera feeds 📸. The application captures frames every 30 seconds, detects relevant variables using the OCR model 🤖, and securely stores the extracted data in XAMPP for further analysis.

🎯 Key Features

📷 Live Camera Feed Processing - Continuously captures frames from a live stream.

🔍 OCR-Based Variable Extraction - Uses a trained .h5 model to detect and extract key variables from images.

⏳ Automated Frame Capture - Captures frames at a fixed interval of 30 seconds.

🗄 Data Storage with XAMPP - Stores extracted variables efficiently for real-time or later analysis.

🖥 Streamlit UI - Provides an easy-to-use web interface for interaction and monitoring.

📂 Project Structure

CCR-Streamlit-OCR/
│── 📜 README.md              # Project documentation
│── 📂 model/                 # OCR model (.h5 file)
│── 📂 data/                  # Captured frames & extracted data
│── 📂 database/              # XAMPP database storage
│── 📜 app.py                 # Main Streamlit app script

🔧 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/himanshikawade/OCR-Streamlit-Project.git
cd CCR-Streamlit-OCR

2️⃣ Install Dependencies

Make sure you have Python 3.8+ installed. Then, install the required packages:

pip install -r requirements.txt

3️⃣ Run the Streamlit App

streamlit run app.py

🛠 Technologies Used

🐍 Python - Core programming language

🎨 Streamlit - Web-based UI for visualization

📜 OCR Model (.h5) - Deep learning model for text extraction

🗄 XAMPP (MySQL Database) - Data storage backend

🖼 OpenCV - Image processing and frame capture

📊 How It Works

1️⃣ The live camera feed captures frames every 30 seconds.2️⃣ The OCR model processes each frame and extracts relevant variables.3️⃣ Extracted data is stored in XAMPP for further analysis.4️⃣ Users can view results via the Streamlit UI in real time.

🤝 Contribution Guidelines

Want to contribute? Follow these steps:

Fork the repository 🍴

Create a new branch 📌

Make your changes and commit them ✅

Push your branch and submit a PR 🚀

📜 License

This project is open-source and available under the MIT License.

⭐ Star the repo if you like it! 🚀

Got feedback? Open an issue or contribute! 😃

