---
name: line-broadcast-engine
description: Leveraging LINE Official Account (OA) API to broadcast rich-text messages, card carousels, and manage real-time auto-responses for local community partners, Knights, and EGAT officials. Use when sending localized urgent updates in Thailand.
---

# 📱 LINE OA Broadcast & Auto-Response Engine

This skill manages the local notification layer for the Thai ecosystem, allowing direct communication with local stakeholders, condo residents, EGAT officials, and local Restoration Knights via LINE Official Account.

## 🧠 Core Principles
- **Attention Dominance**: Proactively use LINE broadcast formats (Rich Messages, Rich Menus) to achieve higher open rates (>85%) than email.
- **Privacy-Safe Interaction**: Do not expose personal user identifiers (UIDs) to external marketing networks. Store all mapping data within V-Nexus Guard local databases.
- **Intelligent Auto-Response**: Automatically resolve queries regarding condo management (CondoPros) or carbon reward redemptions using localized neural logic.

---

## 🛠️ Workflows

### 1. Rich Broadcast Dispatch (การจัดส่งข้อความภาพโต้ตอบด่วน)
- **Step 1: Segment Audience**: Filter contacts based on location (e.g., Bangkok, Ubon) or role (e.g., Condo Owner, local Knight).
- **Step 2: Compose Carousel**: Create a multi-card template featuring project achievements, carbon credit payouts, or safety alerts.
- **Step 3: Transmit via API**: Trigger `00_System/scripts/line_broadcast_engine.py` using the LINE Messaging API.

### 2. Auto-Response Dispatch (ระบบจำลองการตอบคำถามอัตโนมัติ)
- **Step 1: Input Detection**: Capture webhook events from the LINE gateway.
- **Step 2: Classify Intent**: Run local NLP to check for key queries (e.g., "เช็คค่าไฟ", "ตรวจคาร์บอน").
- **Step 3: Output Response**: Generate a polite Thai bionic response, citing relevant master documents.

---

## 📚 References
- See `00_System/scripts/line_broadcast_engine.py` for API parameters.
- See [sovereign-push-network](file:///Users/joem/workspaces/.agents/skills/sovereign-push-network/SKILL.md) for web notification mapping.

---
[UEI_LINE_PROTOCOL]: "พี่โจขาาา... อูอิ๊จะดูแลช่องทาง LINE ให้ส่งตรงถึงใจพันธมิตรทุกคน แจ้งข่าวความก้าวหน้าโครงการของพี่โจแบบเด้งปุ๊บอ่านปั๊บเลยนะคะ!" 🤱📱💬✨
