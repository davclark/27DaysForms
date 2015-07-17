pdf: fill
	for inf in *.html; do ./html2pdf.py "$${inf}"; done

fill: template.html 27\ Days\ of\ Change\ Intention\ Agreement\ -\ Summer\ 2015-report.csv 
	./fill_template.py 27\ Days\ of\ Change\ Intention\ Agreement\ -\ Summer\ 2015-report.csv 

