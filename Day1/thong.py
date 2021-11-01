tổng_số_lẻ = 0
for i in range(1, 1000, 2):
    tổng_số_lẻ += i
print(tổng_số_lẻ)


tổng_chia_hết_3_5 = 0
for i in range(1, 1000):
    if i % 3 == 0 and i % 5 == 0:
        tổng_chia_hết_3_5 += i

print(tổng_chia_hết_3_5)