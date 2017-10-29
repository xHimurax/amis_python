cell_ax = int(input())
cell_ay = int(input())
cell_bx = int(input())
cell_by = int(input())
if ((cell_ax + cell_ay) % 2) == ((cell_bx + cell_by) % 2):
	print('YES')
else:
	print('NO')
input()
