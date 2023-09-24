#!/bin/sh

genname() {
	while :; do
		f="file$(tr -dc A-Za-z0-9 < /dev/urandom | head -c 50; echo '')"
		if ! [ -e "/tmp/$f" ]; then break; fi
	done
	echo "/tmp/$f"
}


count() {
	name=$(genname)
	"$@" > "$name"

	full=$(wc -m < "$name")
	nospace=$(tr -d '[:space:]\t\n' < "$name" | wc -m)
	alnum=$(tr -cd '[:alnum:]' < "$name" | wc -m)

	rm "$name"

	echo "$@ output ($name) stats:"
	echo "  Full        ${full}"
	echo "  no space    ${nospace}"
	echo "  only alnum  ${alnum}"
}

pdf2lazytxt() {
	for file in "$@"; do
		ps2ascii "$file" > "${file%.pdf}.lazytxt"
	done
}


#pdf2lazytxt tmp/lhcb-B2DKstar*pdf

count cat src/200k/*txt
#count ps2ascii tmp/belle*pdf
