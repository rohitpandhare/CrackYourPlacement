class Solution:
    def gcd(self, a: int, b: int) -> int:
        common = []

        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                common.append(i)
                
        return max(common) if common else 1

def main():
    # TCS NQT style input handling
    a = int(input())
    b = int(input())
    
    solution = Solution()
    result = solution.gcd(a, b)
    print(result)

if __name__ == "__main__":
    main()
