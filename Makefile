clean:
	for f in `find . -name "*~"`;do rm -rf $$f; done
	for f in `find . -name "*.pyc"`;do rm -rf $$f; done
