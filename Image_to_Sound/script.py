import pytesseract
from gtts import gTTS

# Set the Tesseract executable path (replace with your actual path)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Specify the language(s) used for OCR
language = 'eng'  # Replace 'eng' with the appropriate language code if needed

# Perform OCR and generate speech
spoken_text = gTTS(pytesseract.image_to_string('My_image.png', lang=language))

# Save or play the generated speech (as shown in the previous response)
spoken_text.save("output.mp3")
