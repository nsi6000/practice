# Neo4j
https://neo4j.com/docs/
* default port: 7474
* default user: admin
* default password: admin


# Concepts

* node
* edge
* label
* property
* uni- and bi-directional relationships

# Commands

INSERT ROW/NODE
	create (n:Student {name:"Bill", age:21});
SELECT *
	match(n) return n;
SELECT * WHERE STUDENT
	match(n:Student) return n;
SELECT NAME, AGE FROM WHERE STUDENT
	match(n:Student) return n.name, n.age;
match (n:Student) return n.nicknames[0];
UPDATE ROW/NODE
	match(n:Student {name:"Tim"}) set n.nicknames=["Ti","Timmy"] return n;
match (n) where n.name="Bill" and n.age=21 return n;
match (n) where n.name="Bill" and n.age<>22 return n;
match(n :Student {name:"Tim"}) remove n:Teacher;
DELETE ROW/NODE
	match (n:User) delete n;
merge ...
CREATE/INSERT RELATIONSHIP
	match (ja:Student {name:"Jack"}),(jm :Student {name:"James"})
	create (ja)-[r :FRIEND {nickname: "Jimbo"}]->(jm)
	return ja, r, jm;

	match (ja:Student {name:"Jack"}),(jm :Student {name:"James"})
	create (ja)<-[r :FRIEND {nickname: "Jacko"}]-(jm)
	return ja, r, jm;

	create p = (j:Student {name:"Jilian",age:23})-[:FRIEND {nickname:"Benji"}]->(b:Student {name:"Ben",age:23})-[:FRIEND {nickname:"Jill"}]->(j) return p;

SELECT RELATIONSHIP
	match (ja:Student {name:"Jack"})-[]->(jm:Student {name:"James"}) return ja, jm;
DELETE RELATIONSHIP
	match (ja:Student {name:"Jack"})-[r:FRIEND]->(jm:Student {name:"James"}) delete r;
UPDATE RELATIONSHIP
	match (:Student {name:"Jilian"})<-[r:FRIEND]-(:Student {name:"Ben"})
	set r.nickname="Jilly"
	return r;
UNIQUE RELATIONSHIP
	match (j:Student {name:"Jilian"})
	create unique (j)-[r:FRIEND]->(d:Student {name:"Dave",age:25})
	return j,type(r),d;

DELETE ALL NODES AND ALL RELATIONSHIPS (DROP DATABASE)
	match (n)
	optional match (n)-[r]-()
	delete n, r;

PATTERN MATCH STUDENT NODES THAT HAVE RELATIONSHIP TO A PROVIDER
	match (a:Student)-->(b:Provider) return a, b; --uni-directional relationship.
	match (a:Student)--(b:Provider) return a, b; --bi-directional relationship.
	match (a)-->(b)-->(c) return a,b,c;
	match (a:Provider)-[:PUBLISHED]-(b:Course)-[:INSTRUCTED_BY]-(c:Instructor) return a,b,c;
	match (a:Student)-->(b:Course)<--(c:Provider) return a,b,c;
	match (a:Student)-[:ENROLLED_IN]->(b:Course)<-[:PUBLISHED]-(c:Provider) return a,b,c;

RETURN AVG AGE OF STUDENTS PER COURSE HAVING MORE THAN 25
	match (s:Student)-[:ENROLLED_IN]->(c:Course)
	with avg(s.age) as avgAge, c
	where avgAge >= 25
	return avgAge, c
	order by avgAge desc
	limit 1;

	match (s:Student) return s, count(s.age);
	match (s:Student) return min(s.age);
	match (s:Student) return max(s.age);
	match (s:Student) return sum(s.age);
	match (p:Provider)<-[:HAS_REGISTERED]-(s:Student) return p.name, collect(s.age);
	match (p:Provider)<-[:HAS_REGISTERED]-(s:Student) with p, collect(s.age) as ages , sum(s.age) as sumAge return p.name, reduce(totalAge=0, age in ages | totalAge + age) as TotalAges, sumAge;

	match paths=(p:Provider)<-[:HAS_REGISTERED]-(s:Student) return extract(node in nodes(paths) | labels(node) + node.name) as labels;

	match paths=(p:Provider)<-[:HAS_REGISTERED]-(s:Student) return filter(node in nodes(paths) where node:Student) as students;

Node Hoping
	match p=(s:Student {name:"Bill"})-[]->(c:Course) return p;
	match p=(s:Student {name:"Bill"})-[*1]->(c:Course) return p;
	match p=(s:Student {name:"Bill"})-[*1..2]->(c:Course) return p;
	match p=(s:Student {name:"Bill"})-[*2]->(c:Course) return p;
	match p=(s:Student {name:"Bill"})-[*1..3]->(i:Instructor) return length(p);
	match p=(s:Student {name:"Bill"})-[*3]->(i:Instructor) return length(p);
	match p=(s:Student {name:"Bill"})-[:HAS_REGISTERED*1..3]-(i:Instructor) return length(p);
	match p=shortestPath((s:Student {name:"Bill"})-[:HAS_REGISTERED*1..3]-(i:Instructor)) return length(p);
	match p=allShortestPaths((s:Student {name:"Bill"})-[:HAS_REGISTERED*1..3]-(i:Instructor)) return length(p);

TEXT SEARCHING (Regex)
	match (c:Course) where c.title =~ 'Spring.*' return c;
	match (c:Course) where c.title =~ '(?i).*framework(s)?.*' return c;

IN for COLLECTIONS
	match (c:Course)<-[:PUBLISHED]-(p:Provider {name:"Udemy.com"})
	where all (tag in c.tags where tag in ["java","programming language"])
	return c;

	match (c:Course)<-[:PUBLISHED]-(p:Provider {name:"Udemy.com"})
	where any (tag in c.tags where tag in ["java","programming language"])
	return c;

	match (c:Course)<-[:PUBLISHED]-(p:Provider {name:"Udemy.com"})
	where none (tag in c.tags where tag in ["java"])
	return c;

	match (c:Course)<-[:PUBLISHED]-(p:Provider {name:"Udemy.com"})
	where single (tag in c.tags where tag in ["java","neo4j"])
	return c;

