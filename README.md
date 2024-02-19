# My Diary

This is a simple diary application built using Python's Tkinter library. It allows users to write, read, and save diary entries for specific dates.

## Features

- **Calendar**: The app features a calendar widget that allows users to select a date.
- **Read Entry**: Users can read previously saved entries for a selected date.
- **Write Entry**: Users can write or update entries for a selected date.
- **Encryption**: Entries are encrypted using a simple algorithm to enhance privacy.

## Installation

1. Clone this repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the `diary_app.py` file.

## Usage

1. **Select a Date**: Use the calendar widget to select a date.
2. **Write Entry**: Type your entry in the text box.
3. **Save Entry**: Click the "Write Entry" button to save your entry.
4. **Read Entry**: To read an entry, select a date and click the "Read Entry" button.

## Encryption

The app uses a simple encryption algorithm to encrypt entries. Each character in the entry is converted to its ASCII value, and the values are stored as a string separated by spaces. To decrypt, the ASCII values are converted back to characters.

## File Structure

- `diary_app.py`: The main application file.
- `requirements.txt`: Contains the required packages for the app.
- `dbdiary.txt`: Stores the encrypted diary entries.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Acknowledgments

-Thanks to me for being inspired by my thoughtsto make a diary app
