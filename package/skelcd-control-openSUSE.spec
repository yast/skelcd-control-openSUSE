#
# spec file for package skelcd-control-openSUSE
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

######################################################################
#
# IMPORTANT: Please do not change the control file or this spec file
#   in build service directly, use
#   https://github.com/yast/skelcd-control-openSUSE repository
#
#   See https://github.com/yast/skelcd-control-openSUSE/blob/master/CONTRIBUTING.md
#   for more details.
#
######################################################################

Name:           skelcd-control-openSUSE
# xmllint
BuildRequires:  libxml2-tools
# xsltproc
BuildRequires:  libxslt-tools
# RNG schema
BuildRequires:  yast2-installation-control >= 3.1.7

######################################################################
#
# Here is the list of Yast packages which are needed in the
# installation system (inst-sys) for the Yast installer
#

# Generic Yast packages needed for the installer
Requires:       autoyast2
Requires:       yast2-add-on
Requires:       yast2-fcoe-client
# For creating the AutoYast profile at the end of installation (bnc#887406)
Requires:       yast2-firewall
Requires:       yast2-iscsi-client
Requires:       yast2-kdump
Requires:       yast2-multipath
Requires:       yast2-network >= 3.1.24
Requires:       yast2-nfs-client
Requires:       yast2-ntp-client
Requires:       yast2-proxy
Requires:       yast2-services-manager
Requires:       yast2-slp
Requires:       yast2-trans-stats
Requires:       yast2-tune
Requires:       yast2-update
Requires:       yast2-users
Requires:       yast2-x11
# this is the default theme
Requires:       yast2-theme-openSUSE-Oxygen
Requires:       yast2-qt-branding-openSUSE

# Architecture specific packages
#

%ifarch %ix86 x86_64
Requires:  yast2-vm
%endif

#
######################################################################

Url:            https://github.com/yast/skelcd-control-openSUSE
AutoReqProv:    off
Version:        13.2.22
Release:        0
Summary:        The openSUSE Installation Control file
License:        MIT
Group:          Metapackages
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         skelcd-control-openSUSE-%version.tar.bz2
# we do not distribute it, but need to have it here, otherwise build service checks complain
Source99:       README.md
Provides:       product_control
Conflicts:      product_control

%description
This package contains the control file used for openSUSE installation.

%prep

%setup -n skelcd-control-openSUSE-%{version}

%build
make -C control

%check
make -C control check

%install
#
# Add control file 
#
mkdir -p $RPM_BUILD_ROOT/CD1

%if "%{name}" == "skelcd-control-openSUSE-promo"
CONTROL_FILE=control.openSUSE-promo.xml
%else
CONTROL_FILE=control.openSUSE.xml
%endif

install -m 644 control/$CONTROL_FILE $RPM_BUILD_ROOT/CD1/control.xml

%ifarch ppc ppc64 ppc64le
sed -i -e "s,http://download.opensuse.org/distribution/,http://download.opensuse.org/ports/ppc/distribution/," $RPM_BUILD_ROOT/CD1/control.xml
sed -i -e "s,http://download.opensuse.org/tumbleweed/,http://download.opensuse.org/ports/ppc/tumbleweed/," $RPM_BUILD_ROOT/CD1/control.xml
sed -i -e "s,http://download.opensuse.org/debug/,http://download.opensuse.org/ports/ppc/debug/," $RPM_BUILD_ROOT/CD1/control.xml
sed -i -e "s,http://download.opensuse.org/source/,http://download.opensuse.org/ports/ppc/source/," $RPM_BUILD_ROOT/CD1/control.xml
#we parse out non existing non-oss repo for Power
xsltproc -o $RPM_BUILD_ROOT/CD1/control_ppc.xml control/nonoss.xsl $RPM_BUILD_ROOT/CD1/control.xml
mv $RPM_BUILD_ROOT/CD1/control{_ppc,}.xml
xmllint --noout --relaxng /usr/share/YaST2/control/control.rng $RPM_BUILD_ROOT/CD1/control.xml 
%endif

%files
%defattr(644,root,root,755)
%dir /CD1
/CD1/control.xml

%changelog
