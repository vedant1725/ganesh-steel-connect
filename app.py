"""
Ganesh Steel Connect - Steel Furniture Business App
Quality Steel Furniture at your Fingertips
"""

import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import os

# Page Configuration
st.set_page_config(
    page_title="Ganesh Steel Connect",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e3a8a;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .tagline {
        text-align: center;
        color: #64748b;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .contact-button {
        background-color: #10b981;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        font-weight: bold;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem;
    }
    .product-card {
        background-color: white;
        border-radius: 1rem;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    .status-badge {
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-weight: bold;
        font-size: 0.875rem;
    }
    .status-in-production { background-color: #fef3c7; color: #92400e; }
    .status-ready { background-color: #d1fae5; color: #065f46; }
    .status-delivered { background-color: #dbeafe; color: #1e40af; }
    .stButton>button {
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
        color: white;
        border: none;
        border-radius: 0.5rem;
    }
    .sidebar-content {
        background-color: #f8fafc;
        padding: 1rem;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Database Setup
def init_database():
    """Initialize SQLite database with orders table"""
    conn = sqlite3.connect('ganesh_steel.db')
    c = conn.cursor()
    
    # Create orders table
    c.execute('''CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        customer_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        item_description TEXT NOT NULL,
        dimensions TEXT,
        status TEXT NOT NULL,
        balance_due REAL NOT NULL,
        advance_paid REAL DEFAULT 0,
        order_date TEXT NOT NULL,
        expected_delivery TEXT
    )''')
    
    # Create custom requests table
    c.execute('''CREATE TABLE IF NOT EXISTS custom_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        item_type TEXT NOT NULL,
        dimensions TEXT NOT NULL,
        additional_info TEXT,
        request_date TEXT NOT NULL,
        status TEXT DEFAULT 'Pending'
    )''')
    
    # Insert sample orders if empty
    c.execute("SELECT COUNT(*) FROM orders")
    if c.fetchone()[0] == 0:
        sample_orders = [
            ('GSF001', 'Rahul Shah', '9876543210', '3-Door Almirah (6x4x2 ft)', '6x4x2 ft', 'In Production', 5000, 3000, '2024-01-10', '2024-01-25'),
            ('GSF002', 'Amit Patel', '9876543211', 'Office Rack (5 shelves)', '4x2x6 ft', 'Ready for Delivery', 0, 8000, '2024-01-08', '2024-01-20'),
            ('GSF003', 'Sneha Gupta', '9876543212', 'Single Bed with Storage', '6x3 ft', 'Delivered', 0, 12000, '2024-01-01', '2024-01-15'),
            ('GSF004', 'Raj Malhotra', '9876543213', 'Kitchen Cabinet', '5x2x2.5 ft', 'In Production', 3500, 5000, '2024-01-12', '2024-01-28'),
            ('GSF005', 'Priya Sharma', '9876543214', '2-Door Wardrobe', '5x4x2 ft', 'Ready for Delivery', 0, 15000, '2024-01-05', '2024-01-18'),
        ]
        c.executemany("INSERT INTO orders VALUES (?,?,?,?,?,?,?,?,?,?)", sample_orders)
    
    conn.commit()
    conn.close()

# Initialize database
init_database()

# Sidebar Navigation
def sidebar():
    st.sidebar.image("https://img.icons8.com/color/96/000000 factory.png", width=60)
    st.sidebar.title("🏭 Ganesh Steel")
    st.sidebar.markdown("---")
    
    menu_options = ["🏠 Home", "📦 Products", "🔍 Track Order", "📝 Quote Request", "📞 Contact"]
    choice = st.sidebar.radio("Navigation", menu_options)
    
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **Ganesh Steel Furniture**
    
    Girdharnagar, Himmatnagar
    
    Quality Steel Furniture 
    at Affordable Prices
    """)
    
    return choice

# Home Page
def home_page():
    # Header
    st.markdown('<p class="main-header">🏭 Ganesh Steel Connect</p>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Quality Steel Furniture at your Fingertips</p>', unsafe_allow_html=True)
    
    # Hero Section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("👋 Welcome to Ganesh Steel Furniture - Your Trusted Steel Furniture Partner in Himmatnagar!")
    
    # Quick Actions
    st.markdown("### 🚀 Quick Actions")
    action_col1, action_col2, action_col3 = st.columns(3)
    
    with action_col1:
        if st.button("🔍 Track My Order", use_container_width=True):
            st.session_state['page'] = 'Track Order'
            st.rerun()
    
    with action_col2:
        if st.button("📝 Request Quote", use_container_width=True):
            st.session_state['page'] = 'Quote Request'
            st.rerun()
    
    with action_col3:
        if st.button("📞 Contact Us", use_container_width=True):
            st.session_state['page'] = 'Contact'
            st.rerun()
    
    st.markdown("---")
    
    # About Section
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### About Ganesh Steel Furniture
        
        Welcome to **Ganesh Steel Furniture**, your trusted destination for high-quality steel furniture in Himmatnagar. 
        We specialize in:
        
        - 🗄️ **Steel Cupboards** - Durable and secure storage solutions
        - 🪜 **Steel Racks** - Perfect for offices and homes
        - 🛏️ **Steel Beds** - Strong and long-lasting
        - 🍳 **Kitchen Cabinets** - Modern kitchen storage
        - 🪑 **Office Furniture** - Professional steel furniture
        
        With years of experience, we craft each piece with precision and care.
        """)
    
    with col2:
        st.markdown("""
        ### Why Choose Us?
        
        ✅ **Premium Quality** - High-grade steel materials
        
        ✅ **Custom Designs** - Furniture made to your specifications
        
        ✅ **Competitive Prices** - Best value for your money
        
        ✅ **Timely Delivery** - We deliver on our promises
        
        ✅ **Excellent Service** - Customer satisfaction is our priority
        
        ✅ **After-Sales Support** - We're here to help even after purchase
        """)
    
    st.markdown("---")
    
    # Contact Quick Links
    st.markdown("### 📞 Get in Touch")
    st.markdown("""
    <div style="text-align: center;">
        <a href="tel:9510706177" class="contact-button">📞 Call: 9510706177</a>
        <a href="mailto:panchalvedant331@gmail.com" class="contact-button" style="background-color: #3b82f6;">✉️ Email Us</a>
    </div>
    """, unsafe_allow_html=True)

# Products Page
def products_page():
    st.markdown("# 📦 Our Products")
    st.markdown("Explore our wide range of steel furniture products")
    
    # Product Categories
    categories = {
        "All Products": [
            {"name": "3-Door Almirah", "price": "₹8,000 - ₹15,000", "desc": "Spacious storage with locking mechanism", "image": "🗄️"},
            {"name": "2-Door Wardrobe", "price": "₹10,000 - ₹18,000", "desc": "Elegant design with hanging rod", "image": "🗄️"},
            {"name": "Office Rack", "price": "₹3,000 - ₹8,000", "desc": "Multi-shelf storage for offices", "image": "🪜"},
            {"name": "Book Shelf", "price": "₹2,500 - ₹6,000", "desc": "Perfect for books and display items", "image": "🪜"},
            {"name": "Single Bed", "price": "₹6,000 - ₹12,000", "desc": "Durable steel frame with storage", "image": "🛏️"},
            {"name": "Double Bed", "price": "₹10,000 - ₹20,000", "desc": "Spacious double bed with storage", "image": "🛏️"},
            {"name": "Kitchen Cabinet", "price": "₹8,000 - ₹15,000", "desc": "Modern kitchen storage solution", "image": "🍳"},
            {"name": "File Cabinet", "price": "₹5,000 - ₹10,000", "desc": "Secure document storage", "image": "📁"},
        ],
        "Almirahs & Wardrobes": [
            {"name": "3-Door Almirah", "price": "₹8,000 - ₹15,000", "desc": "Spacious storage with locking mechanism", "image": "🗄️"},
            {"name": "2-Door Wardrobe", "price": "₹10,000 - ₹18,000", "desc": "Elegant design with hanging rod", "image": "🗄️"},
        ],
        "Racks & Shelves": [
            {"name": "Office Rack", "price": "₹3,000 - ₹8,000", "desc": "Multi-shelf storage for offices", "image": "🪜"},
            {"name": "Book Shelf", "price": "₹2,500 - ₹6,000", "desc": "Perfect for books and display items", "image": "🪜"},
        ],
        "Beds": [
            {"name": "Single Bed", "price": "₹6,000 - ₹12,000", "desc": "Durable steel frame with storage", "image": "🛏️"},
            {"name": "Double Bed", "price": "₹10,000 - ₹20,000", "desc": "Spacious double bed with storage", "image": "🛏️"},
        ],
    }
    
    category = st.selectbox("Select Category", list(categories.keys()))
    products = categories[category]
    
    # Display products in grid
    cols = st.columns(4)
    for i, product in enumerate(products):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="product-card">
                <div style="font-size: 3rem; text-align: center;">{product['image']}</div>
                <h4 style="text-align: center; margin: 0.5rem 0;">{product['name']}</h4>
                <p style="color: #10b981; font-weight: bold; text-align: center;">{product['price']}</p>
                <p style="color: #64748b; text-align: center; font-size: 0.875rem;">{product['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Inquire {product['name']}", key=f"inquire_{i}"):
                st.session_state['page'] = 'Quote Request'
                st.rerun()
    
    st.markdown("---")
    st.info("💡 Need something custom? We also make furniture as per your specifications!")

# Order Tracking Page
def track_order_page():
    st.markdown("# 🔍 Track My Order")
    st.markdown("Enter your phone number to track your order status")
    
    phone = st.text_input("📱 Enter Phone Number", placeholder="e.g., 9876543210")
    
    if phone:
        conn = sqlite3.connect('ganesh_steel.db')
        df = pd.read_sql_query(f"SELECT * FROM orders WHERE phone = '{phone}'", conn)
        conn.close()
        
        if not df.empty:
            st.success(f"Found {len(df)} order(s) for phone: {phone}")
            
            for _, order in df.iterrows():
                # Status badge styling
                status_class = f"status-{order['status'].lower().replace(' ', '-')}"
                st.markdown(f"""
                <div style="background: white; padding: 1.5rem; border-radius: 1rem; margin: 1rem 0; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h3 style="margin: 0;">📦 Order ID: {order['order_id']}</h3>
                        <span class="status-badge {status_class}">{order['status']}</span>
                    </div>
                    <hr style="margin: 1rem 0;">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                        <div>
                            <p><strong>Customer:</strong> {order['customer_name']}</p>
                            <p><strong>Item:</strong> {order['item_description']}</p>
                            <p><strong>Dimensions:</strong> {order['dimensions']}</p>
                        </div>
                        <div>
                            <p><strong>Order Date:</strong> {order['order_date']}</p>
                            <p><strong>Expected Delivery:</strong> {order['expected_delivery']}</p>
                            <p><strong>Advance Paid:</strong> ₹{order['advance_paid']:,}</p>
                            <p style="color: #dc2626;"><strong>Balance Due:</strong> ₹{order['balance_due']:,}</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Progress indicator
                status_steps = ["Order Placed", "In Production", "Ready for Delivery", "Delivered"]
                current_step = status_steps.index(order['status']) if order['status'] in status_steps else 0
                
                st.markdown("### Order Progress")
                progress_cols = st.columns(4)
                for i, step in enumerate(status_steps):
                    with progress_cols[i]:
                        if i <= current_step:
                            st.success(f"✅ {step}")
                        else:
                            st.markdown(f"⬜ {step}")
        else:
            st.warning("No orders found for this phone number. Please check and try again.")
            st.info("💡 Make sure to use the same phone number you provided when placing the order.")

# Quote Request Page
def quote_request_page():
    st.markdown("# 📝 Request a Custom Quote")
    st.markdown("Tell us about your requirements and we'll get back to you!")
    
    with st.form("quote_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("👤 Your Name", placeholder="Enter your full name")
            phone = st.text_input("📱 Phone Number", placeholder="e.g., 9876543210")
        
        with col2:
            item_type = st.selectbox("📦 Item Type", [
                "Select an option",
                "Almirah/Wardrobe",
                "Office Rack",
                "Book Shelf",
                "Bed",
                "Kitchen Cabinet",
                "File Cabinet",
                "Custom Furniture"
            ])
        
        dimensions = st.text_area("📐 Dimensions (Length x Width x Height)", 
                                   placeholder="e.g., 6ft x 4ft x 2ft or specific measurements")
        
        additional_info = st.text_area("📝 Additional Requirements (Optional)",
                                        placeholder="Any specific color, design, or features you'd like...")
        
        submit = st.form_submit_button("📨 Submit Request")
        
        if submit:
            if name and phone and item_type != "Select an option" and dimensions:
                # Save to database
                conn = sqlite3.connect('ganesh_steel.db')
                c = conn.cursor()
                c.execute("""INSERT INTO custom_requests 
                            (name, phone, item_type, dimensions, additional_info, request_date) 
                            VALUES (?, ?, ?, ?, ?, ?)""",
                          (name, phone, item_type, dimensions, additional_info, datetime.now().strftime("%Y-%m-%d")))
                conn.commit()
                conn.close()
                
                st.success("🎉 Thank you! Your quote request has been submitted successfully!")
                st.info("📞 We'll contact you shortly at your provided phone number.")
            else:
                st.error("Please fill in all required fields (Name, Phone, Item Type, Dimensions)")
    
    st.markdown("---")
    st.info("💡 For immediate assistance, call us at **9510706177**")

# Contact Page
def contact_page():
    st.markdown("# 📞 Contact Us")
    st.markdown("We're here to help! Reach out to us anytime.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🏭 Ganesh Steel Furniture
        
        **Address:**
        Girdharnagar,
        Himmatnagar, Gujarat
        
        ---
        
        ### 📞 Contact Information
        
        **Phone:** 9510706177
        
        **Email:** panchalvedant331@gmail.com
        
        ---
        
        ### 🕐 Business Hours
        
        - Monday - Saturday: 9:00 AM - 7:00 PM
        - Sunday: Closed
        """)
        
        # Contact Buttons
        st.markdown("### 🚀 Quick Connect")
        st.button("📞 Call Now: 9510706177")
        st.button("✉️ Email: panchalvedant331@gmail.com")
    
    with col2:
        st.markdown("### 📍 Our Location")
        
        # Map placeholder (in production, use Google Maps embed)
        st.info("""
        🗺️ **Girdharnagar, Himmatnagar**
        
        (Google Maps would be integrated here in production)
        
        Himmatnagar is in Sabarkantha district, Gujarat, India.
        """)
        
        # Contact Form
        st.markdown("### 💬 Send us a Message")
        with st.form("contact_form"):
            contact_name = st.text_input("Your Name")
            contact_phone = st.text_input("Phone Number")
            contact_message = st.text_area("Message")
            
            if st.form_submit_button("📨 Send Message"):
                if contact_name and contact_phone and contact_message:
                    st.success("Message sent! We'll get back to you soon.")
                else:
                    st.error("Please fill in all fields")

# Main App
def main():
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Home'
    
    # Get page from sidebar
    choice = sidebar()
    
    # Map sidebar choice to page
    page_map = {
        "🏠 Home": "Home",
        "📦 Products": "Products",
        "🔍 Track Order": "Track Order",
        "📝 Quote Request": "Quote Request",
        "📞 Contact": "Contact"
    }
    
    st.session_state['page'] = page_map.get(choice, "Home")
    
    # Render the appropriate page
    if st.session_state['page'] == "Home":
        home_page()
    elif st.session_state['page'] == "Products":
        products_page()
    elif st.session_state['page'] == "Track Order":
        track_order_page()
    elif st.session_state['page'] == "Quote Request":
        quote_request_page()
    elif st.session_state['page'] == "Contact":
        contact_page()

if __name__ == "__main__":
    main()
