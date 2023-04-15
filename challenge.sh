#!/bin/bash
terminal_style_type=$TERM
message='THIS IS JUST TO TELL YOU THAT YOU HAVE TO FIND THE VULNERABILITY IN MY BASH SCRIPT'

function show() {
        printf "[+] process execution enheritence via terminal :-\n"
        /usr/bin/ps
        printf "\n"
        echo '----------------'

        if [[ $1 ]]; then
                echo [+] terminal style enherited : $1
                echo [+] COLORTERM : $COLORTERM
                echo [+] you are im $PWD
                echo [+] current shell in use : $SHELL
        fi
        echo '---------------'
        printf "\n\n"
}
function do_stuff() {
        echo hello solver my name is whoamiPwns. Here your terminal utility chart...
        echo '------------------'
        if [[ $1 = "" ]]; then
                show
        else
                show $1
        fi
}
do_stuff $terminal_style_type
if [ $terminal_style_type = 'xterm-256color' ]; then
        echo $message
else
        echo shit
fi
