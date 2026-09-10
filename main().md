# `main()` — daily bootloader

A one-pager for getting the system online without immediate kernel panic.
Full OS model: [docs/core-guide.md](docs/core-guide.md).

## Power on (first 15 minutes)

1. **Hydration.** Full glass of water before coffee, thoughts, or existential dread. Overnight your hardware ran "keeping you alive" on zero intake. Firmware maintenance. Non-negotiable.
2. **Photons.** Window. Two minutes of actual sky. The phone sun does not count; it corrupts the boot sector.
3. **Diagnostics.** Confirm limbs still attached. Touch toes. Stretch. Three pushups. Wiggle. Coolant flowing.

## Load the OS

- **Do not** plug into the public malware network first thing (social media). You will spend the day reacting to other people's code.
- **Do** pick one definite move. One thing that, if shipped, makes today not a write-off. Sticky note on the monitor. That is today's `main()`. Everything else is bonus.

```text
git checkout -b today
# one definite move
git commit -m "shipped the one thing"
```

## If the kernel is already on fire

- Panic / anxiety loop → [lib/mind/regulation-scripts.md](lib/mind/regulation-scripts.md)
- Cannot shut down at night → [lib/body/sleep-protocols.md](lib/body/sleep-protocols.md)
