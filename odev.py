"""
Fizik 1 Laboratuvarı - Geometrik Cisimlerin Yoğunluk ve Hata Analizi
Bu script; silindir ve dikdörtgenler prizması için hacim, yoğunluk, 
bağıl hata ve yüzde hata hesaplamalarını hata yayılması kurallarına göre yapar.
"""

import math

def silindir_hesapla(r, delta_r, h, delta_h, m, delta_m):
    """
    Silindir cisim için hacim, yoğunluk ve hata hesaplaması yapar.
    
    Parametreler:
    r (float): Silindirin yarıçapı (cm)
    delta_r (float): Yarıçap ölçümünün hassasiyeti / hata payı (cm)
    h (float): Silindirin yüksekliği (cm)
    delta_h (float): Yükseklik ölçümünün hassasiyeti / hata payı (cm)
    m (float): Cismin kütlesi (g)
    delta_m (float): Terazi hassasiyeti / kütle hata payı (g)
    """
    print("=" * 45)
    print("       SİLİNDİR HESAPLAMA SONUÇLARI")
    print("=" * 45)
    
    # Hacim formülü: V = pi * r^2 * h
    V = math.pi * (r ** 2) * h
    
    # Hacim bağıl hatası (r'nin karesi alındığı için katsayısı 2 olur)
    bagil_hata_V = 2 * (delta_r / r) + (delta_h / h)
    delta_V = V * bagil_hata_V
    
    # Yoğunluk formülü: rho = m / V
    rho = m / V
    
    # Yoğunluk bağıl hatası (Kütle hatası + Hacim bağıl hatası)
    bagil_hata_rho = (delta_m / m) + bagil_hata_V
    delta_rho = rho * bagil_hata_rho
    yuzde_hata = bagil_hata_rho * 100
    
    print(f"Hacim (V)         : {V:.4f} cm³ ± {delta_V:.4f}")
    print(f"Yoğunluk (ρ)      : {rho:.4f} g/cm³ ± {delta_rho:.4f}")
    print(f"Bağıl Hata        : {bagil_hata_rho:.5f}")
    print(f"Yüzde Hata        : %{yuzde_hata:.2f}")
    print("-" * 45 + "\n")

def prizma_hesapla(a, delta_a, b, delta_b, c, delta_c, m, delta_m):
    """
    Dikdörtgenler prizması için hacim, yoğunluk ve hata hesaplaması yapar.
    
    Parametreler:
    a, b, c (float): Prizmanın kenar uzunlukları (cm)
    delta_a, delta_b, delta_c (float): Kenar ölçümlerinin hassasiyetleri (cm)
    m (float): Cismin kütlesi (g)
    delta_m (float): Terazi hassasiyeti / kütle hata payı (g)
    """
    print("=" * 45)
    print("   DİKDÖRTGENLER PRİZMASI HESAPLAMA SONUÇLARI")
    print("=" * 45)
    
    # Hacim formülü: V = a * b * c
    V = a * b * c
    
    # Hacim bağıl hatası
    bagil_hata_V = (delta_a / a) + (delta_b / b) + (delta_c / c)
    delta_V = V * bagil_hata_V
    
    # Yoğunluk formülü: rho = m / V
    rho = m / V
    
    # Yoğunluk bağıl hatası
    bagil_hata_rho = (delta_m / m) + bagil_hata_V
    delta_rho = rho * bagil_hata_rho
    yuzde_hata = bagil_hata_rho * 100
    
    print(f"Hacim (V)         : {V:.4f} cm³ ± {delta_V:.4f}")
    print(f"Yoğunluk (ρ)      : {rho:.4f} g/cm³ ± {delta_rho:.4f}")
    print(f"Bağıl Hata        : {bagil_hata_rho:.5f}")
    print(f"Yüzde Hata        : %{yuzde_hata:.2f}")
    print("-" * 45 + "\n")

# Ana Çalıştırma Alanı
if __name__ == "__main__":
    print("\nFizik 1 Lab - Yoğunluk ve Hata Analizi Programı Başlatıldı...\n")
    
    # ÖRNEK 1: Silindir (Kendi lab ölçümlerinizle buradaki sayıları güncelleyin)
    # Örn: Yarıçap = 1.5 cm (Hata: 0.05 cm), Yükseklik = 5.0 cm (Hata: 0.05 cm), Kütle = 45.2 g (Hata: 0.01 g)
    silindir_hesapla(
        r=1.5,      delta_r=0.05, 
        h=5.0,      delta_h=0.05, 
        m=45.2,     delta_m=0.01
    )
    
    # ÖRNEK 2: Dikdörtgenler Prizması (Kendi lab ölçümlerinizle buradaki sayıları güncelleyin)
    # Örn: Kenarlar = 2.0, 3.0, 4.0 cm (Hata: 0.05'er cm), Kütle = 96.0 g (Hata: 0.01 g)
    prizma_hesapla(
        a=2.0,      delta_a=0.05, 
        b=3.0,      delta_b=0.05, 
        c=4.0,      delta_c=0.05, 
        m=96.0,     delta_m=0.01
    )
