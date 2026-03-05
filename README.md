# 🎙️ Indian Speech-to-Speech Voice Cloning Pipeline

A **Speech-to-Speech (STS) pipeline** that converts any input voice into a **natural Indian human voice** using APIs from multiple AI voice platforms.

This project combines **Resemble AI**, **Hume AI**, and **STS AI** to create a flexible voice cloning system.

You can input **any recorded voice**, and the system converts it into an **Indian-accented AI-generated voice** using external APIs.

---

# 🚀 Features

* 🎤 Record or provide input voice
* 🔊 Convert speech to **Indian human-like voice**
* 🤖 Uses multiple AI voice APIs
* ⚡ Modular pipeline (each service has its own file)
* 🧩 Easy to extend with new voice APIs
* 📦 Lightweight Python implementation

---

# 🧠 How It Works

The pipeline follows this process:

```
Input Voice (.wav)
      │
      ▼
Speech Processing
      │
      ▼
API Call (Resemble / Hume / STS)
      │
      ▼
Indian Voice Generation
      │
      ▼
Output Voice (.wav)
```

You can choose **any supported provider** to generate the final voice.

---

# 📁 Project Structure

```
.
├── hume.py            # Hume AI voice processing
├── resemble.py        # Resemble AI voice cloning
├── sts.py             # STS AI voice conversion
├── sts_free.py        # Free STS API version
├── record_voice.py    # Records voice from microphone
├── input.wav          # Sample input voice
├── output.wav         # Generated output voice
├── requirements.txt   # Python dependencies
├── LICENSE
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/shauryachawla15/<repo-name>.git
cd <repo-name>
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Setup

You need API keys from the following platforms:

* Resemble AI
* Hume AI
* STS AI

Add your API keys inside the respective Python files:

```
resemble.py
hume.py
sts.py
```

Example:

```python
API_KEY = "your_api_key_here"
```

---

# 🎤 Recording Voice

You can record audio using:

```bash
python record_voice.py
```

This will generate:

```
input.wav
```

---

# 🔊 Running Voice Conversion

## Using Resemble AI

```bash
python resemble.py
```

---

## Using Hume AI

```bash
python hume.py
```

---

## Using STS AI

```bash
python sts.py
```

or

```bash
python sts_free.py
```

---

# 📤 Output

After running the pipeline, the generated voice will be saved as:

```
output.wav
```

---

# 🧩 Use Cases

* Indian voice cloning
* AI voice assistants
* Speech dubbing
* Voice conversion research
* AI narration systems

---

# 🔮 Future Improvements

* Web interface
* Real-time voice conversion
* Multi-language support
* Voice selection options
* Streaming speech pipeline

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Shaurya Chawla**

GitHub:
https://github.com/shauryachawla15

---

# ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 🍴 Fork the project
* 🧠 Contribute improvements

---

# ⚠️ Disclaimer

This project uses third-party APIs. Make sure to comply with the **terms of service of each provider** when using vo
