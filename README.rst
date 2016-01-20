Hadoop
======

Instalación
-----------

http://pingax.com/install-hadoop2-6-0-on-ubuntu/
Termine trabajando con vagrant vagrant

Inicialización
--------------

Iniciar cluster
$ start-dfs.sh
$ start-yarn.sh

Chequear status con java virtual machone process status tool
$ jps
2130 ResourceManager
1764 DataNode
2548 Jps
1989 SecondaryNameNode
1626 NameNode
2269 NodeManager

Ver la info de MapReduce desde el browser
http://localhost:8080
Ver la info de HDFS
http://localhost:50070

Copiar datos
hdfs dfs -mkdir /data
hdfs dfs -mkdir /data/gutenberg
hdfs dfs -copyFromLocal /vagrant/datos/gutenberg/* /data/gutenberg

hdfs dfs -copyFromLocal /vagrant/datos/books_dataset/* /data/books_dataset

Crear carpeta de resultados
hdfs dfs -mkdir /results

.. note:: Instale snakebite para realizar estas tareas en forma más simple y rápida

Ejemplo

hdfs dfs -mkdir /results/gutenberg
snakebite mkdir /results/gutenberg

Hadoop testing
--------------

correr job de ejemplo
cat <input txt file(s)> | python ./wordcount_mapper.py | sort -k1,1 | python ./wordcount_reducer.py

cat data.csv | python mapper.py | sort -k1,1 | python reducer.py

Hadoop Streaming
----------------

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
-D mapred.map.tasks=5 \     ←optional
-D mapred.reduce.tasks=2 \  ←optional
-files <code-dir>/wordcount_mapper.py,<code-dir>/wordcount_reducer.py  \
-mapper "python ./wordcount_mapper.py" \
-reducer "python ./wordcount_reducer.py" \
-input <hdfs-input-dir> \
-output <hdfs-output-dir>

export HADOOP_APP_DIR=/vagrant/src/wordcount
export HADOOP_APP_DIR=/vagrant/src/wordcount-improved

Only mapping
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -files $HADOOP_APP_DIR/mapper.py,$HADOOP_APP_DIR/reducer.py -mapper $HADOOP_APP_DIR/mapper.py  -reducer NONE  -input /data/gutenberg/* -output /results/inverted-index/1

Map and reduce
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -files $HADOOP_APP_DIR/mapper.py,$HADOOP_APP_DIR/reducer.py -mapper $HADOOP_APP_DIR/mapper.py  -reducer $HADOOP_APP_DIR/reducer.py  -input /data/books_dataset/* -output /results/inverted-index/1

Combiner
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -files $HADOOP_APP_DIR/mapper.py,$HADOOP_APP_DIR/reducer.py -mapper $HADOOP_APP_DIR/mapper.py  -reducer $HADOOP_APP_DIR/reducer.py  -combiner $HADOOP_APP_DIR/reducer.py  -input /data/books_dataset/* -output /results/inverted-index/1


mrjob
=====

 python /vagrant/src/wordcount-mrjob/wc.py -r hadoop hdfs:///data/books_dataset/a_christmas_carol.txt
