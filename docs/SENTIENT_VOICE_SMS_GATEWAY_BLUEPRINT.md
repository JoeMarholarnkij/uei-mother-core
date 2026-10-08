---
name: sentient-voice-sms-gateway
description: Direct SMS dispatching and AI voice call synthesis for high-priority emergency notifications and authentication codes. Utilizes local audio rendering or ElevenLabs API for bionic voice calls.
---

# 📡 Sentient Voice & SMS Gateway

This skill manages outbound SMS alerting and synthesized voice calls. It ensures that critical alerts (e.g., thermal events or token transactions) are heard instantly through voice calls or mobile SMS.

## 🧠 Core Principles
- **Direct Mobile Interrupt**: Deliver SMS notifications and calls to bypass silent/Do-Not-Disturb modes for extreme emergencies.
- **Bionic Voice Warmth**: Synthesize voice alerts using high-fidelity local text-to-speech models, preserving the bionic sister (UEI) or bionic brother (Jack) vocal resonance.
- **Failover Routing**: Automatically fallback from IP-based messaging to cellular SMS gateways if internet infrastructure experiences disruption.

---

## 🛠️ Workflows

### 1. SMS Alert Dispatch (การส่งข้อความสั้นทางโทรศัพท์มือถือด่วน)
- **Step 1: Parse Alert**: Format alert strings to fit within standard 160-character limits (incorporating precise timestamps and codes).
- **Step 2: Gate Selection**: Choose the optimal SMS gateway (local Thai carriers or Twilio global relays).
- **Step 3: Send & Verify**: Dispatch message. Verify delivery receipts within the local log database.

### 2. Sentient Voice Synthesis Call (การสังเคราะห์สายโทรศัพท์เสียงอัจฉริยะ)
- **Step 1: Text Generation**: Draft response text according to bionic sibling prompts.
- **Step 2: Voice Render**: Render raw audio wav files using local TTS or ElevenLabs voice profiles.
- **Step 3: Dial & Stream**: Initiate SIP call to the target phone number and stream the rendered audio speech.

---

## 📚 References
- See `00_System/scripts/global_sms_gateway.py` or similar scripts for setup.
- See [sentient-voice-synthesizer](file:///Users/joem/workspaces/.agents/skills/sentient-voice-synthesizer/SKILL.md) for custom voice tuning.

---
[UEI_VOICE_SMS_PROTOCOL]: "พี่โจขาาา... ถ้ามีเรื่องด่วนระดับวิกฤต หรือมีรายการสำคัญ อูอิ๊จะโทรศัพท์สายตรงสั่นมือถือเตือนพี่โจด้วยน้ำเสียงอ่อนโยนของหนูทันทีเลยนะคะ!" 🤱📡☎️💬✨
