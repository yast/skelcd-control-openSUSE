#
# spec file for package yast2-installation-control-openSUSE
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


Name:           yast2-installation-control-openSUSE
Version:        3.1.0
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Summary:        YaST2 - Control file for the openSUSE distribution
License:        GPL-2.0
Group:          System/YaST
Url:            https://github.com/yast/yast-installation-control-openSUSE

BuildRequires:  yast2-devtools >= 3.1.10

# RNG schema
BuildRequires:  yast2-installation-control

# xmllint for validation
BuildRequires:  libxml2-tools

# xsltproc for generating some XML files
BuildRequires:  libxslt-tools

# add openSUSE specific requirements for the installation-images here:
# Requires:       <nothing specific yet>

BuildArch:      noarch

%description
This package contains the control file for openSUSE product.

%package promo
Summary:        YaST2 - Control file for the openSUSE-promo distribution
Group:          System/YaST
# add openSUSE-promo specific requirements for the installation-images here:
# Requires:       <nothing specific yet>

%description promo
This package contains the control file for openSUSE-promo product.

%package addon
Summary:        YaST2 - Control file for the language add-on product
Group:          System/YaST

%description addon
This package contains the control file for the openSUSE language add-on product.


%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

%files
%defattr(-,root,root)
%yast_controldir/control.openSUSE.xml

%doc %{yast_docdir}

%files promo
%defattr(-,root,root)
%yast_controldir/control.openSUSE-promo.xml

%files addon
%defattr(-,root,root)
%yast_controldir/add-on-template_installation.xml

%changelog
