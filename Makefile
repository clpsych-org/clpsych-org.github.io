build:
	mkdir -p _build
	cp -r static/* _build
	python build.py

clean:
	rm -r _build
