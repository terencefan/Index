Title: 记一次算法题的讨论
Date: 2016-02-03 23:22
Tags: meaningless
Category: 漫谈

今天那位[不愿意透露姓名的大哥](http://oreki.moe/)由于公司年终只给涨了500块工资，怒而与我讨论了一晚上面试相关的问题，其中有这么一道题：

> 对于一个n位的2进制数，其中不允许出现连续超过k个0，问可能的数字总数？

> （后来补充，由于可能的总数太多，结果对10 ^ 9 + 7取余即可）

最早我给出的边界是 1 <= n < 1e9, 0 < k <= 10，后来想想...如果不用通项公式，可能还是有点高了。

这位大哥是一位半路出家的Coder，并没有系统的学过算法知识，讨论的过程中也算是意外地有所收获，又想到这是一个绝佳的丰富博客内容的机会，写！


# T(n * 2 ^ n) 算法

这应该是一个最容易想到也是最蠢的办法了，枚举出所有的排列，判断是否有连续k个0

# T(2 ^ n) 算法

实话说我真的没想到还有这么一个算法，在枚举的同时进行剪枝，这样就不需要每次去判断了

# T(nk), Space(nk) 算法

最常规的dp解法，f[n][k]是n位二进制数，其中末尾不超过k个0的种数

```python
# 末尾不允许为0的情况下，只要在n-1的组合后面直接补1就可以了，转移方程为
f[n][0] = sum(f[n - 1][0] + ... + f[n - 1][k])
# 末尾允许k个0的情况下，也就是最后一位补0，前n-1位的末尾有k-1个0，转移方程为
f[n][k] = f[n - 1][k - 1]
```

# T(nk), Space(k) 算法

由于计算f[n]只需要用到f[n-1]，因此空间复杂度可以继续优化

然而数字的拷贝有必要么？并没有，因此还可以换成deque来做

# T(k)，Space(1) 算法

其实观察deque里面的内容，我们能发现这其实就是一个k阶Fibonacci数列！那么或许可以去找到通项公式...

# SPOJ

其实这道题在spoj上面有类似的，[Black And White beads](http://www.spoj.com/problems/BWB/)

贴上代码以供交流～

```python
from collections import deque

N = 10 ** 4
K = 10 ** 2
MOD = 10 ** 9 + 7


class Solution(object):

    def __init__(self):
        f = []
        for k in range(1, K + 1):
            s = deque([0] * (k - 1) + [1, 1])
            t = s[-1]
            dp = [0] * N
            for i in range(N):
                dp[i] = s[-1]
                t = (t * 2 - s.popleft()) % MOD
                s.append(t)
            f.append(list(dp))
        self.f = f

    def solute(self, n, k):
        return self.f[k - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    m, t = [], int(raw_input())
    for i in range(t):
        n, k = map(int, raw_input().split(' '))
        m.append((n, k))

    for n, k in m:
        print s.solute(n, k)
```
