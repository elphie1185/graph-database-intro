import argparse
import pandas as pd

from graphdatascience import GraphDataScience

bolt = "bolt://localhost:7687"
user ="neo4j"
password = None

def parse_arguments():
    parser = argparse.ArgumentParser(description="Looad books and author data in neo4j")
    parser.add_argument(
        "--book-data-file", 
        type=str,
        help="Path to the CSV file containing book data",
        default="data/books.csv"
    )
    parser.add_argument(
        "--author-data-file", 
        type=str,
        help="Path to the CSV file containing author data",
        default="data/authors.csv"
    )
    return parser.parse_args()

if __name__ == "__main__":
    arguments = parse_arguments()
    # https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data
    book_data = pd.read_csv(arguments.book_data_file)
    # https://www.kaggle.com/datasets/choobani/goodread-authors
    author_data = pd.read_csv(arguments.author_data_file)

    # join the two dataframes
    df = pd.merge(
        book_data, 
        author_data, how="left", 
        left_on="Author", 
        right_on="name"
    )

    genres = [eval(genre) for genre in df["Genres"].values]
    df.loc[:, "book_genre"] = [genre[0] if len(genre) > 0 else None for genre in genres]
    df = df[["Book", "Author", "Avg_Rating", "gender", "fan_count", "country", "book_genre"]].dropna()
    
    gds = GraphDataScience(bolt, auth=(user, password))

    gds.run_cypher(
        """
        UNWIND $books as book
        MERGE (b:Book {title: book['Book'], rating: book['Avg_Rating']})
        MERGE (a:Author {name: book['Author'], num_followers: book['fan_count'], country: book['country'], gender: book['gender']})
        MERGE ((a)-[:PUBLISHED]->(b))
        MERGE (g:Genre {genre_name: book['book_genre']})
        MERGE ((b)-[:OF_GENRE]->(g))
        """,
        params={ 'books': df.to_dict(orient='records') }
    )