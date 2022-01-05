_build/html/index.html: *.ipynb
	jupyter-book build .

upload: _build/html/index.html
	rsync -avu _build/html/ lesta01:/www/people/savchenk/public_html/integral-ibis-isgri-le-response/
