import kagglehub

def kaggle_download(site_path):
# Download latest version
    path = kagglehub.dataset_download(site_path)

    print("Path to dataset files:", path)
