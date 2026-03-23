# Derin Ogrenme Proje Plani

## Proje Basligi
Breast Cancer Wisconsin Veri Seti ile Temel ve Regularization Destekli Siniflandirma

## Ana Hedef
Dersin ilk dort haftasinda islenen konulari yeni bir veri seti uzerinde uygulamak ve genis ama yuzeysel bir proje yerine metodolojik derinlik gostermek.

Bu projede Breast Cancer Wisconsin veri seti kullanilarak bir tumorun `malignant` veya `benign` oldugu tahmin edilecektir.

## Neden Bu Veri Seti
- Temiz ve odakli bir `binary classification` problemidir.
- `Logistic regression` icin uygun oldugu icin Week 2 tarafinda guclu bir baseline olusturur.
- `MLP` gibi daha esnek bir modelin anlamli fayda saglayip saglamadigini test etmeye uygundur.
- Veri seti cok buyuk olmadigi icin overfitting ve Week 4 regularization yontemlerinin etkisini gostermek kolaydir.
- Lablarda kullanilan veri setlerinden farkli oldugu icin proje dogrudan kopya gibi gorunmez.

## Hocanin Beklentisi
- Lablarda islenen yontemleri secilen veri setine uygulamak.
- Her yontemin neden secildigini acik sekilde anlatmak.
- Tek bir model degil, birden fazla yontemi karsilastirmak.
- Sadece sonuc skoru degil, teknik derinlik gostermek.
- Kod ile birlikte sunum dosyasi da hazirlamak.

## Proje Stratejisi
Proje, tek bir veri seti uzerinde kontrollu bir karsilastirma olarak kurgulanacaktir.

Akis su sekilde olacak:
1. Veri setini anlama ve on isleme
2. Basit bir baseline model kurma
3. Sinir agi modeli kurma
4. Regularization yontemlerini tek tek ekleme
5. Tum modelleri ayni degerlendirme duzeni ile karsilastirma
6. Hangi yontemin neden daha iyi calistigini teknik olarak aciklama

## Kullanilacak Yontemler

Bu bolumde her haftadaki lab icerigini proje ihtiyacina gore degerlendiriyoruz. Amacimiz butun lablari kopyalamak degil; veri setimize uyan, metodolojik olarak guclu ve hocanin beklentisini karsilayan parcalari secmek.

### Week 2

#### Part 1: Linear Regression from Scratch
- Kullanmayacagiz.
- Neden kullanmiyoruz:
  - Breast Cancer Wisconsin veri seti bir `binary classification` problemidir.
  - Linear regression surekli bir cikti tahmin etmek icin uygundur, bizim problemimizde ise cikti `malignant` veya `benign` gibi iki siniftan biridir.
  - Bu yontemi kullanmak teknik olarak dogru model secimi olmaz.
- Projede nasil anabiliriz:
  - Kisa bir teorik not dusup neden `classification` problemi icin linear regression yerine logistic regression tercih ettigimizi aciklayabiliriz.

#### Part 2: Logistic Regression from Scratch
- Kullanacagiz.
- Neden kullanmaliyiz:
  - Bu veri seti dogrudan `binary classification` oldugu icin en dogal baseline modellerden biridir.
  - Week 2 bilgisini dogrudan uygulamamizi saglar.
  - Hoca "neden bu yaklasimi sectiniz" diye sordugunda verilecek en temiz cevaplardan biridir.
  - MLP gibi daha karmasik modellerin gercekten gerekli olup olmadigini gormek icin guclu bir referans noktasi olusturur.
- Projedeki rolu:
  - Ilk ana baseline model olacak.
  - Tum diger modeller bu modelin sonuclariyla karsilastirilacak.

#### Part 3: Polynomial / Ridge tarzı genisletmeler
- Dogrudan ana odak olarak kullanmayacagiz.
- Neden kullanmiyoruz:
  - Bu kisim daha cok regresyon ve parametre cezalandirma mantigini gostermek icin yararlidir.
  - Bizim projede ayni regularization fikrini Week 4 altinda MLP uzerinde daha anlamli ve daha derin bir bicimde gosterebiliriz.
  - Projenin odagini dagitmadan daha guclu bir metodoloji kurmak istiyoruz.
