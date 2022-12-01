text = """
Oliy Majlis Qonunchilik palatasida vazirliklarning budjet mablag‘larini noqonuniy sarflashiga oid, Davlat moliyaviy nazorati inspeksiyasi aniqlagan ma’lumotlar ochiqlandi.

Deputat Botir Mardayevning e’tibor qaratishicha, joriy yilning o‘tgan 9 oyi davomida tarif razryadlarining noto‘g‘ri qo‘llanishi, ish haqi va moddiy yordam to‘lovlari ortiqcha to‘lanishi hisobiga 138 mlrd so‘mga yaqin xato va kamchiliklar qayd etilgan.

Xususan, xalq ta’limi tizimida 47 mlrd so‘m, sog‘liqni saqlashda 30 mlrd so‘m, maktabgacha ta’lim tizimida 7 mlrd so‘m, Madaniyat vazirligida 5,5 mlrd so‘mga yaqin qonunbuzilish holatlari aniqlangan.

Bundan tashqari, bajarilmagan ishlarni “bajarildi” qilib ko‘rsatish, budjetdan ajratilgan subsidiyalar hisobidan o‘rnatilmagan uskunalarni “o‘rnatildi” deb rasmiylashtirish hisobiga 100 mlrd so‘mdan ortiq qonunbuzilish holatlari va umuman 139 mlrd so‘m budjet mablag‘lari maqsadsiz sarflanishiga yo‘l qo‘yilgan.

Moliya vaziri Timur Ishmetovning ta’kidlashicha, kelajakda bu kabi holatlarning oldini olish maqsadida vazirliklardagi ichki audit tizimlari takomillashtiriladi.
"""

text = text.split()
res = ''

for el in text:
    mark = el[-1]
    word = ''

    for i in range(len(el)-1):
        if el[i]!=mark:
            word+=el[i]

        else:
            word+='.' 

    res += f'{word}{mark} '


print(res)