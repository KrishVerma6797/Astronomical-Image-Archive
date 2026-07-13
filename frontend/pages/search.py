import streamlit as st
from api_client import (
    search_images,
    get_thumbnail_url,
    get_file_url
)

st.title("🔍 Search Astronomical Images")

object_name = st.text_input("Object Name")

col1, col2 = st.columns(2)

with col1:
    telescope = st.text_input("Telescope")
    observer = st.text_input("Observer")
    date_from = st.date_input("Date From", value=None)
    image_format = st.selectbox(
        "Image Format",
        ["", "FITS", "PNG", "JPG", "JPEG", "TIFF"]
    )

with col2:
    instrument = st.text_input("Instrument")
    filter_name = st.text_input("Filter")
    date_to = st.date_input("Date To", value=None)

if st.button("Search Images"):

    params = {
        "object_name": object_name or None,
        "telescope": telescope or None,
        "instrument": instrument or None,
        "observer": observer or None,
        "filter": filter_name or None,
        "date_from": str(date_from) if date_from else None,
        "date_to": str(date_to) if date_to else None,
        "image_format": image_format or None
    }

    try:
        data = search_images(params)

        st.success(f"{data['total_results']} images found")

        for image in data["images"]:

            st.divider()

            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(
                    get_thumbnail_url(image["image_id"]),
                    width=250
                )

            with col2:
                st.subheader(image["object_name"])

                st.write("**Image ID:**", image["image_id"])
                st.write("**Date:**", image["observation_date"])
                st.write("**Time:**", image["observation_time"])
                st.write("**Telescope:**", image["telescope_name"])
                st.write("**Instrument:**", image["instrument_name"])
                st.write("**Observer:**", image["observer_name"])
                st.write("**Filter:**", image["filter_name"])
                st.write("**Exposure Time:**", image["exposure_time"])
                st.write("**RA:**", image["ra"])
                st.write("**DEC:**", image["dec_coord"])
                st.write("**Format:**", image["image_format"])
                st.write("**Size:**", image["image_size_mb"], "MB")

                st.link_button(
                    "Open FITS File",
                    get_file_url(image["image_id"])
                )

    except Exception as e:
        st.error(f"Search failed: {e}")