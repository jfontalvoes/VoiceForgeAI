# 🗣️ VoiceForgeAI

**VoiceForgeAI** is a simple Streamlit-based application that converts user-inputted text into speech using OpenAI's Text-to-Speech API. Users can choose from multiple AI-generated voices and instantly listen to their synthesized audio.

> ⚠️ **Important:** This application requires a valid, paid OpenAI API key to function. Without it, the app will not work.

## 🚀 Features

- 🎙️ Convert custom text into lifelike speech
- 🧠 Powered by OpenAI's `tts-1` model
- 🗣️ Choose from 6 high-quality voices: `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`
- 🌐 Streamlit web interface for instant feedback and playback

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jfontalvoes/VoiceForgeAI.git
   cd VoiceForgeAI
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🔐 OpenAI API Key

This app uses the OpenAI Text-to-Speech API, which **requires a paid account and an API key**.

### Setup:

1. Create a file named `.env` in the root directory.
2. Copy the content from `env.example`:
   ```bash
   cp env.example .env
   ```
3. Open `.env` and replace the placeholder with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## ▶️ Usage

1. Run the app with Streamlit:
   ```bash
   streamlit run app.py
   ```

2. In the browser interface:
   - Enter the text you want to convert.
   - Choose one of the available voices.
   - Click **Generate Speech**.
   - The generated audio will play directly in the browser.

## 📁 Project Structure

```
VoiceForgeAI/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env.example         # Template for OpenAI API key
├── .env                 # Actual API key file (not included in version control)
└── README.md            # Project documentation
```

## 🧪 Example

```text
Input: "Hello! This is an example of voice synthesis using AI."
Voice: nova
Output: A realistic MP3 audio clip streamed back in the browser.
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ✨ Author 

Developed by Jonathan Estiven Fontalvo Aparicio 📧

Feel free to copy this into your repo. If you'd like to contribute or help, just let me know!
