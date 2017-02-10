import base64
def read():
	score = []
	with open("score.bin", "r") as f:
		a = f.readline()
		b = base64.b64decode(a).split()
		score.append((b[0], b[1]))
	print(score)