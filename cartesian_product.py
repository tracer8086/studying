def cartesian_product(*sets):
	source, res = "", []

	for indent in range(len(sets)):
		source += " " * (4 * indent) + "for elem{0} in sets[{0}]:\n".format(indent)

	source += " " * (4 * (indent + 1)) + "res.append((" + ", ".join(["elem" + str(x) for x in range(indent + 1)]) + "))"
	exec(source)

	return res
