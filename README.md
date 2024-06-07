## Moviespro.ai

Moviespro.ai is an AI-powered web application designed to organize, analyze, and provide insights into movie scripts. Leveraging advanced natural language processing techniques, Moviespro.ai allows users to extract keywords and find similar movie plots, enhancing script analysis and organization. The application employs two distinct methods to achieve this: TF-IDF Vectorization and Sentence Transformers. Below is a detailed description of the project, the technologies used, and their functionalities.

### Features

1. **Keyword Extraction**: Extracts significant keywords from movie plots to help users quickly grasp the central themes.
2. **Similar Plot Finder**: Identifies and displays movies with similar plots, aiding users in finding comparable narratives.

### Technologies Used

#### 1. **TF-IDF Vectorization Method**

**TF-IDF (Term Frequency-Inverse Document Frequency)** is a statistical measure used to evaluate the importance of a word in a document relative to a collection of documents (corpus). The application uses the `TfidfVectorizer` from `sklearn` to transform movie plots into TF-IDF vectors.

- **Libraries**:
  - `pandas`: For data manipulation and analysis.
  - `streamlit`: For building the interactive web application.
  - `scikit-learn`: For implementing the TF-IDF Vectorizer and computing cosine similarities.
  - `numpy`: For numerical operations.

- **Functionality**:
  - **Keyword Extraction**: By analyzing the TF-IDF scores of words in a plot, the application identifies and lists the most significant keywords.
  - **Similar Plot Finder**: Computes cosine similarities between the TF-IDF vectors of plots to find and display similar movies.

#### 2. **Sentence Transformers Method**

**Sentence Transformers** provide state-of-the-art sentence embeddings, capturing semantic meanings more effectively than traditional methods. The application uses pre-computed embeddings to find similar plots.

- **Libraries**:
  - `pandas`: For data manipulation and analysis.
  - `streamlit`: For building the interactive web application.
  - `scikit-learn`: For computing cosine similarities.
  - `ast`: For parsing string representations of embeddings into lists.

- **Functionality**:
  - **Similar Plot Finder**: Uses cosine similarity on sentence embeddings of movie plots to identify and display similar movies.

### How It Works

1. **Load Data**: The application loads movie plots from a CSV file, removing duplicates to ensure data quality.
2. **Pagination**: Users can navigate through the movie plots using next and previous buttons, with the current page number displayed.
3. **Display Plot**: For each selected movie, the application displays the title, plot, and a link to its Wikipedia page.
4. **Keyword Extraction (TF-IDF Method Only)**: Upon clicking "Get Keywords", the application extracts and displays the top keywords for the current plot.
5. **Similar Plot Finder**: By clicking "Get similar plots", users can view a list of movies with similar plots, based on either TF-IDF or sentence embeddings.

### Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/moviespro-ai.git
   cd moviespro-ai
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### File Structure

- `app.py`: Main Streamlit application file.
- `American_movie_plots_2005_2021_v1.csv`: Dataset containing movie plots for the TF-IDF method.
- `American_movie_plots_2005_2021_v1_embeddings.csv`: Dataset containing movie plots and their sentence embeddings for the Sentence Transformers method.

### Conclusion

Moviespro.ai showcases the power of AI in text analysis and natural language processing, providing users with tools to efficiently analyze and find similarities in movie scripts. By leveraging both traditional TF-IDF and modern Sentence Transformers, the application offers flexible and robust solutions for different analytical needs.
The application is later integrated with a text paraphraser which used GPT to paraphrase the text content and it was deployed over self scaling AWS Lambda service using AWS SAM as an API sevice which was locally verified using Postman.

Thank you, hope you enjoy the work!