- Projede nasil anabiliriz:
  - `L2 regularization` dusuncesinin erken bir versiyonu gibi kisa teorik baglanti kurulabilir.

#### Part 4: SGD / PyTorch Logistic Regression
- Kullanacagiz.
- Neden kullanmaliyiz:
  - Logistic regression'in hem teorik hem de uygulamali tarafini gostermemizi saglar.
  - PyTorch ile egitim akisini kurmak, sonraki MLP adimina duzgun gecis yaptirir.
  - Gradient tabanli optimizasyon mantigini tek veri seti uzerinde adim adim gosterebiliriz.
- Projedeki rolu:
  - Uygulamada baseline modeli daha duzenli ve yeniden kullanilabilir sekilde kurmak icin uygun olacak.

### Week 3

#### Part 1: XOR Problem and Why Linear Models Fail
- Dogrudan kullanmayacagiz.
- Neden kullanmiyoruz:
  - XOR ornegi egitsel bir kavram gosterisidir; dogrudan proje veri seti ustunde uygulanacak bir algoritma degildir.
  - Breast Cancer Wisconsin veri seti XOR gibi oyuncak bir problem degil, gercek bir tablo veri siniflandirma gorevidir.
- Projede nasil anabiliriz:
  - MLP'ye gecis yaparken "lineer modellerin sinirlarini asmak icin hidden layer ve nonlinear activation gerekir" fikrini teorik olarak burada baglayabiliriz.

#### Part 2: Activation Functions and Softmax
- Kismen kullanacagiz.
- Neden kullanmaliyiz:
  - MLP kurarken nonlinear activation dogrudan gerekli.
  - Aktivasyon fonksiyonlari olmadan cok katmanli yapi anlamli bir temsil gucu kazanamaz.
- Neyi kullanmayacagiz:
  - `Softmax`i ana yontem olarak kullanmayacagiz, cunku bizim problemimiz cok sinifli degil, iki sinifli.
  - Binary problem icin cikista `sigmoid` veya tek logit mantigi daha uygundur.
- Projedeki rolu:
  - Hidden layerlarda `ReLU`, cikista binary classification'a uygun yapi kullanacagiz.

#### Part 3: Build an MLP from Scratch
- Kullanacagiz.
- Neden kullanmaliyiz:
  - Logistic regression ile MLP arasindaki farki gostermek projenin ana teknik omurgasini olusturur.
  - Hoca yalnizca tek yontem degil, farkli yontemlerin karsilastirilmasini istiyor.
  - Bu kisim Week 3 bilgisini proje icine dogrudan tasir.
- Projedeki rolu:
  - Ikinci ana modelimiz olacak.
  - Logistic regression'a gore daha esnek ama ayni zamanda overfitting riski daha yuksek bir model olarak incelenecek.

#### Part 4: Shallow vs Deep / Architecture Comparison
- Sinirli sekilde kullanabiliriz.
- Neden tamamen odak yapmiyoruz:
  - Ana hedefimiz onlarca mimariyi denemek degil, secilen yontemlerin metodolojik etkisini gostermek.
  - Cok fazla mimari denemek projeyi genisletir ama derinligi azaltabilir.
- Neden kismen kullanabiliriz:
  - Tek bir ek karsilastirma olarak "kucuk MLP" ve "biraz daha genis MLP" deneyebiliriz.
  - Bu, model kapasitesi ile overfitting arasindaki iliskiyi gostermek icin faydali olabilir.

### Week 4

#### Part 1: Overfitting in Action
- Kullanacagiz.
- Neden kullanmaliyiz:
  - Veri seti orta-kucuk olcekte oldugu icin MLP ile overfitting gostermek mumkundur.
  - Week 4 tekniklerini neden uyguladigimizi aciklamanin en iyi yolu once problemi gostermektir.
- Projedeki rolu:
  - Plain MLP sonucunda train ve validation davranisini inceleyip regularization ihtiyacini gosterecegiz.

