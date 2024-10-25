import pyttsx3
from PyPDF2 import PdfReader
import keyboard
import threading

# Function to read the PDF
def read_pdf():
    # Open the PDF file
    book = open('progit.pdf', 'rb')

    # Initialize PdfReader
    pdfReader = PdfReader(book)

    # Get the number of pages
    pages = len(pdfReader.pages)
    print(f'Total pages: {pages}')

    # Initialize the text-to-speech engine
    speaker = pyttsx3.init()

    # Set the speech rate (words per minute)
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate - 50)  # Decrease the rate for slower reading

    # Loop through all pages and read the text
    for i in range(pages):
        page = pdfReader.pages[i]  # Access the page directly
        text = page.extract_text()  # Use extract_text()

        if text:  # Check if there is text to read
            speaker.say(text)
            speaker.runAndWait()  # Wait for the speech to finish before continuing

    # Close the PDF file
    book.close()

# Function to listen for a stop key
def listen_for_stop():
    keyboard.wait('esc')  # Wait for the 'Esc' key to be pressed
    print("Stopping the reading...")
    speaker.stop()  # Stop the speech

# Start reading the PDF in a separate thread
speaker = pyttsx3.init()
reading_thread = threading.Thread(target=read_pdf)
reading_thread.start()

# Start listening for the stop command
listen_for_stop()

# Wait for the reading thread to finish
reading_thread.join()