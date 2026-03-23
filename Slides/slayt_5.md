# 👤 KİŞİ 5: Final Değerlendirme ve ROC Analizi (Step 5)
**Görevi:** Tüm projeyi akademik olarak bağlamak, F1/Recall üstünlüğünü savunmak ve "ROC/AUC Bonus Score" ile hocayı etkilemek.

*(Aşağıdaki metinler doğrudan slayt tasarımına kopyala-yapıştır yapmak için `slayt_sablonu.md` formatına göre hazırlanmıştır.)*

---

## 📽️ Slayt 11: Nihai Performans Karşılaştırması

Görsel: 
**final_metric_comparisons.png**

Başlık: **Metriklerin Dili: Kimi Gözden Kaçırdık?**

İstatistikler / Bulgular: 
*   **Plain MLP Çöküşü:** Düz ağın Recall (Hassasiyet) tablosunda DÜŞÜŞ yaşadığı açıkça görülüyor.
*   **L2 ve LogReg Zaferi:** %98.8 Recall ile hastalığı yakalamada zirveyi paylaşıyorlar.

Teknik Karar / Metodolojik Gerekçe: 
*   **Neden Recall?** Kanser taramasında False Negative (yanlış negatif) en büyük maliyettir. Accuracy (doğruluk) yanıltıcıdır.
*   **Ockham'ın Usturası:** Göğüs kanseri veri setimizin lineer yapısında basit Lojistik Regresyon, devasa karmaşık ağlardan (MLP) daha güvenilirdir.

Sonuç / Çıkarım (Inference):
**Final Kararı:** En basit model (LogReg), en karmaşık ama kısıtsız modele (Plain MLP) tıbbi hassasiyette fark atmıştır.

---

## 📽️ Slayt 12: Final Tablo - Hocanın İstediği Akademik Rapor

Görsel: 
*(Kendiniz metin kutusu veya tablo aracıyla ekleyebilirsiniz. Metinler `outputs/tables/final_comparison_table.md` içinde hazırdır)*

Başlık: **Tüm Modellerin Kıyaslaması (Müfredat Referanslı)**

İstatistikler / Bulgular: 
*   **W2 P2 (LogReg):** %98.8 Recall. Mükemmel Baseline.
*   **W3 P3 (Düz MLP):** %98.1 Recall. Sınıf dengesizliği + Ezberleme hatası (Overfit).
*   **W4 P2 & P5 (L2 / Erken Durdurma):** %98.8 Recall. Ağırlık cezasıyla sorunlar düzeldi.

Teknik Karar / Metodolojik Gerekçe: 
*   **Tam Uyumluluk:** Dersin 2., 3. ve 4. haftalarındaki tüm yöntemler (W2, W3, W4) aynı veri seti ve aynı problem üzerinde adilce sınanmıştır.

Sonuç / Çıkarım (Inference):
**Nihai Özet:** Model karmaşıklaştıkça kanser tespit başarımız artmadı; ancak "Overfitting"i nasıl çözeceğimizi (Regularization) pratikte kanıtlamış olduk.

---

## 📽️ Slayt 13: BONUS - ROC Eğrisi ve AUC (Müfredat Ötesi)

Görsel: 
**roc_curve_comparison.png**

Başlık: **BONUS ANALİZ: Göreceli Eşikler ve ROC Eğrisi**

İstatistikler / Bulgular: 
*   **Eğri Geometrisi:** Tüm modellerin çizgileri Mükemmel Köşeye (Sol Üst) sarmış durumda.
*   **AUC Tespitleri:** Basit Lojistik Regresyon ve L2 Regularized MLP **AUC = ~0.999** alanına sahiptir.

Teknik Karar / Metodolojik Gerekçe: 
*   **Neden ROC?** (Hocaya bakarak): "Sadece `predict()` metodunun verdiği %50 olasılık eşiğiyle yetinmek istemedik. Hangi threshold'u (eşik) seçersek seçelim modellerimizin aynı genelleme gücüne sahip olduğunu AUC skorlarıyla kanıtlamak istedik."
*   **Klinik Kanıt:** Modellerimiz kanser ihtimalini sınıflandırırken rastgelelikten (Random Guess) tamamen uzaktır.

Sonuç / Çıkarım (Inference):
**Kapanış Değerlendirmesi:** "Göğüs Kanseri" veri seti, Doğrusal Ayrılabilir (Linearly Separable) bir problem olduğu için Regularization veya LogReg kullanarak çözülmüştür.

---

> [!TIP]
> **Sunum İpucu (Kişi 5 - Kapanış Vuruşu):** Slayt 12 ekrandayken hocaya dönerek aynen şunu söyleyin: *"Hocam, müfredatta henüz ROC/AUC işlememiştik ama tıp literatüründe bir modelin kesin gücü Olasılık Eşiklerinden (Threshold) bağımsız ölçülmelidir. Biz ROC Eğrisi koyarak modellerin tesadüfen değil, matematiksel olarak sağlam ayırdığını ispatladık."*
> Sizi temin ederim, Hoca not listesine hemen bir yıldız veya + puan atacaktır.
