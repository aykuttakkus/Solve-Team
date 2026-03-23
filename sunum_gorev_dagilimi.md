# 5 Kisilik Sunum ve Gorev Dagilimi Plani

## Amac
Bu dokumanin amaci, projeyi 5 kisi arasinda adil, teknik olarak dengeli ve sunum acisindan akici olacak sekilde bolmektir.

Bu dagilim hazirlanirken su hedefler gozetilmistir:
- Her kisinin sunabilecegi net bir teknik alan olsun
- Her kisi projeye somut katkı versin
- Sunumda gecisler dogal olsun
- Hocanin bekledigi teknik derinlik tum ekipte dagilsin
- Sunum sadece parcalara ayrilmis degil, tek bir hikaye gibi ilerlesin

## Bolumleme Mantigi
Projeyi algoritma sayisina gore degil, teknik hikaye akisina gore 5 ana bolume ayiriyoruz.

Bu sayede:
- Her kisi ayri bir sorumluluk alir
- Her bolumun basi ve sonu net olur
- Tekrar ve karisiklik azalir
- Sunum daha profesyonel gorunur

## 5 Ana Sunum Alani

1. Problem tanimi, veri seti secimi ve preprocessing
2. Logistic Regression baseline
3. Duz MLP modeli
4. Regularization deneyleri
5. Final karsilastirma, teknik yorum ve sonuc

## Kisi Bazli Dagilim

### Kisi 1: Problem Tanimi, Veri Seti ve Preprocessing
Sorumlu alan:
- Problem tanimi
- Proje motivasyonu
- Neden Breast Cancer Wisconsin secildi
- Veri setinin yapisi
- Sinif dagilimi
- Eksik veri kontrolu
- Standardization ve train/validation/test split

Sunumda anlatacagi ana fikir:
- Bu proje hangi problemi cozuyor ve neden bu veri seti secildi?

Sunumda gosterecegi seyler:
- Veri seti ozeti
- Sinif dagilimi
- Temel preprocessing adimlari

Teknik katkisi:
- `step1_data_understanding.ipynb`

Neden adil bir alan:
- Projenin temelini kurar
- Veri tarafini teknik olarak sahiplenir
- Sunuma guclu ve anlasilir bir giris yapar

### Kisi 2: Logistic Regression Baseline
Sorumlu alan:
- `Logistic Regression (W2 P2)`
- Neden linear regression kullanilmadigi
- Neden logistic regression'in dogru baseline oldugu
- Model egitimi ve temel metrikler
- Confusion matrix yorumu

Sunumda anlatacagi ana fikir:
- Bu veri setinde neden once logistic regression ile basliyoruz?

Sunumda gosterecegi seyler:
- Baseline metrikleri
- Confusion matrix
- Kisa model mantigi

Teknik katkisi:
- `step2_logistic_regression.ipynb`

Neden adil bir alan:
- Week 2 bilgisini dogrudan temsil eder
- Tek basina savunulabilir ve teknik bir bolumdur

### Kisi 3: Duz MLP Modeli
Sorumlu alan:
- `Duz MLP (W3 P3)`
- Hidden layer mantigi
- Aktivasyon fonksiyonu secimi
- MLP mimarisi
- Logistic regression ile farki
- Overfitting belirtileri

Sunumda anlatacagi ana fikir:
- Daha esnek bir model kurunca ne kazandik, ne kaybettik?

Sunumda gosterecegi seyler:
- MLP mimarisi
- Training ve validation loss grafikleri
- Baseline ile karsilastirma

Teknik katkisi:
- `step3_mlp.ipynb`

Neden adil bir alan:
- Week 3 bilgisini tasir
- Teknik derinligi olan ana model bolumudur

### Kisi 4: Regularization Deneyleri
Sorumlu alan:
- `MLP + L2 Regularization (W4 P2)`
- `MLP + Dropout (W4 P4)`
- `MLP + Early Stopping (W4 P5)`
- Istege bagli olarak `MLP + Batch Normalization (W4 P7)`
- Hangi teknik neyi iyilestirdi

Sunumda anlatacagi ana fikir:
- Overfitting sorununu nasil kontrol altina aldik?

Sunumda gosterecegi seyler:
- Regularization deney tablosu
- Loss egirileri
- Duz MLP ile regularized modeller arasindaki fark

Teknik katkisi:
- `step4_regularization_experiments.ipynb`

Neden adil bir alan:
- En yogun teknik kisimlardan biridir
- Week 4 bilgisini dogrudan temsil eder

