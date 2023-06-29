# Plagiarism Checker

Plagiarism Checker is a Django-based web application that allows users to check for plagiarism in text documents. It utilizes various algorithms and techniques to compare and analyze text similarity.

## How to Run the Project
To run the project, follow these steps:

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd Plagiarism_Checker`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the application: `python manage.py runserver`
5. Access the application in your web browser at: `http://localhost:8000`

## Tech Stack

The Plagiarism Checker web application is built using the following technologies:

- **Python**: The primary programming language used for developing the application. Python is known for its simplicity, readability, and vast ecosystem of libraries and frameworks.

- **Django**: A high-level Python web framework that provides a robust and efficient development environment for building web applications. Django follows the Model-View-Controller (MVC) architectural pattern and offers features like URL routing, template rendering, and database abstraction.

- **NLTK**: The Natural Language Toolkit (NLTK) is a Python library used for natural language processing (NLP). It provides various tools and resources for tasks like tokenization, stemming, part-of-speech tagging, and stopword removal.

- **Google Custom Search JSON API**: The Google Custom Search JSON API is utilized for performing web searches and retrieving search results. It allows the application to query the Google search engine programmatically and obtain relevant information.

- **PyPDF2**: A Python library for extracting text and metadata from PDF files. PyPDF2 enables the application to read and process PDF documents, making it possible to check for plagiarism in PDF files.

## Project Structure

The project follows the following directory structure:

- `plagiarismchecker/`
  - `urls.py`
  - `views.py`
  - `algo/`
    - `ConsineSim.py`
    - `WebSearch.py`
    - `fileSimilarity.py`
    - `main.py`
  - `templates/`
    - `index.html`
    - `doc_compare.html`

### Description of Each File and Directory

- `plagiarismchecker/`: Main directory containing the Django project files.
  - `urls.py`: URL configuration for the Django project.
  - `views.py`: Contains the view functions for handling web requests and rendering templates.
  - `algo/`: Directory containing the algorithm-related modules.
    - `ConsineSim.py`: Module for calculating cosine similarity of two strings.
    - `WebSearch.py`: Module for performing web searches and retrieving search results.
    - `fileSimilarity.py`: Module for calculating file similarity using TF-IDF.
    - `main.py`: Module for finding similarity using the implemented algorithms.
  - `templates/`: Directory containing the HTML templates for rendering the web pages.
    - `index.html`: Template for the main homepage.
    - `doc_compare.html`: Template for comparing two documents.

## URLs Configuration

The urls.py file in the project handles the URL routing and maps them to the corresponding view functions. Here's a brief overview of the URL patterns:

- `path('')`: The main homepage URL that renders the home view function.

- `path('compare/')`: URL for comparing two documents, mapped to the fileCompare view function.

- `path('test/')`: URL for performing a web search for a given text and displaying the results, mapped to the test view function.

- `path('filetest/')`: URL for performing a web search for a text document (in .txt or .docx format) and displaying the results, mapped to the filetest view function.

- `path('twofiletest1/')`: URL for comparing two text inputs, mapped to the twofiletest1 view function.

- `path('twofilecompare1/')`: URL for comparing two text documents (in .txt or .docx format), mapped to the twofilecompare1 view function.

These URL patterns define the different routes available in the Plagiarism Checker web application and specify the corresponding functions that handle the requests and generate the appropriate responses.

## Views 

- `home(request)`: Renders the homepage template (`index.html`) when a GET request is made to the root URL ("/").

- `test(request)`: Performs web search and calculates the similarity percentage for a given text query. Renders the homepage template (`index.html`) with the search results.

- `filetest(request)`: Reads the content of a text file (.txt) or a Word document (.docx), performs web search, and calculates the similarity percentage. Renders the homepage template (`index.html`) with the search results.

- `fileCompare(request)`: Renders the document comparison page template (`doc_compare.html`).

- `twofiletest1(request)`: Compares two text inputs and calculates the similarity percentage. Renders the document comparison page template (`doc_compare.html`) with the comparison result.

- `twofilecompare1(request)`: Reads the content of two text files (.txt) or Word documents (.docx), compares them, and calculates the similarity percentage. Renders the document comparison page template (`doc_compare.html`) with the comparison result.

These views handle different actions and interactions within the web application, such as searching for plagiarism, comparing text or document similarity, and rendering the appropriate templates with the results.

## Algorithm/ Directory

### `ConsineSim.py`

This file implements the cosine similarity algorithm, which is used to measure the similarity between two strings. The algorithm calculates the cosine of the angle between two vectors, where each vector represents the frequency of words in the respective strings. The file contains the following functions:

- `get_cosine(vec1, vec2)`: Calculates the cosine similarity between two vectors by computing the dot product and magnitudes of the vectors.
- `text_to_vector(text)`: Converts a text string into a word frequency vector using the `Counter` class from the `collections` module.
- `cosineSim(text1, text2)`: Calculates the cosine similarity between two text strings by converting them to vectors and calling the `get_cosine` function.

### `WebSearch.py`

This file provides functionality for performing web searches and retrieving search results. It uses the Google Custom Search API for querying the web and obtaining search results. The file contains the following functions:

- `searchWeb(text, output, c)`: Performs a web search for the given text and retrieves search results. It calculates the cosine similarity between the search query and each search result using the `ConsineSim.cosineSim` function. It updates the `output` and `c` dictionaries with the similarity scores and frequencies of the search results.

### `fileSimilarity.py`

This file implements the file similarity algorithm, which calculates the similarity between two text files using the TF-IDF (Term Frequency-Inverse Document Frequency) approach. The algorithm compares the unique words in the files and computes the TF-IDF values for each word. The file contains the following function:

- `findFileSimilarity(inputQuery, database)`: Calculates the similarity between the input query and a database (file) by computing TF (Term Frequency) and IDF (Inverse Document Frequency) values. It returns the match percentage between the query and the database.

### `main.py`

This file serves as the main module for finding similarity using the implemented algorithms. It includes functions for splitting text into queries, finding similarity in web searches, and calculating total similarity percentage. The file contains the following functions:

- `getQueries(text, n)`: Splits the input text into queries of length `n` and returns a list of query strings.
- `findSimilarity(text)`: Finds the similarity between the input text and web search results. It calls the `getQueries` function to split the text into queries and performs web searches using the `WebSearch.searchWeb` function. It calculates the total similarity percentage based on the search results and returns it along with the output links.

These algorithm files provide the core functionality of the plagiarism checking process, including calculating similarity scores and performing web searches. They are used in the Django views to process user input and generate plagiarism reports.

## Multiple File Formats Support
The application supports checking for plagiarism in various file formats, including plain text files (.txt), Microsoft Word documents (.docx), and PDF files (.pdf). Users can upload files in these formats for analysis and comparison.

## Document Comparison
In addition to checking individual documents for plagiarism, the application provides a document comparison feature. Users can compare two text inputs or two text documents to evaluate their similarity. The application calculates the similarity percentage and presents the comparison result to the user.

## Search Result Analysis
When performing web searches to find similar content, the application not only retrieves search results but also analyzes them. It calculates the similarity scores for each search result and presents them to the user. This analysis helps users identify the most relevant and similar sources from the search results.

## User-Friendly Interface
The application provides a user-friendly interface that is easy to navigate and interact with. It offers clear instructions and prompts for user actions, making the plagiarism checking process intuitive and straightforward.

## Key Takeaways
- The application is built using Django, a powerful Python web framework, which provides a solid foundation for developing web applications.

- The Natural Language Toolkit (NLTK) is utilized for text processing tasks such as tokenization, stemming, part-of-speech tagging, and stopword removal.

- The Google Custom Search JSON API is integrated to perform web searches and retrieve search results, enhancing the plagiarism checking capabilities of the application.

- The PyPDF2 library enables the application to read and process PDF documents, expanding the scope of plagiarism detection to include PDF files.

- The implemented algorithms, including cosine similarity and TF-IDF, play a crucial role in measuring text similarity and calculating plagiarism scores.

- The application supports various input methods, including entering text directly, uploading text files (.txt) or Word documents (.docx), and comparing two texts or documents.

- The web interface provides an intuitive user experience, allowing users to easily interact with the application, perform searches, and view plagiarism results.

## References
Here are some resources and references that were helpful in the development of the Plagiarism Checker web application:

- Django Documentation: Official documentation for the Django web framework. Available at https://docs.djangoproject.com.

- NLTK Documentation: Official documentation for the Natural Language Toolkit (NLTK) library. Available at https://www.nltk.org.

- Google Custom Search JSON API Documentation: Documentation for the Google Custom Search JSON API, which is used for web searching in the application. Available at https://developers.google.com/custom-search.

- PyPDF2 Documentation: Official documentation for the PyPDF2 library, which is used for extracting text from PDF files. Available at https://pythonhosted.org/PyPDF2.

- Cosine Similarity: Article on cosine similarity on Wikipedia. Available at https://en.wikipedia.org/wiki/Cosine_similarity.

Please refer to these resources for more information on the technologies, libraries, and algorithms used in the development of the Plagiarism Checker web application.
