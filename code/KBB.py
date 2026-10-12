import random  as rd

nguoi = input("Nhập kéo, búa, bao: ")

while nguoi not in ["kéo", "búa", "bao"]:
    nguoi = input("Nhập lại: ")

may = rd.choice(['kéo', 'búa','bao'])
print("Máy ra:", may)

def KBB(nguoi, may):
        if nguoi=='kéo' and may =='bao':
            print("Người thắng máy")
        elif nguoi=='búa' and may =='kéo':
            print("Người thắng máy")
        elif nguoi=='bao' and may =='búa':
            print("Người thắng máy")
        elif nguoi==may:
            print("Hòa")
        else:
            print("Người thua máy")

print(KBB(nguoi, may))




