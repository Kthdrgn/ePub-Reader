# 🚀 Quick Start Guide

## Get Your PWA Running in 3 Steps!

### Step 1: Create Icons
1. Open `create-icons.html` in any web browser
2. Click the download links to save:
   - `icon-192.png`
   - `icon-512.png`
3. Place both icons in the same folder as `index.html`

### Step 2: Start a Server

**Option A - Python (Easiest)**
```bash
python -m http.server 8000
```
Open: http://localhost:8000

**Option B - Using the Setup Script**
```bash
chmod +x setup.sh
./setup.sh
```

**Option C - Node.js**
```bash
npx serve
```

### Step 3: Test PWA Features

1. Open the app in your browser
2. Press F12 to open DevTools
3. Go to "Application" tab
4. Check "Service Workers" - should show "activated"
5. Check "Manifest" - should show app info
6. Try going offline (Network tab → Offline) and refresh!

---

## 📱 Install on Your Device

### Desktop (Chrome/Edge)
- Look for install icon in address bar (⊕)
- Click to install

### Android
- Tap the "Add to Home Screen" banner
- Or: Menu → Install app

### iOS
- Safari → Share → Add to Home Screen

---

## 🌐 Deploy Online (FREE!)

### GitHub Pages
```bash
git init
git add .
git commit -m "PWA ready"
git remote add origin YOUR_REPO
git push -u origin main
```
Enable Pages in Settings → Your site: `https://username.github.io/repo`

### Netlify (Drag & Drop)
1. Go to app.netlify.com
2. Drag your folder
3. Done! ✨

---

## ✅ What You Get

- 📵 Works offline after first load
- 📱 Installs like a native app
- ⚡ Loads instantly from cache
- 🔄 Syncs to Google Drive (optional)
- 🌙 Dark mode
- 📖 EPUB3 + audio support
- 💾 Progress tracking

---

## ⚙️ Google Drive Sync Setup (Optional)

1. Visit: https://console.cloud.google.com
2. Create project → Enable Drive API
3. Create OAuth Client ID + API Key
4. In app: ☰ Menu → Sync → ⚙️ Configure
5. Paste credentials

---

## 🆘 Troubleshooting

**"Service Worker failed to register"**
- Must use HTTPS or localhost
- Check browser console for errors

**"Icons not showing"**
- Run `create-icons.html` first
- Place icons in root folder

**"Install button doesn't appear"**
- Only works on HTTPS (or localhost)
- Some browsers don't support PWA install

---

## 📚 Next Steps

1. ✅ Create icons
2. ✅ Test locally
3. ✅ Deploy online
4. ✅ Install on devices
5. ✅ Set up Drive sync (optional)
6. 📖 Start reading!

**Enjoy your new PWA! 🎉**
