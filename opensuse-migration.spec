#
# spec file for package opensuse-migration.spec
#
# Copyright (c) 2019 SUSE LLC
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

Name:           opensuse-migration
Version:        0.0.1
Release:        0
Summary:        Easy migration between openSUSE Leap versions
License:        GPL-2.0
Group:          System/Monitoring
Url:            https://github.com/ikapelyukhin/opensuse-migration
Source0:        opensuse-migration-%{version}.tar.bz2
Requires:       %{rubygem thor}
BuildRequires:  ruby
BuildRequires:  %{rubygem thor}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

# FIXME: macros that work for both 42.* and 15.*
%define state_dir /var/lib/opensuse-migration
%define data_dir /usr/share/opensuse-migration

%description

Provides a set of zypper services for openSUSE Leap version and leap-cli utility
for switching between the versions.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{data_dir}
mkdir -p %{buildroot}%{state_dir}/backup

install -D -m755 leap-cli %{buildroot}%{_bindir}/leap-cli
cp -ar services/ %{buildroot}%{data_dir}

%files
%defattr(-,root,root)
%{_bindir}/leap-cli
%dir %{data_dir}
%dir %{data_dir}/*
%{data_dir}/**/*
%dir %{state_dir}
%dir %{state_dir}/backup

%post
if [ $1 -eq 1 ]; then
    /usr/bin/leap-cli init
fi

%preun
if [ $1 -eq 0 ]; then
    /usr/bin/leap-cli cleanup
fi

%changelog
