//http://www.careercup.com/question?id=5175660836290560
#include <stdio.h>
#include <string.h>

int max_length_of_strings(int m, int n, char str[m][n])
{
	int max = 0;
	for  (int i = 0; i < m; i++)
	{
		int len = strlen(str[i]);
		if (len > max)
		{
			max = len;
		}
	}
	return max;
}

void convert(int m, int n, char str[m][n])
{
	int max = max_length_of_strings(m, n, str);
	for (int i = 0; i < max; i ++)
	{
		for (int j = 0; j < m; j++)
		{
			int len = strlen (str[j]);
			if (i < len)
			{
				printf("%c ",str[j][i]);
			}
			else
			{
				printf("  ");
			}
		}
		printf("\n");
	}
}

int main(int argc, char *argv[])
{
	int m = 4;
	int n = 25;
	char str[m][n];
	strcpy(str[0], "I AM SO COOOOOOLL");
	strcpy(str[1], "Of course I am :)");
	strcpy(str[2], "TESTTTTINGGG");
	
	convert(m, n, str);
    return 0;
}
