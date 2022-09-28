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





##SCALA BASICS:
values, variables and types (Unit == no return)
expressions
code block (result = result last expression)
functions
type inference
(tail) recursion (factorial example)
	call-by-name and call-by-value
	default and named arguments
	smart operations on strings

##OOP:
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

##Functional:
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

##Scala Best Practices:
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



##Scala Performance:
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



