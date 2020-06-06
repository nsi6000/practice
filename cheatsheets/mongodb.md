# MongoDB
## Websites
* <https://docs.mongodb.com/manual/>
* <https://github.com/ramnes/awesome-mongodb>
* MongoDB Atlas - DBaaS which handles Replication
* MongoDB Compass - MongoDB GUI Client
* mongo shell
* Default Port: 27017

# Concepts
* Cluster: group of servers that store data.
* Replica Set: a Cluster where each server stores the same data.
* PRIMARY: most often where all reads are done. Must be used for all writes. One and only one PRIMARY per Cluster.
* [JSON](https://en.wikipedia.org/wiki/JSON): JavaScript Object Notation. Basic Data Types := Number, String, Boolean, Array, Object, Null.
* Database: Namespace for a Collection.
* Collection: Stores Documents.
* Documents: Individual records.


# Commands
* show dbs
* show collections
* use <db_name>
* db.moviesScratch.insertOne({title:"Star Wars", year: 1982, imdb:"tt0084726"}) //implicitly creates the Collection.
* db.moviesScratch.find().pretty()
* db.moviesScratch.insertMany([{title:"Star Wars I", year: 1982}, {title:"Star Wars II", year: 1987}]) //inserts Documents as Array.
* db.moviesScratch.find({"year":1987})
* db.movieDetails.find({"awards.wins":2, "awards.nominations":2}).count()

