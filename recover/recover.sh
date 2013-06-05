#!/bin/bash
set -e

python extract.py

cd posts
for post in `ls`; do
	coffee ../html2md.coffee $post

	sed -i "s/&#8216;/'/g" $post
	sed -i "s/&#8217;/'/g" $post
	sed -i "s/&#8211;/–/g" $post
	sed -i "s/&#8220;/\"/g" $post
	sed -i "s/&#8221;/\"/g" $post
	sed -i "s/&amp;/&/g" $post
	sed -i "s/&gt;/>/g" $post
	sed -i "s/&lt;/</g" $post
	sed -i "s/^]//g" $post
	sed -i "s/<pre>\`//g" $post
	sed -i "s/\`<\/pre>//g" $post

	python ../hardwrap.py $post

	# cp $post ../../source/_posts/
done

