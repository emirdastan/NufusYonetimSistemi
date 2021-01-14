def menu():
    print('''
--------------------------------------
1 - Yeni Kayıt
2 - Arama İşlemi(TC'ye göre)
3 - Kişi güncelleme
4 - Kişi Silme(TC'ye göre)
5 - Tüm veriler
6 - Çıkış  
--------------------------------------    
    ''')

def tc_dogrulama(value):
    value = str(value)

    # 11 hanelidir.
    if not len(value) == 11:
        return False

    # Sadece rakamlardan olusur.
    if not value.isdigit():
        return False

    # Ilk hanesi 0 olamaz.
    if int(value[0]) == 0:
        return False

    digits = [int(d) for d in str(value)]

    # 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun
    # 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
    if not sum(digits[:10]) % 10 == digits[10]:
        return False

    # 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı
    # çıkartıldığında, elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize
    # 10. haneyi verir.
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False


    return True



class Nufus(object):

    def toplam_kisi(self):
        return len(self.tum_kisileri_getir())

    def kisi_varmi(self, tc_no):
        kisiler = self.tum_kisileri_getir()
        bulundu = False
        for kisi in kisiler:
            if kisi.get('tc_no') == tc_no:
                bulundu = True

        return bulundu

    def kisi_guncelle(self):
        tc_no = input("TC No Giriniz:")
        kisiler = self.tum_kisileri_getir()
        bulundu = False
        bulunan_index = -1
        for index, kisi in enumerate(kisiler):
            if kisi.get('tc_no') == tc_no:
                bulundu = True
                bulunan_index = index
                break

        if not bulundu:
            print(f'{tc_no} tc no kişi bulunamadı.')
            return

        adi = input("Ad Giriniz         (Boş bırakabiliriniz.) :").lower().capitalize()
        soyadi = input("Soyad Giriniz      (Boş bırakabiliriniz.) :").upper()
        baba_adi = input("Baba Adı Giriniz   (Boş bırakabiliriniz.) :").lower().capitalize()
        anne_adi = input("Anne Adı Giriniz   (Boş bırakabiliriniz.) :").lower().capitalize()
        dogum_yeri = input("Doğum Yeri Giriniz (Boş bırakabiliriniz.) :").lower().capitalize()
        medeni_durumu = input("Medeni Durumu Giriniz('B Bekar' 'E Evli') :").lower()
        kan_grubu = input("Kan Grubu Giriniz  (Boş bırakabiliriniz.) :").upper()
        kutuk_sehir = input("Kutuk Şehir Giriniz(Boş bırakabiliriniz.) :").lower().capitalize()
        kutuk_ilce = input("Kutuk İlçe Giriniz (Boş bırakabiliriniz.) :").lower().capitalize()
        ikametgah_il = input("İkametgah İl Giriniz (Boş bırakabiliriniz.):").lower().capitalize()
        ikametgah_ilce = input("İkametgah İlçe Giriniz (Boş bırakabiliriniz.):").lower().capitalize()

        kisiler[bulunan_index]['adi'] = kisiler[bulunan_index].get('adi') if adi == '' else adi
        kisiler[bulunan_index]['soyadi'] = kisiler[bulunan_index].get('soyadi') if soyadi == '' else soyadi
        kisiler[bulunan_index]['baba_adi'] = kisiler[bulunan_index].get('baba_adi') if baba_adi == '' else baba_adi
        kisiler[bulunan_index]['anne_adi'] = kisiler[bulunan_index].get('anne_adi') if anne_adi == '' else anne_adi
        kisiler[bulunan_index]['dogum_yeri'] = kisiler[bulunan_index].get(
            'dogum_yeri') if dogum_yeri == '' else dogum_yeri
        kisiler[bulunan_index]['medeni_durumu'] = kisiler[bulunan_index].get(
            'medeni_durumu') if medeni_durumu == '' else 'Bekar' if medeni_durumu == 'b' or medeni_durumu == 'bekar' else 'Evli'
        kisiler[bulunan_index]['kan_grubu'] = kisiler[bulunan_index].get('kan_grubu') if kan_grubu == '' else kan_grubu
        kisiler[bulunan_index]['kutuk_sehir'] = kisiler[bulunan_index].get(
            'kutuk_sehir') if kutuk_sehir == '' else kutuk_sehir
        kisiler[bulunan_index]['kutuk_ilce'] = kisiler[bulunan_index].get(
            'kutuk_ilce') if kutuk_ilce == '' else kutuk_ilce
        kisiler[bulunan_index]['ikametgah_il'] = kisiler[bulunan_index].get(
            'ikametgah_il') if ikametgah_il == '' else ikametgah_il
        kisiler[bulunan_index]['ikametgah_ilce'] = kisiler[bulunan_index].get(
            'ikametgah_ilce') if ikametgah_ilce == '' else ikametgah_ilce

        print("Kişi güncelleme işlemi başarılı..")
        self.veriyi_db_atma(kisiler)

    def kisi_ekle(self):
        tc_no = input("TC No Giriniz  :")

        if not tc_dogrulama(tc_no):
            print('TC Numarısı yanlış veya eksik girildi..')
            return

        kisiler = self.tum_kisileri_getir()
        bulundu = False
        for kisi in kisiler:
            if kisi.get('tc_no') == tc_no:
                bulundu = True
                break

        if bulundu:
            print(f'{tc_no} tc no kişi zaten mevcut..')
            return

        adi = input("Ad Giriniz :").lower().capitalize()
        soyadi = input("Soyad Giriniz :").upper()
        baba_adi = input("Baba Adı Giriniz :").lower().capitalize()
        anne_adi = input("Anne Adı Giriniz :").lower().capitalize()
        dogum_yeri = input("Doğum Yeri Giriniz :").lower().capitalize()
        medeni_durumu = input("Medeni Durumu Giriniz('B Bekar' 'E Evli'):").lower()
        kan_grubu = input("Kan Grubu Giriniz :").upper()
        kutuk_sehir = input("Kutuk Şehir Giriniz :").lower().capitalize()
        kutuk_ilce = input("Kutuk İlçe Giriniz :").lower().capitalize()
        ikametgah_il = input("İkametgah İl Giriniz :").lower().capitalize()
        ikametgah_ilce = input("İkametgah İlçe Giriniz :").lower().capitalize()
        medeni_durumu = 'Bekar' if medeni_durumu == 'b' or medeni_durumu == 'bekar' else 'Evli'

        data = {
            'tc_no': tc_no, 'adi': adi, 'soyadi': soyadi, 'baba_adi': baba_adi, 'anne_adi': anne_adi,
            'dogum_yeri': dogum_yeri, 'medeni_durumu': medeni_durumu, 'kan_grubu': kan_grubu,
            'kutuk_sehir': kutuk_sehir, 'kutuk_ilce': kutuk_ilce,
            'ikametgah_il': ikametgah_il, 'ikametgah_ilce': ikametgah_ilce
        }
        kisiler.append(data)
        print("Kişi ekleme işlemi başarılı..")
        self.veriyi_db_atma(kisiler)

    def kisi_sil(self, tc_no):
        kisiler = self.tum_kisileri_getir()
        bulundu = False
        for index, kisi in enumerate(kisiler):
            if kisi.get('tc_no') == tc_no:
                bulundu = True
                del kisiler[index]

        if bulundu:
            self.veriyi_db_atma(kisiler)
            print("*Kişi başarıyla silindi.")
        else:
            print(f"**{tc_no} bu tc'ye sahip kişi bulunamadı..")

    def arama_islemi(self, tc_no):
        kisiler = self.tum_kisileri_getir()

        bulundu = False
        for kisi in kisiler:
            if kisi.get('tc_no') == tc_no:
                bulundu = True
                print('##########################################')
                print('##############KİŞİ BİLGİLERİ##############')
                print(f"TC No          : {kisi.get('tc_no')}")
                print(f"Ad             : {kisi.get('adi')}")
                print(f"Soyad          : {kisi.get('soyadi')}")
                print(f"Baba Adı       : {kisi.get('baba_adi')}")
                print(f"Anne Adı       : {kisi.get('anne_adi')}")
                print(f"Doğum Yeri     : {kisi.get('dogum_yeri')}")
                print(f"Medeni Durumu  : {kisi.get('medeni_durumu')}")
                print(f"Kan Grubu      : {kisi.get('kan_grubu')}")
                print(f"Kutuk Şehir    : {kisi.get('kutuk_sehir')}")
                print(f"Kutuk İlçe     : {kisi.get('kutuk_ilce')}")
                print(f"İkametgah İl   : {kisi.get('ikametgah_il')}")
                print(f"İkametgah İlçe : {kisi.get('ikametgah_ilce')}")
                print('##########################################')

        if not bulundu:
            print(f"**{tc_no} tc'ye  sahip kişi bulunamadı..")

    def tum_kisileri_getir(self):
        kisiler = []
        with open(file='kisiler.db', mode='r', encoding='utf8') as dosya:
            kolon_adlari = dosya.readline()
            veriler = dosya.readlines()

            for veri in veriler:
                tc_no, ad, soyad, baba_adi, anne_adi, dogum_yeri, medeni_durumu, kan_grubu, kutuk_sehir, kutuk_ilce, ikametgah_il, ikametgah_ilce = veri.strip().split(
                    ';')
                data = {
                    'tc_no': tc_no, 'adi': ad, 'soyadi': soyad, 'baba_adi': baba_adi, 'anne_adi': anne_adi,
                    'dogum_yeri': dogum_yeri, 'medeni_durumu': medeni_durumu,
                    'kan_grubu': kan_grubu, 'kutuk_sehir': kutuk_sehir, 'kutuk_ilce': kutuk_ilce,
                    'ikametgah_il': ikametgah_il, 'ikametgah_ilce': ikametgah_ilce
                }
                kisiler.append(data)
        return kisiler

    def veriyi_db_atma(self, kisiler):
        db_verileri = 'kimlik_no;adi;soyadi;baba_adi;anne_adi;dogum_yeri;medeni_durumu;kan_grubu;kutuk_sehir;kutuk_ilce;ikametgah_il;ikametgah_ilce\n';
        with open(file='kisiler.db', mode='w', encoding='utf8') as dosya:
            for kisi in kisiler:
                db_verileri += f'{kisi["tc_no"]};{kisi["adi"]};{kisi["soyadi"]};{kisi["baba_adi"]};{kisi["anne_adi"]};{kisi["dogum_yeri"]};{kisi["medeni_durumu"]};{kisi["kan_grubu"]};{kisi["kutuk_sehir"]};{kisi["kutuk_ilce"]};{kisi["ikametgah_il"]};{kisi["ikametgah_ilce"]}\n'
            dosya.write(db_verileri)

    def tum_kisi_bas(self):
        kisiler = self.tum_kisileri_getir()
        print('{:12}{:18}{:18}{:18}{:18}{:18}{:18}{:11}{:15}{:15}{:15}{:15}'.format('Tc No', 'Ad', 'Soyad', 'Baba Adı',
                                                                                    'Anne Adı', 'Doğum Yeri',
                                                                                    'Medeni Durumu', 'Kan Grubu',
                                                                                    'Kütük Şehir', 'Kütük İlçe',
                                                                                    'İ. İl', 'İ. İlçe'))
        print('{:12}{:18}{:18}{:18}{:18}{:18}{:18}{:11}{:15}{:15}{:15}{:15}'.format('-' * 11, '-' * 15, '-' * 15,
                                                                                    '-' * 15, '-' * 15, '-' * 15,
                                                                                    '-' * 15, '-' * 9, '-' * 14,
                                                                                    '-' * 14, '-' * 14, '-' * 14))
        for kisi in kisiler:
            print(
                f'{kisi["tc_no"]:12}{kisi["adi"]:18}{kisi["soyadi"]:18}{kisi["baba_adi"]:18}{kisi["anne_adi"]:18}{kisi["dogum_yeri"]:18}{kisi["medeni_durumu"]:18}{kisi["kan_grubu"]:11}{kisi["kutuk_sehir"]:15}{kisi["kutuk_ilce"]:15}{kisi["ikametgah_il"]:15}{kisi["ikametgah_ilce"]:15}')


