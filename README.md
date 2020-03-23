# This is project to remove duplicates in data.
# To run main script you have to follow next steps:
### 1. Install GIT for your OS using the guide from the [link](https://www.atlassian.com/git/tutorials/install-git).
### 2. Clone current git repository:
```
git clone https://gitlab.spd-ukraine.com/rnd-ml/duplicate-finder.git
```
### 3. Install python for your OS using the guide from the [link](https://realpython.com/installing-python).
### 4. Install virtual environment library via command line:
```
pip3 install virtualenv
```
### 5. Go to the repository via command line:
```
cd path-to-the-repository
```
### 6. Create and activate virtual environment, install required libraries via command line:
**FOR LINUX AND MACOS**
```
python3 -m venv path-to-venv-folder
source path-to-venv-folder/bin/activate
pip install -r requirements.txt
```
**FOR WINDOWS**
```
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```
### 7. After this you can run main script using command line. It contain few arguments which you must passed:
- **_data_** - path to the csv file with data;
- **_folder-to-save_** - folder where new data without duplicates have to be saved;
- **_threshold (not required parameter)_** - maximum value for returned Levenshtein distance between two samples in data;
```
python main.py -data Data.csv -folder-to-save . -threshold 2
```
### Also you can run tests using command line:
```
python -m unittest test/duplicate_remover_test.py
```