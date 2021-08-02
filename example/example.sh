#!/bin/bash
python3 example.py \
  --SPARK_HOME=spark3 \
  --spark_conf_medium___spark.network.timeout=5000 \
  --spark_conf_medium___spark.executor.memory=6g \
  --wrong.param=1000 \
  --spark_conf_medium___spark.sql.hive.convertMetastoreParquet=True \
  --spark_conf_low___spark.executor.memory=2g \
  --spark_conf_low___spark.network.timeout=1000