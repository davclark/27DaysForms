# Below are "rules" that can be run like:
#    $ make fill2pdf
# That rule will run the other rules after the ":"
# If you type make by itself:
#    $ make
# then it will run the first rule (fill2pdf).
# So, the default rule does not hit the server.
# If you want to run all the steps in one go:
#    $ make all

fill2pdf: fill pdf ;

all: get fill pdf ;

pdf:
	for inf in html_forms/*.html; do ./html2pdf.py "$${inf}"; done

fill: template.html
	./fill_template.py responses/0.json

get:
	./get_typeform.py

