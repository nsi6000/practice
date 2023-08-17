# Scala
* [https://docs.scala-lang.org/](https://docs.scala-lang.org/)
* [https://docs.scala-lang.org/overviews/scala-book/introduction.html](https://docs.scala-lang.org/overviews/scala-book/introduction.html)
## Setup
* docker run -it --name scala_dev hseeberger/scala-sbt:8u222_1.3.5_2.13.1 bash
	- apt-get install vim
	- sbt new sbt/scala-seed.g8
	- sbt
	- => run
	- export SCALA_HOME="/usr/share/scala"
	- export PATH="$PATH:$SCALA_HOME/bin"
	- printenv
	- vim hello.scala => edit file with scala code.
```scala
		object HelloWorld {
			def main(args: Array[String]): Unit = {
				println("Hello, world!")
			}
		}
```
* in vim:
	- :w
	- :!scalac hello.scala && scala HelloWorld

## Concepts
* value vs variable
* type and type inference
* expression
* function
* recursion
* call-by-name vs call-by-value
* default and named arguments
* operations on strings
* exceptions
* package and import
* OOP:
  - class
  - [abtsract class](https://docs.scala-lang.org/overviews/scala-book/abstract-classes.html)
  - anonymous class
  - [case class](https://docs.scala-lang.org/overviews/scala-book/case-classes.html)
  - object
  - method
  - inheritence
  - abstract classes
  - traits
  - generics
* Functional Programming (FP):
  - [anonymous function](https://docs.scala-lang.org/overviews/scala-book/anonymous-functions.html)
  - higher-order function (HOF)
  - curries
  - map
  - flatmap
  - filter
  - for-comprehension
  - pattern matching
* Collections:
  - list
  - array
  - vector
  - tuple
  - option
* abc





## SCALA BASICS:
values, variables and types (Unit == no return)
expressions
code block (result = result last expression)
functions
type inference
(tail) recursion (factorial example)
	call-by-name and call-by-value
	default and named arguments
	smart operations on strings

## OOP:
method notations
objects
inheritance
abstract classes
traits
generics + companion object
anonymous classes
case classes
enums
exceptions (try-throw-catch-case-finally)
packaging and imports

## Functional:
anonymous functions
HOFs
curries
map, flatmap, filter and for-comprehension
sequences: list, array, vector
sets, tuples and maps
options
handling failure
Pattern matching
Braceless syntax


=> Async with Futures.
=> Parser Combinator: StatementLine ADT, Token Parsers, Next & Goto, BNF Translation, Packrat Parsers.
=> Macros.
=> Functors, Monads, Applicative Functors.

## Scala Best Practices:
- On mutability and immutability: recursion is ok with no impact (vs loops) if used correctly. (tail rec optimized)
- NULLs vs Options: get rid of all NULLs in Scala. Use Option->Some+None. (use Scalastyle library)
- May the Fors be with you: for(Generator(<-), Guard(if), Inline Assignment(=))-yield.
- Untying Unit: respect referential transparency: no effect are not visible in FP. (e.g.: def f(i: Int) {i * i} => Invisible Unit. Always use empty parenthesis when calling Unit methods: println() -> 6.toString is ok.
- Use Try/Either/Or instead of try...catch...case. (it doesn't block the logic, it's more FP.) def f(): Int Or ErrorMessage = {...}.
- Getting Loopy about recursion
- Mastery of Collections
- The Case for case classes: use case classes when possible.
- If you use a match: pattern-match a case class.
- Fancy a Curry
- Classy Implicits: favor implicit classes over implicit conversions when possible.
- Operation operator
- Beware the by-names

=> Loan Pattern (Auto Resource Management). => scala-arm library (with managed function).



## Scala Performance:
- when and where to optimize:
	- the code should work.
	- KISS.
- benchmarks: run multiple times (for the JVM to warm up / runtime optimization).
- collections: example: use Vector instead of List for Fibonacci. (Time it!) Arrays are fast (but unsafe/mutable).
- while loops and tail calls: @tailrec "converts" into a WHILE: its approx the same time.
	- sqrt & trig & random functions on JVM are quite slow.
	- the JVM can optimize your hotspots. (so leave it be.)
- JVM computations tips
- Primitives and Arrays
- Performance testing
- Profiling
- Caching: lazy val, CATS eval, ScalaZ memoize, Guava CacheBuilder,...

=> in PRs, prove that something is a hotspot (bottleneck), before fixing it.
=> Use Oracle free performance tool: VisualVM. (using "Sampler" and "Profiler" tabs ("CPU" button).)
=> Use bitshift random generator.


## Random notes

=> no break/continue. avoid "return".


PATH=$PATH:/usr/local/sbin/sbt/bin/
sbt new scala/scala-seed.g8 --branch 2.12.x
sbt clean
sbt test
sbt package

```scala
object Hello extends App {
	def main(args: Array[String]) {
		println("Hello.")
	}
}
```


## Scala 101:
* source: FP in Scala book.
```scala
val test: String = "Hello"
	println("Hello " + "World")
printf("Hello %s!", "World")
import scala.io.StdIn.readLine ; val lastName = readLine("Last Name: ")
4.+(5)
"Hello".toUpperCase
1 to 10
var i = 1; i += 1 (no i++)
import scala.math._ ; sqrt(2)
	"Hello"(4)
var i = 1; if (i > 0) "positive" else -1
var i = 1; var n = 10; while (n > 0) { i += n ; n -= 1}; println("i: " + i)
var x = 1; var n = 10; for (i <- 1 to n) { x *= n }
val s = "Hello"; for (i <- 0 until s.length if i != 2) println(i + " " + s(i))
for-comprehension: for (i <- 1 to 10) yield i % 3
function: def fac(n: Int): Int = if (n <= 0) 1 else n * fac(n - 1); fac(6)
default & named args: def decorate(str: String, left: String = "[", right: String = "]") = { left + str + right }; decorate("Hello", left = ">>>[")
variable args: def sum(args: Int*) = {var r = 0; for (arg <- args) r += arg; r}; sum(1 to 5: _*)
procedure(no return value, no "="): def box(s: String): Unit = {println("|" + s + "|")}; box("Hello")
lazy values: lazy val i = 1
```

## Arrays:
```scala
val n = new Array[Int](10)
val s = Array("Hello", "World")
s(0)
s(0) = "Goodbye"
s
import scala.collection.mutable.ArrayBuffer
val b = ArrayBuffer[Int]()
b += 1
b += (1, 2, 3)
b ++= Array(4, 5, 6)
b.trimEnd(5)
b.insert(2, 6, 7, 8)
b.remove(2, 3)
b.append(1, 2, 3)
val c = b.toArray
b.sum / c.sum
b.min / c.min
b.max / c.max
	val bSorted = b.sorted(_ < _)
scala.util.Sorting.quickSort(c)
b.mkString("<", ",", ">")
Multidim array: val m = Array.ofDim[Double](3, 4)
m(1)(2) = 42
	al m2 = new Array[Array[Int]](10)
for (i <- 0 until b.length) println(i + " : " + b(i))
for (i <- 0 until (b.length, 2)) println(i + " : " + b(i))
for (elem <- b) println(elem)
	val r = for (elem <- b if b % 2 == 0) yield 2 * elem
val r = b.filter(_ % 2 == 0).map(2 * _)
```

## Map (~ HashTable or TreeMap) & Tuples:
```scala
idiomatic: val scores = Map("Alice" -> 10, "Bob" -> 3, "Cindy" -> 8)
non-idiomatic: val scores = Map(("Alice", 10), ("Bob", 3), ("Cindy", 8))
val scores = scala.collection.mutable.Map("Alice" -> 10, "Bob" -> 3, "Cindy" -> 8)
val scores = new scala.collection.mutable.HashMap[String, Int]
val bobsScore = scores("Bob")
non-idiomatic: val bobsScore = if (scores.contains("Bob")) scores("Bob") else 0
idiomatic: val bobsScore = scores.getOrElse("Bob", 0)
scores.get("Bob") //returns Option/Some.
on mutable map: scores("Bob") = 10 //create or update.
scores += ("Alice" -> 10, "Cindy" -> 8)
scores -= "Alice"
on immutable (copy + upsert): val/var newScores = scores + ("Bob" -> 1, "David" -> 9)
val newScores = scores - "Alice"
for ((k, v) <- scores) println(k + " : " + v)
scores.keySet; for (v <- scores.values) println(v)
reversing keys-values: for ((k, v) <- scores) yield (v, k)
TreeMap: val scores = scala.collection.immutable.SortedMap("Alice" -> 10, "Bob" -> 3, "Cindy" -> 8)
Insertion order access with LinkedHashMap: val scores = scala.collection.mutable.LinkedHashMap("Alice" -> 10, "Bob" -> 3, "Cindy" -> 8)
Tuple: val t = (1, 3.14, "Fred")
val second = t._2 //position of tuples start at 1, not 0.
tuple pattern-matching: val (first, second, _) = t
Zipping:
val symbols = Array("<", "-", ">")
val counts = Array(2, 10, 2)
val pairs = symbols.zip(counts)
for ((s, n) <- pairs) print(s * n)
pairs.toMap
```

## Classes & Objects:
```scala
//general class definition.
class Counter {
	private var value = 0 //you must initialize the field.
	def increment() { value += 1 } //Methods are public by default.
	def current() = value //or without () to enforce not using ().
}
val myCounter = new Counter //or new Counter().
myCounter.increment() //use () with a mutator.
println(myCounter.current) //don't use () with an accessor.

//getter and setter create automatically by Scala.
vim Person.scala
	class Person {
		var age = 0
	}
scalac Person.scala
	scala -private Person //doesn't work
javap -p Person.class //shows getter and setter created under the hood by Scala.
val fred = new Person
fred.age = 21 //calls fred.age_=(21)
println(fred.age) //calls the method fred.age()

//redefine getter and setter manually.
class Person {
	private var privateAge = 0 //make private and rename.
	def age = privateAge
	def age_=(newValue: Int) {
		if (newValue > privateAge) privateAge = newValue; //can't get younger.
	}
}
val fred = new Person
fred.age = 30
fred.age = 21
println(fred.age) //30

//object-private fields. Scala allows access to private fields of all oobjects of its class.
class Counter {
	private var value = 0
	def increment() { value += 1 }
	def ifLess(other: Counter) = value < other.value //can access "other" since it's a Counter object.
	//to manually restrict access, use the statement below.
	private[this] var value = 0 //accessing someObject.value is not allowed.
	//to generate Java-compliant getter and setter names, use @BeanProprety.
	@BeanProprety var name: String = _ //generates name, name_, getName(), setName().
}

//Auxilliary constructors.
class Person {
	private var name = ""
	private var age = 0

	def this(name: String) { //An auxilliary constructor.
		this() //calls primary constructor. mandatory.
		this.name = name
	}

	def this(name: String, age: Int) { //Another auxilliary constructor.
		this(name) //calls the previous auxilliary constructor. mandatory.
		this.age = age
	}
}
val p1 = new Person //Primary constructor.
val p2 = new Person("Fred") //First auxilliary constructor.
val p3 = new Person("Fred", 42) //Second auxilliary constructor.

//Primary constructor.
class Person(val name: String = "John", val age: Int = 20) {
	println("Just created another person.")
	def description = name + " is " + age + " years old."
}
val fred = new Person("Fred", 42)
val john = new Person
println(fred.description)
println(john.description)

//to make the private primary constructor, use this...
class Person private(val id: Int) {}

//nested classes
import scala.collection.mutable.ArrayBuffer
class Network {
	class Member(val name: String) {
		var contacts = new ArrayBuffer[Member]
	}
	private val members = new ArrayBuffer[Member]
	def join(name: String) = {
		val m = new Member(name)
		members += m
		m
	}
}
val chatter = new Network
val myFace = new Network
val fred = chatter.join("Fred")
val wilma = chatter.join("Wilma")
fred.contacts += wilma //OK. Adding wilma is allowed since in the same "chatter" object.
val barney = myFace.join("Barney")
fred.contacts += barney //No. Not allowed since "myFace" is not "chatter".
//=> 2 solutions: add a companion object or use a type projection (new ArrayBuffer[Network#Member]).
```

## Objects:
```scala
//Singletons: single class instance.
object Accounts { private var lastNumber = 0; def newUniqueNumber() = { lastNumber += 1; lastNumber } }
Accounts.newUniqueNumber()

//companion object: class and its companion object. Use the same name.
//in REPL, class and object must be defined in the same :paste block. In code, should be in the same source file.
class Accounts { val id = Accounts.newUniqueNumber() }
object Accounts { private var lastNumber = 0; def newUniqueNumber() = { lastNumber += 1; lastNumber } }
val test1 = new Accounts
val test2 = new Accounts
println(test1.id + test2.id)

//Enumerations
object TrafficLightColor extends Enumeration { val Red, Yellow, Green = Value }
TrafficLightColor.Red
object TrafficLightColor2 extends Enumeration {
	type TrafficLightColor2 = Value //type alias. useful for imports.
	val Red = Value(0, "Stop") //assigned both ID and name.
	val Yellow = Value(10) //name = "Yellow".
	val Green = Value("Go") //ID = 11.
}
println("" + TrafficLightColor2.Red.id + " " + TrafficLightColor2.Red)
println("" + TrafficLightColor2.Yellow.id + " " + TrafficLightColor2.Yellow)
println("" + TrafficLightColor2.Green.id + " " + TrafficLightColor2.Green)
import TrafficLightColor2._
def doWhat(color: TrafficLightColor2) = { if (color == Red) "stop" else "go" }
doWhat(TrafficLightColor2.Red)
doWhat(TrafficLightColor2.Green)
//list all values from ENUM.
for (c <- TrafficLightColor2.values) println(c.id + ": " + c)
//access ENUM values.
TrafficLightColor2(10)
TrafficLightColor2.withName("Yellow")

//Class extension
class Person { val name: String = "" }
class Employee extends Person { val EmployeeID = 0 }
val fred  = new Employee
fred.name

//method overriding
class Person (val name: String = "") { override def toString = getClass.getName + "[name=" + name + "]" }
val fred = new Person("Fred")
fred.toString

//access superclass with keyword "super"
class Employee extends Person { val salary = 1000; override def toString = super.toString + "[salary=" + salary + "]" }
val fred = new Employee

//Type check and cast
val p = new Employee
if (p.isInstanceOf[Employee]) { val s = p.asInstanceOf[Employee]; s } //check if object belongs to a given class.
if (p.getClass == classOf[Employee]) { val w = p.asInstanceOf[Employee]; w } //refers to object but not a subclass.
//process using pattern-matching.
val p = new Person("Chad")
class Bird {}; val b = new Bird
def typeTest(p: Object) = {
	p match {
		case s: Person => println("Person name is: " + s.name) //process s as a Person.
		case _ => println("not a Person!") //p isn't an Person.
	}
}
typeTest(p); typeTest(b)

//abstract classes: class that cannot be instanciated.
abstract class Person(val name: String) { var id: Int /* abstract field. not instanciated. */ }
val roger = new Person //generate an error "cannot be instanciated".
```





