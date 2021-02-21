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
