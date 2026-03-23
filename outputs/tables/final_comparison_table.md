# Proje Final Karşılaştırma Tablosu (Aşama 6 Teslimi)

| Model Adı | Müfredat Referansı | Accuracy (%) | Precision (%) | Recall (Hassasiyet) (%) | F1-Score (%) | Kısa Yorum (Metodolojik Sonuç) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | W2 P2 | %99.1 | %99.3 | **%98.8** | %99.0 | Mükemmel Baseline. Lineer ayrılabilir veride tek nöronla ulaşılan tavan performans. |
| **Düz MLP (Plain)** | W3 P3 | %98.2 | %98.1 | %98.1 | %98.1 | Aşırı kapasite + Çoklu Bağlantı (Multicollinearity) birleşince gürültüyü ezberledi (Overfit). Recall düştü. |
| **MLP + L2 Regularization** | W4 P2 | %99.1 | %99.3 | **%98.8** | %99.0 | Ağırlık cezasıyla (Weight Penalty) çoklu bağlantı problemi çözüldü, ezberleme durdu. İlk limitlere (baseline) geri dönüldü. |
| **MLP + Early Stopping** | W4 P5 | %99.1 | %99.3 | **%98.8** | %99.0 | Validation Loss yükselmeden eğitim kesilerek (Sabır: 10) L2 ile aynı genelleme gücüne daha hızlı ulaşıldı. |
