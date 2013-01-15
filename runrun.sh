HOME=/Users/kkung/private/chooseok

source $HOME/env/bin/activate
python gohome.py data_0930.json &
python gohome.py data_1001.json &
python gohome.py data_0929_1001.json &
echo "gogogo"
