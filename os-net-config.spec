%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:			os-net-config
Version:		7.3.7
Release:		1%{?dist}
Summary:		Host network configuration tool

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python-pbr
BuildRequires:	python-sphinx
BuildRequires:	python-oslo-sphinx

Requires:	python-anyjson >= 0.3.3
Requires:	python-eventlet >= 0.18.2
Requires:	python-oslo-concurrency >= 3.8.0
Requires:	python-oslo-config
Requires:	python-oslo-utils >= 3.20.0
Requires:	python-netaddr >= 0.7.13
Requires:	python-iso8601 >= 0.1.11
Requires:	python-six >= 1.9.0
Requires:	initscripts
Requires:	iproute
Requires:	ethtool
Requires:	openvswitch
Requires:	dhclient
Requires:	PyYAML >= 3.10
Requires:	python-pbr >= 2.0.0
Requires:	python-jsonschema >= 2.0.0

%description
Host network configuration tool for OpenStack.

%prep

%setup -q -n %{name}-%{upstream_version}

%build
%{__python} setup.py build
%{__python} setup.py build_sphinx

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%doc doc/build/html
%{_bindir}/os-net-config
%{python_sitelib}/os_net_config*


%changelog
* Mon Sep 24 2018 RDO <dev@lists.rdoproject.org> 7.3.7-1
- Update to 7.3.7

* Tue May 29 2018 RDO <dev@lists.rdoproject.org> 7.3.6-1
- Update to 7.3.6

* Mon Apr 23 2018 RDO <dev@lists.rdoproject.org> 7.3.5-1
- Update to 7.3.5

* Wed Mar 07 2018 RDO <dev@lists.rdoproject.org> 7.3.4-1
- Update to 7.3.4

* Mon Feb 12 2018 RDO <dev@lists.rdoproject.org> 7.3.3-1
- Update to 7.3.3

* Wed Nov 22 2017 RDO <dev@lists.rdoproject.org> 7.3.2-1
- Update to 7.3.2

* Tue Oct 10 2017 rdo-trunk <javier.pena@redhat.com> 7.3.1-1
- Update to 7.3.1

* Sun Sep 10 2017 rdo-trunk <javier.pena@redhat.com> 7.3.0-1
- Update to 7.3.0

* Thu Aug 24 2017 Alfredo Moralejo <amoralej@redhat.com> 7.2.0-1
- Update to 7.2.0

