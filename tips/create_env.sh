
env_name="test"
virtualenv -p /Users/yurei/opt/anaconda3/bin/python ~/$env_name
source ~/$env_name/bin/activate
pip install --upgrade pip
pip install -r requirements_basic.txt
python -m ipykernel install --name $env_name
