# HTML-HEALER
🌐 Introducing HTML Healer: Your go-to solution for diagnosing and fixing HTML code effortlessly! 🛠️ Say goodbye to buggy pages and hello to flawless web experiences. Perfect for developers and web enthusiasts alike.

## Description
This Python script is designed to parse HTML files and identify common errors such as unclosed tags, missing images with an empty `src` attribute, and the use of obsolete tags. It leverages BeautifulSoup for HTML parsing, `tqdm` for displaying a progress bar during processing, and `colorama`, `sys`, and `textwrap` to enhance its readability.

## Features
- **Unclosed Tag Detection**: Identifies tags that have been opened but not properly closed.
- **Missing Image Detection**: Identifies images without a `src` attribute or with an empty `src` attribute.
- **Obsolete Tag Identification**: Detects the use of tags that are considered obsolete in modern HTML standards.

## Prerequisites
- Python 3.x
- Python libraries: `BeautifulSoup`, `tqdm`, `colorama`.

## Installations to be Made
1. Ensure Python 3.x is installed on your system.
2. Install the required dependencies by executing in the terminal: pip install beautifulsoup4 tqdm colorama


## Usage
To use this script, run it in your terminal: `python main.py`

When the script is executed, you will be prompted to provide the path to the HTML file you want to parse, like so: 
`Enter the path of the HTML file: C:/path_to_your_file`                                            
(Please replace `C:/path_to_your_file` with the actual path to your HTML file.)

After the analysis, the script will display the results directly in the console, organized into three categories: unclosed or malformed tags, missing images, and obsolete tags.

## Contribution
Contributions to this project are welcome. Please feel free to submit bug fixes, improvements, or new features via pull requests. For major changes, please open an issue first to discuss what you would like to change.
