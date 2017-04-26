.PHONY: run clean doc doctest

run:
	touch test.py
	echo "import Main\n\nMain.start()\n" > test.py
	python test.py
	rm -rvf test.py

clean:
	rm -rvf *.pyc documentation/*.html

doc:
	pydoc -w ./
	mv *.html	documentation/

dts:
	python Editor.py -v
	python In_out.py -v

