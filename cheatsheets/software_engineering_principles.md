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
* CLEAN code (Cohesive, Loosely Coupled, Encapsulated, Assertive, Non-redundant code.)
* CUPID (Composable, UNIX philosophy, Predictable, Idiomatic, Domain-based.) (<https://cupid.dev/>)
* DOTDIW (do one thing, do it well.)
* POGE.
* RTFM.
* TDD/unit tests.
* LINT. ("Lint early, lint often." - Expert C Programming book)
* Security / DevSecOps. (Bandit, Vulture, Sonarqube, Splint,... Secrets Management.)
* MECE.
* DRY/WET/OAOO (Dont repeat yourself, Write everything twice, once and only once.)
* KISS (Keep it short and simple).
* Syntactic Consistency principle. (cf. McLennan Programming Principles book)
* Follow conventions where possible (ISO, OpenAPI, Avro specs,...)
* Boy-Scout Rule (Leave code base in better state than when you arrived.)
* Docs as code. (<https://www.writethedocs.org/guide/docs-as-code/>)
* UNIX Philosophy:
    * Modularity (=> correct usage of functions)
    * Readability (Write code that reads easily.)
    * Extensability
    * KISS programs
    * Prototype ASAP
    * Portability over Efficiency
    * Store data in text files
    * Every program is a filter
* Symmetry
* RERO / TETO / CECO / LELO / CECO2 (release, test, commit, lint, comment,...)
* SPOT (single point of truth) (== DRY)
* Developers Time >> Machines Time >> Machines Space.
* 

## Practice
* Top-Down Design (reqs > docs (HLD+LLD/Design Docs(function type signature)) > comments > function type signatures > tests > code logic.)
* Coding Pyramid/Pillars (from top to bottom)
    * Code Optimization
        * idiomatic code ("Pythonic code"))
        * programming language specific optimizations
        * fast track/path
        * fail fast and loud
        * defensive programming / guard clauses
        * add error handling
    * Algorithmic Complexity (DSA) (time and space complexity)
    * Clean Code (data typing (mypy), meaningful comments, improve readability,...) (remove dead code/comments/tests/imports/artifacts.)
    * Pipeline
        * docs
        * lint
        * tests (TDD/RGR, Testing Pyramid, Test Coverage,...)
        * CVS (git+hooks)
        * CICD (make)(automated build)
        * logs
        * DevSecOps (bandit,vulture,sonarqube. secrets.)
* Testing Pyramid
* Test Coverage
* Data Generation (Faker)
* MADRs (<https://adr.github.io/>) (<https://github.com/npryce/adr-tools>)
* Linting (<https://github.com/super-linter/super-linter>)
* Fuzzing (radamsa)
* Red-Green-Refactor / Arrange-Act-Assert.
* Guard Clauses / Defensive Programming (IFs at start of functions | IF Not A: PRINT, RETURN.)
* Close your files. (python WITH statement)
* edge cases for testing
* dependency management (python poetry, java maven, scala sbt,...)
* Good Functions/Methods/Classes:
    * explicit: reveals intention and behavior. (e.g. explicit return type in Python: f(x) -> Int: ...)
    * DOTDIW
    * one level of abstraction per function.
    * no side effects.
    * SRP (in SOLID)
    * Rule of 30 ()


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
* The Algorithms (<https://the-algorithms.com/>) (<https://github.com/TheAlgorithms>)
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
* pro/g/ramming challenges.
* TIOBE index (<https://www.tiobe.com/tiobe-index/>)
* Ruby Koans (<https://www.rubykoans.com/>)
* Awesome System Design (<https://github.com/alexpate/awesome-design-systems>)
* Awesome of Awesome (<https://github.com/sindresorhus/awesome>)
* TAOUP (<http://www.catb.org/esr/writings/taoup/html/>)
* Master Foo teachings: The Unix Koans of Master Foo "Rootless Root" (<http://www.catb.org/esr/writings/taoup/html/unix_koans.html>)
