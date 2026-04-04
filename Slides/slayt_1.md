# 👤 KİŞİ 1: Giriş, Problem ve Veri Hazırlığı (Step 1)
**Görevi:** Projeyi başlatmak, veri setini ve neden bizde olduğunu anlatmak.

---

## 📽️ Slayt 1: Neden Bu Veri Setini Seçtik? (Müfredat Uyumu)
*   **Aİ Önerileri:** `load_iris()`, `load_wine()` gibi seçenekler değerlendirildi.
*   **Seçilme Nedeni:** 2 sınıf (Binary) oluşu Week 2 teorisiyle, 30 özellik (Complexity) oluşu Week 3 MLP mimarisiyle tam uyumludur.

---

## 📽️ Slayt 2: Problem Tanımı ve Motivasyon
**Görsel:** [class_distribution.png](../../outputs/figures/step1/class_distribution.png)

*   **İstatistikler:**
    *   **Veri Seti:** UCI Breast Cancer Wisconsin.
    *   **Örnek Sayısı:** 569 örnek / 30 özellik.
*   **Hedef:** Tıbbi öznitelikleri kullanarak kitlenin iyi (Benign) veya kötü (Malignant) huylu oluşunu tahmin etmek.

---

## 📽️ Slayt 3: Veri Özeti ve Preprocessing (Scaling Gerekçesi)
**Görsel:** [top_features_distribution.png](../../outputs/figures/step1/top_features_distribution.png)

*   **Sayısal Kanıtlar:** `mean area` (max: 2501.0) vs `smoothness error` (min: 0.0017).
*   **Stratejik Hazırlık:** Planlanan **Lojistik Regresyon** ve **MLP** modelleri gradyan tabanlıdır. Ölçek farkları gradyan güncelleme hızlarını bozacağı için **StandardScaler** (Z-Score) kullanılmıştır.
*   **Veri Akışı:** Bilgi sızmasını (leakage) önlemek için scaling sadece eğitim verisi üzerinden fit edilmiştir.

---

## 📽️ Slayt 4: Öznitelik İlişkileri ve Stratejik Çıkarım
**Görsel:** [top_feature_correlation_heatmap.png](../../outputs/figures/step1/top_feature_correlation_heatmap.png)

*   **İstatistiksel Bulgular:**
    *   **Hedef Korelasyonu:** `worst concave points` (**-0.79**) ve `worst perimeter` (**-0.78**) hedef değişkenle en güçlü bağa sahip özniteliklerdir.
    *   **Multicollinearity Tespiti:** `mean radius` ve `mean perimeter` arasındaki **+0.99** korelasyon, veride "redundant" (gereksiz tekrar eden) bilgi olduğunu kanıtlar.
*   **Teknik Karar (Geleceğe Yatırım):**
    *   **Risk:** Yüksek korelasyonlu öznitelikler, modelin belirli ağırlıklara aşırı güvenmesine (Overfitting) yol açar.
    *   **Week 4 Bağlantısı:** Verideki bu "çoklu bağlantı" (multicollinearity) yapısı, Week 4'te uygulayacağımız **L2 Regularization** (Ağırlık Cezalandırma) ihtiyacının temel teknik gerekçesidir.
*   **Çıkarım:** Step 1'deki bu analiz, projenin final aşamasındaki (Week 4) genelleştirme stratejimizi şimdiden belirlememizi sağlamıştır.

> [!TIP]
> **Sunum İpucu (Kişi 1):** Sadece "korelasyon var" demek yerine, "Bakın bu yüksek korelasyon nedeniyle 4. haftadaki modelimizde L2 Regularization kullanarak overfitting'i engelleyeceğiz" derseniz sunumunuzun teknik derinliği hocanın beklentisinin üzerine çıkacaktır.
