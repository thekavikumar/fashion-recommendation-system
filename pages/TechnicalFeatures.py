import streamlit as st

st.set_page_config(page_title="Gallery",
                   page_icon=":shopping_bags:")

st.markdown("# :female_fairy: :frame_with_picture:")
st.markdown("# :rainbow[Technical Features] :magic_wand:")
st.divider()

st.write("The system takes in an image as an input and output similar outfits based on visual similarity attributes. The overall system looks like the following: ")

# system overview
st.image('images/flowcharts/serving_stg.png')
st.caption("As a user inputs a query item, the system detects individual fashion objects to obtain their individual vector embeddings. It then runs a similarity search algorithm on items currently available in the vector index and returns the most similar items.")

# vector index creation
st.image('images/flowcharts/vector_index.png')
st.caption("To create the vector index, the embedding model extract latent features from every item in the catalog and store it in a vector index based on their similarities. I used a Flat Index with L2 distance as its similarity measure for this project. ")

# technical features
st.divider()
st.markdown("#### Technical Features:")
st.markdown("* **Object Detection Model:** Leveraged the power of the YOLOv5 model trained on fashion images to detect fashion objects in images. ")
st.markdown("* **Feature Extraction:** Utilized a Convolutional Autoencoder implemented with PyTorch to extract latent features from detected fashion objects. ")
st.markdown("* **Vector Index and Similarity Search Algorithm:** Implemented FAISS library to construct an index, facilitating the search for visually similar outfits based on their distinct attributes. ")