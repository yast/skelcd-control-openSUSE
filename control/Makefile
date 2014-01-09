
# generate the control.openSUSE-promo.xml control file
control.openSUSE-promo.xml: control.openSUSE-promo.xsl control.openSUSE-promo.changes.xml control.openSUSE.xml
	xsltproc control.openSUSE-promo.xsl control.openSUSE.xml > control.openSUSE-promo.xml

# checks only those control files that belong to this package
check: control.openSUSE-promo.xml
	xmllint --relaxng /usr/share/YaST2/control/control.rng --noout *.xml

clean:
	rm -f control.openSUSE-promo.xml

