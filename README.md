# OCR

You are given a bank statement (PDF) of a customer, and you will need to write a program to extract the following information.
1. Name of customer
2. Address of customer
3. Bank account number
4. Statement Date
5. List of transactions with following information (Date, Description, Amount, transaction type - Debit or Credit)

# Solutions
Extracting data from documents is one of important things people that work in data must be aware of. Since mostly we don't have access to the master file, we need to come up with another solution of getting and transfrom the data from paper or document to accessible format so we could do analysis on it. The most common way to extract information from pdf files is using OCR (Optical Character Recognition). First, we need to convert the pdf files into images and then use OCR to read the content of the image.

There are 2 solutions here.
1. Generic solution, extract all content as it is
2. Extract specific information such as name, address, etc.
