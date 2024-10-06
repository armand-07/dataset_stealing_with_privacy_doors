# White-box Data Stealing in MLPs
This project is based on the theoretical framework presented in the paper Privacy Backdoors: Stealing Data with Corrupted Pretrained Models by Shanglun Feng and Florian Tramèr. The study explores the vulnerabilities introduced when pretrained machine learning models are tampered with, creating privacy backdoors that can compromise the finetuning data.

In this practical study, it has been implemented and tested the concepts outlined in the paper. The experiments demonstrate how an attacker can manipulate pretrained model weights (MNIST) to extract sensitive information from finetuned datasets (Fashion MNIST). The following image shows the result after corrupting only 64 neurons. It shows how some images can be rescontructed perfectly, as they were in the dataset.  

![image](https://github.com/user-attachments/assets/8a724a8f-78b9-474e-8085-a5c53deb7375)


The goal of this project is to provide a deeper understanding of the risks associated with using untrusted pretrained models and to highlight the importance of securing the machine learning supply chain. By sharing the findings and code, the aim is to contribute to the development of more robust defenses against privacy backdoors in machine learning.

This repository contains a series of Jupyter notebooks that demonstrate various aspects of white-box data stealing in Multi-Layer Perceptrons (MLPs). Each notebook covers a specific topic or experiment related to this subject. **Please, follow the order specified to replicate results:**

## Notebooks

### 1. Pretraining_MNIST.ipynb
This notebook demonstrates the pretraining process on the MNIST dataset. It includes data loading, model definition, training, and evaluation. Moreover it presents how the attacker can aim to capture all kinds of data or specific distributed data. 

### 2. Finetuning_F_MNIST.ipynb
This notebook shows how to fine-tune a pretrained model on the Fashion MNIST dataset. It covers data loading, model adjustment, training, and evaluation. 

### 3. Data_Stealing_Attack.ipynb
This notebook illustrates a data stealing attack on an MLP. It includes the loading of both models, and the extraction of data from the finetuned model.

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/white-box-data-stealing-mlps.git
   cd white-box-data-stealing-mlps

2. **Create a virtual environment:**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install the required packages:**
    ``` sh
    pip install -r requirements.txt

4. **Run Jupyter Notebook:**
    ```
    jupyter notebook

5. **Open the desired notebook in the Jupyter interface and run the cells.**

## Requirements
- Python 3.6 or higher
- Jupyter Notebook
- PyTorch
- torchvision
- matplotlib
- numpy

## Usage
Each notebook is designed to be run independently, but to replicate the results it is important to be runned following the mentioned order. Follow the instructions within each notebook to understand the specific steps and code execution.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
The MNIST and Fashion MNIST datasets are provided torchvision, developed by Yann LeCun and Zalando, respectively.
The PyTorch library is used for model implementation and training.
The general backdoor working theory was developed by Shanglun Feng and Florian Tramèr.
