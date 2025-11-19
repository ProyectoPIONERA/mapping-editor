3Xmap Studio is a visual editor for **[R2RML](https://www.w3.org/TR/r2rml/)** and **[RML](https://w3id.org/rml/core/spec)** mappings. It is built with [Streamlit](https://github.com/streamlit/streamlit) and uses [Morph-KGC](https://github.com/morph-kgc/morph-kgc/) to create the knowledge graph.

## Features :sparkles:

- Supports relational databases and CSV files (more formats to come).
- Guide mapping development through pre-loaded ontologies.
- Create [RML views](https://www.w3.org/TR/r2rml/#r2rml-views) over relational databases with SQL.
- Export the RML mapping and create the knowledge graph.
- Explore your mapping.
- Save the session for later.

## Getting Started :rocket:

You can run 3Xmap Studio by cloning this repository and executing:

```bash
pip install -r requirements.txt
python -m streamlit run 0_3xmap-studio.py
```

We recommend to use [virtual environments](https://docs.python.org/3/library/venv.html#) to install 3Xmap Studio.
