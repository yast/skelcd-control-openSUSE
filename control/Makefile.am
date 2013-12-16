# Makefile.am for yast2-installation-control/control
#

controldir = $(yast2dir)/control

control_DATA = \
	control.rnc \
	control.rng

# install the XML control files into documentation dir
# they are not used directly, they are just picked there by a specific
# skelcd-control-* package
xmldir = $(docdir)/control_files

xml_DATA = \
	control.SLED.xml \
	control.SLES.xml \
	control.SLES-for-VMware.xml \
	control.openSUSE.xml \
        control.openSUSE-promo.xml \
	add-on-template_installation.xml

CLEANFILES = control.openSUSE-promo.xml control.SLES-for-VMware.xml

# generate the control.openSUSE-promo.xml control file
control.openSUSE-promo.xml: control.openSUSE-promo.xsl control.openSUSE-promo.changes.xml control.openSUSE.xml
	xsltproc control.openSUSE-promo.xsl control.openSUSE.xml > control.openSUSE-promo.xml

# generate the control.SLES-for-VMware.xml control file
control.SLES-for-VMware.xml: control.SLES-for-VMware.xsl control.SLES.xml
	xsltproc control.SLES-for-VMware.xsl control.SLES.xml > control.SLES-for-VMware.xml

# Note: The control.*.glade -> control.*.xml symlink is required to make xgettext
# auto-detect the type of this file (glade) so it will extract all
# <label>..</label> tags. The symlink is created in the toplevel
# configure.in.in file upon "autoconf" (via "make -f Makefile.cvs").
# Unfortunately, CVS doesn't support checking in symlinks - it would duplicate
# the file. 

# Distribute also the generated control.rng file, the reason is that "trang"
# is a Java tool which adds huge dependency in OBS.
#
# The conversion happens during "make package" when building the tarball.
# The RNG file gets automatically updated after any change by the "control.rng"
# rule below.
#
# At build time the RNG file from tarball will have a newer time stamp
# and thus it will not need rebuild/update making "trang" unnecessary.
EXTRA_DIST =  $(control_DATA) $(xml_DATA) indent.xsl

include $(top_srcdir)/Makefile.am.common

control.rng: control.rnc
	trang -I rnc -O rng control.rnc control.rng

# checks only those control files that belong to this package
check-local: control.rng $(xml_DATA)
	xmllint --relaxng control.rng --noout $(xml_DATA)
