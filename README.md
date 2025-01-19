# Kali-Linux----DesktopAssistant ( JARVIS )
This is a simple Python-based desktop assistant designed with flexibility in mind. The main goal is to make it easily customizable for individual use cases, allowing users with basic Python knowledge to modify and expand its functionality according to their specific needs .



# Desktop Assistant - Python

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A simple and **customizable desktop assistant** built using Python. It helps automate tasks such as searching Wikipedia, checking the time, opening applications, and performing system control tasks like shutdown, restart, and updates. This project provides a flexible and extensible foundation, making it easy to modify and add new commands to fit personal or professional use.

> Important: This project is primarily designed for Kali Linux users. Make sure you have the required tools installed on your system before running the assistant. Feel free to customize the code by adding new commands to suit your needs.

## Features

- **Voice Recognition**: Listen to user commands and perform actions accordingly.
- **Customizable**: Easily add, remove, or modify commands and functionality.
- **Task Automation**: Open websites, applications, perform system tasks like shutdown, restart, and update.
- **Wikipedia Search**: Get answers directly from Wikipedia using voice commands.
- **System Control**: Shutdown, restart, and update your system using voice commands.

## Requirements

This assistant requires Python 3.x and the following Python libraries:

- `pyttsx3` – Text-to-speech conversion.
- `speech_recognition` – Speech recognition for listening to commands.
- `pyautogui` – GUI automation (mouse and keyboard control).
- `wikipedia` – Wikipedia search functionality.
- `datetime` – Handling date and time.
- `subprocess` – Running system commands.

### Installation

1. **Clone this repository**:

   ```bash
   git clone https://github.com/yourusername/desktop-assistant.git
   cd desktop-assistant
