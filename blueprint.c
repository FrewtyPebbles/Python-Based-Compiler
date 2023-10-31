/*
# this is a comment
# programming language
# the entire file is the main function

// data is freed at the end of its scope
	// ex:
	{
		data1 created here!
		...
		do some stuff
		{
			data2 created here!
			still doing some stuff
			data2 freed here!
		}
		...
		data1 is freed here!
	}
	

# module: ./lib/test_import.spk

fn mod_test(arg:str):int[] {
	print(f"your arg is {arg}!");
	return [1,2,3];
}

print("The test import has been imported");

# end module: test_import.spk

# module: main.spk

imp lib.test_import as ti;

fn give_int(arg:int):bool {
	ti.mod_test(f"the integer of {arg} plus 1 which equals {arg + 1}");
	if arg < 1 {
		return true;
	}
	else {
		return false;
	}
}

print(f"give_int returned {STR(give_int(INT(cli_args[1])))}");

# end module: main.spk
*/

///////// Compiled C program
// note: Code will be unformatted in actual compilation

// includes
#include <stdlib.h>
#include <stdarg.h>
#include <stdio.h>
#include <string.h>

#include "compiler/standard_lib.c"

// program

// detects that return value is a literal and makes it a constant return type
std_function_definition(
	std_string_format_operation(std_format_1, 3, "your arg is ", arg, "!")
	std_call_function_no_return(puts, std_format_1)
	std_call_function_no_return(free, std_format_1)
	std_list_static(std_array_literal_1, 3, int, 0, 1, 2)
	std_return(std_array_literal_1),
	const int *,
	ti_mod_test,
	char * arg
)
std_function_definition(
	std_cast_int_string(std_format_2_arg_2, arg)
	std_math_operation(std_add_1, int, arg, +, 1)
	std_cast_int_string(std_format_2_arg_4, std_add_1)
	std_string_format_operation(std_format_2, 4, "the integer of ", std_format_2_arg_2, " plus 1 which equals ", std_format_2_arg_4)
	std_call_function_no_return(ti_mod_test, std_format_2)
	std_conditional_operation(std_conditional_operation_1, arg, <, 1)
	std_if(
		std_call_function_no_return(free, std_format_2)
		std_return(true),
		std_conditional_operation_1
	)
	std_else(
		std_call_function_no_return(free, std_format_2)
		std_return(false)
	),
	bool,
	give_int,
	int arg
)
std_function_definition(
	std_call_function_no_return(puts, "The test import has been imported")
	// format_1 means its the first time format has been called in the program
	std_cast_string_int(std_give_int_arg_1, argv[1])
	std_call_function_with_return(std_give_int_result, give_int, bool, std_give_int_arg_1)
	std_cast_bool_string(std_format_3_arg_2, std_give_int_result)
	std_string_format_operation(std_format_3, 2, "give_int returned ", std_format_3_arg_2)
	std_call_function_no_return(puts, std_format_3)
	std_call_function_no_return(free, std_format_3)
	std_return(0),
	int,
	main,
	int argc,
	char const *argv[]
)