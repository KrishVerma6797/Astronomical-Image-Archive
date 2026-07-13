import streamlit as st

st.set_page_config(page_title="Astronomical Image Archive",page_icon="🔭",layout="wide")
st.title("🔭 Astronomical Image Archival & Retrieval System")
st.write("Search, explore and archive astronomical FITS images.")
st.divider()
st.subheader("Welcome")
st.write("""
This system provides:

- 🔍 Astronomical image search
- 🖼️ Thumbnail preview
- 📄 FITS image metadata
- 📥 Original FITS file access
- 📤 FITS image archival
""")