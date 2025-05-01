# smolder
A quick and easy summary tool to evaluate counts inside the QA and PROD FHIR servers. 

To install the summary library to permit the example runner script to run, run the following command:

pip install -e .

This will install it in a way that will allow your edits to the library to be used without having to reinstall. 


# smolder notebook


### An easy way to run FHIR queries



### Prerequisites
* **Jupyter Notebook:**  You'll need Jupyter Notebook installed.  If you don't have it, follow the instructions at [https://jupyter.org/install](https://jupyter.org/install)
* **Python:**  Ensure you have a compatible version of Python installed. This notebook is designed for Python 3.12.2

## Installation
1.  **Install Jupyter**
    ```bash
    pip install jupyterlab

2. **Clone the repository:**
   ```bash
   git clone https://github.com/include-dcc/smolder.git

## Setting Up the `fhir_hosts` File

### 1. Obtain the Necessary Secret

1. To create a valid `fhir_hosts` file, you'll need to obtain a secret that includes the credentials and other information necessary to authenticate with the FHIR server. You can request these credentials by contacting Singh, Natasha at <SINGHN4@chop.edu>.

### 2. Create the `fhir_hosts` File
1. create file named `fhir_hosts` in the smolder root directory
2. copy and paste the text below in the `fhir_hosts` file
3. replace [replace me] with the acquired credintials

```yaml
QA:
    auth_type: "auth_kf_openid"
    client_id: "[replace me]"
    client_secret: "[replace me]"
    token_url: "[replace me]"
    target_service_url: "https://include-api-fhir-service-upgrade-qa.includedcc.org"
    
PROD:
    auth_type: "auth_kf_openid"
    client_id: "[replace me]"
    client_secret: "[replace me]"
    token_url: "[replace me]"
    target_service_url: "https://include-api-fhir-service-upgrade.includedcc.org"
```
## Use
1. **Navigate to smolder directory**
    ```bash
    cd smolder
2. **Start jupyter lab**
    ```bash
    jupyter lab
3. **double click on smolder_notebook.ipynb**
<br>   <img width="400" alt="image"  src="https://github.com/user-attachments/assets/4fb61606-00f7-40fb-9c51-31dc375151c3" style="margin-left: 20px!important;">

4. **Select Run all cells from top menu**
<br>   <img width="400" alt="image" src="https://github.com/user-attachments/assets/5838a15c-cf8d-478f-aedc-0e1e932b3b34">