nufus   = Nufus();

print("###############################################")
print(f"Toplam {nufus.toplam_kisi()} kişi var.")
print("###############################################")
while True:
    menu()
    islem = input('Lütfen yapılacak işlemi giriniz:')

    if islem == '1':
        print("######################################")
        print("########## EKLEME İŞLEMİ #############")
        print('Ekleme işlemi yapılacak.')
        nufus.kisi_ekle()
        print("######################################")

    elif islem == '2':
        print("######################################")
        print("############ ARAMA İŞLEMİ#############")
        print('Arama işlemi yapılacak.')
        tc_no = input('Lütfen tc numarasını giriniz:');
        nufus.arama_islemi(tc_no)
        print("######################################")

    elif islem == '3':
        print("######################################")
        print("############ GÜNCELLEME İŞLEMİ###########")
        nufus.kisi_guncelle()
        print("######################################")

    elif islem == '6':
        print("######################################")
        print("############ ÇIKIŞ ###################")
        print('Çıkış işlemi yapıldı.')
        print("######################################")
        break;

    elif islem == '4':
        print("######################################")
        print("############ SİLME İŞLEMİ###########")
        print('Silme işlemi yapılacak...')
        tc_no = input('Lütfen tc numarasını giriniz:');
        nufus.kisi_sil(tc_no)
        print("######################################")

    elif islem == '5':
        print("######################################")
        print("############ LİSTELEME ##############")
        nufus.tum_kisi_bas()
        print("######################################")
