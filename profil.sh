#!/bin/bash
for i in {1..500}; do
	echo $i >count.txt
	curl https://profile-counter.glitch.me/KAnggara75/count.svg >profile.svg
done
