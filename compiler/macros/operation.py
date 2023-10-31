from __future__ import annotations
from enum import Enum
from compiler.compiler_globals import numbered_prefixes, defined_function_types
from compiler.types import Literal, Scalar_Type


class OperationType(Enum):
	Return = "std_return"
	Create_Scalar_Stack = "std_scalar_create_stack"
	Create_Scalar_Heap = "std_scalar_create_heap"
	Free = "std_free"
	Create_List = "std_list_create"
	Create_List_Static = "std_list_static"
	Cast_Bool_String = "std_cast_bool_string"
	Cast_String_Int = "std_cast_string_int"
	Cast_Int_String = "std_cast_int_string"
	Call_Function_With_Return = "std_call_function_with_return"
	Call_Function_No_Return = "std_call_function_no_return"
	Math_Operation = "std_math_operation"
	Conditional_Operation = "std_conditional_operation"
	Ternary = "std_ternary_operation"
	Format_String = "std_string_format_operation"

# also includes functions
class Operation:
	def __init__(self, operation_type:OperationType, name:str = None, *args:Operation | Literal | str) -> None:
		self.prefixed_operations:list[Operation] = []
		self.frees:list[Operation] = []
		self.name = name
		self.type = operation_type
		self.args = list(args)
		self.special_argument_behavior()
		self.value_type = self.get_scalar_value_type()# this is the return type
		for stmt_arg_num, stmt_arg in enumerate(self.args):
			if isinstance(stmt_arg, Operation):
				self.handle_operation(stmt_arg_num, stmt_arg)
			else:
				pass
	
	def get_scalar_value_type(self) -> Scalar_Type:
		ret_type = Scalar_Type.null
		match self.type:
			case OperationType.Create_Scalar_Stack:
				ret_type = Scalar_Type(self.args[1])
			case OperationType.Create_Scalar_Heap:
				ret_type = Scalar_Type(self.args[1])
			case OperationType.Create_List:
				ret_type = Scalar_Type(self.args[1])
			case OperationType.Create_List_Static:
				ret_type = Scalar_Type(self.args[1])
			case OperationType.Cast_Bool_String:
				ret_type = Scalar_Type.str
			case OperationType.Cast_String_Int:
				ret_type = Scalar_Type.i32
			case OperationType.Cast_Int_String:
				ret_type = Scalar_Type.str
			case OperationType.Call_Function_With_Return:
				ret_type = defined_function_types[self.args[1]]
			case OperationType.Math_Operation:
				ret_type = Scalar_Type(self.args[0])
			case OperationType.Conditional_Operation:
				ret_type = Scalar_Type.bool
			case OperationType.Ternary:
				ret_type = Scalar_Type.bool
			case OperationType.Format_String:
				ret_type = Scalar_Type.str
		return ret_type

	def handle_operation(self, stmt_arg_num: int, stmt_arg: Operation):

		if self.args[stmt_arg_num].type.value in numbered_prefixes.keys():
			numbered_prefixes[self.args[stmt_arg_num].type.value] += 1
		else:
			numbered_prefixes[self.args[stmt_arg_num].type.value] = 1


		# place the argument macro before the current operation
		self.args[stmt_arg_num].name = f"{self.args[stmt_arg_num].type.value}_{numbered_prefixes[self.args[stmt_arg_num].type.value]}"

		# Determine if inline data needs to be freed: 
		match self.args[stmt_arg_num].type:
			case OperationType.Format_String:
				self.frees.append(Operation(OperationType.Free, None, Literal(self.args[stmt_arg_num].name)))
		
		self.prefixed_operations.append(self.args[stmt_arg_num])
		
		self.args[stmt_arg_num] = Literal(self.args[stmt_arg_num].name)
		

	def special_argument_behavior(self):
		# check own type to see how arguments should be handled
		for stmt_arg_num, stmt_arg in enumerate(self.args):
			if not isinstance(stmt_arg, str):
				match self.type:
					case OperationType.Format_String:
						match self.args[stmt_arg_num].value_type:
							case Scalar_Type.i32:
								# wrap the current argument in a cast from i32 to str
								self.args[stmt_arg_num] = Operation(OperationType.Cast_Int_String, None, self.args[stmt_arg_num])

							case Scalar_Type.bool:
								# wrap the current argument in a cast from bool to str
								self.args[stmt_arg_num] = Operation(OperationType.Cast_Bool_String, None, self.args[stmt_arg_num])


	def render(self) -> str:
		# render prefix operations first
		prefix_str = ""
		for op in self.prefixed_operations:
			prefix_str += op.render()

		ret_str = f'{prefix_str}{self.type.value}({f"{self.name}," if self.name != None else ""}'
		ret_str += ",".join([str(arg) for arg in self.args])
		ret_str += ")"
		for free in self.frees:
			ret_str += free.render()
		return ret_str