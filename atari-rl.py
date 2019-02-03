!wget https://www.dropbox.com/s/rbgg6mbunq8qtr3/newCallback.py
!wget ????
!wget https://www.dropbox.com/s/g69yj8ia900bk1p/dqn_Atari_512.py

#!pip install tensorflow==1.6.0
!apt-get install cmake
#!apt-get install swig
!pip install gym[atari]
#!pip install gym[Box2D]
#!pip install keras-rl

!pip install dropbox

!git clone https://github.com/matthiasplappert/keras-rl.git
#import os
#os.chdir('keras-rl/')
%cd keras-rl/
!python setup.py install
#!pip install -e .
#os.chdir('../')
import rl
%cd ../


!python3 ./dqn_Atari_512.py
