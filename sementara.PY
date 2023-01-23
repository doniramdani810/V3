from PIL import Image
import pytesseract

# Membuka gambar capcha
image = Image.open(r"C:\Users\Doni\Downloads\t.png")

# Mengubah gambar capcha ke teks
text = pytesseract.image_to_string(image)

# Mencetak teks capcha
print(text)
