#!/bin/bash

spark-submit --master  k8s://https://192.168.178.69:8443 \
--deploy-mode cluster \
--name aria-spark \
--class io.codextension.aria.App \
--conf spark.kubernetes.authenticate.driver.serviceAccountName=spark-sa \
--conf spark.kubernetes.namespace=aria \
--conf spark.executor.instances=2 \
--conf spark.kubernetes.container.image.pullPolicy=Always \
--conf spark.kubernetes.container.image=localhost:5000/spark:aria \
--conf spark.kubernetes.driver.volumes.persistentVolumeClaim.spark-pv-storage.options.claimName=spark-pv-claim \
--conf spark.kubernetes.driver.volumes.persistentVolumeClaim.spark-pv-storage.mount.path=/opt/spark/work-dir/ \
--conf spark.kubernetes.driverEnv.CX_KAFKA_URL=192.168.178.63:9092 \
--conf spark.kubernetes.driver.secretKeyRef.CX_DB_NAME=db-access:schema \
--conf spark.kubernetes.driver.secretKeyRef.CX_DB_USER=db-access:schema_user \
--conf spark.kubernetes.driver.secretKeyRef.CX_DB_PWD=db-access:schema_pwd \
local:///opt/spark/work-dir/aria-spark-1.0-SNAPSHOT.jar