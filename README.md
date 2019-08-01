# ut-demographics-perspective

A data viewer for demographics data from 2008-2018 for the University of Texas at Austin, using [Perspective](https://perspective.finos.org), a blazing-fast data transformation and visualization tool.

This allows us to quickly graph, sort, filter, and analyze data provided by the University in relation to student population demographics. 

Currently, the viewer shows demographics for students based on college, gender, and race. Student numbers are aggregated by the University and delivered for each year from 2008 to 2018.

As Perspective is easy to initialize and pass data into, most of the development time is spend on navigating Tableau's clunky download interface and performing manual/scripted cleanup of the data provided. Additional datasets are forthcoming.

Datasets are downloaded from UT's Tableau, cleaned and transformed from CSV into [Apache Arrow](https://arrow.apache.org), and loaded into the Perspective viewer at [index.html](https://sc1f.github.io/ut-demographics-perspective).

Best viewed on a computer.

[Data Source](https://reports.utexas.edu/spotlight-data/students)

### Developing

1. Activate venv and install dependencies:
```
python3 -m venv venv
pip install -r requirements.txt
source venv/bin/activate
```

2. Run data transformation scripts
```
python3 parser.py
python3 csv2arrow.py
```

3. Open the `index.html` file
