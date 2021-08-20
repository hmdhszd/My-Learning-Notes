
while [ 1 ]
do

	sleep 30

	x=`curl --max-time 5 --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/ | cat | grep -m 1 -o 1 | xargs`

	if [ $x+1 != "1+1" ]

	then
		notify-send " OMG tor is not working "
		systemctl restart tor
	fi

done
