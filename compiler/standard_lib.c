// includes
#include <stdlib.h>
#include <stdarg.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/// Macros

// Return
#define std_return(value) return value;

// Create Scalar Values
#define std_scalar_create_stack(name, value, type)\
	type name = value;

#define std_scalar_create_heap(name, value, type)\
	type * name = (type*)malloc(sizeof(type));\
	memcpy(name, value, sizeof(type));

//remove from heap
#define std_free(var_name)\
	free(var_name);

// Create List
#define std_list_create(name, value, type) \
	type * name = (type*)malloc(sizeof(value));\
	memcpy(name, value, sizeof(value));

// Create Static List
#define std_list_static(name, array_size, type, contents...)\
	static type name[array_size] = {contents};

// Casts

#define std_cast_bool_string(name, value)\
	const char * name = (value) ? "true" : "false";

#define std_cast_string_int(name, value)\
	int name = atoi(value);

#define std_cast_int_string(name, value)\
	char name[28];\
	sprintf(name, "%i", value);

// Function calls
#define std_call_function_with_return(name, function, type,  arguments...)\
	type name = function(arguments);

#define std_call_function_no_return(function,  arguments...)\
	function(arguments);

// operations
#define std_math_operation(name, type, value_1, operation, value_2)\
	type name = value_1 operation value_2;

#define std_conditional_operation(name, value_1, operation, value_2)\
	bool name = value_1 operation value_2;

#define std_ternary_operation(name, value, result_1, result_2)\
	bool name = value ? result_1 : result_2;

#define std_string_format_operation(name, arg_count, arguments...)\
	char * name = std_format_string(arg_count, arguments);

// Scope
#define std_function_definition(inner, type, name, arguments...)\
	type name(arguments) {\
		inner\
	}

#define std_for(inner, itterator_declaration, itterator_condition, itterator_increment)\
	int itterator_declaration;\
	for(itterator_declaration; itterator_condition; itterator_increment) {\
		inner\
	}

#define std_while(inner, condition)\
	while(condition) {\
		inner\
	}

#define std_do_while(inner, condition)\
	do {\
		inner\
	} while(condition);

#define std_else_if(inner, condition)\
	else if(condition) {\
		inner\
	}

#define std_if(inner, condition)\
	if(condition) {\
		inner\
	}

#define std_else(inner)\
	else {\
		inner\
	}

// Functions

char * std_format_string(size_t num_of_args,...) {
	// va_list includes string parameters with their size
	// ex: "hello", 6, "hi", 3
	va_list valist;

	va_start(valist, num_of_args);
	int arg;
	std_list_create(ret_str, "", char);
	size_t ret_str_length = 0;
	for (arg = 0; arg < num_of_args; arg++) {
		char * current = va_arg(valist, char *);
		size_t current_str_length = strlen(current);
		ret_str_length += current_str_length;
		size_t alloc_len = (ret_str_length + current_str_length + 1);
		char * cat_cpy = (char*)malloc(alloc_len*sizeof(char));
		strcpy(cat_cpy, ret_str);
		strcat(cat_cpy, current);
		ret_str = (char*)realloc(cat_cpy, alloc_len*sizeof(char));
	}
	return ret_str;
}