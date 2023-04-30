from typing import List

class Solution:
    @staticmethod
    def event_to_minutes(event: List[str]) -> List[int]:
        return [sum([x*y for x,y in zip(map(int, event[0].split(':')), [60,1])]),
                sum([x*y for x,y in zip(map(int, event[1].split(':')), [60,1])])]

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        s1, e1 = self.event_to_minutes(event1)
        s2, e2 = self.event_to_minutes(event2)

        return s1 in range(s2, e2+1) or \
               e1 in range(s2, e2+1) or \
               s2 in range(s1, e1+1)

# Testing
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.haveConflict(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"])
    print(Solve) # --> True
    Solve = Sol.haveConflict(event1 = ["10:00","11:00"], event2 = ["14:00","15:00"])
    print(Solve) # --> False
