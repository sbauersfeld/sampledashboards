from pyspark.sql.functions import udf, array
from pyspark.sql.types import IntegerType

@udf(IntegerType())
def sumRow(*row):
  return sum(row)
 