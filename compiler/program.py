from compiler.macros import Operation, Scope
from subprocess import Popen, PIPE, STDOUT

class Program:
	def __init__(self, code:str) -> None:
		self.code = code
		self.nodes:list[Scope] = []
	
	def render(self) -> str:
		ret_str = '#include <stdlib.h>\n#include <stdarg.h>\n#include <stdio.h>\n#include <string.h>\n#include "compiler/standard_lib.c"\n'
		for node in self.nodes:
			ret_str += node.render()
		
		return ret_str

	def compile(self):
		p = Popen(['gcc', '-x', 'c', '-o', 'compiler_test', '-'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
		stdout_data = p.communicate(input=self.render().encode())[1]
		p.wait()
		print(stdout_data.decode())