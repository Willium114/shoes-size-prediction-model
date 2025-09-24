
# 👟 Shoe Size Prediction App

This project is a **Machine Learning-based Shoe Size Prediction Web App** built using **Streamlit**.  
Users can input their **Age, Height, and Gender** to predict the most suitable shoe size.

---

## 🚀 Features

- 🧠 **Trained ML Model** – Uses a pre-trained model (`model.pkl`) and label encoder (`label_encoder.pkl`).
- 🖥 **Interactive UI** – Built with Streamlit for a clean, fast, and responsive web interface.
- ⚡ **Real-time Predictions** – Get predictions instantly after entering values.
- 🗂 **Easy Deployment** – Can be hosted on Streamlit Cloud, Heroku, or any cloud platform.

---

## 🛠 Installation & Setup

Follow these steps to run the app locally:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Willium114/Shoe_Size-Prediction.git

# 2️⃣ Navigate to project folder
cd Shoe_Size-Prediction/app

# 3️⃣ Create a virtual environment (recommended)
python -m venv venv

# 4️⃣ Activate the virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 5️⃣ Install dependencies
pip install -r requirements.txt

# 6️⃣ Run the Streamlit app
streamlit run app.py
````

---

## 📂 Project Structure

```
Shoe_Size-Prediction/
│
├── app/
│   ├── app.py              # Main Streamlit app
│   ├── model.pkl           # Trained ML model
│   └── label_encoder.pkl   # Label encoder for gender
│
├── assets/                 # (Optional) Any extra files, dataset, images
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

---

## 🧑‍💻 How It Works

1. **Input:** User enters `Age`, `Height (cm)`, and selects `Gender`.
2. **Processing:** The app uses the ML model (`model.pkl`) to predict the shoe size.
3. **Output:** Displays the predicted shoe size instantly on the page.

---


## 📌 Requirements

* Python 3.8+
* Streamlit
* Pandas
* Scikit-learn
* Numpy

(Already included in `requirements.txt`)

---

## 🤝 Contributing

Pull requests are welcome!
If you find any issue or want to improve the app, feel free to open an issue or submit a PR.

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify it.

````

---

### ✅ Next Steps:
1. Isko `README.md` naam se save karo project ke root folder me.  
2. Phir GitHub pe push karne ke liye commands:
```bash
git add README.md
git commit -m "Added professional README file"
git push
````

---

