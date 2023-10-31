
from enum import Enum


class Scalar_Type(Enum):
	i32 = "int"
	u32 = "unsigned int"
	bool = "bool"
	str = "char *"
	char = "char"
	f32 = "float"
	variable = "variable"
	null = "NULL"

class Literal:
	# Literal's values are still strings for the sake of compilation to c code
	# but they maintain a type for casting, etc. purposes
	def __init__(self, raw:str) -> None:
		# Takes in raw code of a literal and creates an instance of the correct type
		if raw == "true" or raw == "false":# bool
			self.value_type = Scalar_Type.bool
			self.value = raw
		elif raw.startswith("\'") and raw.endswith("\'") and (len(raw) == 3 or len(raw) == 4):# char
			self.value_type = Scalar_Type.char
			self.value = raw
		elif raw.startswith("\"") and raw.endswith("\""):# str
			self.value_type = Scalar_Type.str
			self.value = raw
		elif raw.startswith("\'") and raw.endswith("\'"):# err
			# throw error: char cant be more than 1 character
			pass
		elif raw.isdecimal():# u32
			self.value_type = Scalar_Type.u32
			self.value = raw
		elif raw.startswith("-") and raw.lstrip("-").lstrip().isdecimal():# i32
			self.value_type = Scalar_Type.i32
			self.value = raw
		elif "." in raw and raw.replace(".", "").lstrip("-").isdecimal():# f32
			self.value_type = Scalar_Type.f32
			self.value = raw
		elif len(raw.split()) == 1 and raw.replace("_", "").isalnum():# variable
			self.value_type = Scalar_Type.variable
			self.value = raw
		else:
			self.value_type = Scalar_Type.null
			self.value = "NULL"
	
	def __repr__(self) -> str:
		return self.value
	
	def __str__(self) -> str:
		return self.value