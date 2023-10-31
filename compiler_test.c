#include <stdlib.h>
#include <stdarg.h>
#include <stdio.h>
#include <string.h>
#include "compiler/standard_lib.c"
int main(int argc, char const *argv[])
{
	int std_math_operation_1 = 5 + 5;
	char std_cast_int_string_1[28];
	sprintf(std_cast_int_string_1, "%i", std_math_operation_1);
	char *std_string_format_operation_1 = std_format_string(3, "five plus five equals: ", std_cast_int_string_1, "!");
	puts(std_string_format_operation_1);
	free(std_string_format_operation_1);
	int std_math_operation_2 = 2 + 5;
	char std_cast_int_string_2[28];
	sprintf(std_cast_int_string_2, "%i", std_math_operation_2);
	char *std_string_format_operation_2 = std_format_string(3, "two plus five equals: ", std_cast_int_string_2, "!");
	puts(std_string_format_operation_2);
	free(std_string_format_operation_2);
	return 0;
}