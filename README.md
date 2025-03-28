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
The graph database can be created by running the `generate_graph_db.py` script <using poetry or uv>

```bash
<commmand to run using uv>
```

