pkgname = "opensuse-migration"
ver = $(shell rpm -q --specfile --qf '%{VERSION}' $(pkgname).spec)

tar:
	mkdir "$(pkgname)-$(ver)"
	cp -r leap-cli services/ "$(pkgname)-$(ver)"
	tar -cjf "$(pkgname)-$(ver).tar.bz2" "$(pkgname)-$(ver)"
	rm -rf "$(pkgname)-$(ver)"

