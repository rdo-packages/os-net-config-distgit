%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:			os-net-config
Version:		6.1.1
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

Requires:	python-setuptools
Requires:	python-anyjson
Requires:	python-babel
Requires:	python-eventlet
Requires:	python-oslo-concurrency
Requires:	python-oslo-config
Requires:	python-oslo-utils
Requires:	python-netaddr
Requires:	python-iso8601
Requires:	python-six >= 1.5.0
Requires:	initscripts
Requires:	PyYAML
Requires:	python-pbr

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
* Tue Sep 05 2017 rdo-trunk <javier.pena@redhat.com> 6.1.1-1
- Update to 6.1.1

* Fri Apr 28 2017 rdo-trunk <javier.pena@redhat.com> 6.1.0-1
- Update to 6.1.0

* Mon Mar 06 2017 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-1
- Update to 6.0.0

* Fri Feb 10 2017 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-0.1.0rc1
- Update to 6.0.0.0rc1

