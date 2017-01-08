arr1 = ['п', 'ф', 'к', 'т', 'ш', 'с', 'х', 'ц', 'ч', 'щ']
arr2 = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'л', 'м', 'н', 'р']
arr3 = ['м', 'н', 'л', 'р']
arr4 = ['а', 'о', 'у', 'и', 'э', 'ы']

chart = input("Please enter a sequence of numbers from 1 to 4: ")
source, res = "", []

for indent in range(len(chart)):
	source += " " * (4 * indent) + "for elem{0} in arr{1}:".format(indent, int(chart[indent])) + "\n"

res_pattern = "(" + ", ".join(["elem" + str(x) for x in range(indent + 1)]) + ")"

source += " " * (4 * (indent + 1)) + "res.append(" + res_pattern + ")"

exec(source)

for sequence in res:
	print(sequence) 
