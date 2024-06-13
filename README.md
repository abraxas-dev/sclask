# Sclask
Sclask is a learning project created to explore web scraping technology using Scrapy. The project demonstrates a scraper capable of doing auth on the board website. It extracts the latest number from the site and awards points based on user-entered values. Once 100 points are accumulated, the scraper automatically stops its activities.

## Project Overview 

### Features
- **Login**: Automatically logs into the website.
- **Account Creation**: Creates a new account if no account exists and saves the credentials in `my_profile.txt`.
- **Number Parsing**: Parses a specific number from the website.
- **Target Checking**: Compares the parsed number with a target number.
- **Automation Stop**: Stops the script once 100 points are reached.

### Learning Objectives
This project aims to develop and apply fundamental skills in web scraping using Scrapy. It showcases how Scrapy can automate web-based tasks such as data extraction and executing actions on websites.

### Note
- This scraper is designed to be used for my other project - board.
- There is no validation for the correctness of login data or port in the scraper. Please ensure the login data and port information is accurate before use.
- Tested on Unix Systems.

### Usage
1. Clone the repository
```
git clone https://github.com/abraxas-dev/sclask.git
```
2. Navigate to the project directory
```
cd ./sclask
```
3. Create and activate a virtual environment
```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
4. Install scrapy
```
sudo pip3 install scrapy
```
5. Running the spider
```
scrapy crawl sclaskspider
```
