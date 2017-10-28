a = input().split()
[print(a[i-1], a[i]) for i in range(1, len(a)) if (int(a[i-1]) < 0 and int(a[i]) < 0) or (int(a[i-1]) > 0 and int(a[i]) > 0)]