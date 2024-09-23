import math

# Adım 1: Noktaları temsil eden demetlerin bulunduğu points listesi
points = [(1, 2), (3, 4), (5, 6), (7, 8)]  # Örnek olarak 4 nokta verdim

# Adım 2: Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Adım 3: Tüm nokta çiftleri arasındaki mesafeleri saklamak için distances listesi
distances = []

# Adım 4: Her nokta çifti arasındaki mesafeyi hesapla ve distances listesine ekle
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Adım 5: Minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print("Minimum mesafe:", min_distance)
