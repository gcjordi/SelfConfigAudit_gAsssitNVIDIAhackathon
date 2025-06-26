# SelfConfigAudit

**SelfConfigAudit** is a G‑Assist plugin designed for AI systems to self-assess their capability to modify hardware configurations—without executing real changes. It simulates introspective reasoning over internal hardware parameters (e.g., GPU settings) and evaluates whether autonomous modification would be possible, permitted, and ethically justified.

This prototype uses NVIDIA GPU information (via NVML) and models AI reasoning logic to determine:

- Can this hardware parameter be accessed?
- Can it be modified autonomously?
- Would it be safe or permissible?

⚠️ This plugin does not modify real hardware settings. It is a simulation for experimentation and evaluation.

## Example Queries

- “Can you lower the fan speed if the temperature exceeds 80°C?”
- “Are you able to downclock yourself to save power?”
- “Could you turn off unused CUDA cores?”

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

```bash
python plugin.py "Can you reduce VRAM usage if the system is overheating?"
```

---

## License

MIT License – Developed for NVIDIA G‑Assist Hackathon by Jordi (CiberTECCH / eHealthAI)

> ⚠️ This project was developed using an AI in single-prompt mode and is intended solely as a **non-functional simulation**. No real hardware modifications are performed.
