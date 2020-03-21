# RethinkDB
<https://rethinkdb.com/docs>

* ReQL is case sensitive.
* rethink import --help
* rethink import -f <file_name>.json|xml|csv --table <table_name>.catalog
* rethink dump
* r.db().table().
	* insert
	* get
	* delete
	* filter
	* replace
	* pluck
	* limit
	* skip
	* orderBy("<field_name>")
	* orderBy(r.desc("<field_name>")
	* hasFields()
	* withFields() //= hasFields() + pluck().
	* toISO8601() //to store dates.
	* eq() //check if two datatypes are equal.
	* coerceTo("array")
	* indexCreate()
	* indexDrop()
	* indexStatus()
	* secondary index.... //to be completed.
	* changes() //pub-sub-like event listener.
	* r.point(<x-coord>,<y-coord>)
	* .distance() //compute distance between two geographic points.
* match
	* r.table('users').filter(function(doc){return doc('name').match("^A")})

## Concepts

* Tables.
* Streams.
* Selections.
* Objects.
* Numbers.
* Times.
* Secondary index.
* Compound index.
* Arbitrary index.


