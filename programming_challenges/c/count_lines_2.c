#include <stdio.h>

main()
{
	int c, b, t, nl;

	b = 0;
	t = 0;
	nl = 0;
	while ((c = getchar()) != EOF)
	{
		if (c == '\n')
			++nl;
		if (c == ' ')
			++b;
		if (c == '\t')
			++t;
	}
	printf("newlines: %d\n", nl);
	printf("blanks: %d\n", b);
	printf("tabs: %d\n", t);
}
