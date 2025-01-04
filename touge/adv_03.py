from typing import List

def new_2d_arr(d1_len: int, d2_len: int) -> List[List[bool]]:
    result = list()
    for i in range(d2_len):
        result.append([False] * d1_len)
    return result

def can_devide(nums: List[int], k: int) -> bool:
    n = len(nums)
    dp = new_2d_arr(k, n + 1)
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(k):
            if dp[i - 1][j]:
                dp[i][(j + nums[i - 1] % k + k) % k] = True
                dp[i][(j - nums[i - 1] % k + k) % k] = True

    return dp[n][0]

def main() -> None:
    data = input().split(' ')
    n = int(data[0])
    k = int(data[1])
    nums = [int(m) for m in input().split(' ')]
    assert len(nums) == n

    if can_devide(nums, k):
        print('Divisible')
    else:
        print('Not divisible')

if __name__ == '__main__':
    main()