#### Part 2: L2 Regularization
- Kesinlikle kullanacagiz.
- Neden kullanmaliyiz:
  - Hoca metodolojik derinlik istiyor; regularization bu derinligi gosteren temel tekniklerden biridir.
  - Kucuk ve ozellik bazli veri setlerinde agirliklari kontrol altina almak genellemeyi iyilestirebilir.
  - Logistic regression ve MLP tarafinda teorik bag kurmamizi saglar.
- Projedeki rolu:
  - Plain MLP ile dogrudan karsilastirilacak ilk regularization deneyi olacak.

#### Part 3: L1 Regularization and Sparsity
- Muhtemelen kullanmayacagiz.
- Neden kullanmiyoruz:
  - Projenin temel hedefi fazla sayida yontem yigmak degil, secilen yontemleri derin anlatmaktir.
  - L1 ilginc bir teknik olsa da, bu projede `L2`, `dropout` ve `early stopping` ile zaten yeterli regularization karsilastirmasi kurabiliyoruz.
  - L1'i eklemek deney sayisini artirir ama sunum ve analiz yukunu de gereksiz sekilde buyutebilir.
- Ne zaman eklenebilir:
  - Zaman kalirsa bonus veya ek deney olarak denenebilir.

#### Part 4: Dropout From Scratch
- Kesinlikle kullanacagiz.
- Neden kullanmaliyiz:
  - Week 4'un en temel regularization tekniklerinden biridir.
  - MLP'de nöronlara asiri bagimliligi azaltarak genellemeyi iyilestirme ihtimali vardir.
  - Sunumda anlatmasi kolay ve teknik olarak anlamli bir yontemdir.
- Projedeki rolu:
  - `Plain MLP` ile `MLP + Dropout` arasindaki farki gosterecegiz.

#### Part 5: Early Stopping
- Kesinlikle kullanacagiz.
- Neden kullanmaliyiz:
  - Kucuk veri setlerinde en pratik ve etkili regularization yaklasimlarindan biridir.
  - Validation loss izleyerek gereksiz egitimi durdurmak, metodolojik olarak olgun bir deney kurdugumuzu gosterir.
  - Hocanin teknik derinlik beklentisine iyi uyar.
- Projedeki rolu:
  - En az bir modelde early stopping uygulanarak validation performansina gore egitimin durdurulmasi gosterilecek.

#### Part 6: Data Augmentation and Label Smoothing
- Kullanmayacagiz.
- Neden kullanmiyoruz:
  - Data augmentation daha cok goruntu verisi gibi yapisal veri tiplerinde anlamlidir.
  - Bizim veri setimiz tablo verisidir; goruntu benzeri augmentasyonlar burada dogal degildir.
  - Label smoothing de bu proje icin temel ihtiyac degil; daha cok buyuk veya daha karmasik siniflandirma yapilarinda anlam kazanir.

#### Part 7: Batch Normalization
- Istege bagli olarak kullanabiliriz.
- Neden kesin zorunlu degil:
  - Veri setimiz cok buyuk degil ve kuracagimiz MLP de asiri derin olmayacak.
  - Bu nedenle batch normalization'in katkisi sinirli kalabilir.
- Neden yine de dusunulebilir:
  - Eger plain MLP'nin egitimi dengesiz gorunurse veya ek bir Week 4 yontemi gostermek istersek guzel bir artidir.
- Projedeki rolu:
  - Ana cekirdek planda degil, zaman kalirsa ek deney olarak dusunulecek.

#### Part 8: Grand Comparison
- Kullanacagiz.
- Neden kullanmaliyiz:
  - Hocanin istedigi seylerden biri de birden fazla yontemi karsilastirip nedenlerini aciklamak.
  - Bu kisim tum projeyi tek tablo ve tek yorum seti uzerinde birlestirmemizi saglar.
- Projedeki rolu:
  - Tum modelleri ayni metriklerle karsilastiracagiz ve final teknik yorumu burada yapacagiz.

## Nihai Model Listesi
Projede karsilastirilacak ana modeller:

1. Logistic Regression (W2 P2)
2. Duz MLP (W3 P3)
3. MLP + L2 Regularization (W4 P2)
4. MLP + Dropout (W4 P4)
5. MLP + Early Stopping (W4 P5)

Istege bagli ek model:
6. MLP + Batch Normalization (W4 P7)

