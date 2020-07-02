#include <stdio.h>

main()
{
	int c;

	c = getchar();
	printf("%d\n", c != EOF);

	int d;

	d = EOF;
	printf("%d\n", d != EOF);

	printf("%3d\n", EOF);
}


