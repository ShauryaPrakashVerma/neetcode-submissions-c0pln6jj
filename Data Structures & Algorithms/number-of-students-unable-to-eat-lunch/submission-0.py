class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0 
        while students and count <= len(students):
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
                count = 0
            else:
                first_student = students.pop(0)
                students.append(first_student)
                count += 1

        if count > 0:
            return count-1
        else:
            return count