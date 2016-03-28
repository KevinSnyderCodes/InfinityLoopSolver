# Infinity Loop Solver, by Kevin Snyder
# VERSION: 0.1

import sys

# B: Blank
# 0: One side
# 1: Two sides (straight)
# 2: Two sides (curved)
# 3: Three sides
# 4: Four sides
def processFile(boardFile):
	board = []
	for line in boardFile:
		row = [x for x in line.strip().split()]
		board.append(row)
	return board

# Orientation uses N, S, E, W (compass directions) and X (undetermined)
# 0: Open end
# 1: Open end
# 2: N means left and top ends are open
# 3: Middle open end faces N
# 4: Always N
def solvePuzzle(board):
	orientation = [[["N","S","W","E"] for piece in row] for row in board]
	# Keep running through board until solved
	unsolved = True
	while unsolved:
		unsolved = False
		for i in range(len(board)):
			for j in range(len(board[i])):
				if len(orientation[i][j]) > 1:
					unsolved = True
					# Insert default N's
					if board[i][j] == "B" or board[i][j] == "4":
						orientation[i][j] = ["N"]
					# Check available compass directions
					else:
						final = {
							"N": False,
							"S": False,
							"W": False,
							"E": False
						}
						if "N" in orientation[i][j]:
							if i-1 < 0 or board[i-1][j] == "B":
								orientation[i][j].remove("N")
							else:
								if board[i-1][j] == "0":
									if all(n not in orientation[i-1][j] for n in ["S"]):
										orientation[i][j].remove("N")
									elif len(orientation[i-1][j]) == 1:
										final["N"] = True
								elif board[i-1][j] == "1":
									if all(n not in orientation[i-1][j] for n in ["N", "S"]):
										orientation[i][j].remove("N")
									elif len(orientation[i-1][j]) == 1:
										final["N"] = True
								elif board[i-1][j] == "2":
									if all(n not in orientation[i-1][j] for n in ["S", "W"]):
										orientation[i][j].remove("N")
									elif len(orientation[i-1][j]) == 1:
										final["N"] = True
								elif board[i-1][j] == "3":
									if all(n not in orientation[i-1][j] for n in ["E", "S", "W"]):
										orientation[i][j].remove("N")
									elif len(orientation[i-1][j]) == 1:
										final["N"] = True
								elif board[i-1][j] == "4":
									final["N"] = True
						if "S" in orientation[i][j]:
							if i+1 >= len(board) or board[i+1][j] == "B":
								orientation[i][j].remove("S")
							else:
								if board[i+1][j] == "0":
									if all(n not in orientation[i+1][j] for n in ["N"]):
										orientation[i][j].remove("S")
									elif len(orientation[i+1][j]) == 1:
										final["S"] = True
								elif board[i+1][j] == "1":
									if all(n not in orientation[i+1][j] for n in ["N", "S"]):
										orientation[i][j].remove("S")
									elif len(orientation[i+1][j]) == 1:
										final["S"] = True
								elif board[i+1][j] == "2":
									if all(n not in orientation[i+1][j] for n in ["N", "E"]):
										orientation[i][j].remove("S")
									elif len(orientation[i+1][j]) == 1:
										final["S"] = True
								elif board[i+1][j] == "3":
									if all(n not in orientation[i+1][j] for n in ["W", "N", "E"]):
										orientation[i][j].remove("S")
									elif len(orientation[i+1][j]) == 1:
										final["S"] = True
								elif board[i+1][j] == "4":
									final["S"] = True
						if "W" in orientation[i][j]:
							if j-1 < 0 or board[i][j-1] == "B":
								orientation[i][j].remove("W")
							else:
								if board[i][j-1] == "0":
									if all(n not in orientation[i][j-1] for n in ["E"]):
										orientation[i][j].remove("W")
									elif len(orientation[i][j-1]) == 1:
										final["W"] = True
								elif board[i][j-1] == "1":
									if all(n not in orientation[i][j-1] for n in ["W", "E"]):
										orientation[i][j].remove("W")
									elif len(orientation[i][j-1]) == 1:
										final["W"] = True
								elif board[i][j-1] == "2":
									if all(n not in orientation[i][j-1] for n in ["E", "S"]):
										orientation[i][j].remove("W")
									elif len(orientation[i][j-1]) == 1:
										final["W"] = True
								elif board[i][j-1] == "3":
									if all(n not in orientation[i][j-1] for n in ["N", "E", "S"]):
										orientation[i][j].remove("W")
									elif len(orientation[i][j-1]) == 1:
										final["W"] = True
								elif board[i][j-1] == "4":
									final["W"] = True
						if "E" in orientation[i][j]:
							if j+1 >= len(board[i]) or board[i][j+1] == "B":
								orientation[i][j].remove("E")
							else:
								if board[i][j+1] == "0":
									if all(n not in orientation[i][j+1] for n in ["W"]):
										orientation[i][j].remove("E")
									elif len(orientation[i][j+1]) == 1:
										final["E"] = True
								elif board[i][j+1] == "1":
									if all(n not in orientation[i][j+1] for n in ["W", "E"]):
										orientation[i][j].remove("E")
									elif len(orientation[i][j+1]) == 1:
										final["E"] = True
								elif board[i][j+1] == "2":
									if all(n not in orientation[i][j+1] for n in ["W", "N"]):
										orientation[i][j].remove("E")
									elif len(orientation[i][j+1]) == 1:
										final["E"] = True
								elif board[i][j+1] == "3":
									if all(n not in orientation[i][j+1] for n in ["S", "W", "N"]):
										orientation[i][j].remove("E")
									elif len(orientation[i][j+1]) == 1:
										final["E"] = True
								elif board[i][j+1] == "4":
									final["E"] = True
						# DEBUGGING ONLY
						# print(i, ",", j, ": ", board[i][j], orientation[i][j], final)
						# Set orientation, if possible
						if board[i][j] == "0":
							for key, val in final.items():
								if val == True:
									orientation[i][j] = [key]
						if board[i][j] == "1":
							if len(orientation[i][j]) in [2, 3]:
								if all(n in orientation[i][j] for n in ["N", "S"]):
									orientation[i][j] = ["N"]
								if all(n in orientation[i][j] for n in ["W", "E"]):
									orientation[i][j] = ["W"]
							else:
								for key, val in final.items():
									if val == True:
										orientation[i][j] = [key]
						elif board[i][j] == "2":
							if len(orientation[i][j]) == 2:
								if all(n in orientation[i][j] for n in ["N", "E"]):
									orientation[i][j] = ["E"]
								if all(n in orientation[i][j] for n in ["E", "S"]):
									orientation[i][j] = ["S"]
								if all(n in orientation[i][j] for n in ["S", "W"]):
									orientation[i][j] = ["W"]
								if all(n in orientation[i][j] for n in ["W", "N"]):
									orientation[i][j] = ["N"]
							elif len(orientation[i][j]) > 2:
								o = []
								for key, val in final.items():
									if val == True:
										o.append(key)
								if len(o) == 2:
									if all(n in o for n in ["N", "E"]):
										orientation[i][j] = ["E"]
									if all(n in o for n in ["E", "S"]):
										orientation[i][j] = ["S"]
									if all(n in o for n in ["S", "W"]):
										orientation[i][j] = ["W"]
									if all(n in o for n in ["W", "N"]):
										orientation[i][j] = ["N"]
								elif len(o) == 1:
									if "N" in o:
										if "E" not in orientation[i][j]:
											orientation[i][j] = ["N"]
										elif "W" not in orientation[i][j]:
											orientation[i][j] = ["E"]
									if "S" in o:
										if "E" not in orientation[i][j]:
											orientation[i][j] = ["W"]
										elif "W" not in orientation[i][j]:
											orientation[i][j] = ["S"]
									if "W" in o:
										if "N" not in orientation[i][j]:
											orientation[i][j] = ["W"]
										elif "S" not in orientation[i][j]:
											orientation[i][j] = ["N"]
									if "E" in o:
										if "N" not in orientation[i][j]:
											orientation[i][j] = ["S"]
										elif "S" not in orientation[i][j]:
											orientation[i][j] = ["E"]
						elif board[i][j] == "3":
							if len(orientation[i][j]) == 3:
								if "N" not in orientation[i][j]:
									orientation[i][j] = ["S"]
								elif "S" not in orientation[i][j]:
									orientation[i][j] = ["N"]
								elif "W" not in orientation[i][j]:
									orientation[i][j] = ["E"]
								elif "E" not in orientation[i][j]:
									orientation[i][j] = ["W"]
							elif len(orientation[i][j]) > 3:
								o = []
								for key, val in final.items():
									if val == True:
										o.append(key)
								if len(o) == 3:
									if "N" not in o:
										orientation[i][j] = ["S"]
									elif "S" not in o:
										orientation[i][j] = ["N"]
									elif "W" not in o:
										orientation[i][j] = ["E"]
									elif "E" not in o:
										orientation[i][j] = ["W"]
		# DEBUGGING ONLY
		# for row in orientation:
		# 	print(row)
		# input()
	return orientation


# def fixEdges(board, final):


boardFile = open(sys.argv[1])

board = processFile(boardFile)

orientation = solvePuzzle(board)

for row in orientation:
	print(row)