# https://leetcode.com/problems/product-of-the-last-k-numbers/
class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.zeroes = -1

    def add(self, num: int) -> None:
        if num == 0 :
            self.zeroes = len(self.stream)
            self.stream.append(num)
        else :
            if len(self.stream) == 0 or self.stream[-1] == 0 :
                self.stream.append(num)
            else :
                self.stream.append(num*self.stream[-1])

    def getProduct(self, k: int) -> int:
        if len(self.stream) == k and self.zeroes == -1 :
            return self.stream[-1]
        if len(self.stream)-k > self.zeroes :
            if self.stream[len(self.stream)-k-1] == 0 :
                return self.stream[-1]
            else :
                return int(self.stream[-1]/self.stream[len(self.stream)-k-1])
        else :
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# Implementation in O(1) for both add and getProduct operations.
