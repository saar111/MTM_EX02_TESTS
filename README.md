## 1. Creating local environemnt on the server
Run the following command to create a local environment to run the tests (on the csl server):\
source <(curl -s https://bit.ly/3poR8nU) <path-to-your-eventManager.py>

<b>Example from my configuration on the server (after first login):</b>\
cd /home/saar.ofek/mtm/ex02/\
source <(curl -s https://bit.ly/3poR8nU) ./eventManager.py


## 2. Running the tests after step 1
Step 1 will create a directory called "tests" in the current directory you are at (where you did cd to).

<b>Now run:</b>\
cd saars_tests\
python3.6 ./test_runner.py

This will run the tests locally on the server.