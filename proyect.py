# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from PyPDF2 import PdfReader
import os

def extract_words_from_pdf(pdf_path):
    extracted_words = []

    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            words = text.split()
            extracted_words.extend(words)

    return extracted_words[:5]  # Extract only the first 5 words


def process_words(words):
    processed_words = ""
    for word in words:
        if any(char.isdigit() for char in word):
            break
        processed_words += word + " "
    return processed_words.strip()

def main():
    folder_path = 'recibos'  # Folder where all the PDF receipts are stored

    # Iterate over all the PDFs in the folder
    for filename in os.listdir(folder_path):
        # Get the full path of the PDF
        pdf_path = os.path.join(folder_path, filename)

        # Extract only the first 5 words, which should contain the name
        extracted_words = extract_words_from_pdf(pdf_path)

        # Process the words to get only the name
        processed_words = process_words(extracted_words)

        # Generate a string with the name, which will be the new PDF name
        new_filename = processed_words + ".pdf"
        new_pdf_path = os.path.join(folder_path, new_filename)

        # Rename the PDF
        os.rename(pdf_path, new_pdf_path)

        print("Renamed PDF file:", new_filename)

if __name__ == "__main__":
    main()


    
