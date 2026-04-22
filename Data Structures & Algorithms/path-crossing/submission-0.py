class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current_x = 0
        current_y = 0
        visited = {(0,0)}
        for char in path:
            if char == "N":
                current_y += 1
            elif char == "S":
                current_y -= 1
            elif char == "W":
                current_x -= 1
            else:
                current_x +=1
            
            new_pos = (current_x, current_y)
            
            if new_pos in visited:
                return True
            
            visited.add(new_pos)

        return False
        