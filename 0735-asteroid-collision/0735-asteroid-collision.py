class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        ans = []

        for a in asteroids:
            alive = True
            while alive and ans and ans[-1] >0 and a <0:
                if ans[-1] < -a:
                    ans.pop()
                    continue
                if ans[-1] == -a:
                    ans.pop()
                alive = False
            if alive:
                ans.append(a)
        return ans


        