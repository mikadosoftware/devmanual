#CONSTANTS
PYTHON=python

#TARGETS
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<

##book: build The Software Mind (book)
.PHONY: book 
book:
	cd bin;	sh mkdocs.sh

# useful reference for make: https://swcarpentry.github.io/make-novice/reference
