# 🔍 Python Network Scanner

A simple **network scanner** built with Python and **Scapy** to detect live hosts on a network by sending ARP requests. This tool helps identify active devices by retrieving their **IP and MAC addresses**. Documenting my journey in **learning how to build pentesting tools** with Python—this is my second project, a **basic network scanner** for discovering live hosts on a network.

## 🚀 How It Works
1. The script **takes an IP range as input** (e.g., `192.168.1.0/24`).
2. It **crafts an ARP request** asking all devices in the subnet to respond.
3. The request is sent in **broadcast mode** so all devices receive it.
4. Devices that respond are considered **live hosts**, and their **IP & MAC addresses** are displayed.

## 🛠️ Installation
Make sure you have **Python 3** installed. Then, install Scapy if you haven't already:

```bash
pip install scapy
```
📜 Usage
Run the script and enter the target IP range:
```bash
python network_scanner.py
```
## Example:
```bash
Enter IP range: 192.168.1.0/24
----------------------------------
Live hosts in: 192.168.1.0/24

IP: 192.168.1.1   MAC: AA:BB:CC:DD:EE:FF
IP: 192.168.1.2   MAC: 11:22:33:44:55:66
...
