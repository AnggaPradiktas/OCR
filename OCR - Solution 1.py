#!/usr/bin/env python
# coding: utf-8

# ### Solution 1

# So here we need to extract informations from raw pdf document. I borrow codes from https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/ to convert the pdf into images and then using PyTesseract to recognize text on the images. Before we run this code, make sure every packages was properly installed.
# Packages needed:
# 1. pip install pytesseract
# 2. pip install pdf2images
# 
# And don't forget to download tesseract.exe (https://github.com/tesseract-ocr/tesseract/wiki) and install it in your computer 
# 
# This solution is pretty generic and would work for any format and layout of any pdf files, but the output file is not producing specific information defined in the assignment such as column name, etc. However I try to create another possible solution. in separate notebook.

# In[1]:


from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 


# In[2]:


# Tell the system the directory of our tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# In[3]:


# Path of the pdf 
PDF_file = "bankstatementinput.pdf"


# In[4]:


# Store all the pages of the PDF in a variable 
pages = convert_from_path(PDF_file)


# In[5]:


'''
Part 1 - Convert PDF into Images
'''

# Counter to store images of each page of PDF to image 
image_counter = 1
  
# Iterate through all the pages stored above 
for page in pages: 
  
    # Declaring filename for each page of PDF as JPG 
    # For each page, filename will be: 
    # PDF page 1 -> page_1.jpg 
    # .... 
    # PDF page n -> page_n.jpg 
    filename = "page_"+str(image_counter)+".jpg"
      
    # Save the image of the page in system 
    page.save(filename, 'JPEG') 
  
    # Increment the counter to update filename 
    image_counter = image_counter + 1


# In[6]:



''' 
Part 2 - Recognizing text from the images using OCR 
'''

# Variable to get count of total number of pages 
filelimit = image_counter-1

# Creating a text file to write the output 
outfile = "output_text_solution_1.txt"

# Open the file in append mode so that  
# All contents of all images are added to the same file 
f = open(outfile, "a") 

# Iterate from 1 to total number of pages 
for i in range(1, filelimit + 1): 

  # Set filename to recognize text from 
  # Again, these files will be: 
  # page_1.jpg 
  # page_2.jpg 
  # .... 
  # page_n.jpg 
  filename = "page_"+str(i)+".jpg"
        
  # Recognize the text as string in image using pytesserct 
  text = str(((pytesseract.image_to_string(Image.open(filename)))))

  # The recognized text is stored in variable text 
  # Any string processing may be applied on text 
  # Here, basic formatting has been done: 
  # In many PDFs, at line ending, if a word can't 
  # be written fully, a 'hyphen' is added. 
  # The rest of the word is written in the next line 
  # Eg: This is a sample text this word here GeeksF- 
  # orGeeks is half on first line, remaining on next. 
  # To remove this, we replace every '-\n' to ''. 
  text = text.replace('-\n','')

  # Finally, write the processed text to the file. 
  f.write(text)

# Close the file
f.close() 


# #### output: https://github.com/AnggaPradiktas/OCR/blob/master/output_text_solution_1.txt
