# Makefile.am for yast2-installation-control-openSUSE/control
#

control_DATA = \
	control.openSUSE.xml \
        control.openSUSE-promo.xml \
	add-on-installation.xml

CLEANFILES = control.openSUSE-promo.xml

# generate the control.openSUSE-promo.xml control file
control.openSUSE-promo.xml: control.openSUSE-promo.xsl control.openSUSE-promo.changes.xml control.openSUSE.xml
	xsltproc control.openSUSE-promo.xsl control.openSUSE.xml > control.openSUSE-promo.xml

EXTRA_DIST =  $(control_DATA)

include $(top_srcdir)/Makefile.am.common

# checks only those control files that belong to this package
check-local: $(control_DATA)
	xmllint --relaxng $(controldir)/control.rng --noout $(control_DATA)
