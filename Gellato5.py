from itertools import combinations

def generate_valid_splits(s, max_len=3):
    n = len(s)
    splits = []
    
    # ایجاد گراف از رشته به کمک گره‌ها (هر بخش از 1 تا max_len)
    edges = []
    for i in range(n):
        for j in range(i + 1, min(i + max_len + 1, n + 1)):
            edges.append((i, j))
    
    # بررسی مسیرهای ممکن در گراف
    def is_valid_split(path):
        seen = set()
        for start, end in zip(path, path[1:]):
            segment = s[start:end]
            # بررسی پیشوندها
            if any(segment.startswith(other) for other in seen):
                return False
            seen.add(segment)
        return True

    # جستجو در گراف برای یافتن تقسیم‌بندی‌های معتبر
    def backtrack(start, path):
        if start == n:
            splits.append(path[:])
            return
        
        for _, end in filter(lambda edge: edge[0] == start, edges):
            path.append(end)
            if is_valid_split([0] + path):
                backtrack(end, path)
            path.pop()

    backtrack(0, [])
    return splits
splits = generate_valid_splits('01110')
print(splits)