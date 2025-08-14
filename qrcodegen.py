import qrcode
import random
import os

# Create folder for saving QR codes
folder = "generated_qr"
os.makedirs(folder, exist_ok=True)

print("=== Simple QR Code Generator ===")
while True:
    data = input("\nEnter data (or press Enter to quit): ")
    if not data.strip():
        break
    filename = os.path.join(folder, f"qr_{random.randint(101,9999)}.png")
    qrcode.make(data).save(filename)
    print(f"QR code saved as {filename}")
