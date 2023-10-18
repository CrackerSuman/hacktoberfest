import requests
from bs4 import BeautifulSoup

# NEPSE IPO URL (replace with the specific IPO page you want to check)
nepse_ipo_url = "https://nepalstock.com.np/ipo-result"

# Send an HTTP GET request to the NEPSE IPO page
response = requests.get(nepse_ipo_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract and display IPO subscription or result information
    # You will need to inspect the specific elements on the page to extract data
    # For example, use soup.select or soup.find to locate the relevant data
    
    # Example:
    # result_table = soup.find('table', {'class': 'ipo-result-table'})
    # for row in result_table.find_all('tr'):
    #     cells = row.find_all('td')
    #     if len(cells) >= 3:
    #         company_name = cells[0].text
    #         applied = cells[1].text
    #         allotted = cells[2].text
    #         print(f"Company: {company_name}, Applied: {applied}, Allotted: {allotted}")
else:
    print("Failed to retrieve the NEPSE IPO page. Check the URL or your internet connection.")
