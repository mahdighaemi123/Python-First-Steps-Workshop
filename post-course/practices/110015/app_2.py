# https://quera.org/problemset/110015/

n = int(input())

for i in range(8+1):
    if i == 0:
        print("########.......########")
        continue

    if i == 8:
        print("#######################")
        continue

    if (1+i) % 2 == 1:
        print("########.......########")
        continue

    ghorfe_l = "ghorfe"+str(i) if n >= i else "......."
    ghorfe_r = "ghorfe"+str(i+1) if n >= (i+1) else "......."

    print(f"#{ghorfe_l}.......{ghorfe_r}#")