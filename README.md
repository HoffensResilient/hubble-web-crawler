# Web Crawler

## Overview

The **Web Crawler** is a tool designed to extract URLs and titles from webpages. This utility can be run via the command line and provides functionality to search and retrieve data from specified URLs.

## Latest Update

The web crawler is now accessible via a web browser! Please allow up to 50 seconds for the activation of the crawler once you visit the URL.

**Hosted URL:** [Insert your hosted URL here]

## How to Run the Web Crawler

Follow these steps to set up and run the web crawler:

### Setup

1. **Create a Directory**  
   Ensure you have a directory named `datas` in the same location as the `input.py` script. This directory is used to store the data collected by the crawler.

2. **Install Dependencies**  
   Ensure Python is installed on your system. Install the necessary packages by running:

   ```sh
   pip install requests beautifulsoup4
   ```

3. **Run the Crawler**  
   Execute the `input.py` script with the following command:

   ```sh
   python input.py
   ```

   Follow the prompts to input the URL and search query. The script will then perform the crawling and search operations, and output the results.

## Usage

- **Input**: Provide a URL and search query when prompted.
- **Output**: The crawler extracts URLs and titles from the specified webpage and stores the results in CSV files.

## Troubleshooting

If you encounter issues or need further assistance:

- **Check Dependencies**: Ensure all required packages are installed correctly.
- **Verify Directory Structure**: Confirm that the `datas` directory exists and is correctly named.
- **Review Logs**: Check for error messages or logs generated during execution for more details.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes with clear messages.
4. Push your branch and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for more details.

## Contact

For questions or feedback, please open an issue on GitHub or contact [rohitrajsarrafnp@gmail.com](mailto:rohitrajsarrafnp@gmail.com).