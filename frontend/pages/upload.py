import streamlit as st
from api_client import upload_image

st.title("📤 Upload Astronomical Image")

st.write("Upload a FITS file to the astronomical archive.")

file = st.file_uploader(
    "Choose FITS File",
    type=["fits", "fit"]
)

if file is not None:

    st.write("**File Name:**", file.name)

    if st.button("Upload Image"):

        try:
            response = upload_image(file)

            if response.status_code == 200:
                st.success(
                    "Image uploaded and archived successfully."
                )

            elif response.status_code == 409:
                st.warning("Image already archived.")

            else:
                st.error(
                    response.json().get(
                        "detail",
                        "Upload failed"
                    )
                )
        except Exception as e:
            st.error(f"Upload failed: {e}")