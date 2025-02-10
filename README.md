# 🚀 Website Extractor

This Python script extracts and downloads the HTML, CSS, and JavaScript files from a given website. 🌍✨

## 🎯 Features
- 📜 Downloads the main HTML file of the target website.
- 🎨 Extracts and downloads linked CSS files.
- 🛠️ Extracts and downloads JavaScript files.
- 📂 Saves all assets inside the `website_assets` folder for easy access.

## 🔧 Prerequisites
Before running the script, ensure that you have the following installed on your system:
- **🐍 Python** (Make sure Python is installed. You can check by running `python --version` in the terminal.)
- **☕ Java** (Check if Java is installed using `java -version`. If not installed, download it from [Oracle](https://www.java.com/en/download/))

## 📥 Installation
1. Install the required Python libraries by running:
   ```bash
   pip install requests beautifulsoup4
   ```

## ▶️ Usage
1. Open the `extract_site.py` file and replace `Target-Website-URL` with the URL of the website you want to extract.
2. Run the script using the following command:
   ```bash
   python extract_site.py
   ```
3. If everything is correct, the extracted files (HTML, CSS, and JS) will be saved inside the `website_assets` folder. ✅
4. Navigate to `website_assets` and copy the extracted files as needed. 📁

## 📂 Output
After execution, the script will create the following folder structure:
```
website_assets/
│-- index.html  # Extracted HTML file
│-- css/        # Folder containing CSS files
│-- js/         # Folder containing JS files
```

## ⚠️ Notes
- 🔍 This script does not download images or other assets (like fonts or videos) from the website.
- 🚨 Ensure that you have permission to scrape the target website before using this script.

## 💡 Credits
Developed with ❤️ by **Laky**  
📧 Email: [mandujayaweera2003@gmail.com](mailto:mandujayaweera2003@gmail.com)

## 📜 License
This project is licensed under the **MIT License**. 📝

✅ Happy coding! 🚀