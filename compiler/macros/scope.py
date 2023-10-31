from __future__ import annotations

from enum import Enum
from compiler.macros import Operation
from compiler.compiler_globals import numbered_prefixes, defined_function_types


class Scope_Type(Enum):
	Function = "std_function_definition"
	For = "std_for"
	While = "std_while"
	Do_While = "std_do_while"
	If = "std_if"
	Else_If = "std_else_if"
	Else = "std_else"


class Scope:
	def __init__(self, type:Scope_Type, statement_args:list[str | Operation], *scope_args:Scope | Operation) -> None:
		self.prefixed_operations:list[Operation] = []
		self.type = type
		self.statement_args = statement_args
		self.scope_args = list(scope_args)
		if self.type == Scope_Type.Function:
			defined_function_types[self.statement_args[1]] = self.statement_args[0]
		for stmt_arg_num, stmt_arg in enumerate(self.statement_args):
			if isinstance(stmt_arg, Operation):
				if self.type.value in numbered_prefixes.keys():
					numbered_prefixes[stmt_arg.type.value] += 1
				else:
					numbered_prefixes[stmt_arg.type.value] = 1
				
				self.statement_args[stmt_arg_num].name = f"{stmt_arg.type.value}_{numbered_prefixes[stmt_arg.type.value]}"
				self.prefixed_operations.append(self.statement_args[stmt_arg_num])
				self.statement_args[stmt_arg_num] = self.statement_args[stmt_arg_num].name
			else:
				pass


	def render(self) -> str:
		# render prefix operations first
		prefix_str = ""
		for op in self.prefixed_operations:
			prefix_str += op.render()

		ret_str = f"{prefix_str}{self.type.value}("
		for scope_arg in self.scope_args:
			ret_str += scope_arg.render()
		ret_str += ","
		ret_str += ",".join(self.statement_args)
		ret_str += ")"
		return ret_str
