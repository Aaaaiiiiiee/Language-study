# import egoing, k8805
# print(egoing.a())

# from egoing import a
# import k8805
# print(a())
# print(k8805.a())

from egoing import a as z
import k8805 as k

print(z())
print(k.a())