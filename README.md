# 🚘 Vehicle Damage Detection System

An AI-powered web app that detects visible damage in vehicles from uploaded images.  
**Simple to use. Fast results. Built for real-world applications.**

---

## 📸 What This Project Does

Just upload a photo of a car, and this smart tool will instantly tell you whether the vehicle shows visible **damage** or not.  
The system uses a deep learning model trained on real vehicle images to make accurate predictions.

---

## 🌟 Key Highlights

- ✅ **No technical skills needed** – Just upload and get a result
- ⚙️ **AI-driven analysis** – Powered by computer vision & deep learning
- 💻 **Web interface** – Built with Streamlit for an easy, modern experience
- 🔍 **Real-world use cases** – Designed for insurance, dealerships, logistics, and more

---

## 🧠 How It Works (Simplified)

1. 📷 Upload a clear image of a vehicle
2. 🧠 The AI model scans it for signs of damage
3. 📢 The app displays whether damage is **Detected** or **Not Detected**

---

## 💼 Who Is This For?

- **Insurance companies** – Automate claim inspections
- **Vehicle manufacturers** – Detect damages in assembly lines
- **Logistics & Fleet managers** – Monitor vehicle conditions efficiently
- **Used car marketplaces** – Assess damage before listings
- **Anyone** looking to apply AI in real-world problems

---

## 🖥️ Technologies Used

| Feature           | Technology         |
|-------------------|--------------------|
| AI Model          | PyTorch (ResNet50) |
| Frontend UI       | Streamlit          |
| Image Handling    | PIL (Python Imaging Library) |
| Hyperparameter Tuning | Optuna (optional) |
| Deployment Ready  | Yes                |

---

## 🚀 Getting Started (For Developers)

To run this locally:

```bash
git clone https://github.com/satwiksahoo/vehicle-damage-detection.git
cd vehicle-damage-detection
pip install -r requirements.txt
streamlit run app.py