## Degerlendirme Metrikleri
Bu proje `binary classification` problemidir. Bu nedenle tek basina `accuracy` yeterli olmayacaktir. Degerlendirme, tum ana modeller icin ayni metriklerle yapilacaktir.

Tum modeller icin raporlanacak metrikler:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

MLP tabanli modeller icin ek olarak:
- Training loss egrisi
- Validation loss egrisi

Istege bagli ek metrik:
- ROC-AUC

## Cevaplamamiz Gereken Teknik Sorular
- `Logistic Regression (W2 P2)` bu veri seti icin neden guclu bir baseline?
- `Duz MLP (W3 P3)`, logistic regression'a anlamli bir ustunluk sagliyor mu?
- `Duz MLP (W3 P3)` overfit oluyor mu?
- `MLP + L2 (W4 P2)`, `MLP + Dropout (W4 P4)` ve `MLP + Early Stopping (W4 P5)` arasinda en iyi genelleme hangisinde goruluyor?
- Bu veri setinde daha karmasik model kullanmak gercekten gerekli mi, yoksa baseline model yeterli mi?

## Is Paketleri

### 1. Problem Tanimi
- Hedef degiskeni tanimla: `malignant` / `benign`
- Girdi ozelliklerini tanimla: tumor olcumlerinden gelen sayisal ozellikler
- Problemin `binary classification` oldugunu net sekilde yaz
- Proje amacini kisa ve teknik bir paragraf ile ifade et
- Neden bu veri setinin secildigini bir paragrafta acikla

### 2. Veri Anlama
- Veri setini yukle
- Boyut, ozellik adlari ve sinif dagilimini incele
- Eksik veri olup olmadigini kontrol et
- Gerekliyse temel gorsellestirmeler yap
- Ozellikleri egitimden once standardize et
- Bu asamanin ciktilarini tablo veya kisa not olarak kaydet

### 3. Veri Bolme
- Train, validation ve test bolumlerini olustur
- Tum modeller icin ayni bolme stratejisini kullan
- Adil karsilastirma icin ayni preprocessing adimlarini koru
- Gerekirse `stratified split` kullanarak sinif dengesini koru

### 4. Baseline Model: Logistic Regression (W2 P2)
- Logistic regression modelini kur
- Egit ve degerlendir
- Metrikleri ve confusion matrix sonucunu kaydet
- Sonraki tum modeller icin referans nokta olarak kullan
- Sonucunu tek bir baseline tablo satiri olarak hazirla

### 5. Sinir Agi Modeli: Duz MLP (W3 P3)
- PyTorch ile temel bir MLP kur
- `30 -> 32 -> 1` veya `30 -> 64 -> 32 -> 1` gibi sade bir mimari ile basla
- Binary cross-entropy tabanli kayip ile egit
- Sonuclari logistic regression ile dogrudan karsilastir
- Training ve validation davranisini incele
- Gerekirse overfitting belirtilerini not et

### 6. Regularization Deneyleri
- `MLP + L2 Regularization (W4 P2)` modelini kur
- `MLP + Dropout (W4 P4)` modelini kur
- `MLP + Early Stopping (W4 P5)` modelini kur
- Istege bagli olarak `MLP + Batch Normalization (W4 P7)` modelini ekle
- Her deneyde yalnizca ilgili farki degistir; diger ayarlari mumkun oldugunca sabit tut
- Hyperparameter secimlerini kisa teknik notlarla belgeleyerek ilerle

### 7. Sonuc Analizi
- Tum modeller icin bir karsilastirma tablosu hazirla
- Sonuclari teknik olarak yorumla
- Underfitting ve overfitting durumlarini tartis
- Hangi yontemin neden ise yaradigini veya yaramadigini acikla
- Nihai yorumu tek bir sonuc bolumunde topla
- Hoca icin en kritik soru olan "neden bu yontemi digerine tercih ettik" sorusuna acik cevap ver

### 8. Dokumantasyon
- Temiz bir README hazirla
- Notebooklari anlasilir ve duzenli tut
- Deney kurulumunu acik sekilde anlat
- Tekrarlanabilirlik icin random seed ve kutuphane listesini belirt
- Sonuc tablolarini ve varsa grafik dosyalarini tek yerde topla
- Her notebook'un bastan sona tek basina calisabildigini kontrol et

