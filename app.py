import streamlit as st
from burnx import Analyzer
from style import style_code


st.set_page_config(
    page_title="Burnx - analyze skin burn degree", page_icon=":material/emergency_heat:"
)
st.html(style_code)

st.title("Burnx :material/emergency_heat:")
st.subheader("Analyze Skin Burn Degree")

tab1, tab2, tab3 = st.tabs(["Burnx", "How-To", "About"])

with tab1:
    st.write("")
    with st.container(border=True, key="burnx"):
        use_cam = st.toggle("Use camera", key="use_cam")

        img_file = (
            st.camera_input(":material/add_a_photo: Take a picture of burned skin")
            if use_cam
            else st.file_uploader(
                ":material/image_arrow_up: Upload burned skin image",
                type=["jpg", "jpeg", "png"],
                accept_multiple_files=False,
            )
        )

        if st.button("Analyze image", type="primary", use_container_width=True):
            if img_file is not None:
                with st.spinner("Analyzing..."):
                    st.toast("Image is being analyzed.", icon=":material/hourglass:")
                    predicted = Analyzer(img_file)
                    st.write("")
                    st.write("")
                    st.write(":material/task_alt: Predicted image")
                    st.image(
                        predicted, caption="Predicted image", use_container_width=True
                    )
                    st.toast("Image analyzed successfully!", icon=":material/task_alt:")
            else:
                st.toast("Please upload an image", icon=":material/warning:")

with tab2:
    st.write("")
    with st.container(border=True, key="howto"):
        st.markdown(
            """
            ### How to Use
        
            Using the app is simple and intuitive:

            1. **Prepare your image**  
            - Ensure it is a clear, close-up image of the burned skin area.  
            - Accepted formats: `.jpg`, `.jpeg`, `.png`.
            
            2. **Upload your image**  
            - Either **toggle on "Use Camera"** to take a live photo, or toggle off to **upload** from your device.  
            - You can **drag and drop** the image or click **"Browse files"** to select manually.
            
            3. **Analyze the image**  
            - Click the **"Analyze Image"** button.  
            - Wait a few seconds while the AI processes the image.

            > :material/warning: This tool is for demonstration and educational purposes only. It is **not a replacement for professional medical diagnosis**.
            """
        )

with tab3:
    st.write("")
    with st.container(border=True, key="about"):
        st.markdown(
            """
            ### About the App
            
            This is an AI-powered app designed to automatically detect and classify **burn injuries** from skin images into **four severity levels**:
            
            - **First-degree burns** (superficial)  
            - **Second-degree burns** (superficial partial-thickness)  
            - **Second-degree burns** (deep partial-thickness)  
            - **Third-degree burns** (full thickness)
            
            Leveraging deep learning and computer vision, this tool helps provide **instant burn classification** and **visual bounding box localization** on the affected area.
            
            ---
            
            **Key Features**:
            
            - **Camera capture support**
            - **Drag & Drop** or **Choose File** image upload  
            - **One-click image analysis**  
            - **Visual output** with bounding boxes and classification  
            - **Simple, fast, responsive interface**
            
            > This project was built as part of my portfolio.
            """
        )
