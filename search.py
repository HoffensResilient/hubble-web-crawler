import os
import csv

def search_webpages(search_query):
    data_folder = 'datas'
    csv_filepath = os.path.join(data_folder, 'webpages.csv')

    if not os.path.exists(csv_filepath):
        return "No data found. Please run the crawler first to generate the data.", []

    search_results_filepath = os.path.join(data_folder, 'search-results.csv')
    found_results = []

    with open(csv_filepath, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            url, title = row
            if search_query.lower() in title.lower():
                found_results.append((url, title))

    # Write search results to CSV
    with open(search_results_filepath, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Title'])
        writer.writerows(found_results)

    if found_results:
        return None, found_results
    else:
        return "No matching results found.", []
