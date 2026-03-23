# 👤 KİŞİ 3: Düz MLP Modeli (Step 3)
**Görevi:** Karmaşıklığı artırdığımızda (Gizli Katmanlar eklendiğinde) başımıza ne geldiğini grafiklerle ispatlamak.

---

## 📽️ Slayt 7: Neden MLP? (Esneklik ve Kapasite)

Görsel: 
**plain_mlp_confusion_matrix.png**

Başlık: **Düz MLP Performansı: Karmaşıklık İşe Yaradı Mı?**

İstatistikler / Bulgular: 
*   **Mimarimiz:** 2 Gizli Katman (64 ve 32 Nöron), ReLU aktivasyonu.
*   **Accuracy Düşüşü:** %99.1'den (LogReg) -> **%98.2**'ye (MLP) düştü!
*   **Klinik Kayıp (Recall):** %98.8'den -> **%98.1**'e geriledik.

Teknik Karar / Metodolojik Gerekçe: 
*   **Model Kapasitesi:** Lojistik Regresyona (tek nöron) karşı, 64x32 nöronlu ağ çok daha "güçlüdür".
*   **Paradoks:** Modelin gücü artmasına rağmen başarısı neden DÜŞTÜ? Gizli katmanlar işe yaramadı mı?

Sonuç / Çıkarım (Inference):
**Klinik Tehdit:** Modelimiz hastaları daha "kötü" tespit etmeye başladı!

---

## 📽️ Slayt 8: Loss Curves (Overfitting'in Doğuşu)

Görsel: 
**plain_mlp_loss_curves.png**

Başlık: **Ezberleme (Overfitting) Teşhisi**

İstatistikler / Bulgular: 
*   **Yeşil Çizgi (Eğitim):** Training loss dibe vuruyor (Sürekli öğreniyor).
*   **Kırmızı Çizgi (Validation):** Belli bir Epoktan Sonra yükselişe geçiyor.
*   **Ayrışma (Gap):** Grafikteki "V/U şekli" ezberlemenin (Overfitting) başladığı yerdir.

Teknik Karar / Metodolojik Gerekçe: 
*   **Matematiksel Teşhis:** Model datadaki gerçek kuralları değil, training setindeki "gürültüyü" (noise) ezberlemiştir.
*   **Ağırlık Kontrolsüzlüğü:** Parametre sınırlandırılması (Regularization) olmadığı için ağ kontrolden çıkmıştır. 

Sonuç / Çıkarım (Inference):
**Köprü Soru:** Eğitim (Training) kaybımız sıfıra giderken, test (Validation) kaybımız artıyor! Bu ezberlemeyi durdurmak (Regularization) Kişi 4'ün görevidir.

---

> [!TIP]
> **Sunum İpucu (Kişi 3):** Hocanın en sevdiği yer burasıdır. Klasik öğrenci "Modelim çok iyi" der, profesyonel araştırmacı "Zorladım ve model patladı, işte grafiği!" der. Slayt 8'i sunarken yeşil çizgiyle kırmızı çizginin birbirinden ayrılmaya başladığı o "Ayrışma" anını parmağınızla gösterin ve gururla Overfit ettiğinizi anlatın. Daha sonra Kişi 4'e dönerek "Şimdi bu bozuk modeli Kişi 4 tamir edecek" deyin.
