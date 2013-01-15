HOME=/Users/kkung/private/chooseok

source $HOME/env/bin/activate
echo "gogogo"
for i in $(seq 1 5)
do
    python gohome.py lunar.json &
done
echo "waiting.."
wait
