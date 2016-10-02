## Install comet
cd /home/
virtualenv comet
. comet/bin/activate
cd comet/
mkdir logs/
mkdir src/
apt-get update
pip install comet


## Install Fourpisky
git clone https://github.com/4pisky/fourpiskytools.git
cd fourpiskytools/
pip install .
cd examples

source listen_for_voevents.sh

