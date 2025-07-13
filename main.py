from web3 import Web3
import time

# === SETUP ===

RPC_URL = "https://api.zan.top/node/v1/eth/sepolia/"  # ganti RPC testnet kamu

TO_A = "0x56cEede20DBd2A1E3DA44dA81fEbc71734019fD0"
TO_B = "0x1234567890123456789012345678901234567890"

loop_count = int(input("Berapa kali loop bridge? "))
amount = float(input("Jumlah ETH per bridge? "))
bolak_balik = input("Apakah ingin bolak-balik? (y/n): ").lower() == "y"

# === BACA WALLET ===

with open("wallets.txt", "r") as f:
    private_keys = [line.strip() for line in f if line.strip()]

# === FUNGSI BRIDGE ===

def send_bridge(w3, account, to_address, amount_eth):
    sender = account.address
    nonce = w3.eth.get_transaction_count(sender, "pending")
    tx = {
    "from": sender,
    "to": to_address,
    "value": w3.to_wei(amount_eth, "ether"),
    "gas": 100000,
    "gasPrice": w3.to_wei("3", "gwei"), # atau "10" jika masih lambat
    "nonce": nonce,
    "chainId": w3.eth.chain_id
    }


    signed_tx = w3.eth.account.sign_transaction(tx, private_key=account.key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"  🚀 Tx terkirim: {w3.to_hex(tx_hash)}")

    try:
        print("  ⏳ Menunggu konfirmasi...")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=300, poll_latency=5)
        print(f"  ✅ Terkonfirmasi di block {receipt.blockNumber}")
    except Exception as e:
        print(f"  ⚠️ Transaksi pending terlalu lama. Error: {e}")
        print(f"  ⏸️ Lanjut ke transaksi berikutnya...")

    


# === LOOP PER WALLET ===
while True:
    try:
        for pk in private_keys:
            print(f"\n🧾 Wallet baru\n======================")
            w3 = Web3(Web3.HTTPProvider(RPC_URL))
            account = w3.eth.account.from_key(pk)
            sender = account.address
            balance = w3.eth.get_balance(sender)
            balance_eth = w3.from_wei(balance, "ether")
            print(f"🔑 {sender}")
            print(f"💰 Saldo: {balance_eth} ETH")

            # === CEK SALDO MENCUKUPI UNTUK 1 LOOP ===
            gas_limit = 100000
            gas_price = w3.to_wei("3", "gwei")
            total_per_tx = w3.to_wei(amount, "ether") + gas_limit * gas_price
            max_tx = 2 if bolak_balik else 1
            total_biaya_1_loop = total_per_tx * max_tx

            if balance < total_biaya_1_loop:
                print("❌ Saldo tidak cukup untuk 1 loop (Base dan Arb). Wallet dilewati.\n")
                continue

            # === LOOP BRIDGE ===
            for i in range(loop_count):
                print(f"\n🔁 Loop {i+1}/{loop_count} - Wallet: {sender}")
                print("🚀 Kirim ke Arb...")
                send_bridge(w3, account, TO_A, amount)

                if bolak_balik:
                    print("🔄 Kirim balik ke Base")
                    send_bridge(w3, account, TO_B, amount)
                time.sleep(2)

        print("\n✅ Semua selesai!")
        print("⏳ Menunggu 6 jam sebelum mengulang semua wallet...\n")
        time.sleep(21600) 
    except KeyboardInterrupt:
        print("\n🛑 Dihentikan oleh pengguna. Keluar dengan aman...")
        break
    except Exception as e:
        print(f"⚠️ Terjadi kesalahan: {e}")
        print("🔄 Mencoba lagi dalam 5 detik...")
        time.sleep(5)
