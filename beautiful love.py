import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle
import random

# Siapkan figure dengan ukuran yang cukup besar
plt.figure(figsize=(12, 10))
plt.axis('equal')

# Fungsi untuk membuat bentuk love
def love_shape(t):
    x = 16 * (np.sin(t) ** 3)
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

# Buat parameter t
t = np.linspace(0, 2*np.pi, 1000)
x, y = love_shape(t)

# Warna-warni untuk love shape - gradien dari merah muda ke merah
colors = np.linspace(0, 1, len(x))
cmap = LinearSegmentedColormap.from_list("love_colors", ['#FF69B4', '#FF1493', '#FF0000'])

# Plot love shape dengan gradien warna
plt.scatter(x, y, c=colors, cmap=cmap, s=30, edgecolor='none', alpha=0.8)

# Isi bentuk love dengan warna
plt.fill(x, y, color='#FF69B4', alpha=0.3)

# Tambahkan outline yang lebih tebal untuk bentuk love
plt.plot(x, y, color='#FF1493', linewidth=2.5)

# Fungsi untuk menambahkan hiasan bunga
def add_flower(x, y, size, color):
    angles = np.linspace(0, 2*np.pi, 6, endpoint=False)
    for angle in angles:
        dx = size * np.cos(angle)
        dy = size * np.sin(angle)
        plt.plot([x, x+dx], [y, y+dy], color=color, linewidth=1.5)
    circle = Circle((x, y), size/3, color=color, alpha=0.7)
    plt.gca().add_patch(circle)

# Fungsi untuk menambahkan bintang
def add_star(x, y, size, color):
    angles = np.linspace(0, 2*np.pi, 10, endpoint=False)
    xs, ys = [], []
    for i, angle in enumerate(angles):
        r = size if i % 2 == 0 else size/2.5
        xs.append(x + r * np.cos(angle))
        ys.append(y + r * np.sin(angle))
    plt.fill(xs, ys, color=color, alpha=0.7, edgecolor='white', linewidth=0.5)

# Pallete warna untuk hiasan
pastel_colors = ['#FFD1DC', '#FFADAD', '#FFD6A5', '#FDFFB6', '#CAFFBF', '#9BF6FF', '#A0C4FF', '#BDB2FF', '#FFC6FF']

# Tambahkan hiasan bunga di sekitar love shape
for _ in range(25):
    angle = random.uniform(0, 2*np.pi)
    radius = random.uniform(20, 35)
    flower_x = radius * np.cos(angle)
    flower_y = radius * np.sin(angle)
    flower_size = random.uniform(1.5, 3)
    flower_color = random.choice(pastel_colors)
    add_flower(flower_x, flower_y, flower_size, flower_color)

# Tambahkan hiasan bintang di sekitar love shape
for _ in range(15):
    angle = random.uniform(0, 2*np.pi)
    radius = random.uniform(22, 40)
    star_x = radius * np.cos(angle)
    star_y = radius * np.sin(angle)
    star_size = random.uniform(0.8, 1.5)
    star_color = random.choice(pastel_colors)
    add_star(star_x, star_y, star_size, star_color)

# Tambahkan titik-titik kecil sebagai glitter di sekitar love
for _ in range(200):
    angle = random.uniform(0, 2*np.pi)
    radius = random.uniform(5, 45)
    glitter_x = radius * np.cos(angle)
    glitter_y = radius * np.sin(angle)
    plt.scatter(glitter_x, glitter_y, s=random.uniform(1, 5), 
                color=random.choice(pastel_colors), alpha=random.uniform(0.5, 1))

# Tambahkan lingkaran kecil di dalam bentuk love
for _ in range(50):
    angle = random.uniform(0, 2*np.pi)
    radius = random.uniform(0, 12)
    inner_x = radius * np.cos(angle)
    inner_y = radius * np.sin(angle) * 0.8  # Sesuaikan dengan bentuk love
    if inner_y > -5:  # Hanya tampilkan di bagian dalam love
        plt.scatter(inner_x, inner_y, s=random.uniform(5, 20), 
                    color=random.choice(['white', '#FFD1DC', '#FFC6FF']), 
                    alpha=random.uniform(0.3, 0.7))

# Tambahkan latar belakang gradien
background = np.random.random((100, 100))
plt.imshow(background, cmap=LinearSegmentedColormap.from_list("bg", ['#FFEFFD', '#F9F2FF']), 
           extent=[-45, 45, -45, 45], alpha=0.3, aspect='auto')

# Sembunyikan sumbu
plt.axis('off')

# Tambahkan judul
plt.title('Beautiful Love', fontsize=20, fontweight='bold', color='#FF1493', 
          fontname='Comic Sans MS', pad=20)

# Tampilkan gambar
plt.tight_layout()
plt.show()
