# title

## Creating venv with UV

Create and activate virtual environment: 

```
uv venv
source .venv/bin/activate
```

If needed you can add libraries to the venv with `uv add graphdatascience`

## Running Neo4Jj and creating the database

In this project we will run Neo4J locally to create a local graph database. 
Run `bin/start_neo4j_locally.sh` to start the local database. 
If you run into permissions errors, add the permission to execute the shell script with 
```bash
❯ chmod +x bin/start_neo4j_locally.sh
```

To create the graph database of books and authors make sure you have the 2 datasets 
books.csv and authors.csv in a data directory. These datasets can be dowloded from 
kaggle
https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data
https://www.kaggle.com/datasets/choobani/goodread-authors
The graph database can be created by running the `generate_graph_db.py` script uv.

```bash
uv run python generate_graph_db.py
```

