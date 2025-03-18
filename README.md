# Accounting Entry Assistant Bot

## 📋 Description
A bot developed in Python to automate accounting entries, allowing accountants and financial professionals to save significant time on repetitive tasks. The system reads data from an Excel spreadsheet and performs automatic insertion into accounting systems, eliminating the need for manual data entry.

![Captura de tela 2025-03-18 184332](https://github.com/user-attachments/assets/5f6b0381-f84c-40ba-a892-8d43b4374cbf)

> **Important note:** This repository contains a demonstration version of the code, using a spreadsheet with fictional data and a simulated frontend that was created specifically for demonstration purposes. The structure and logic of the code are identical to the real solution implemented for the client but were adapted to protect sensitive data and intellectual property.

## 🚀 Project Impact
- **Time savings**: Approximately 10 hours weekly
- **Financial savings**: About R$625 monthly (R$7500 annually)
- **Productivity increase**: Freeing up the professional for strategic activities

## 🛠️ Technologies Used
- **Python**: Base programming language
- **PyAutoGUI**: Automation of mouse and keyboard movements
- **OpenPyXL**: Reading and manipulating Excel files
- **PyperClip**: Facilitates copy and paste operations
- **OS**: Navigation between system directories and files

## 📦 Prerequisites
- pip install openpyxl pyautogui pyperclip

## 🔧 How It Works
1. The script reads an Excel spreadsheet containing the data to be entered
2. For each row in the spreadsheet, the bot:
   - Copies information from a specific field
   - Positions the cursor in the corresponding field of the system
   - Pastes the information
   - Navigates between different pages/stages of the form
   - Completes the registration and starts a new one

## 📋 Spreadsheet Structure
The spreadsheet should contain the following columns (adaptable as needed):
1. Product name
2. Description
3. Category
4. Product code
5. Weight
6. Dimensions
7. Price
8. Quantity in stock
9. Expiration date
10. Color
11. Size
12. Material
13. Manufacturer
14. Country of origin
15. Notes
16. Barcode
17. Warehouse location

## ⚙️ Customization
The code can be easily adapted for different systems and form layouts by adjusting the click coordinates and the structure of the source spreadsheet.

## 📄 License
6HTR66. 
This is a demonstration version project. All rights reserved.
