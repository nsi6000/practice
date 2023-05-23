# Software Engineering Principles

## Principles
* Immutability (no side effects)
* Orthogonality (no side effects) (e.g. TV buttons sound and channels impacting each others.)
* Idempotency
* Composability (talk in files) (cf. TAOUP)
* Compactness (simple mental model) ("Formalization is better than heuristics.")
* Transparency (== compactness + predictable)
* Regularity (no special cases) (cf. Linus Torvalds TED talk Linked List example)
* Modularity (simple parts, clean interface)
* Representation (complex data structures, simple code) (cf. TAOUP)

## Practice
* Top-Down Design (reqs > docs (HLD+LLD/Design Docs(function type signature)) > comments > function type signatures > tests > code logic.)
* Testing Pyramid
* Test Coverage
* Data Generation (Faker)
* MADRs (<https://adr.github.io/>) (<https://github.com/npryce/adr-tools>)
* Linting (<https://github.com/super-linter/super-linter>)
* Fuzzing (radamsa)
* CICD
* Red-Green-Refactor / Arrange-Act-Assert.
* Guard Clauses
* Close your files. (python WITH statement)
* edge cases for testing
* dependency management (python poetry, java maven, scala sbt,...)
* Good Functions/Methods/Classes:
- explicit: reveals intention and behavior.
- DOTDIW
- one level of abstraction per function.
- no side effects.
- SRP (in SOLID)
- Rule of 30 ()


## Random stuff
* vimtutorial
* gittutorial
* BLIND75 (<https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions>)
* GRIND75 (<https://www.techinterviewhandbook.org/grind75>)
* NEETCODE150 (<https://neetcode.io/>)
* AlgoExpert (170) (<https://www.algoexpert.io/product>)
* Sean Prashad (171) (<https://seanprashad.com/leetcode-patterns/>)
* EPI Judge (<https://github.com/adnanaziz/EPIJudge>)
* Big O Cheatsheet (<https://www.bigocheatsheet.com/>)
* The Algorithms (<https://the-algorithms.com/>)
* Fast Inverse Square Root for Quake III (FISR) (<https://www.youtube.com/watch?v=p8u_k2LIZyo>)
* Hyperpolyglot (<https://hyperpolyglot.org/>)
* Refactoring Guru (<https://refactoring.guru/design-patterns/java>)
* Java Design Patterns (<https://java-design-patterns.com/>)
* Fork bomb (<https://en.wikipedia.org/wiki/Fork_bomb>)
* List of Public APIs (<https://github.com/public-apis/public-apis>)
* Scala Exercises (<https://www.scala-exercises.org/>)
* Twitter Scala School (<https://twitter.github.io/scala_school/>)
* Tour of Scala (<https://docs.scala-lang.org/tour/tour-of-scala.html>)
* Developer Roadmap (<https://github.com/kamranahmedse/developer-roadmap>) (<https://roadmap.sh/>)
* Donne Martin System Design Primer (<https://github.com/donnemartin/system-design-primer>)
* Yandere Technique (anti-pattern)
* FizzBuzz EE
* Foolean
* Subteranean Elves
* TIOBE index (<https://www.tiobe.com/tiobe-index/>)
* Ruby Koans (<https://www.rubykoans.com/>)
* Awesome System Design (<https://github.com/alexpate/awesome-design-systems>)
* Awesome of Awesome (<https://github.com/sindresorhus/awesome>)
* TAOUP (<http://www.catb.org/esr/writings/taoup/html/>)
* Master Foo teachings: The Unix Koans of Master Foo "Rootless Root" (<http://www.catb.org/esr/writings/taoup/html/unix_koans.html>)