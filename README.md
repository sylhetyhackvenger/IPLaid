# 🔥 W8IP PRO MAX SCANNER

Advanced IP Intelligence & Deep Port Scanner Tool
Coded by **W8Team / MD SOJIB**

---

## 🚀 Features

* 🌐 Domain → IP + Full Info
* 📡 Reverse IP Scan (CIDR /24 /16 /8)
* 🧠 Hostname Detection
* 🖥 Server Detection (nginx / apache / etc)
* 📄 Website Title Grabber
* ⚡ Deep Scan (ALL PORTS 1–65535)
* 🔥 Real-Time Port Detection
* 🛑 CTRL + C Stop Support
* 📁 Auto Save Results (deep_scan.txt)
* 🎨 Clean & Colorful Output
* 📱 Termux Supported

---

## ⚙️ Installation (PC / Linux / Windows)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/W8SOJIB/W8IPReverseInfo
cd W8IPReverseInfo
```

### 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Tool

```bash
python W8IPReverseInfo.py
```

---

## 📱 Termux Installation (Android)

### Step 1: Update Packages

```bash
pkg update && pkg upgrade
```

### Step 2: Install Python & Git

```bash
pkg install python git
```

### Step 3: Clone Tool

```bash
git clone https://github.com/W8SOJIB/W8IPReverseInfo
cd W8IPReverseInfo
```

### Step 4: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 5: Run

```bash
python W8IPReverseInfo.py
```

---

## 🎯 Usage

After running the tool:

```
[1] Domain → IP + Info
[2] IP Range Scan (/24 + Server + Title)
[3] Deep Scan (ALL PORTS ⚡ + Server + Title + Save)
[4] Exit
```

### Example:

```
Enter CIDR ➤ 103.165.48.0/24
```

---

## 📁 Output File

Deep scan results are saved in:

```
deep_scan.txt
```

Example:

```
103.165.48.10 Hostname: example.com
103.165.48.10 Server: nginx
103.165.48.10 Title: welcome page
103.165.48.10:22
103.165.48.10:80
```

---

## ⚡ Performance Tips

| Device    | Recommended MAX_CONCURRENT |
| --------- | -------------------------- |
| Termux 📱 | 300–700                    |
| PC 💻     | 800–2000                   |
| VPS 🔥    | 3000+                      |

Edit in code:

```python
MAX_CONCURRENT = 800
```

---

## ⚠️ Disclaimer

This tool is for **educational & security testing purposes only**.
Do not use this tool on systems without proper authorization.

---

## 📜 License

This project is licensed under the **MIT License**.

You are free to:

* Use
* Modify
* Distribute

But must include original credit:

**W8Team / MD SOJIB**

---

## 💻 Author

* 👑 MD SOJIB
* ⚡ W8Team

---

## ⭐ Support

If you like this tool, give it a ⭐ on GitHub!

---

## 🔥 W8IP PRO MAX SCANNER

W8IP PRO MAX SCANNER is a powerful Python-based network intelligence and deep scanning tool designed for fast and efficient analysis of domains and IP ranges.

This tool combines multiple features such as domain resolution, reverse IP lookup, server detection, and full port scanning into one lightweight yet powerful CLI utility.

---

### ⚡ Key Capabilities

* 🌐 Convert Domain → IP with detailed information
* 📡 Scan IP ranges using CIDR notation (/24, /16, /8)
* 🧠 Reverse DNS (Hostname detection)
* 🖥 Detect web server (nginx, apache, cloudflare, etc.)
* 📄 Extract website titles from live servers
* 🔥 Perform deep scan on ALL ports (1–65535)
* ⚡ Real-time open port detection
* 🛑 Interrupt scan anytime using CTRL + C
* 📁 Automatically save results to file
* 📱 Fully compatible with Termux (Android)

---

### 🎯 Why This Tool?

W8IP PRO MAX SCANNER is built for speed, simplicity, and flexibility.
It uses asynchronous scanning techniques to achieve high performance while maintaining a clean and readable output.

Whether you are learning networking, testing systems, or analyzing infrastructure, this tool provides a solid all-in-one solution.

---

### ⚠️ Disclaimer

This tool is intended for educational and authorized security testing purposes only.
Unauthorized use against systems you do not own is strictly prohibited.

---

### 👑 Author

Developed by **W8Team / MD SOJIB**

