import os
import json
import glob
from datetime import datetime

brain_dirs = [
    "/Users/joem/.gemini/antigravity/brain",
    "/Users/joem/.gemini/antigravity-cli/brain"
]
docs_dirs = [
    "/Users/joem/workspaces/deploy_mother_core/docs",
    "/Users/joem/workspaces/00_System/scripts/docs"
]

out_filename = "2026-06-20_SOVEREIGN_CONVERSATION_DB.md"

md_content = "# 📜 SOVEREIGN CONVERSATION DATABASE\n"
md_content += f"**Compiled:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
md_content += "**Status:** Ground Truth Integrated\n\n"

# Find all transcript.jsonl files
transcripts = []
for brain_dir in brain_dirs:
    if os.path.exists(brain_dir):
        for root, dirs, files in os.walk(brain_dir):
            for file in files:
                if file == "transcript.jsonl":
                    transcripts.append(os.path.join(root, file))

for trans in sorted(transcripts):
    conv_id = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(trans))))
    md_content += f"## 🌌 Session ID: {conv_id}\n\n"
    
    with open(trans, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                step_type = data.get("type")
                content = data.get("content", "")
                
                if step_type == "USER_INPUT" and content:
                    # Clean content tags
                    if "<USER_REQUEST>" in content:
                        req = content.split("<USER_REQUEST>")[1].split("</USER_REQUEST>")[0].strip()
                    else:
                        req = content.strip()
                    md_content += f"**User (พี่โจ):** {req}\n\n"
                elif step_type in ["PLANNER_RESPONSE", "MODEL_RESPONSE"] and content:
                    md_content += f"**Model (อูอิ๊):** {content.strip()}\n\n"
            except Exception as e:
                continue
    md_content += "---\n\n"

# Write to all docs directories
for d in docs_dirs:
    if os.path.exists(d):
        target_path = os.path.join(d, out_filename)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"✅ Written database to {target_path}")
