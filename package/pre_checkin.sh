#! /bin/sh

cp skelcd-control-openSUSE.changes  skelcd-control-openSUSE-promo.changes
sed -e 's,^Name.*,Name: skelcd-control-openSUSE-promo,' skelcd-control-openSUSE.spec > skelcd-control-openSUSE-promo.spec

osc service localrun format_spec_file

