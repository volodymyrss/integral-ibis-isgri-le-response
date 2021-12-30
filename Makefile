book: 
	make -C $@

version:
	bash version.sh


upload-isdc-web-page: book
	rsync -avu book/_build/html/ cdcihn:/www/people/savchenk/public_html/integral-ibis-isgri-le-response/

.PHONY: book
