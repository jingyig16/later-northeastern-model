# later-northeastern-model
### Fall 2024

This repository is for DATA Pacticum semester client project with Later, a social media and influencer marketing company. 
In this project, we want to explore about if images be classified into useful categories at scale and at low cost, and with one million images with no words or labels, we'd like to conduct research on available open-source models and look for solutions to categorize images, as well as add labels and keywords to each piece of media.

Note: File path configuration of this project was changed accordingly to avoid absolute path. Some changes in individual files and environment setup may be needed to successfully run this project on local laptop or cloud computing services.

To run this project on local laptop:
- save images by changing dataset path and run `utils.py`
- download Python dependencies by `pip install -r requirements.txt`, 
- download mistral-7b-instruct-v0.2.Q5_K_M.gguf to `models` folder from [https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/tree/main]
- click run in `main.py` or through `python main.py`

Data: 

Access with Northeastern Google account: [https://drive.google.com/file/d/1GQDtwXT3Vkmi7-0wUKfW5JJoww3t3XfS/view?pli=1]

File structure:

later-northeastern-model/

├── README.md                     # Project documentation

├── .gitignore                   # Git ignore rules

├── main.py                  # Main application code

├── config.py                  # Configuration of file pathes

├── utils.py                  # Script to download images to local folder

│

├── models/                  # Model-related code

│   ├── __init__.py

│   ├── clip_model.py        # CLIP model implementation

│   ├── faiss_model.py       # FAISS indexing implementation

│   ├── vlm_model.py         # Vision Language Model implementation

│   └── mistral-7b-instruct-v0.2.Q5_K_M.gguf       # FAISS indexing implementation

│

│── preprocessing/           # Data preprocessing code

│   └── preprocessing.py     # Image preprocessing logic

│

│── embeddings/              # Embedding generation code

│   └── embeddings.py        # Embedding generation logic

│

├── clustering/              # Clustering logic

│   ├── __init__.py

│   └── categorymanager.py   # Category management implementation

│

├── data/                        # Data directory

│   └── dataset.csv              # Original Dataset file

├── images/                        # Image directory downloaded from utils.py

├── .gitignore                     

│

└── faiss_index/                  # Output directory

    └── index_file.index         # FAISS index file

contents in .gitignore:
  ```
  /models/mistral-7b-instruct-v0.2.Q5_K_M.gguf
  /normalized_data
  /images
  /data
  ```