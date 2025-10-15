#  Matris Zar Oyunu (Python)

Bu proje, Python ile yazılmış **zar atma tabanlı bir matris simülasyonudur**.  
Kullanıcıdan matris boyutları alınır, matris rastgele sayılarla doldurulur ve her zar atışında belirli bir kurala göre matris güncellenir.  
Belirli bir satırın tüm elemanları `-1` olduğunda program sonlanır.

---

##  Proje Mantığı

1. Kullanıcı, matrisin **satır** ve **sütun** sayısını girer.  
2. Matris, `[2 - 35]` aralığında rastgele sayılarla oluşturulur.  
3. Her turda **3 zar atılır** (`1 - 6` arası).  
4. Zarların:
   - **En büyük**,  
   - **En küçük**,  
   - **Ortanca** değeri hesaplanır.  
5. Formül uygulanır: aranacak_değer = ortanca * en_büyük + en_küçük
6.  Bu değer matriste aranır:
- Eğer bulunursa o hücre **-1** yapılır.  
- Bulunmazsa bilgi mesajı bastırılır.  
7. Eğer bir satırın **tüm elemanları -1 olursa**, program durur.

##  Örnek Çıktı

Zarlar: 6, 5, 4  
Matris içinde aranacak değer: 34  
Matrisin 1. satırının 2. sütunu -1 yapıldı  

**Güncellenen Matris:**
[[-1 -1 -1]
[-1 2 -1]
[-1 -1 34]]

Matrisin 1. satırının tüm elemanları -1 olduğu için program sonlandırıldı.


