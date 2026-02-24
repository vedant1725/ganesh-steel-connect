# Ganesh Steel Connect - Deployment Guide

## 🚀 Deploy to Streamlit Cloud (Free)

### Option 1: Quick Deploy via Streamlit Cloud

1. **Create a GitHub Repository**
   - Go to [GitHub.com](https://github.com)
   - Create a new repository named `ganesh-steel-connect`
   - Upload these files to the repository:
     - `app.py`
     - `requirements.txt`

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository (`ganesh-steel-connect`)
   - Select branch `main`
   - Set main file path to `app.py`
   - Click "Deploy!"

3. **Your app will be live at:** 
   `https://ganesh-steel-connect.streamlit.app`

---

### Option 2: Deploy from Local Machine

```
bash
# Install GitHub CLI
# Download from: https://cli.github.com/

# Initialize git (in ganesh_steel_app folder)
cd ganesh_steel_app
git init
git add .
git commit -m "Initial commit"

# Create repository on GitHub and push
gh repo create ganesh-steel-connect --public --source=. --push

# Then deploy from streamlit.io
```

---

### Option 3: Deploy to Heroku

```
bash
# Install Heroku CLI
# Create Procfile: echo "web: streamlit run app.py --server.port $PORT" > Procfile
# Deploy using Heroku Git
heroku create ganesh-steel-connect
git push heroku main
```

---

## 📁 Files Included

- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- This README file

## 🌐 Features

✅ Product Catalog with categories
✅ Order Tracking by phone number  
✅ Custom Quote Request form
✅ Contact Information & Location
✅ SQLite database (auto-created)
✅ Responsive design

## 📞 Support

For deployment help, contact: panchalvedant331@gmail.com
