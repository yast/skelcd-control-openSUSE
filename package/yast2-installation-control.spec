#
# spec file for package yast2-installation-control
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           yast2-installation-control
Version:        3.1.2
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Summary:        YaST2 - RNG schema for installation control files
License:        GPL-2.0
Group:          System/YaST
Url:            https://github.com/yast/yast-installation-control

BuildRequires:  yast2-devtools >= 3.1.10

# xmllint for validation
BuildRequires:  libxml2-tools

BuildArch:      noarch

%description
This package contains RNG schema for validating the installation control files.
Also the control files for some base products and a language add-on is present.

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

%files
%defattr(-,root,root)
%dir /usr/share/YaST2/control
/usr/share/YaST2/control/*.rng
/usr/share/YaST2/control/*.rnc

%doc %{yast_docdir}

%changelog
