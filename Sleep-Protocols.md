### **sleep_protocols.md**

*A library of scripts and environmental configs for initiating and maintaining the system's scheduled downtime.*

#### **1. Environmental Configuration (config.sys)**

Your sleep environment is the server room. It needs to be optimized for a single, critical task. Any deviation introduces potential points of failure.

* **headless_mode=true (Kill All Photons):** Your optical sensors are designed to detect photons, which is the primary trigger for the is_daytime flag in your firmware. Even a tiny LED from a power strip can be enough to corrupt the sleep cycle. The goal is absolute, uncompromising darkness. Use blackout curtains. Put electrical tape over every single goddamn LED. Run the system in headless mode.  
* **thermal_throttle_limit=19C (Cool Down):** Your core temperature **must** drop to initiate deep sleep. A hot room is like trying to render a 4K video on a passively cooled laptop; it will thermal throttle, lag, and eventually crash. The ideal temperature is cool, around 18-20°C (65-68°F).  
* **audio_input=dither (Configure Noise):** A sudden, sharp noise (a car alarm, a door slam) is a hardware interrupt that can cause a kernel panic. You have two options:  
  * **Noise Gate:** High-quality earplugs to block everything.  
  * **Dithering:** Use a brown or pink noise generator. This masks unpredictable, jarring interrupts with a constant, steady signal, making them less likely to wake the system. You can use your Home Assistant to automate this.

#### **2. The Shutdown Sequence (shutdown -h now)**

You can't just kill the power. A proper shutdown sequence prevents data corruption.

* **The Brain Dump Daemon:** An hour before scheduled downtime, your CPU is likely still spinning with dozens of open threads (worries, ideas, to-do lists). You must terminate these processes manually. Run a brain dump: open a text file or a physical notebook and write down every single thought, task, or idea. Get it out of RAM and onto a physical drive. This is the single most effective patch for a racing mind.  
* **Deprecate Blue Light:** Blue light is a system-level command that screams "IT'S NOON!" at your motherboard. An hour before sleep, kill all screens. If you absolutely must use a screen, use an aggressive system-wide blue light filter. This is non-negotiable.  
* **The Home Assistant Sequence:** As a DIY enthusiast, you can automate this. Create a "Sleep Mode" automation that runs 90 minutes before bed:  
  1. All smart lights shift to a deep, warm red/orange at <20% brightness.  
  2. Smart speakers begin playing a low-stimulus "sleep" playlist (e.g., ambient music, boring podcasts, Alan Watts lectures).  
  3. Send a notification to your phone: // SYSTEM ANNOUNCEMENT: Shutdown sequence initiated. Please save your work and disconnect from the network.

#### **3. Emergency Overrides**

* **--force Flag (When You Can't Sleep):** If you've been trying to shut down for more than 20-30 minutes and it's not working, abort the command. Don't lie there compiling anxiety. Get out of bed, go to another dimly lit room, and do something profoundly boring (read a technical manual, fold laundry) until you feel the system drowsiness signal again. Then, and only then, attempt a reboot.