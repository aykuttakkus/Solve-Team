# Derin Ogrenme Proje Roadmap'i

## Amac
Bu roadmap'in amaci, [planlama.md](/Users/aykutakkus/Desktop/Solve/planlama.md) icindeki stratejiyi uygulamaya donusturmek ve projeyi hocanin beklentilerine gore tam puan odakli sekilde yonetmektir.

Bu projede hedefimiz:
- Lablarda gorulen yontemleri yeni bir veri setine uygulamak
- Tek bir model degil, birden fazla yontemi adil sekilde karsilastirmak
- Her modelin neden secildigini teknik olarak savunmak
- Kod, dokumantasyon ve sunum tarafini birlikte guclu tutmak

## Hocanin Beklentisine Gore Basari Formulu
Hocanin mesajlarina gore proje su dort alanda guclu olmak zorunda:

1. Code correctness and topic inclusions
2. Number of methods
3. Technical documentation
4. Technical depth of methods

Bu nedenle roadmap boyunca her adimda su mantik korunacak:
- "Gercek hayat" (real-world) senaryolarindan uzak durulup, tamamen matematige ve metodolojik titizlige (Methodological Rigor) odaklanilacak.
- Kod calisir durumda olacak, Week 2, 3 ve 4 baglantilari acik sekilde gosterilecek.
- En az 5 ana model ayni veri seti uzerinde karsilastirilacak.
- Sonuclar sadece skor olarak degil, teknik jargon (Gradient, L2, Overfitting vb.) ile sunulacak.

## Proje Kapsami
Veri seti:
- Breast Cancer Wisconsin

Ana modeller:
1. Logistic Regression (W2 P2)
2. Duz MLP (W3 P3)
3. MLP + L2 Regularization (W4 P2)
4. MLP + Dropout (W4 P4)
5. MLP + Early Stopping (W4 P5)

Istege bagli ek model:
6. MLP + Batch Normalization (W4 P7)

## Temel Ilke
Bu proje genislik degil derinlik odakli yurutecek.

Yani:
- Tek veri seti uzerinde kalacagiz
- Kontrollu deneyler yapacagiz
- Her modeli ayni veri bolmesi ve ayni metriklerle test edecegiz
- Her yeni model icin "neden bunu ekledik" sorusunu cevaplayacagiz

## Asama 1: Proje Altyapisini Kur
Amac:
- Calisma yapisini bastan duzenli kurmak

Yapilacaklar:
- `notebooks/` klasor yapisini olustur
- Notebook isimlerini plana gore sabitle
- `outputs/figures/` ve `outputs/tables/` klasorlerini tanimla
- `requirements.txt` icin kullanilacak kutuphaneleri belirle
- Tum notebook'larda kullanilacak ortak random seed degerini sabitle

Beklenen ciktIlar:
- Duzenli klasor yapisi
- Tekrarlanabilir notebook akisi
- Karisik degil, teslime uygun proje iskeleti

Tam puan gerekcesi:
- Temiz proje yapisi, kod dogrulugu ve teknik dokumantasyon puanini dogrudan guclendirir

## Asama 2: Veri Anlama ve On Isleme
Notebook:
- `step1_data_understanding.ipynb`

Amac:
- Veri setini teknik olarak anlamak
- Tum sonraki modeller icin ortak ve dogru veri akisini kurmak

Yapilacaklar:
- Veri setini yukle
- Ornek sayisi ve ozellik sayisini yaz
- Sinif dagilimini goster
- Eksik veri kontrolu yap
- Temel istatistikleri incele
- Gerekirse basit grafiklerle veri yapisini goster
- **KRITIK YASA (Data Leakage):** Standardizasyon uygularken `StandardScaler.fit_transform()` SADECE Train setine uygulanacak. Validation ve Test setlerine sadece `.transform()` yapilacak.
- Train/validation/test ayrimini yap
- Mumkunse `stratified split` kullan

Beklenen ciktIlar:
- Veri seti ozet tablosu
- Sinif dagilimi bilgisi
- Preprocessing kararlarinin kisa teknik aciklamasi
- Sonraki notebook'larin kullanacagi net veri akisi

Tam puan gerekcesi:
- Veri anlama kismini iyi kurmak, sonraki modellerin dogru ve adil karsilastirilmasi icin zorunludur
- Hocanin "neden bu yaklasimi sectiniz" sorusuna ilk cevaplar burada verilir

## Asama 3: Baseline Modeli Kur
Notebook:
- `step2_logistic_regression.ipynb`

Model:
- Logistic Regression (W2 P2)

