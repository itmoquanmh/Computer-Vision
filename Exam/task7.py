# s = "BBBDDDDDDDDDXYZLLLYXOOOSKOLKKK"

# def rle_negative_lengths(s):
#     result = []
#     i = 0

#     while i < len(s):
#         # đếm chuỗi lặp
#         j = i + 1
#         while j < len(s) and s[j] == s[i]:
#             j += 1

#         run_len = j - i

#         if run_len >= 2:
#             # đoạn lặp: ghi số dương + ký tự
#             result.append(f"{run_len}{s[i]}")
#             i = j
#         else:
#             # đoạn không lặp: gom các ký tự đơn
#             start = i
#             i += 1

#             while i < len(s):
#                 j = i + 1
#                 while j < len(s) and s[j] == s[i]:
#                     j += 1

#                 if j - i >= 2:
#                     break

#                 i += 1

#             literal = s[start:i]
#             result.append(f"-{len(literal)}{literal}")

#     return "".join(result)

# encoded = rle_negative_lengths(s)

# original_len = len(s)
# encoded_len = len(encoded)
# compression_ratio = original_len / encoded_len

# print("Original:", s)
# print("Original length:", original_len)

# print("Encoded:", encoded)
# print("Encoded length:", encoded_len)

# print("Compression ratio:", round(compression_ratio, 2))
# print("Answer:", f"{encoded}; {compression_ratio:.2f}")
import math

square_size = 50
gap = 10
se_size = 3

# Với SE 3x3, mỗi lần dilation làm mỗi cạnh nở ra 1 pixel
radius = se_size // 2

# Hai hình vuông cùng nở về phía khe hở nên mỗi chu kỳ giảm khe hở 2 pixel
cycles = math.ceil(gap / (2 * radius))

print("\nMorphology answer:", cycles)
print("Need sequence: dilation", cycles, "times, then erosion", cycles, "times")
print("Number to enter:", cycles)