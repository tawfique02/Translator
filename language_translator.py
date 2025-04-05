#This script help the users to translate language by using google.
from deep_translator import GoogleTranslator
from colorama import Fore, Back, Style, init
import time
import sys

# Initialize colorama
init(autoreset=True)

# Developer Info
DEVELOPER_INFO = """
Developer: Md Tawfique Elahey
Purpose: Universal language translator using Google
Version: 1.3
GitHub: https://github.com/tawfique02
Email: stifen38@gmail.com
"""

# Common languages for selection
LANGUAGES = {
    "1": ("auto", "Detect Automatically"),
    "2": ("en", "English"),
    "3": ("bn", "Bangla"),
    "4": ("hi", "Hindi"),
    "5": ("fr", "French"),
    "6": ("es", "Spanish"),
    "7": ("ar", "Arabic"),
    "8": ("ru", "Russian"),
    "9": ("zh", "Chinese"),
    "10": ("de", "German")
}

def show_language_menu():
    """Displays available languages with descriptions."""
    print(Fore.CYAN + "\nChoose a language to translate from:")
    for key, (code, name) in LANGUAGES.items():
        print(Fore.YELLOW + f"  {key}. {name} ({code})")

def get_language(prompt):
    """Prompt user to select a language and handle invalid input."""
    while True:
        show_language_menu()
        choice = input(Fore.GREEN + prompt).strip()
        if choice in LANGUAGES:
            return LANGUAGES[choice][0]
        else:
            print(Fore.RED + "[!] Invalid choice. Please try again.")

def translate_text(text, source='auto', target='en'):
    """Performs translation and handles errors."""
    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        return translated
    except Exception as e:
        return Fore.RED + f"[!] Translation failed: {e}"

def loading_animation():
    """Shows a simple loading animation to enhance user experience."""
    loading = [".", "..", "..."]
    for _ in range(5):
        for dots in loading:
            sys.stdout.write(Fore.YELLOW + f"\r[+] Translating{dots}")
            sys.stdout.flush()
            time.sleep(0.5)

def print_boxed_text(text, color=Fore.MAGENTA, border_char='*'):
    """Prints text inside a box with a customizable color and border character."""
    width = len(text) + 6  # Added space for better visual padding
    print(color + border_char * width)
    print(color + f"{border_char}  {text}  {border_char}")
    print(color + border_char * width)

def display_developer_info():
    """Displays a more stylish developer information box."""
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "          Universal Language Translator")
    print(Fore.YELLOW + "               Developer Information")
    print(Fore.CYAN + "=" * 50)
    print_boxed_text(DEVELOPER_INFO, color=Fore.GREEN, border_char='═')

def ask_exit_option():
    """Asks if the user wants to exit the program and provides guidance."""
    print(Fore.CYAN + "\nWould you like to exit the program? (y/n): ")
    choice = input(Fore.YELLOW + "> ").strip().lower()
    if choice == 'y':
        print(Fore.RED + "Exiting the program. Goodbye!\n")
        farewell_message()
        sys.exit()
    elif choice == 'n':
        print(Fore.GREEN + "Returning to the translator...\n")
    else:
        print(Fore.RED + "[!] Invalid choice. Please type 'y' to exit or 'n' to continue.")

def farewell_message():
    """Displays a brief farewell message when the user exits the program."""
    print(Fore.CYAN + "\nThanks for using the Universal Translator!")
    print(Fore.GREEN + "See you next time. Goodbye!")

def select_ui():
    """Allow user to select UI type (Termux or Linux) and provides clear instructions."""
    print(Fore.CYAN + "\nSelect your interface:")
    print(Fore.YELLOW + "1. Termux (customized colors)")
    print(Fore.GREEN + "2. Linux (default terminal style)")

    choice = input(Fore.GREEN + "[?] Select UI (1 or 2): ").strip()
    if choice == '1':
        # Customize for Termux UI
        return "termux"
    elif choice == '2':
        # Default Linux UI
        return "linux"
    else:
        print(Fore.RED + "[!] Invalid choice. Defaulting to Linux UI.")
        return "linux"

def apply_ui_style(ui_type):
    """Applies different styles based on UI selection."""
    if ui_type == "termux":
        # Termux-specific style (bright colors)
        init(autoreset=True)
        return {
            'heading_color': Fore.CYAN,
            'text_color': Fore.YELLOW,
            'box_color': Fore.GREEN
        }
    else:
        # Linux style (simple and clean)
        return {
            'heading_color': Fore.BLUE,
            'text_color': Fore.WHITE,
            'box_color': Fore.MAGENTA
        }

def provide_instructions():
    """Provides an informative guide to the user."""
    print(Fore.CYAN + "\n[INFO] Welcome to the Universal Translator.")
    print(Fore.YELLOW + "You can translate text between different languages.")
    print(Fore.GREEN + "Please select a source language and a target language for translation.")
    print(Fore.YELLOW + "Once you enter the text, the translation will be displayed shortly.")

def main():
    # Provide instructions to the user
    provide_instructions()

    # Select UI (Termux or Linux)
    ui_type = select_ui()
    ui_style = apply_ui_style(ui_type)

    # Display developer info and introduction
    display_developer_info()
    print_boxed_text("=== Universal Translator with Language Selector ===", ui_style['heading_color'], border_char='═')

    # Select source and target languages
    source_lang = get_language(ui_style['text_color'] + "[?] Select source language: ")
    target_lang = get_language(ui_style['text_color'] + "[?] Select target language: ")

    # Get user input for translation
    print(ui_style['text_color'] + "\n[+] Enter text to translate:")
    text = input(ui_style['text_color'] + "> ")

    # Show translation process with loading animation
    print(ui_style['heading_color'] + "\n[+] Translating...")
    loading_animation()  # Call loading animation

    # Translate the text and display the result
    result = translate_text(text, source_lang, target_lang)
    
    print_boxed_text(f"[+] Translated: {result}", ui_style['box_color'], border_char='═')

    # Ask if the user wants to exit
    ask_exit_option()

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
#Don't try to copy this script. It is made for educational purposes only.
