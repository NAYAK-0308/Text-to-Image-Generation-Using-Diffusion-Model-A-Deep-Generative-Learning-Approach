
# 🖼️ Text-to-Image Generation using Diffusion Models and CLIP

This project is a **Text-to-Image Generation web application** built using **Diffusion Models**, **CLIP**, and **Flask**.
Users can enter a text prompt, and the system generates an image that matches the description.

The application leverages **Stable Diffusion (v1.5)** from Hugging Face and runs locally on CPU or GPU (if available).

---

## 🚀 Features

* Generate images from text prompts
* Uses **Stable Diffusion v1.5**
* Integrated **CLIP** for text–image understanding
* Flask-based web interface
* Works on **CPU** (GPU optional)
* Automatic model download via Hugging Face Hub

---

## 🛠️ Tech Stack

* Python 3.9+
* Flask
* PyTorch
* Diffusers
* Hugging Face Hub
* CLIP
* Stable Diffusion

---

## 📂 Project Structure

```
Text-to-Image-Generation-using-Diffusion-Models-and-CLIP/
│
├── app.py                  # Flask application
├── clip.py                 # CLIP model logic
├── diffusion.py            # Diffusion process
├── encoder.py              # VAE Encoder
├── decoder.py              # VAE Decoder
├── model_converter.py      # Model conversion utilities
├── requirements.txt        # Dependencies
├── templates/              # HTML files
├── static/                 # CSS / generated images
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Text-to-Image-Generation-using-Diffusion-Models-and-CLIP.git
cd Text-to-Image-Generation-using-Diffusion-Models-and-CLIP
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```powershell
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Hugging Face Authentication (Important)

To avoid slow downloads and rate limits, login to Hugging Face:

```bash
huggingface-cli login
```

Paste your **HF Token** when prompted
(Create token here: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens))

---

## ▶️ Run the Application

```bash
python app.py
```

The app will start at:

```
http://127.0.0.1:5000
```

Open this URL in your browser.

---

## 🧪 Usage

1. Enter a text prompt (example: *"a cat sitting on a chair"*)
2. Click **Generate**
3. Wait (CPU generation may take 1–5 minutes)
4. Generated image will be displayed on the page

---

## ⚠️ Notes & Warnings

* **CUDA warnings** mean GPU is not available — CPU mode is used (this is normal).
* Image generation is **slow on CPU**.
* `.safetensors` warnings are safe — the model falls back to `.bin` weights.
* Flask runs in **development mode** by default (not for production).

---

## 🚀 Performance Tips (Optional)

For better CPU stability:

```python
pipe.enable_attention_slicing()
```

If you have an NVIDIA GPU:

* Install CUDA-supported PyTorch
* Set `device="cuda"`

---

## 📌 Future Improvements

* Add GPU support by default
* Improve UI/UX
* Add image download option
* Prompt history & gallery
* Deploy using Docker / Cloud

---

## 👨‍💻 Author

**Sharath Kumar Reddy**
AI / ML Enthusiast | Full Stack Developer

---

## 📜 License

This project is for **educational purposes** only.
Model rights belong to their respective owners.


