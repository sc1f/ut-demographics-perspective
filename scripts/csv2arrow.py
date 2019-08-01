import os
import pyarrow as pa
from pyarrow import csv

if __name__ == "__main__":
    # read CSV
    csv_name = os.path.join(os.path.dirname(__file__), "../static/csv/demographics.csv")
    # make sure bools are read correctly
    options = csv.ConvertOptions(
            column_types = 
            {
                "Number of students": pa.int32(),
                "Year": pa.int32()
            })
    table = csv.read_csv(csv_name, convert_options = options)
    # write table to arrow
    writer = pa.RecordBatchFileWriter(os.path.join(os.path.dirname(__file__), "../static/arrow/demographics.arrow"), table.schema)
    writer.write_table(table)
    writer.close()
    