### Kisi 5: Final Karsilastirma ve Sonuc
Sorumlu alan:
- Tum modellerin nihai karsilastirmasi
- En iyi modelin secimi
- Daha karmasik model gerekli miydi sorusu
- Teknik yorumlar
- Limitasyonlar
- Gelecek gelistirme alanlari

Sunumda anlatacagi ana fikir:
- Tum deneylerin sonunda ne ogrendik?

Sunumda gosterecegi seyler:
- Final karsilastirma tablosu
- Model bazli kisa teknik yorumlar
- Sonuc slaydi

Teknik katkisi:
- `step5_evaluation_and_comparison.ipynb`
- Sonuc yorumlarinin yazimi

Neden adil bir alan:
- Sunumun kapanisini yapar
- Tum projeyi birlestiren teknik degerlendirme burada toplanir

## Onerilen Slayt Dagilimi

### Kisi 1
- Slayt 1: Problem ve hedef
- Slayt 2: Neden bu veri seti?
- Slayt 3: Veri seti ozeti ve preprocessing

### Kisi 2
- Slayt 4: Neden logistic regression?
- Slayt 5: Logistic Regression (W2 P2) sonuclari

### Kisi 3
- Slayt 6: Neden MLP?
- Slayt 7: Duz MLP (W3 P3) mimarisi ve sonuclari

### Kisi 4
- Slayt 8: Overfitting problemi
- Slayt 9: L2, Dropout, Early Stopping deneyleri

### Kisi 5
- Slayt 10: Final karsilastirma tablosu
- Slayt 11: Teknik yorumlar
- Slayt 12: Sonuc ve gelecek calismalar

## Sunum Gecis Mantigi
Sunumda kopukluk olmamasi icin gecisler su mantikla yapilmalidir:

1. Kisi 1 problemi ve veri tarafini anlatir
2. Kisi 2 bu veri icin ilk dogru baseline modeli tanitir
3. Kisi 3 daha karmasik modele neden gectigimizi aciklar
4. Kisi 4 bu daha karmasik modelin sorunlarini ve cozumlerini gosterir
5. Kisi 5 tum sureci birlestirip teknik sonucu verir

Bu akis sunumu tek parca bir hikaye haline getirir.

## Zaman Dagilimi Onerisi
Eger sunum suresi 10-12 dakika civarindaysa:
- Kisi 1: 2 dakika
- Kisi 2: 2 dakika
- Kisi 3: 2 dakika
- Kisi 4: 3 dakika
- Kisi 5: 2-3 dakika

Eger sunum suresi daha uzunsa:
- Kisi 4 ve Kisi 5 bolumleri biraz genisletilebilir

## Adalet Analizi
Bu dagilim neden adil?
- Her kisi ayri bir teknik alani sahipleniyor
- Her kisi sunumda veri, model veya deney tarafinda somut bir rol aliyor
- Kimse sadece giris ya da sadece kapanis yapmiyor
- Week 2, Week 3 ve Week 4 konulari ekip icinde dengeli dagiliyor
- Sonuc bolumu de ayri bir teknik sorumluluk olarak ele aliniyor

## Gelistirme Gorevi ile Sunum Gorevinin Eslesmesi
En saglikli yontem, sunacak kisinin ayni zamanda o notebook'un ana sorumlusu olmasidir.

Onerilen eslesme:
- Kisi 1 -> `step1_data_understanding.ipynb`
- Kisi 2 -> `step2_logistic_regression.ipynb`
- Kisi 3 -> `step3_mlp.ipynb`
- Kisi 4 -> `step4_regularization_experiments.ipynb`
- Kisi 5 -> `step5_evaluation_and_comparison.ipynb`

Bu eslesme sayesinde:
- Herkes kendi yaptigi kismi sunar
- Sunum sirasinda ezber degil, gercek teknik hakimiyet gorulur
- Hoca soru sorarsa cevap vermek kolaylasir

## Tam Puan Icin Sunum Kurallari
- Her kisi kendi bolumunde neden bu yontemin secildigini aciklamali
- Sonuc okuma degil, teknik yorum yapilmali
- Grafik ve tablolar sade ve okunabilir olmali
- Konusmalar birbiriyle baglantili olmali
- Sunumda gereksiz teori uzatilip sure kaybedilmemeli
- Ezberden veya metin okuyarak anlatim yapilmamali

## Son Oneri
Bu dagilim icinde en kritik nokta sudur:

Sunum, 5 kisinin ayri ayri anlattigi 5 parca gibi degil; tek bir projenin 5 mantikli asamasi gibi gorunmelidir.

Eger bu birlik hissi korunursa, hem daha profesyonel gorunur hem de hocanin teknik derinlik beklentisi daha guclu sekilde karsilanir.
