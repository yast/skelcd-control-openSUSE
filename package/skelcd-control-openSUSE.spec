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


Name:           skelcd-control-openSUSE
# xmllint
BuildRequires:  libxml2-tools
# xsltproc
BuildRequires:  libxslt-tools
# RNG schema
BuildRequires:  yast2-installation-control

Url:            https://github.com/yast/skelcd-control-openSUSE
AutoReqProv:    off
Version:        13.2.3
Release:        0
Summary:        The openSUSE Installation Control file
License:        MIT
Group:          Metapackages
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         skelcd-control-openSUSE-%version.tar.bz2
Provides:       product_control
Conflicts:      product_control

# NOTE: Do not patch the control file in OBS, fork
# https://github.com/yast/skelcd-control-openSUSE instead and create a pull
# request. The package is autosubmitted from Git by Jenkins CI
# (http://ci.opensuse.org/view/Yast/)

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

%ifarch ppc ppc64
sed -i -e "s,http://download.opensuse.org/distribution/,http://download.opensuse.org/ports/ppc/distribution/," $RPM_BUILD_ROOT/CD1/control.xml
sed -i -e "s,http://download.opensuse.org/debug/,http://download.opensuse.org/ports/ppc/debug/," $RPM_BUILD_ROOT/CD1/control.xml
sed -i -e "s,http://download.opensuse.org/source/,http://download.opensuse.org/ports/ppc/source/," $RPM_BUILD_ROOT/CD1/control.xml
xmllint --noout --relaxng /usr/share/YaST2/control/control.rng $RPM_BUILD_ROOT/CD1/control.xml 
%endif

%files
%defattr(644,root,root,755)
%dir /CD1
/CD1/control.xml

%changelog
