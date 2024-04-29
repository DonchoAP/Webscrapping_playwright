#Import selected scrapping tool
from playwright.sync_api import sync_playwright
import re

def extract_words_from_text(text):
    # Using a regular expression to extract only words from the text
    words = re.findall(r'\b\w+\b', text)
    return words

def save_words_to_txt(words, filename):
    # Saving words to a text file
    with open(filename, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

def scrape_and_save_words(url, output_filename):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        # Extracting text from the page
        text = page.inner_text('body')
        # Extracting words from the text
        words = extract_words_from_text(text)
        # Saving the words to a text file
        save_words_to_txt(words, output_filename)
        browser.close()

# URL of the webpage you want to scrape
url = 'https://buchkodex.de/blog/verben/'
# Name of the text file where the words will be saved
output_filename = 'extracted_words_german.txt'

# Calling the function to scrape and save the words
scrape_and_save_words(url, output_filename)

