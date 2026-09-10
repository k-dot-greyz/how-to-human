# Sleep Protocols

Scripts and environmental configs for initiating and maintaining scheduled downtime.

## 1. Environmental configuration (`config.sys`)

Your sleep environment is the server room. Optimize it for one critical task. Any deviation is a point of failure.

- **`headless_mode=true` (kill all photons):** Optical sensors treat photons as the `is_daytime` flag. A single power-strip LED can corrupt the cycle. Blackout curtains. Electrical tape over every LED. Absolute darkness.
- **`thermal_throttle_limit=19C`:** Core temperature must drop for deep sleep. A hot room is a 4K render on a passively cooled laptop: throttle, lag, crash. Target 18–20°C / 65–68°F.
- **`audio_input=dither`:** A car alarm is a hardware interrupt. Either a noise gate (earplugs) or dithering (brown/pink noise) so unpredictable spikes do not wake the system. Home Assistant can automate this.

## 2. Shutdown sequence (`shutdown -h now`)

You cannot just kill the power. A proper shutdown prevents data corruption.

- **Brain dump daemon:** An hour before downtime, terminate open threads. Write every worry, idea, and to-do out of RAM onto a notebook or text file. Highest-ROI patch for a racing mind.
- **Deprecate blue light:** Blue light is a system command that screams `IT'S NOON`. Kill screens an hour before sleep, or run an aggressive blue-light filter.
- **Home Assistant sequence (optional):** 90 minutes before bed:
  1. Lights shift to deep warm red/orange at under 20% brightness.
  2. Speakers play low-stimulus audio (ambient, boring podcasts, Alan Watts).
  3. Phone notification: `// SYSTEM ANNOUNCEMENT: Shutdown sequence initiated. Save work and disconnect.`

## 3. Emergency overrides

- **`--force` (when you cannot sleep):** If shutdown fails for 20–30 minutes, abort. Do not lie there compiling anxiety. Dim room, profoundly boring task (technical manual, laundry) until drowsiness returns. Then retry.
