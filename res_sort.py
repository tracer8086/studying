#returns sorted list based on several sorted lists of arbitrary length
def res_sort(*arrs):
	inds = [0 for i in range(len(arrs))]
	res, current = [], [0, 0]
	minimal = arrs[0][0]
	res_len = sum([len(a) for a in arrs])

	for n in range(len(arrs)):
		if arrs[n][0] <= minimal:
			minimal = arrs[n][0]
			current[0] = n
			current[1] = 0

	inds[current[0]] = -1 if len(arrs[current[0]]) == 1 else 1
	res.append(minimal)

	while len(res) < res_len:
		for n in range(len(arrs)):
			if inds[n] > 0:
				minimal = arrs[n][inds[n]]
				break

		for n in range(len(arrs)):
			if inds[n] >= 0 and arrs[n][inds[n]] <= minimal:
				minimal = arrs[n][inds[n]]
				current[0] = n
				current[1] = inds[n]

		if len(arrs[current[0]]) - 1 == current[1]:
			inds[current[0]] = -1
		else:
			inds[current[0]] += 1

		res.append(minimal)

	return res
