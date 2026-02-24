# Ganesh Steel Connect - Deployment Guide

## GitHub Repository
Your code is ready at: https://github.com/vedant1725/ganesh-steel-connect

---

## Option 1: Deploy to Streamlit Cloud (Recommended)

1. **Go to:** https://share.streamlit.io
2. **Sign in** with your GitHub account
3. **Click "New app"**
4. **Select:**
   - Repository: `vedant1725/ganesh-steel-connect`
   - Branch: `master`
   - Main file path: `app.py`
5. **Click "Deploy!"**
6. **Your app will be live at:** `https://ganesh-steel-connect.streamlit.app`

### Add Custom Domain (Streamlit Cloud):
1. In your deployed app, go to **Settings**
2. Click **Custom Domain**
3. Enter your domain and follow the instructions

---

## Option 2: Deploy to Render

### Quick Deploy:
1. **Go to:** https://dashboard.render.com
2. **Sign in** with GitHub
3. **Click "New +"** → **"Web Service"**
4. **Connect:** Select `vedant1725/ganesh-steel-connect`
5. **Configure:**
   - Name: `ganesh-steel-connect`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run app.py --server.port=$PORT`
6. **Click "Create Web Service"**
7. **Wait 2-3 minutes** for deployment

### Add Custom Domain (Render):
1. After deployment, go to **Settings**
2. Scroll to **Custom Domains**
3. Click **Add Custom Domain**
4. Enter your domain (e.g., `ganeshsteel.com`)
5. Follow the DNS configuration instructions

---

## Files Included
- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `render.yaml` - Render deployment configuration
- `.streamlit/config.toml` - Streamlit configuration

---

## Need Help?
Contact: panchalvedant331@gmail.com
