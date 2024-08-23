=======================================
PSAS Standard Operating Procedure - VPN
=======================================

Purpose

Describe the procedure needed to set up a new VPN connection on a device.

Standards and References

https://openvpn.net/community-resources/reference-manual-for-openvpn-2-4/
  
Acronyms and Terms
  
- VPN - Virtual Private Network
- VPN Gateway - A device or software that connects a local network to a VPN for sending encrypting data across the internet.

Notes/Issues

Procedure

1. Request VPN access. You will receive a VPN email with the OreFlat RADIUS Login Instructions.
  
   WARNING: The PrivateBin page(s) which is within the VPN email you receive are set to expire after visiting once or after one week of inactivity. Once these pages expire, the contents will be deleted and no longer available.

2. Retrieve Your Credentials: You can find your RADIUS Login Credentials via pasting the link provided from your VPN email into a browser. 
The password to view the PrivateBin page(s) is your username.
- Username: firstname.lastname
  
3. Save and Import the Attached OpenVPN Config in your VPN Email: Attached to your VPN email will be your *.ovpn VPN config file.  It is recommended that you import this *.ovpn file into your native network-manager (such as NetworkManger on Linux) and connect to the VPN through the native manager.

   WARNING: Running openvpn in the command-line may not always update your local DNS information. Therefore, LAN-exclusive domains may not work when connecting this way.

4. Log Into the VPN: Once you have retrieved and saved your credentials from the link provided within your VPN email, you may log into the VPN with the OpenVPN Config file attached in your VPN email.
See https://openvpn.net/connect-docs/import-profile.html for platform-specific details on running openvpn on your system.
- Username: See Credentials on PrivateBin page accessed from the link provided within your VPN email,
- PIN: See Credentials on PrivateBin page accessed from the link provided within your VPN email,
- Password: PIN + 2FA Code
     - To obtain the 2FA Code, setup Authenticator App (do only one of the following):
       1. Scan the QR Code on PrivateBin page accessed from the link provided within your VPN email into an Authenticator App (This is done to get a 6 digit code that regenerates every 30s from the App).
       2. Manually enter 2FA Setup Key in an Authenticator App.
  Example: If your PIN is 1111, and your 2FA Code is 222 222, then your password will be 1111222222

Change Log
Date: 2024-06-30
Ver: 1
Changes: Created document





