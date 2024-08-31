# def get_website_url():
# Replace the URL below with the website you want to crawl
# return "http://books.toscrape.com/"
# Dependencies to install before running it
# pip install requests beautifulsoup4


import os


def get_user_input():
    website_url = input("Enter the URL of the website to crawl: ")
    search_query = input("Enter search query: ")

    # Call crawl.py and search.py with the user input
    os.system(f"python crawl.py {website_url}")
    os.system(f"python search.py {search_query}")


if __name__ == "__main__":
    get_user_input()


# import sys
# import subprocess

# def get_user_input():
#     website_url = input("Enter the URL of the website to crawl: ")
#     search_query = input("Enter search query: ")

#     # Call crawl.py
#     subprocess.run(['python', 'crawl.py', website_url])

#     # Call search.py
#     result = subprocess.run(['python', 'search.py', search_query], capture_output=True, text=True)
#     print(result.stdout)

# if __name__ == "__main__":
#     get_user_input()
