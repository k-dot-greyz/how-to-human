# how-to-human

> git gud @life

## The Manifesto

The world is a mess. Everything is hard for no good fucking reason. If you look around, you see that we technically have everything we could ever want or at least the materials to build what's not already there. Recently I've realized many things, but one of the main ones is that we're operating our vessels without a proper instruction manual. Anyone who has tried to build a LEGO set or a piece of IKEA furniture knows that sometimes it really does pay to RTFM (Read The Fucking Manual). If a shelf needs a booklet with warnings, do's and don't's, a parts list and some assembly and usage diagrams, then how come we as human beings don't have anything resembling that? I guess the closest thing we do have is the insert main text for your belief system here, but that is like going to Hogwarts with only your Physics 101 book in hand. Don't get me wrong, I love physics, but the information is not entirely context appropriate.

At the same time I look around and see most adults act like kindergartners, and some kindergartners drop wisdom bombs that would go over the heads of states. So if nobody told you, I will: the mods are asleep at the wheel while getting head and sucking you dry at the same time.

So.

I figure it would be a waste not to at least attempt documenting the lessons that were learned, forgotten and re-learned many times. My memory has never been my strongest asset, so this is my attempt at getting down the basic template for life's amazing and annoying quirks, processes, procedures and protocols.

---

## Table of Contents
- [The Core Guide](./The-Core-Guide.md)
- [Hardware Tuning](./Hardware-Tuning.md)
- [Identity Protocols](./Identity-Protocols.md)
- [Input Management](./Input-Management.md)
- [Regulation Scripts](./Regulation-Scripts.md)
- [Thermal Regulation](./Thermal-Regulation.md)
- [Sleep Protocols](./Sleep-Protocols.md)

---

## Quick Start
- Read The-Core-Guide.md for the full OS-level model.
- Use Regulation-Scripts.md in emergencies (panic/anxiety).
- Set up Sleep-Protocols.md tonight; it's the highest ROI patch.
- Pick one module to implement this week and branch your habit: `git checkout -b new-habit`.

## 💰 Support This Project

Help keep this documentation alive and growing. Your support enables continued development of protocols, procedures, and frameworks for navigating life's complexity.

### 🚀 Quick Donate

