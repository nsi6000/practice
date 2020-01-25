//run with: cqlsh -f helloworld.cql

create keyspace helloworld
with replication = {'class':'SimpleStrategy','replication_factor':1};

use helloworld;

create table if not exists helloworld (
id UUID primary key,
message text
);

insert into helloworld (id, message) values (uuid(), 'Hello');
insert into helloworld (id, message) values (uuid(), 'world');

select
 id
,message
from helloworld
;

drop table helloworld;


