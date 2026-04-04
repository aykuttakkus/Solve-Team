# 👤 KİŞİ 4: Regularization (Ezberleme Kontrolü)
**Görevi:** Kişi 3'ün "Ağımız ezberledi ve çöktü" diyerek bıraktığı modeli "Düzeltici Tekniklerle (Regularization)" ayağa kaldırmak.

*(Aşağıdaki metinler doğrudan slayt tasarımına kopyala-yapıştır yapmak için `slayt_sablonu.md` formatına göre hazırlanmıştır.)*

---

## 📽️ Slayt 9: L2 Yöntemi (Weight Decay) Bizi Nasıl Kurtardı?

Görsel: 
**regularized_loss_curves.png** 

Başlık: **Overfit Çözümü 1: L2 Regularization (Ağırlık Cezası)**

İstatistikler / Bulgular: 
*   **Kanama Durdu:** Düz MLP'de gerileyen Score tekrar %99.0 seviyesine (Lojistik limitine) fırladı.
*   **Gap (Boşluk) Kapandı:** Kayıp eğrisindeki (Loss Curve) o korkunç makas daraldı.
*   **Recall Kurtarılması:** Kanser teşhisindeki %98.1'lik düşüş tekrar %98.8'e kurtarıldı.

Teknik Karar / Metodolojik Gerekçe: 
*   **Neden L2?** Kişi 1'in öngördüğü Multicollinearity (Çoklu Bağlantı) problemi ağı ezberlemeye itmişti. L2 ağırlık cezasıyla bu hileyi matematiksel olarak yasakladık.
*   **Ağır Ceza (Alpha):** `alpha=0.1` gibi sert bir penaltı vererek modeli genellemeye zorladık.

Sonuç / Çıkarım (Inference):
**Matematiksel Teşhis:** Ağırlıkların aşırı büyümesini cezalandırarak (L2), modelimizin gürültüyü ezberlemesini kalıcı olarak durdurduk.

---

## 📽️ Slayt 10: Deney 2 - Erken Durdurma (Early Stopping)

Görsel: 
*(Gerekiyorsa aynı regularized_loss_curves.png görselinin sağ tarafındaki subplot gösterilir)*

Başlık: **Overfit Çözümü 2: Early Stopping (Sabır Mekanizması)**

İstatistikler / Bulgular: 
*   **Mükemmel Geri Dönüş:** L2 ile aynı şekilde %98.8'lik Recall skoruna geri dönüldü.
*   **Durdurma Noktası:** Doğrulama kaybının (Validation loss) artmaya başladığı noktada ağırlıklar donduruldu.
*   **Zaman ve İvme:** Model 200 epok beklemeden hedefine minimum işlem gücüyle ulaştı.

Teknik Karar / Metodolojik Gerekçe: 
*   **Neden Early Stopping?** Ağırlıkları ezmeye değil, modelin "ezberlemeye" (memorization) başladığı saniyeyi radarda tespit edip eğitimi anında kesmeye odaklandık.
*   **Patience (Sabır):** 10 epok bekleme süresiyle modelin "belki iyileşir" ihtimali kontrollü test edildi.

Sonuç / Çıkarım (Inference):
**Klinik Kurtarma:** Hem L2 hem de Early Stopping ağın klinikte çökmesini engelledi. Sözü nihai karşılaştırma için Kişi 5'e bırakıyorum.

---

> [!TIP]
> **Sunum İpucu (Kişi 4):** Slayt 9'u sunarken doğrudan Kişi 1'in sunumuna atıf yapın. *"Hatırlarsanız en başta Kişi 1, verimizde +0.99 korelasyon bulmuştu. İşte o zehirli veri MLP'de ezberlemeye yol açtı. Ben de L2 Regularization (Weight Decay) ile o zehri temizledim"* derseniz hoca takım çalışmasına ve teknik derinliğe tam puan verecektir.