[![Donate Crypto](https://img.shields.io/badge/Donate-Crypto-brightgreen?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com/k-dot-greyz/how-to-human)

### 💳 Supported Cryptocurrencies

#### Bitcoin (BTC)
```text
bc1q3rfg8nxtqtmqvqk9yted68j3ny9v3xzlh2tqen
```

![BTC QR Code](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAACsklEQVR4nO1aUWrkMAyVlUA/E9gDzFEyNyt7s/goPcBC8llw0CLZzmRccBzYzsaN3keoR48iEJKfJBuCI7B4iA6g/Dxwx55C+Xngjj2F8vPAHXsK5eeBO/YUyr8C3wS0ALYPR4A5fDzuL/SnHHiAe2H+QIwJwLxPi4GBHBjTNyy+GjHRuf0vBl6UP8cMtZzEEtWxcyC/+cR+rT+lwGLmNfltciZ7B/DJOnyY1/uDyv9WvnnnWmz7hdO5IRr/8f/fA+4ynqH8svztOGdnrs/9n5aGjxYI5sVIJtOJ/Ufll/CtSOReqvIbSerGz+Ll8zO/GKj8/8oHegZnMomclr9SjGfzH5WfB4WoOpD+iGgKt64cYYgfjW/FfJJYcpClIEt/tOl/f9+IK/Xr/CkHHuBeOH8Hia+HtL6cq53bWDV/q75/JwAfVR9Gb3A82HJAYxxiaXxr40PIUA6jv3DX63hkq/9EzaXxrVg/g4Q2CCpO2OmLutb41q2fGy7NTcxVEH0lWH87m/+o/LL9Qsv6+dOYe+fikqHjIs1Hrt4JvxSo/HPUZ+dlVLiJ10kHRBGt9blmvjUt+NSVWszHIK04sWV6qf1vjXyIHe5javVY6DehEw6dkuZv1fUZNgV5WkM7NdsirfGtvf8NkP6oCfqZs1vzt2I++V7IjzGCYA7rQq+0PnU/WPN+34RT48Amj3LmX453/nHJfzb/UfmH3k+SNLwsmB87JeDnHKqff8b7SYYPrb2FSPtN/3hq/0uBF94PDiKj4iZpM45W/fxz3scCuJbHlY4AlpbsjcDA/EZmGM/oPyo/D1pXR4+GKIwru3VTqPlbKx/irEoQHuR4VQU+vnE6rfGttz7Tel4fPIdMBo91U3g2/1H5WWDe/AXKzwN37CmUnwfu2FMoPw/csadQfh7fra/+AlDLOKl2jaeJAAAAAElFTkSuQmCC)

#### Ethereum (ETH)
```text
0x0000000000000000000000000000000000000000
```

> ⚠️ **Note**: The ETH address above is a placeholder. Please verify the correct address before sending any funds.

![ETH QR Code](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKAQAAAABTUiuoAAACFUlEQVR4nO2aQYrkMAxFv5TALF3QB5ijdG5WV0uO0jeIlw0JGiTLaWZR4F40MW39RSp23kIgvi3ZRYJGbdxKAoFyoAi0WRwoAm0WBwoVuWbQouNNB0uu00tPsTaJfzX6Lqrd3k+iZ3mbbFY6i7VF/LvRXC20PSbB9gBkLaabu4u1QTwKmme12uFr4g0BvBS//jQoKuooIP+R/mMdD539N2l2MkA6kO3vUaalp1g5UOAqAumh9cYO0PPDsniWkrCzWDG6t+QaC/JJ9nC//XQAHCi+iZLaqtZ/k9CSbCU8yTuvnmIdGUVpqVZMAmiOrPPSUqO0X1odOsJ3x8rDoyipEDEzacpqT+xzqQ7W22PlQKHyRTAdkDVdrVYp489YCbtB4cbRRMluttKUqcuuRdBXR747Vh4ehedjr/uWLYdlaM1yimz1t2/taqv9OsuopxpuushWdyh53e6O+tq8Yt/qqzsmpE+SjSYhYDoIyT/T+/5We2e+O1YOFCpbCa2sKLXFmolst7Kv4a3evFU0HbI9dk3ZOQP57aiVh+r2WDlQ/H93TEvW635rtTRRei/ZWawDo6gVvB2/X3V7OdXwuagJe0VFdzB6yid9JS/2rV69JdpgubQxvhAJb6EbNPnJu/3dyfqtehBf10R0EytG95bLyngdmsHsAqWU9uEtVYd3xyiP6+WI7riK0SwOFIE2iwNFoM3i4dF/giVM58wZs3YAAAAASUVORK5CYII=)

#### Solana (SOL)
```text
Eh8yq5CWVVJu5dM73XxQzTnptaRwpKGeXMNqnTKPqqkw
```

![SOL QR Code](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAACvklEQVR4nO1bbYqkQAxNRaF/KuwB5ijODfZIwx5pblB1lD5Ag/4csMmS1Me2DlTZCzra5v1wtPJoAo9XJrHGEDwDh0/RAZSfBxbicyg/DyzE51B+HliIz6H8PLAQn0P5Z+CbgBrAteERHF9giLH3DfNZDnyCe2J+R4wewHz0dxPW+oqLr0pCtO/8FwNPyh+iQx2bmOU2hp3Ma97Y2+azFLiY6XF2Plm+/OGtuUtO/sF8SsAi49z8evZsOtmJm1sN0Iw1wbBtPqj8VfRtWFbW0rW3WiSWi+k+w91//j4qfw98JyVyy1XV9ULmgy/vw4WVvfvyedt8FgOXU0/sX/q34N5GtvMI5N6+DE3du7/8Ufl5kG9+WFDuj4h6boh66ZlGbpKkUwo8snvLH5W/RN/Oy5dEZmkBKvLSWrlTfQ/Ih+DL1BqxlmJi8S/ZJphY/XtIPnjdvGFlkxYZRVUKl+hp1fe4+vYVmzjOIkVaaJKx+U71PXR9RXFD5kX/1m1C4AGq73HrK/j2WD34V+urQ/IhvnAfVfVvYuulnb6Y95Y/Kj8P8oaNrW+slaW0okfh1b8Hnl+5thoNNDywGqoR3O8bj6N/sXfv/JGh3SofVP46/q3it3w/vwrlNKQiWv177PnzyK/ZHoKJ4W6IHwmGegyBTfJB5a9TP49pTJVGkyR3aRKt/j3y/CpAauVQREOYOmv9/ELnJzv+YOTRfPH5yenaPvNfDjz5+UmyLKiYuLteop1lbct8FgOXU8/e/wIX0XGgEWeWCbo/vwTf8IFYslw/20FO5STNfySfErDImOLsfKKr7MWxHbbNCHISS/9/4SXOT5rukydZELverr/X0FluhzfJB5W/xvs3oJqc1KHU/+r3/Vc5P0nhb+x/A2iv+aPys8B8+BuUnwcW4nMoPw8sxOdQfh5YiM+h/DzWrq/+AlDLOKl2jaeJAAAAAElFTkSuQmCC)

### 🎯 Donation Tips

- **Test First**: Send a small amount to verify the address
- **Privacy**: Addresses may rotate for privacy protection
- **Support**: Your donations help maintain and improve this project
- **Questions**: Open an issue for any donation-related questions

### 📊 What Your Support Enables

- 🐛 Bug fixes and improvements to protocols
- 🚀 New modules and enhancements
- 📚 Expanded documentation and examples
- 🎨 Better organization and structure
- 🔧 Infrastructure and hosting

---

**Thank you for supporting how-to-human!** 🙏

🔗 **Project**: [how-to-human](https://github.com/k-dot-greyz/how-to-human)

## Contributing

PRs that improve clarity, add practical scripts, or fix broken metaphors are welcome. Keep the tone direct, useful, and minimally preachy. Structure long additions as modules and link them in the TOC.

## License

GPL-3.0
