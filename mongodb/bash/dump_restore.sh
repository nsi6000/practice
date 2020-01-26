#run in MongoDB container with: bash dump_restore.sh


mongodump -d faker1 -o .

mongorestore -d faker1_backup faker1/


