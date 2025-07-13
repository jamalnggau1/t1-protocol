# 🌉 T1 Protocol - ETH Bridge Automation (Base ↔ Arbitrum, Testnet)

Skrip Python ini digunakan untuk mengotomatisasi bridging ETH dari jaringan **Base** ke **Arbitrum** (dan sebaliknya, jika diaktifkan), menggunakan banyak wallet, dan berjalan berulang setiap 6 jam secara otomatis.

---

## 🚀 Fitur

- 🔁 Kirim ETH dari Base ke Arbitrum
- 🔄 Opsi transaksi bolak-balik (Arbitrum ke Base)
- ⏱️ Loop otomatis setiap 6 jam
- 🧾 Dukungan multi-wallet (`wallets.txt`)
- ⚖️ Cek saldo sebelum transaksi
- 🧯 Bisa dihentikan kapan saja dengan `Ctrl + C`

---

## 📦 Kebutuhan

- Python 3.8+
- Library:
  ```bash
  pip install web3
📂 Cara Menggunakan
Buat file wallets.txt dan isi dengan private key wallet (satu per baris):

Copy
Edit
0xabc123...
0xdef456...
Jalankan script:

bash
Copy
Edit
python t1_protocol.py
Masukkan input yang diminta:

Berapa kali loop bridge per wallet

Jumlah ETH per transaksi

Apakah ingin bolak-balik (y/n)



⚙️ Konfigurasi
Edit langsung di file main.py:

RPC Testnet (Base dan Arbitrum harus disediakan oleh RPC yang mendukungnya, contoh pakai ZAN RPC untuk Base Sepolia):

python
Copy
Edit
RPC_URL = "https://api.zan.top/node/v1/eth/sepolia/..."
Alamat tujuan bridge:

python
Copy
Edit
TO_A = "0x..."  # Alamat kontrak Arbitrum
TO_B = "0x..."  # Alamat kontrak Base
🔁 Siklus Otomatis
Semua wallet akan diproses satu per satu

Setelah selesai semua, script akan menunggu 6 jam

Kemudian semua transaksi akan diulang otomatis

⚠️ Disclaimer
❗ Skrip ini ditujukan hanya untuk keperluan edukasi dan testnet.

Jangan gunakan private key utama atau wallet dengan dana penting.

Penulis tidak bertanggung jawab atas kerugian atau kesalahan penggunaan.

📄 Lisensi
MIT License

