from compiler import Program
from compiler.macros import Operation, Scope, OperationType, Scope_Type
from compiler.types import Literal

my_program = Program("")

my_program.nodes = [
	Scope(Scope_Type.Function, ["int", "main", "int argc", "char const *argv[]"],
		Operation(OperationType.Call_Function_No_Return, None, "puts",
			Operation(OperationType.Format_String, None, "3", 
				"\"five plus five equals: \"",
				Operation(OperationType.Math_Operation, None, "int", Literal("5"), "+", Literal("5")),
				"\"!\""
			)
		),
		Operation(OperationType.Return, None, "0")
	)
]

print(my_program.render())

my_program.compile()