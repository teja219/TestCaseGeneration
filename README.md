# TestCaseGeneration

Installation 

1. Clone the project locally
2. Create a virtual environment in the root folder: python3.10 -m venv env
3. Activate the virtual environment: source env/bin/activate
4. brew install graphviz
5. pip install --global-option=build_ext --global-option="-I$(brew --prefix graphviz)/include/" --global-option="-L$(brew --prefix graphviz)/lib/" pygraphviz
6. Install all packages in requirements.txt file: python3.10 -m pip install -r requirements.txt