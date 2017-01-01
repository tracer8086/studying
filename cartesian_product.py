def cartesian_product(*sets):
	function_code, res = "", []

	for indent in range(len(sets)):
		function_code += " " * (4 * indent) + "for elem{0} in sets[{0}]:\n".format(indent)

	function_code += " " * (4 * (indent + 1)) + "res.append((" + ", ".join(["elem" + str(x) for x in range(indent + 1)]) + "))"
	exec(function_code)

	return res
