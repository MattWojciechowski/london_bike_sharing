import os

def download_dataset(dataset_id, output_dir):
    """
    Downloads a dataset from Kaggle using Kaggle API and stores it in the specified directory.

    Parameters:
    - dataset_id (str): The ID of the Kaggle dataset (e.g., "hmavrodiev/london-bike-sharing-dataset").
    - output_dir (str): The directory where the dataset files will be saved.

    Returns:
    - str: The path to the directory where the dataset is saved.
    """
    # Create the output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # Construct the Kaggle API command
    command = f"kaggle datasets download -d {dataset_id} -p {output_dir} --unzip"

    # Execute the command
    print(f"Downloading dataset {dataset_id} to {output_dir}...")
    os.system(command)

    print(f"Dataset downloaded to: {output_dir}")
    return output_dir


if __name__ == "__main__":
    # Kaggle dataset ID
    DATASET_ID = "hmavrodiev/london-bike-sharing-dataset"

    # Directory to save the dataset
    OUTPUT_DIR = "data"

    # Download the dataset
    dataset_path = download_dataset(DATASET_ID, OUTPUT_DIR)
    print(f"Dataset available at: {dataset_path}")