Amac:
- Guclu, sade ve savunulabilir bir baseline olusturmak

Yapilacaklar:
- Logistic regression modelini kur
- Modeli egit
- Test metriklerini hesapla
- Confusion matrix uret
- Sonuclari tabloya kaydet
- Bu modelin neden secildigini yaz

Mutlaka cevaplanacak sorular:
- Neden bu veri seti icin ilk tercih logistic regression oldu?
- Hedef kanser teshisi oldugundan verideki sinif dengesizligi (%63 Benign) referans alinarak; Naif Baseline olan %63 "kor tahmin" basarisi asildi mi?
- Model performansi Neden sadece Accuracy ile degil, **Recall ve F1-Score** ile olculmelidir?

Beklenen ciktIlar:
- Accuracy, precision, recall, F1-score
- Confusion matrix
- Baseline sonuc tablosu
- Kisa teknik yorum

Tam puan gerekcesi:
- Bu adim Week 2 bilgisini dogrudan uygular
- Tum sonraki modellerin anlamli olup olmadigi bu baseline ile olculecek

## Asama 4: Duz MLP Modelini Kur
Notebook:
- `step3_mlp.ipynb`

Model:
- Duz MLP (W3 P3)

Amac:
- Logistic regression ile daha esnek bir sinir agi modelini karsilastirmak

Yapilacaklar:
- Basit bir MLP mimarisi kur
- ReLU gibi uygun aktivasyon kullan
- Binary classification'a uygun cikis yapisi kur
- Modeli egit
- Validation ve test sonuclarini kaydet
- Loss egirilerini cikar
- Sonuclari baseline ile karsilastir

Mutlaka cevaplanacak sorular:
- MLP, logistic regression'dan daha iyi mi?
- Daha iyi ise neden?
- Daha iyi degilse neden?

Beklenen ciktIlar:
- MLP test metrikleri
- Training loss ve validation loss grafikleri
- Logistic regression ile yan yana karsilastirma

Tam puan gerekcesi:
- Bu adim Week 3 bilgisini dogrudan tasir
- Hoca icin "tek model degil, yontem karsilastirma" beklentisini guclendirir

## Asama 5: Overfitting'i Goster ve Regularization Uygula
Notebook:
- `step4_regularization_experiments.ipynb`

Modeller:
- MLP + L2 Regularization (W4 P2)
- MLP + Dropout (W4 P4)
- MLP + Early Stopping (W4 P5)
- Istege bagli: MLP + Batch Normalization (W4 P7)

Amac:
- Duz MLP'nin zayif yonlerini gostermek
- Regularization tekniklerinin genellemeyi nasil etkiledigini gostermek

Yapilacaklar:
- Duz MLP sonucunu referans al
- L2 ile yeni model kur
- Dropout ile yeni model kur
- Early stopping ile yeni model kur
- Tum modellerde mumkun oldugunca ayni veri bolmesini ve benzer ayarlari koru
- Her model icin train/validation davranisini incele
- Sonuclari tek bir deney tablosunda topla

Mutlaka cevaplanacak sorular:
- Duz MLP overfit oldu mu?
- Hangi regularization en iyi sonucu verdi?
- Hangi regularization daha dengeli bir egitim sagladi?

Beklenen ciktIlar:
- Her regularized model icin metrikler
- Loss egirileri
- Karsilastirma tablosu
- Teknik yorumlar

Tam puan gerekcesi:
- Teknik derinlik puaninin en guclu kismi buradan gelir
- Week 4 bilgisini sadece isim olarak degil, deney olarak gostermis oluruz

## Asama 6: Tum Sonuclari Birlestir
Notebook:
- `step5_evaluation_and_comparison.ipynb`

Amac:
- Tum modelleri tek yerde, adil ve temiz bicimde karsilastirmak

Yapilacaklar:
- Tum model sonuclarini tek tabloda topla
- Guzel grafik ve confusion matrix ozetlerini sec
- **BONUS PUAN FIRSATI:** Hoca tarafindan henuz islenmemis ama projeyi asiri profesyonel gosterecek olan **ROC Curve ve AUC (Area Under Curve)** analizini modellere entegre et.
- En iyi modeli sadece skorla degil yorumla (F1/Recall) belirle
- "daha karmasik model gerekli mi?" sorusunu cevapla
- Final teknik sonuc yazisini hazirla

Final karsilastirma tablosunda bulunmasi gerekenler:
- Model adi
- Week/Part referansi
- Accuracy
- Precision
- Recall
- F1-score
- Kisa yorum

