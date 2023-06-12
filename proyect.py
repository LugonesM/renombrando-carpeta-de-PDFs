# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import PyPDF2
import os


def extract_words_from_pdf(pdf_path):
    extracted_words = []

    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extract_text()
            words = text.split()
            extracted_words.extend(words)

    return extracted_words[:5]  # Extrae solo las primeras 5 palabras


def process_words(words):
    processed_words = ""
    for word in words:
        if any(char.isdigit() for char in word):
            break
        processed_words += word + " "
    return processed_words.strip()




def main():

    folder_path = 'recibos' #carpeta donde estan todos los recibos en pdf

    # Itera por todos los pdfs de la carpeta
    for filename in os.listdir(folder_path):
    
        # toma el full path del pdf
        pdf_path = os.path.join(folder_path, filename)

        # extrae solo las primeras 5 palabras que es donde se encuentran los nombres
        extracted_words = extract_words_from_pdf(pdf_path)

        # Procesa las palabras para que sean SOLO el nombre 
        processed_words = process_words(extracted_words)

        # Generata un string con el nombre que sera el nombre del pdf
        new_filename = processed_words + ".pdf"
        new_pdf_path = os.path.join(folder_path, new_filename)

        # Renombra el pdf
        os.rename(pdf_path, new_pdf_path)

        print("Renamed PDF file: ", new_filename)
            



if __name__ == "__main__":
    main()   
    
    