# Mükemmel Sunum Slaytı Şablonu (Harvard/Hoca Standartı)

Gönderdiğiniz 3 görseli (Step 1) inceledim. Gözlemlediğim kadarıyla slaytlarınızın inanılmaz derecede profesyonel ve belirgin bir "Izgara (Grid)" yapısı var. Tasarımlar mükemmel bir **[Teori (Sol) + Kanıt (Sağ)]** dengesine oturmuş. 

İşte tüm projede (Step 2, 3, 4, 5) kullanacağımız ve bu tasarımı otomatik olarak besleyecek o **standart metin şablonumuz**:

---

## 📄 Şablon Formatı (Kopyala-Yapıştır İçin)

```text
Görsel: 
[Görselin dosya adı, örn: logreg_confusion_matrix.png] (Tasarımın SAĞ tarafına büyük oturacak)

Başlık: [Slaytın Ana Vurgusu, örn: Lojistik Regresyon Başarısı ve Tıbbi Riskler] (Tasarımın SOL ÜST tarafına)

İstatistikler / Bulgular: (ASLA UZUN CÜMLE KURMA! Sadece anahtar kelime, sayı, kısa not. Ekranda okumayacağız, üstüne konuşacağız!)
* [Kısa Veri/Bilgi 1]
* [Kısa Veri/Bilgi 2]

Teknik Karar / Metodolojik Gerekçe: (Hoca için 1-2 teknik kelime, kısa vurgu)
* Neden: [Kısa Gerekçe 1]
* Risk: [Kısa Gerekçe 2]

Sonuç / Çıkarım (Inference): (Ekranın altında vurucu tek bir kısa cümle)
[Maksimum 5-6 kelimelik sonuç]
```

---

## 🔍 Görsellerin Analizi ve Şablonun Mantığı

Gönderdiğiniz harika tasarımları analiz ettiğimde şu matematiksel dizilimi görüyorum:

1.  **Ana Başlık (Top Left):** Çok büyük ve kalın fontlarla, olayın ne olduğunu süzüyor. *(Örn: "Feature Relationships and Strategic Insight")*
2.  **Veritabanı / İstatistikler (Middle Left):** Madde işaretleriyle (bullet points) sayısal kanıtları sunuyor. Slaytın can damarı burası.
3.  **Teknik Karar Düğümü (Bottom Left):** Hocanızın "Neden bunu yaptınız?" sorusunu cevaplayan o akademik kısım. *(Örn: "Why StandardScaler?", "Technical Decision (Future-Oriented)")*. İşte bu kısım bizi diğer takımlardan ayıracak o jargonlu kısım.
4.  **Matematiksel Kanıt (Right):** Ekranın en az %50'sini kaplayan devasa bir Python çıktısı. (Histogram, Scatter, Heatmap vs.)
5.  **Kapanış Cümlesi (Bottom Right/Center):** O slayttan cepte neyle çıkılacağını söyleyen net mesaj. *(Örn: "Result: We normalize the data to mean = 0 and std = 1 to ensure a fair learning process.")*

Bütün slaytları bu şablona dökerek "Slayt Metinleri" hazırladığımızda, siz de tasarım aracınıza (Canva vb.) bu formatı doğrudan hızla girebileceksiniz. Şablon `Slides/` klasörüne **`slayt_sablonu.md`** adıyla kaydedilmiştir.
