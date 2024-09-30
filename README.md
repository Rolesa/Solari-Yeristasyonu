# Solari TIKA (TARIMSAL İNSANSIZ KARA ARACI) Ground Control Station V1.0

**Solari TIKA GCS** is a GUI for using TEKNOFEST TIKA, developed by Rolesa.

---

**WARNING:** Due to optimization issues, it is recommended to use V1.0 in Windows light mode. It is anticipated that this issue will be resolved in future versions.

The **SOLARI** ground station works together with the Raspberry Pi, STM32, and Pixhawk present in the TIKA vehicle. The Raspberry Pi and SOLARI ground station must be on the same Wi-Fi network, and their IP addresses need to be adjusted accordingly. Valid tabs in the control station: **Camera**, **Waypoint Saving**, **Home**, and others are not in use.

## Waypoint Saving:

- **Get GPS:** Used to retrieve the current GPS location of the vehicle.
- **Send Waypoints Button:** Used to save the GPS locations obtained from the manual coordinate entry section or from the Get GPS button as waypoints.
- **Waypoints for Hoe Lift:** This section is used to lift the hoe controlled by the STM positioned on the vehicle at the specified waypoints.
- **Waypoints for Hoe Drop:** This section is used to drop the hoe controlled by the STM positioned on the vehicle at the specified waypoints.
- **Send Mission:** Assigns the task of lifting and dropping the hoe at the specified waypoints.

## Camera:

- **Start:** Begins receiving and processing images from the IP address where the stream is being broadcast.
- **Stop-Close (Performs the same function):** Stops receiving and processing the stream.
- **Last Location:** Displays the approximate GPS location produced by estimating the position of the detected object (the plant) at a specified distance from the vehicle.
- **Detection Count:** Non-functional.

## Home:

- **Tasks-Status Information (Loadcell data, Connection status):** Some are undefined.
- **Mavlink:** Specifies which port will be used for the MAVLink connection with Pixhawk.
- **Connect Button:** Initiates the MAVLink connection from the specified port.
- **Hoe Lift-Drop:** Added to test the movement of the hoe positioned on the vehicle. Used for the manual up-down movement of the hoe.
- **Start-HOLD-MANUAL-FORCE_ARM-DISARM Buttons:** Used to switch the vehicle between AUTO-HOLD-MANUAL modes and to arm and disarm.

---
## Anaconda Kütüphanelerini Kurma

Anaconda kütüphanelerini kurmak için aşağıdaki komutu kullanabilirsiniz:

```bash
conda env create -f environment.yml
```
# 💫 About Me:
🔭 I’m currently working on control automation software development.<br>
💬 Ask me about Pixhawk, Python, PyQt, and embedded software.<br>
I am a first-year student in Electrical and Electronics Engineering at 19 Mayıs University.

## 🌐 Socials:
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/tunahangenc_c) 

# 💻 Tech Stack:
![AssemblyScript](https://img.shields.io/badge/assembly%20script-%23000000.svg?style=for-the-badge&logo=assemblyscript&logoColor=white) 
![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white) 
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi) 
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) 
![TOR](https://img.shields.io/badge/tor-%237E4798.svg?style=for-the-badge&logo=tor-project&logoColor=white) 
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)

# 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=rolesa&theme=dark&hide_border=false&include_all_commits=false&count_private=false)<br/>
![](https://github-readme-streak-stats.herokuapp.com/?user=rolesa&theme=dark&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=rolesa&theme=dark&hide_border=false&include_all_commits=false&count_private=false&layout=compact)

### ✍️ Random Dev Quote
![](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical)

---

[![](https://visitcount.itsvg.in/api?id=rolesa&icon=0&color=0)](https://visitcount.itsvg.in)

<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->
