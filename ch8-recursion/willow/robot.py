def navigate(grid):
	"""
	A grid is a 2D list of 1s and 0s.
	0s are impassable blocks, 1s are viable paths.
	Don't pass grids with different lengths of rows plz :D
	"""
	return explore(0,0,grid,[]) or "Unnavigable :|"

def explore(robot_x, robot_y, grid, path):
	if robot_y == len(grid) -1 and robot_x == len(grid[0]) - 1:
		return path

	if robot_y <= len(grid) -2 and grid[robot_y + 1][robot_x]:
		my_path = path[0:]
		my_path.append("DOWN")
		# Avoid returning None if going right would work.
		going_down = explore(robot_x, robot_y + 1, grid, path=my_path)
		if going_down:
			return going_down

	if robot_x <= len(grid[0]) -2 and grid[robot_y][robot_x + 1]:
		my_path = path[0:]
		my_path.append("RIGHT")
		return explore(robot_x + 1, robot_y, grid, path=my_path)

print(navigate([
	[1,1,1],
	[1,1,0],
	[1,1,1],
	[1,0,1],
]))
