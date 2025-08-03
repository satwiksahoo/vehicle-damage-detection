# import streamlit as st
# from model_helper import predict 

# st.title('VEHICLE DAMAGE DETECTION')

# uploaded_file = st.file_uploader('upload your file' , type =['jpg' , 'png'])

# if uploaded_file :
#     image_path = 'temp_file.png'
#     with open(image_path , 'wb') as f:
        
#         f.write(uploaded_file.getbuffer())
#         st.image(uploaded_file , caption='uploaded file' , use_container_width=True)
#         prediction = predict(image_path)
#         st.info(f'predicted class : {prediction}')
        
    
# ----------------------------------------------====================================-----------------------------------------------


# import streamlit as st
# from model_helper import predict

# # Page configuration
# st.set_page_config(
#     page_title="Vehicle Damage Detection",
#     page_icon="🚗",
#     layout="centered"
# )

# # Title section
# st.markdown(
#     "<h1 style='text-align: center; color: #2E86AB;'>🚗 Vehicle Damage Detection</h1>",
#     unsafe_allow_html=True
# )

# st.markdown(
#     "<p style='text-align: center; color: #555;'>Upload an image of a vehicle, and our model will predict the type of damage (if any).</p>",
#     unsafe_allow_html=True
# )

# # File uploader
# uploaded_file = st.file_uploader(
#     "📤 Upload a vehicle image (.jpg, .png)", 
#     type=["jpg", "png"], 
#     help="Make sure the image is clear and shows the vehicle part clearly"
# )

# # Processing and display
# if uploaded_file:
#     image_path = "temp_file.png"
    
#     # Save the uploaded image
#     with open(image_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     # Display uploaded image
#     st.image(uploaded_file, caption="📸 Uploaded Image", use_container_width=True)

#     with st.spinner("Analyzing image..."):
#         prediction = predict(image_path)

#     # Output section
#     st.success("✅ Prediction complete!")
#     st.markdown(
#         f"<h3 style='text-align: center; color: #27AE60;'>Predicted Class: <b>{prediction}</b></h3>",
#         unsafe_allow_html=True
#     )

#     st.markdown("---")
#     st.caption("Model powered by PyTorch + Streamlit")


# --------------------------------------------================================-------------------------------------


import streamlit as st
from model_helper import predict

# Page setup
st.set_page_config(
    page_title="Vehicle Damage Detection System",
    layout="wide"
)

# Custom styling
st.markdown("""
    <style>
    body {
        background-color: #f4f6f8;
    }
    .title {
        text-align: left;
        font-size: 36px;
        color: #ffffff;
        font-weight: 700;
        padding-bottom: 10px;
        border-bottom: 2px solid #e5e7eb;
    }
    .subheader {
        color: #6b7280;
        font-size: 18px;
        padding-bottom: 25px;
    }
    # .upload-box {
    #     background-color: #ffffff;
    #     border: 1px solid #e5e7eb;
    #     border-radius: 10px;
    #     padding: 25px;
    #     margin-top: 15px;
    # }
    .prediction-box {
        background-color: #ecfdf5;
        padding: 20px;
        border: 1px solid #10b981;
        border-radius: 8px;
        color: #065f46;
        font-weight: 600;
        font-size: 20px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Layout
st.markdown('<div class="title">Vehicle Damage Detection System</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Upload a clear image of a vehicle to detect visible damage using our AI model.</div>', unsafe_allow_html=True)

# File uploader
# st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload a vehicle image (.jpg, .png)", type=["jpg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

# Main processing
if uploaded_file:
    image_path = "temp_file.png"
    
    # Save file
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Show image and predict
    st.image(uploaded_file, caption="Uploaded Vehicle Image", use_container_width=True)

    with st.spinner("Running model inference..."):
        prediction = predict(image_path)

    # Result box
    st.markdown(f'<div class="prediction-box">Predicted Class: {prediction}</div>', unsafe_allow_html=True)

    st.markdown("----")
    st.caption("This tool uses deep learning to automate vehicle damage inspection.")

# Optional: Sidebar
# with st.sidebar:
#     st.header("🧠 Model Info")
#     st.write("• Architecture: ResNet50")
#     st.write("• Framework: PyTorch")
#     st.write("• Accuracy: ~80% on test set")
#     st.write("• Use case: Insurance, manufacturing, fleet inspection")







# import streamlit as st
# from model_helper import predict

# # Page Configuration
# st.set_page_config(
#     page_title="Vehicle Damage Detection",
#     layout="centered",
#     page_icon="🚗"
# )

# # Custom CSS
# st.markdown("""
#     <style>
#     .main {
#         background-color: #f9fafb;
#         padding: 2rem;
#     }
#     .title {
#         font-size: 2.5rem;
#         font-weight: 700;
#         color: #111827;
#         text-align: center;
#         margin-bottom: 1rem;
#     }
#     .description {
#         font-size: 1rem;
#         color: #6b7280;
#         text-align: center;
#         margin-bottom: 2rem;
#     }
#     .upload-section {
#         background-color: #ffffff;
#         border: 1px solid #e5e7eb;
#         border-radius: 0.75rem;
#         padding: 2rem;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.05);
#     }
#     .result-box {
#         background-color: #fef3c7;
#         border-left: 5px solid #f59e0b;
#         padding: 1rem;
#         border-radius: 0.5rem;
#         font-size: 1.1rem;
#         font-weight: 500;
#         color: #92400e;
#         margin-top: 1.5rem;
#         text-align: center;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown('<div class="title">Vehicle Damage Detector</div>', unsafe_allow_html=True)
# st.markdown('<div class="description">Upload a photo of a vehicle and let the model detect any visible damage.</div>', unsafe_allow_html=True)

# # Upload section
# st.markdown('<div class="upload-section">', unsafe_allow_html=True)
# uploaded_file = st.file_uploader("📤 Upload Image (.jpg or .png)", type=["jpg", "png"])
# st.markdown('</div>', unsafe_allow_html=True)

# # Prediction
# if uploaded_file:
#     image_path = "temp_uploaded_image.png"
#     with open(image_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
    
#     st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

#     with st.spinner("🔍 Analyzing image..."):
#         prediction = predict(image_path)

#     st.markdown(f'<div class="result-box">Predicted Class: {prediction}</div>', unsafe_allow_html=True)

#     st.caption("⚙️ Powered by a ResNet-based deep learning model")

# # Optional footer
# st.markdown("---")
# st.caption("Made with ❤️ using Streamlit • Ideal for insurance & fleet inspection applications")