### 9. Sunum
- Problem tanimi ve motivasyon
- Veri seti ozeti
- Kullanilan yontemler ve week-part baglantilari
- Model karsilastirmalari
- Ana teknik bulgular
- Sonuc ve gelistirme alanlari
- Her model icin neden secildigi kisa ve net anlatilsin

## Onerilen Repo Yapisi
```text
project/
  data/
  notebooks/
    step1_data_understanding.ipynb
    step2_logistic_regression.ipynb
    step3_mlp.ipynb
    step4_regularization_experiments.ipynb
    step5_evaluation_and_comparison.ipynb
  outputs/
    figures/
    tables/
  README.md
  requirements.txt
  presentation.pdf
```

Dosya sorumluluklari:
- `step1_data_understanding.ipynb`: veri yukleme, inceleme, standardizasyon ve veri bolme
- `step2_logistic_regression.ipynb`: `Logistic Regression (W2 P2)` egitimi ve baseline sonucu
- `step3_mlp.ipynb`: `Duz MLP (W3 P3)` egitimi ve temel sinir agi sonuclari
- `step4_regularization_experiments.ipynb`: `MLP + L2 (W4 P2)`, `MLP + Dropout (W4 P4)`, `MLP + Early Stopping (W4 P5)` ve istege bagli `MLP + BatchNorm (W4 P7)`
- `step5_evaluation_and_comparison.ipynb`: tum modeller icin ortak metrik, grafik ve karsilastirma tablosu uretimi

Notebook kurallari:
- Her notebook en bastan calistirildiginda tek basina sonuc uretebilmeli
- Veri bolme mantigi tum notebook'larda ayni olmali
- Random seed sabit tutulmali
- Kod tekrarini azaltmak icin ortak hucre yapisi korunmali
- Gereksiz deneme hucreleri teslimden once temizlenmeli

## Uygulama Sirasi
1. Veri yukleme, inceleme ve preprocessing akisinin dogru calistigini dogrula
2. `Logistic Regression (W2 P2)` baseline modelini kur
3. `Duz MLP (W3 P3)` modelini kur
4. `MLP + L2 (W4 P2)`, `MLP + Dropout (W4 P4)` ve `MLP + Early Stopping (W4 P5)` deneylerini ekle
5. Tum sonuclari `step5_evaluation_and_comparison.ipynb` icinde tek tablo ve tek grafik setinde topla
6. README, teknik aciklamalar ve sunum dosyasini hazirla

## Basari Kriterleri
Projeyi basarili saymak icin:
- Kodun uctan uca temiz sekilde calismasi
- En az 5 modelin adil sekilde karsilastirilmasi
- Metriklerin acik sekilde raporlanmasi
- Raporda her yontemin neden secildiginin anlatilmasi
- Sunumun sadece skor gostermeyip teknik derinlik sunmasi
- Week 2, Week 3 ve Week 4 baglantilarinin acik sekilde gosterilmesi
- Notebook yapisinin duzenli, okunabilir ve bastan sona tekrar calistirilabilir olmasi

## Riskler ve Onlemler
- Risk: MLP, logistic regression'dan cok az daha iyi olabilir
  Onlem: Bunu basarisizlik gibi degil, anlamli bir teknik bulgu olarak sun

- Risk: Veri seti kucuk oldugu icin overfitting olabilir
  Onlem: Validation split, early stopping ve regularization kullan

- Risk: Proje gereksiz sekilde genisleyebilir
  Onlem: Tek veri seti ve birbiriyle dogrudan karsilastirilabilir yontemlerde kal

- Risk: Cok fazla ek deney ana hikayeyi zayiflatabilir
  Onlem: Cekirdek model listesine sadik kal, istege bagli modeli ancak zaman kalirsa ekle

## Hemen Sonraki Adimlar
1. Proje klasor yapisini olustur
2. `step1_data_understanding.ipynb` ile veri setini yukleyip incele
3. `step2_logistic_regression.ipynb` ile baseline modeli kur
4. `step3_mlp.ipynb` icin ilk MLP mimarisini belirle
5. Deney takibi icin ortak sonuc tablosu yapisini hazirla
