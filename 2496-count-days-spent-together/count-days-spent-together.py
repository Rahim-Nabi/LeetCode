class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def dayOfYear(date):
            month, day = map(int, date.split("-"))
            return sum(months[:month - 1]) + day
        
        start = max(dayOfYear(arriveAlice), dayOfYear(arriveBob))
        end = min(dayOfYear(leaveAlice), dayOfYear(leaveBob))

        return max(0, end - start + 1)