n = float(input())
impostos = 0
total = n
if total > 2000:
    if total > 4500:
        impostos += (total - 4500) * 0.28
        total -= total - 4500
    if total > 3000:
        impostos += (total - 3000) * 0.18
        total -= total - 3000
    if total > 2000:
        impostos += (total - 2000) * 0.08
        total -= total - 2000
    print(f"R$ {impostos:.2f}")
else:
    print("Isento")