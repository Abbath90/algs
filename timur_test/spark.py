from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import functions as f
from pyspark.sql import Column, DataFrame
from abc import ABC, abstractmethod
from enum import Enum

spark = SparkSession.builder.appName("TableJoinExample").getOrCreate()


class BaseValuesFilter(str, Enum):
    @property
    @abstractmethod
    def column(self) -> str:
        """"""

    @property
    def eq(self):
        return f.col(self.column) == self.value

    @property
    def ne(self):
        return f.col(self.column) != self.value


class TransactionTypes(BaseValuesFilter):
    SALE = "Manager"
    RETURN = "RETURN_ORDER"

    @property
    def column(self) -> str:
        return "profession"

schema1 = StructType([
    StructField("name", StringType(), nullable=False),
    StructField("age", IntegerType(), nullable=False)
])

data1 = [("John", 25), ("Alice", 30), ("Bob", 35)]
table1 = spark.createDataFrame(data1, schema1)

schema2 = StructType([
    StructField("name", StringType(), nullable=False),
    StructField("profession", StringType(), nullable=False)
])

data2 = [("John", "Engineer"), ("Alice", "Manager"), ("Charlie", "Developer")]
table2 = spark.createDataFrame(data2, schema2)

joined_table = table1.join(table2, "name").where(TransactionTypes.SALE.eq)

joined_table.show()
print(TransactionTypes.SALE.column)
print(TransactionTypes.RETURN.column)