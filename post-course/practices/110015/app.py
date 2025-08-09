# https://quera.org/problemset/110015/

n = int(input())

ghorfe1 = "ghorfe1" if n >= 1 else "......."
ghorfe2 = "ghorfe2" if n >= 2 else "......."
ghorfe3 = "ghorfe3" if n >= 3 else "......."
ghorfe4 = "ghorfe4" if n >= 4 else "......."
ghorfe5 = "ghorfe5" if n >= 5 else "......."
ghorfe6 = "ghorfe6" if n >= 6 else "......."
ghorfe7 = "ghorfe7" if n >= 7 else "......."
ghorfe8 = "ghorfe8" if n >= 8 else "......."

r = f"""########.......########
#{ghorfe1}.......{ghorfe2}#
########.......########
#{ghorfe3}.......{ghorfe4}#
########.......########
#{ghorfe5}.......{ghorfe6}#
########.......########
#{ghorfe7}.......{ghorfe8}#
#######################"""

print(r)