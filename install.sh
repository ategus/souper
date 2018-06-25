#!/bin/bash
#pip3 install selenium
#pip3 install pandas
cp chromedriver $HOME/.local/bin
PATH=$PATH:$HOME/.local/bin/chromedriver
chmod +x $HOME/.local/bin/chromedriver
export PATH 