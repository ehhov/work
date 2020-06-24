#!/bin/bash
replace() {
	# replace all appearances of $1 with $2 in files accessible by 'grep -r'
	# pattern can only contain normal letters and /
	# filenames can include any of '#@!&*${}"'\ ' and so on
	# works perfectly with all types of links and saves file permissions
	f="$1"
	what="${f//\//\\\/}"
	with="${2//\//\\\/}"
	grep -Rl "$f" | while IFS= read -r file; do 
		cat "$file" >| /tmp/temp
		sed "s/$what/$with/g" /tmp/temp >| "$file"
	done
}
funcs=""

py_to_2(){
	replace '/bin/python3' '/bin/3python'
	replace '/bin/python2' '/bin/python'
	replace '/bin/python' '/bin/python2'
	replace '/bin/3python' '/bin/python3'
}
funcs="$funcs py_to_2"

env_py_to_2() {
	replace '/bin/env python3' '/bin/env 3python'
	replace '/bin/env python2' '/bin/env python'
	replace '/bin/env python' '/bin/env python2'
	replace '/bin/env 3python' '/bin/env python3'
}
funcs="$funcs env_py_to_2"

ipy_to_2(){
	replace '/bin/ipython3' '/bin/3ipython'
	replace '/bin/ipython2' '/bin/ipython'
	replace '/bin/ipython' '/bin/ipython2'
	replace '/bin/3ipython' '/bin/ipython3'
}
funcs="$funcs ipy_to_2"

env_ipy_to_2() {
	replace '/bin/env ipython3' '/bin/env 3ipython'
	replace '/bin/env ipython2' '/bin/env ipython'
	replace '/bin/env ipython' '/bin/env ipython2'
	replace '/bin/env 3ipython' '/bin/env ipython3'
}
funcs="$funcs env_ipy_to_2"

PS3='Choose a function: '
select func in $funcs exit
do
	$func
done
