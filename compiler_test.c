#include <stdarg.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "compiler/standard_lib.c"
std_function_definition(
	std_math_operation(std_math_operation_1,int,5,+,5)
	std_cast_int_string(std_cast_int_string_1,std_math_operation_1)
	std_string_format_operation(std_string_format_operation_1,3,"five plus five equals: ",std_cast_int_string_1,"!")
	std_call_function_no_return(puts,std_string_format_operation_1)
	std_free(std_string_format_operation_1)
	std_return(0),
	int,
	main,
	int argc,
	char const *argv[]
)