Tam puan gerekcesi:
- Hocanin istedigi "neden bu yaklasim digerine tercih edildi" sorusunun ana cevabi burada verilir
- Number of methods ve technical depth puanlari burada guclu sekilde gorunur

## Asama 7: Teknik Dokumantasyon
Amac:
- Projeyi sadece calisan kod olarak degil, anlasilir bir teknik calisma olarak teslim etmek

Yapilacaklar:
- README hazirla
- Proje amacini yaz
- Veri seti secim gerekcesini yaz
- Kullanilan modelleri week/part referanslariyla yaz
- Deney kurulumunu anlat
- Sonuclarin ozetini yaz
- Tekrarlanabilirlik icin kutuphane ve seed bilgisini ekle

README'de mutlaka bulunmali:
- Proje konusu
- Veri seti bilgisi
- Kullanilan modeller
- Calistirma sirasi
- Sonuc ozeti
- GitHub repo duzeni

Tam puan gerekcesi:
- Technical documentation notunun ana kaynagi burasidir

## Asama 8: Sunum Hazirlama
Teslim:
- PDF veya PPTX

Amac:
- Teknik olarak guclu ama akici bir sunum hazirlamak

Slayt akisi:
1. Problem ve hedef
2. Neden Breast Cancer Wisconsin?
3. Hocanin lablarina gore secilen yontemler
4. Kullanilmayan yontemler ve nedenleri
5. Veri seti analizi
6. Logistic Regression (W2 P2)
7. Duz MLP (W3 P3)
8. Regularization deneyleri: W4 P2, W4 P4, W4 P5
9. Final karsilastirma tablosu
10. Teknik yorumlar ve sonuc

Sunumda dikkat edilecek SIFIR TOLERANS KURALLARI:
- **JARGON ZORUNLULUGU:** Skor okumak yerine "Weight penalty, Gradient saturation, Linear Separability" gibi metodolojik teknik yorum yapilacak.
- Her modelin neden secildigini bir cumlede anlatin.
- Grafik ve tablolar temiz olsun.
- **SIFIR NOKTASI (0 PUAN UYARISI):** Hocanin uyarisi nettir: "if you read from somewhere, you will get 0". Slaytlarda yazi minimumda tutulacak ve ASLA ekrandan yazi okunmayacaktir.
- Sunum akisi hizli ve metodolojiye dayali (real-world degil) olacaktir.

Tam puan gerekcesi:
- Hoca sunumda teknik jargon kullanimina (%40) ve kagitlara/ekrana bakmadan dogal anlatima (%30) bakiyor. Oran cok buyuk!

## Kalite Kontrol Listesi
Teslimden once su maddeler tek tek kontrol edilecek:

- Tum notebook'lar bastan sona hatasiz calisiyor mu?
- Veri bolmesi tum notebook'larda ayni mi?
- Tum ana modeller tamamlandi mi?
- Sonuc tablosu tek formatta hazirlandi mi?
- Logistic regression baseline net mi?
- Duz MLP ile baseline farki anlatildi mi?
- L2, dropout ve early stopping etkileri net gosterildi mi?
- Confusion matrix ve temel metrikler var mi?
- README tamamlandi mi?
- Sunum PDF/PPTX hazir mi?
- GitHub repo temiz mi?
- Notebook'larda gereksiz hucreler temizlendi mi?

## Tam Puan Icin Kritik Kurallar
- Tek veri seti uzerinde derin gidin, konu dagitmayin
- En az 5 modelin adil karsilastirmasini yapin
- Week 2, Week 3 ve Week 4 baglantilarini acik yazin
- Her model icin neden secildigini mutlaka savunun
- Sadece en iyi sonucu gostermeyin; neden o sonucun ciktigini da anlatin
- Sunum ile kod birebir uyumlu olsun
- Repo duzeni temiz ve profesyonel gorunsun

## Onerilen Calisma Sirasi
1. `step1_data_understanding.ipynb`
2. `step2_logistic_regression.ipynb`
3. `step3_mlp.ipynb`
4. `step4_regularization_experiments.ipynb`
5. `step5_evaluation_and_comparison.ipynb`
6. `README.md`
7. Sunum dosyasi

## Son Not
Bu roadmap'in ana felsefesi sudur:

Bu proje, "bir veri setine birkac model denedik" seviyesinde kalmamali. Bunun yerine, "dersin ilk dort haftasinda ogrendigimiz metodolojileri yeni bir veri setinde neden-sonuc iliskisiyle uyguladik ve teknik olarak savunduk" seviyesine cikmalidir.
