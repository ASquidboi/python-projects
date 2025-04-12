import zipfile

with zipfile.ZipFile("potential_bomb.zip", "w") as zf:
	data = "A" + (10**8)
	zf.writestr("file1.txt", data)
