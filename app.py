from flask import Flask, render_template, request, send_from_directory
from crawl import crawl_website
from search import search_webpages

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    website_url = request.form['search_url']
    search_query = request.form['search_query']

    # Trigger the crawling process
    crawl_website(website_url)

    # Perform the search on the newly generated CSV file
    error, results = search_webpages(search_query)

    return render_template('search-result.html', error=error, results=results)

@app.route('/download')
def download_csv():
    data_folder = 'datas'
    filename = 'webpages.csv'
    return send_from_directory(directory=data_folder, path=filename, as_attachment=True)

@app.route('/download_search_results')
def download_search_results():
    data_folder = 'datas'
    filename = 'search-results.csv'
    return send_from_directory(directory=data_folder, path=filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
