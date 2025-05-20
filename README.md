# 🤖 Jarvis - Your Voice-Controlled Virtual Assistant

**Jarvis** is a voice-activated virtual assistant written in Python. It listens for a wake word (`"Jarvis"`) and performs various tasks such as opening websites, playing songs, answering general queries using Google's Gemini AI, and more.

---

## 🚀 Features

- 🎙️ Wake word recognition (`"Jarvis"`)
- 🗣️ Text-to-speech interaction using `pyttsx3`
- 🌐 Open popular websites (Google, YouTube, WhatsApp, etc.)
- 🎵 Play theme songs from a predefined music library
- 🧠 Answer queries using **Google Gemini**
- 📁 Open local image file
- 📅 Announces current date and time
- 📰 (Optional) News headlines feature (currently commented out)
- 💬 Gracefully exits on `"stop"`, `"quit"`, or `"exit conversation"`

---

## 🛠️ Technologies & Libraries Used

- Python 3
- `speech_recognition` – For converting speech to text
- `pyttsx3` – For text-to-speech functionality
- `webbrowser` – To open URLs in the default browser
- `os` – For local file handling
- `requests` – For API calls (optional news feature)
- `google.generativeai` – For processing AI responses using Google Gemini

---

## 🎧 How It Works

1. Jarvis listens for the wake word `"Jarvis"`.
2. Once triggered, it asks for your command.
3. Based on the command:
   - It can open websites like Google, YouTube, WhatsApp, Facebook, etc.
   - It can play specific theme songs (`got`, `friends`, `pubg`, etc.).
   - It can answer questions using Gemini AI.
   - It can open an image file.
   - It exits the chat when asked to stop.

---

## 📁 Music Library

You can trigger these using `play <songname>`:

| Song Name | Description                  |
|-----------|------------------------------|
| got       | Game of Thrones Theme        |
| friends   | Friends Theme                |
| tahm      | Two and a Half Men Theme     |
| himym     | How I Met Your Mother Theme  |
| pubg      | PUBG Background Score        |
| waka      | Waka Waka by Shakira         |

---

## ✅ Commands You Can Try

- `"open google"`
- `"open youtube"`
- `"play got"`
- `"what is a black hole?"`
- `"stop conversation"` / `"exit conversation"` / `"quit conversation"`

---

## 🔐 API Keys

- **Google Gemini API Key** – Required for AI responses
- **News API Key** – Optional (currently commented out)

---

## 📦 Setup Instructions

1. **Install dependencies:**

```bash
pip install pyttsx3 SpeechRecognition requests


Install PyAudio (required for speech_recognition):

```bash
# For Windows (use pipwin if facing issues)
pip install pipwin
pipwin install pyaudio