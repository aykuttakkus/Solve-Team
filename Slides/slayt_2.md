# 👤 KİŞİ 2: Logistic Regression (Step 2)
**Görevi:** İlk algoritmayı savunmak ve baseline sonuçlarını sunmak.

*(Aşağıdaki metinler doğrudan slayt tasarımına kopyala-yapıştır yapmak için `slayt_sablonu.md` formatına göre hazırlanmıştır.)*

---

## 📽️ Slayt 5: Neden Lojistik Regresyon? (Lineer Ayrılabilirlik)

Görsel: 
**linear_separability_check.png** (Tasarımın SAĞ tarafına büyük oturacak)

Başlık: **Neden Lojistik Regresyon? Geometrik İspat**

İstatistikler / Bulgular: 
*   **Ayrılabilirlik:** `worst concave points` vs `worst perimeter` (Net çapraz çizgi).
*   **Sınıflar:** Malignant vs Benign belirgin şekilde kopuk.
*   **Naive Baseline:** Hedef asgari %63 (Kör model Benign tahmini).

Teknik Karar / Metodolojik Gerekçe: 
*   **Neden LogReg?** Verideki bu "lineer" (doğrusal) yapı, Sigmoid fonksiyonu için mükemmel bir geometrik zemin hazırlıyor.
*   **Metodoloji:** Karmaşık ağlardan (MLP) önce basit bir baz modeli (baseline) şarttır.

Sonuç / Çıkarım (Inference):
**Klinik Tahmin:** Lojistik Regresyon, lineer ayrılabilirliğiyle en güçlü ve yorumlanabilir referans noktamızdır.

---

## 📽️ Slayt 6: Lojistik Regresyon Sonuçları (Baseline Zaferi)

Görsel: 
**logreg_confusion_matrix.png** (Tasarımın SAĞ tarafına büyük oturacak)

Başlık: **Baseline Zaferi: Tek Bir Nöronun Gücü**

İstatistikler / Bulgular: 
*   **Accuracy:** %99.1
*   **F1-Score:** %99.0
*   **Recall (Duyarlılık):** %98.8
*   **Confusion Matrix:** Neredeyse sıfır "Gözden Kaçırma" (False Negative).

Teknik Karar / Metodolojik Gerekçe: 
*   **Sınıf Dengesizliği:** %37 vs %63 durumunda Accuracy yanıltıcıdır.
*   **Klinik Karar:** Tıbbi risk (kanser) sebebiyle Accuracy değil, Recall (Hassasiyet) hedeflendi.
*   **Baseline'ı Kırmak:** %63 Naif tahmin, tek bir Sigmoid nöronuyla paramparça edildi.

Sonuç / Çıkarım (Inference):
**Köprü Soru:** Tek bir nöron %99 ise; gizli katmanlar (MLP) modeli geliştirecek mi, yoksa ezberletecek mi (Overfit)?

---

> [!TIP]
> **Sunum İpucu (Kişi 2):** Son cümledeki ("Tek bir nöron %99'a ulaşıyorsa...") ifadeyi direkt hocaya bakarak retorik bir soru şeklinde sorup, sözü Kişi 3'e devredin. Etkisi muazzam olacaktır.
