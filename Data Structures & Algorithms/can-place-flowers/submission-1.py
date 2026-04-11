class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        count = 0
        for key, value in enumerate(flowerbed):
            
            if value == 0:
                if key == (len(flowerbed) - 1):
                    if flowerbed[key-1] == 0:
                        flowerbed[key] = 1
                        count += 1
                elif key == 0:
                    if flowerbed[key + 1] == 0:
                        flowerbed[key] = 1
                        count += 1
                else:
                    if flowerbed[key-1] == 0 and flowerbed[key + 1] == 0:
                        flowerbed[key] = 1
                        count += 1
            else:
                continue
        
        if count >= n :
            return True
        else:
            return False
        '''

        f = [0] + flowerbed + [0]

        for i in range (1, len(f)-1):
            if f[i-1] == 0 and f[i]==0 and f[i+1]==0:
                f[i] = 1
                n -= 1
        return n<=0
        