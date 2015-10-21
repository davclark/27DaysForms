pdf: fill
	for inf in html_forms/*.html; do ./html2pdf.py "$${inf}"; done

fill: template.html
	./fill_template.py responses/0.json

