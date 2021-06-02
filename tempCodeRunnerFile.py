  high = max(int(n[0:index] + x + n[index:]), high)
#     else:
#         for (val, index) in enumerate(n[0:]):
#             high = max(int(n[0:index] + x + n[index:]), high)
#     return high
# print(maxValue("99",9))