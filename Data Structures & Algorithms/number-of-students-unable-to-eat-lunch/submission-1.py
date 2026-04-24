class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)

        count = {}
        for s in students:
            if s not in count:
                count[s] = 0
            count[s] += 1
        
        for s in sandwiches:
            if count.get(s, 0) > 0:
                res -= 1
                count[s] -= 1
            else:
                return res
        
        return res
