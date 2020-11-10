#K&R ISO C Book Notes:
=> gcc -ansi -pedantic -Wall -Werror -Wextra
- variable types:
	external/global. (init = zero.)
	automatic/local. (init = undefined.)
	static. (init = zero.)
	register. (init = undefined.)
- variable definition vs declaration (int c;) vs initialization (int low = 0;) vs assignment (low =0;).
- variable scope: extern int sp;.
	tip: avoid naming variables the same way in and out of scope. (p.85)
- static: (not visible to other files.)
	variable: static int bufp = 0;
	function: ???
- register variables: tells the compiler the variable will be heavily used.
	register int x;
	f(register unsigned m){...}
- avoid using too much global variable. (it breaks modularity.)
- arguments: call by reference vs call by value.
- file inclusion (include):
	#include <stdio.h>
	#include "calc.h"
- define: expands as in-line code.
	#define MAXVAL 100
	#define max(A,B)	((A)>(B)?(A):(B))
	note: careful of side effects, multiple evaluations and order of operations.
	#undef getchar //to ensure a routine is a function and not a macro.
- conditional inclusion:
	#if
	#elif //else if.
	#else
	#endif //end of if.
	#ifdef //if defined.
	#ifndef //if not defined.
- main
- printf / scanf
- variable. (all lowercase.)
- data types (char, (short, long) int, float, (long) double.) (signed vs unsigned.)
	type conversion. => implicit conversion.
	truncation.
	type coercion. => "cast(ing)". implicit casting via function calls.
- arithmetic expression
- loop.
	while (expression)
		statement
	
	for (expr1 ; expr2 ; expr3)
		statement
	
	/!\ comma operator/expression -> guarantee left-to-right evaluation. /!\

	do
		statement
	while (expression);

	break; //only exits from the innermost loop.
	
	continue; //only for loops, not 'switch' (unlike 'break;'.).

	goto and labels. //scope = same function.
	goto error;
	error:
		statement

- symbolic constant. (all uppercase.)
- cc main.c getline.c strindex.c
- cc main.c getline.o strindex.o
- comments.
- I/O: getchar() / putchar().
- increment/drecement. (++i/--i)
- null statement.(;)
- condition.
	if (expression)
		statement
	else if (expression)
		statement
	<...>
	else
		statement

	switch (expression) {		/!\ fall-throughs /!\
		case const-expr: statements (break;)
		<...>
		default: statements (break;)
	}
- boolean expression. (A == B, A != B, A || B,...)
- functions.
	return-type function-name (argument declarations)
	{
		declarations;
		statements;
		return expression;
	}
	
	tip: use <void> in function without arguments. (p.72)
	note: functions are global by default. Use static if needed.
- arrays and character arrays.
- operators vs statements vs expressions.
	arithmetic operators (+-*/%)
	logical operators (< <= > >= == != && ||)
	=> operators precedence and associativity. (see Table 2-1, page 53.)
	unary negation operator.
	cast operator.
	increment and decrement operator. (difference between ++i and i++.)
	bitwise operators (6: & | ^ << >> ~)
	assignment operators (10: expr1 op = expr2 | for arithmetic and bitwise operators.)
- reserved keywords. (all lowercase.)
- decimal (31) vs octal (037) vs hexadecimal (0x1f).
- ASCII character set and escape sequences (\n \r \t \\ ...).
- string constant/string literal. ("hello world")
- enumeration constant. (enum boolean {NO, YES};)
- const qualifier. (const char[];)
- pointer := variable that contains the address of a variable.
	& applies only to variables and array elements.
	* unary indirection/deferencing operator.
	p = &c; //assigns address of c to p.
	int x = 1, y = 2;
	int *ip;	//ip is a pointer.
	ip = &x;	//ip now points to x.
	y = *ip;	//y is now 1. copies the value of x into y.
	*ip = 0;	//x is now 0.
	
	*p++ = val; //push val onto stack.
	val = *--p; //pop stack into val.
- array: difference with a pointer: an array is not a variable. (i.e. no a=pa or a++.)
	the array name *is* the address of the zeroth element.
- pointer/address arithmetic:
	p++; //increments to point 1 element beyond actual.
	p += i; //increments to point i elements beyond actual.
	0 is *never* a valid address for data. Therefore used to return abnomalies.
	comparison is valid for pointers of the same array. (with one exception, see p.103.)
	all the pointer manipulations automatically take into account the size of the object pointed to.
	valid operations:
		assignment of pointers of same type;
		adding/substracting a pointer and an integer;
		substracting/comparing two pointers of the same array;
		assigning/comparing to zero.
- structure: collection of one or more variables under a single name.
	struct point {
		int x;
		int y;
	} x, y, z; //if mentionned, reserve storage. else, not.
	"point" is called a "structure tag".
	"x" and "y" are called "structure members".
	struct point maxpt = {320, 200};
	structure can be nested.
	struct rect {
		struct point pt1;
		struct point pt2;
	};
	struct key {
		char *word;
		int count;
	} keytab[NKEYS] = {
		"auto", 0,
		"break", 0,
		/* ... */
		"while", 0
	}; //declares an array of structures.
- typdefs: creates new data types names (but only based on existing ones).
	2 reasons:
		parametrize against protability issues.
		to provide better documentation.
- union: similar to a struct holding widest value size.
- bit-field / field. Similar syntax as structs.

