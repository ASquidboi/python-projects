import zipfile

with zipfile.ZipFile("potential_bomb.zip", "w") as zf:
	i = 0
	while i < 1000:
		data = "A" * (1000**8)
		zf.writestr("file1.txt", data)
