# 🤖 AURAA - Artificial User Response & Automation Assistant

A powerful voice-controlled virtual assistant built in Python. **AURAA** mimics the real-world JARVIS system—listening to your voice commands and performing intelligent tasks like playing YouTube videos, searching Google, reading battery status, telling jokes, chatting via GPT, sending WhatsApp messages, and much more — all hands-free.

---

## 🚀 Features

- 🎤 Voice recognition using `speech_recognition`
- 🔊 Speak responses using `win32com.client`
- 😂 Tell random jokes via `pyjokes`
- 🧠 Respond intelligently using OpenAI GPT-3 (`text-davinci-003`)
- 🔋 Read system battery status with `psutil`
- 🎵 Play random local music from your Music folder
- 📺 Play specific videos on YouTube by voice
- 🔍 Google search through voice commands
- 📲 Send WhatsApp messages with `pywhatkit`
- 🧾 Log all commands with timestamps into `log.txt`
- 🤖 Chat memory via OpenAI for natural conversations

---

## 📦 Installation Guide

### 1. Clone the repository
git clone https://github.com/yourusername/AURAA.git
cd AURAA
2. Create and activate a virtual environment (recommended)
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate   # For Windows
3. Install required packages
Install using the provided requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
Or manually install the dependencies:

bash
Copy
Edit
pip install openai speechrecognition pyttsx3 pyjokes psutil pywhatkit
🔐 OpenAI Setup
Sign up at OpenAI

Get your API key.

Create a config.py file in the project root:

python
Copy
Edit
apikey = "your-openai-api-key-here"
🛠 Usage
Run the assistant:

bash
Copy
Edit
python main.py
Then speak clearly when prompted.

🎙 Example Voice Commands
Say This	AURAA Will
"Play Tum Hi Ho on YouTube"	Open YouTube and play the video
"Search Python OOPs concepts"	Perform a Google search
"Tell me a joke"	Respond with a random joke
"Battery status"	Read your system battery percentage
"Open calculator"	Launch the Calculator app (Windows only)
"Jarvis quit"	Exit the program

🧾 Logs & Memory
✅ All voice commands are saved in log.txt with timestamps

🧠 GPT responses saved in the /Openai/ folder for reference

🧠 Planned Enhancements
⛅ Weather updates via public APIs

📧 Email reading and sending features

👤 Face recognition-based login

🪟 GUI chatbot interface (text + voice)

📁 Project Structure
css
Copy
Edit
AURAA/
├── main.py
├── config.py
├── requirements.txt
├── log.txt
├── Openai/
│   └── [saved GPT responses]
👩‍💻 Developer
Made with 💙 by Swati Pandey
Bringing together speech recognition, automation, and artificial intelligence to create your own digital assistant.

vbnet
Copy
Edit

Let me know if you want a logo, GitHub repo description, or license (like MIT).
