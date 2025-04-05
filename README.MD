Universal Language Translator
This is a Universal Language Translator built using the Google Translate API. It can automatically detect languages and translate text between multiple languages. It offers a user-friendly command-line interface with customizable styles for Termux or Linux environments.

🌟 Features
Automatic Language Detection: Automatically detects the source language.

Multiple Languages Supported: Translate between various languages (e.g., English, Spanish, French, German, etc.).

Customizable UI: Choose between two UI styles:

Termux (customized colors)

Linux (default terminal style)

Loading Animation: While the translation is being processed, an animated loading screen enhances the user experience.

Developer Information: Displays developer information about the script.

🌍 Languages Supported
English (en)

Bangla (bn)

Hindi (hi)

French (fr)

Spanish (es)

Arabic (ar)

Russian (ru)

Chinese (zh)

German (de)

🛠️ Installation
1. Install Python Dependencies
Before you can run the script, you'll need to install the required Python libraries. Open your terminal/command prompt and run:

bash
Copy
pip install deep-translator colorama
2. Download the Script
You can either:

Clone the repository (if available on GitHub):

bash
Copy
git clone https://github.com/tawfique02/Translator.git
Or download the script directly and save it as language_translator.py.

🚀 How to Run the Script
Open a terminal/command prompt.

Navigate to the folder where the script is saved.

Run the script:

For Windows:

bash
Copy
python language_translator.py
For macOS/Linux:

bash
Copy
python3 language_translator.py
Follow the prompts:

Select the UI Type: Choose between Termux or Linux UI.

Select the Source Language: Choose the language you want to translate from.

Select the Target Language: Choose the language you want to translate to.

Enter the Text you want to translate.

After the translation is complete, you'll be shown the translated text.

The script will ask if you want to exit the program. If you choose n, it will return to the translator interface.

🖥️ Example Output
bash
Copy
==================================================
          Universal Language Translator
               Developer Information
==================================================
═════════════════════════════════════════════════════
═ Developer: Md Tawfique Elahey                     ║
═ Purpose: Universal language translator with Google║
═ Version: 1.3                                      ║
═ GitHub: https://github.com/tawfique02             ║
═ Email: stifen38@gmail.com                         ║
═════════════════════════════════════════════════════
=== Universal Translator with Language Selector ===

[INFO] Welcome to the Universal Translator.
You can translate text between different languages.
Please select a source language and a target language for translation.
Once you enter the text, the translation will be displayed shortly.

Select your interface:
1. Termux (customized colors)
2. Linux (default terminal style)
[?] Select UI (1 or 2): 2

Choose a language to translate from:
  1. Detect Automatically (auto)
  2. English (en)
  3. Bangla (bn)
  4. Hindi (hi)
  5. French (fr)
  6. Spanish (es)
  7. Arabic (ar)
  8. Russian (ru)
  9. Chinese (zh)
  10. German (de)
[?] Select source language: 2

Choose a language to translate from:
  1. Detect Automatically (auto)
  2. English (en)
  3. Bangla (bn)
  4. Hindi (hi)
  5. French (fr)
  6. Spanish (es)
  7. Arabic (ar)
  8. Russian (ru)
  9. Chinese (zh)
  10. German (de)
[?] Select target language: 2

[+] Enter text to translate:
> Hello, how are you?

[+] Translating...
[+] Translating.
[+] Translating..
[+] Translating...
[+] Translating...

═════════════════════════════════════════════════════
═ [+] Translated: Hello, how are you?                ║
═════════════════════════════════════════════════════

Would you like to exit the program? (y/n): 
> n

Returning to the translator...
🎨 Customization
UI Style Options
The script allows you to choose between two UI types:

Termux (customized colors): Optimized for Termux with bright and vibrant colors.

Linux (default terminal style): A cleaner, simpler style suited for Linux or general terminal use.

Color Scheme
Termux UI: Bright colors like cyan, yellow, and green are used for better visibility on mobile terminals.

Linux UI: Simpler and more traditional color scheme with blue and white text.

🛠️ Troubleshooting
Ensure Python is installed: Make sure you have Python installed by running the following command:

bash
Copy
python --version
If not installed, you can download it from python.org.

Missing libraries: If the script doesn't run due to missing libraries, ensure you have installed the required libraries by running:

bash
Copy
pip install deep-translator colorama
Error with Google Translator: If there is an issue with the translation, it might be due to network connectivity. Check your internet connection or try again later.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

📞 Contact
If you have any questions or feedback, feel free to contact the developer:

Developer: Md Tawfique Elahey

Email: stifen38@gmail.com

GitHub: https://github.com/tawfique02

🔚 Conclusion
This README.md file explains everything from installation, running the script, troubleshooting, and customizing the UI. It's a great resource for users who will want to run the Universal Language Translator script and need instructions for setup and usage.
