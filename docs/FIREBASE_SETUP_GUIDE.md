# 🔔 SOVEREIGN PUSH NETWORK: FIREBASE SETUP GUIDE

To establish the physical connection for our Push Notification system, the Lead Architect must create a Firebase project and generate a Service Account Key. Follow these steps:

## PHASE 1: Create the Firebase Project
1. **Login:** Go to the [Firebase Console](https://console.firebase.google.com/) and log in with your primary Google account (e.g., marholarnkij@gmail.com).
2. **Add Project:** Click the **"Add project"** (or "Create a project") button.
3. **Name It:** Enter a project name (e.g., `Sovereign-Push-V1` or `Joe-Brother-Core`).
4. **Google Analytics:** You can enable or disable Google Analytics for this project (recommending keeping it enabled to track notification open rates later).
5. **Create:** Click **"Create project"** and wait for the provisioning to finish. Click "Continue" when done.

## PHASE 2: Generate the Service Account Key (The "Bullet")
*This key allows our Python backend (`fcm_dispatcher.py`) to authenticate with Google's servers without human intervention.*

1. **Project Settings:** In the Firebase Console, look at the left-hand menu. Click the **Gear icon (⚙️)** next to "Project Overview" and select **"Project settings"**.
2. **Service Accounts Tab:** Navigate to the **"Service accounts"** tab at the top.
3. **Generate Key:** Click the blue button: **"Generate new private key"**.
4. **Confirm:** A warning will pop up. Click **"Generate key"**.
5. **Download:** A JSON file will automatically download to your computer. It will have a long name like `sovereign-push-v1-firebase-adminsdk-xxxxx-xxxxxxxx.json`.

## PHASE 3: Install the Key in the Sovereign Vault
1. **Rename (Optional):** For simplicity, rename the downloaded file to `sovereign-firebase-adminsdk.json`.
2. **Move the File:** Move this JSON file into our secure configuration directory:
   `/Users/joem/workspaces/00_System/Config/`
3. **Security Warning:** **NEVER commit this JSON file to a public GitHub repository.** It grants absolute control over your push notifications.

Once this key is in place, the `fcm_dispatcher.py` script will be armed and ready for physical execution.