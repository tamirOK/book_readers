### How to run
Run `docker-compose up` and wait for 5-7 minutes until `web` service prints in stdout:

`Watching for file changes with StatReloader`

#### How to use

_Default limit value is **100** and offset value is **0**_

* `localhost:8000/books/<id>` - get details of the book with id `<id>`. **Range of ids in [1;100000]**    
* `localhost:8000/reader/<id>` - get details of the reader with id `<id>`. **Range of ids in [1;50000]**    
* `localhost:8000/export/books&limit=500&offset=10` - Exports books info in csv format    
* `localhost:8000/export/readers&limit=500&offset=10` - Exports readers info in csv format     

### Design reasoning
In database I have used simple master-slave architecture(_Postgres streaming replication_), in which application can 
both read and write to master DB instance, but slave DB instance is read-only. Changes made after insert/update/delete
operations on master are propagated to slave instance. I have made only one slave instance for the sake of simplicity.

On the very first run django command `populate_db` is invokes which creates 100_000 book instances 
and 50_000 reader instances using `mimesis` python library.

I haven't used http server,reverse proxy server for the sake of simplicity.
