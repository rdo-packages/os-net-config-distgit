%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora} >= 28
%global with_python3 1
%endif

Name:			os-net-config
Version:		XXX
Release:		XXX
Summary:		Host network configuration tool

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

Requires:	initscripts
Requires:	iproute
Requires:	ethtool
Requires:	dhclient

BuildArch:	noarch

%if 0%{?with_python3} == 0
# begin python2 requirements
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python2-pbr
BuildRequires:	python2-sphinx
BuildRequires:	python2-oslo-sphinx

Requires:	python-anyjson >= 0.3.3
Requires:	python2-eventlet >= 0.18.2
Requires:	python2-oslo-concurrency >= 3.8.0
Requires:	python2-oslo-config
Requires:	python2-oslo-utils >= 3.20.0
Requires:	python2-netaddr >= 0.7.13
Requires:	python2-iso8601 >= 0.1.11
Requires:	python2-six >= 1.9.0
Requires:	PyYAML >= 3.10
Requires:	python2-pbr >= 2.0.0
Requires:	python2-jsonschema >= 2.0.0
Requires:	python-pyudev >= 0.15
# end python2 requirements
%else
# begin python3 requirements
BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
BuildRequires:	python3-pbr
BuildRequires:	python3-sphinx
BuildRequires:	python3-oslo-sphinx

Requires:	python3-anyjson >= 0.3.3
Requires:	python3-eventlet >= 0.18.2
Requires:	python3-oslo-concurrency >= 3.8.0
Requires:	python3-oslo-config
Requires:	python3-oslo-utils >= 3.20.0
Requires:	python3-netaddr >= 0.7.13
Requires:	python3-iso8601 >= 0.1.11
Requires:	python3-six >= 1.9.0
Requires:	python3-PyYAML >= 3.10
Requires:	python3-pbr >= 2.0.0
Requires:	python3-jsonschema >= 2.0.0
Requires:	python3-pyudev >= 0.15
# end python3 requirements
%endif

%description
Host network configuration tool for OpenStack.

%prep

%setup -q -n %{name}-%{upstream_version}

%build
%if 0%{?with_python3} == 0
%{py2_build}
%{__python2} setup.py build_sphinx
%else
%{py3_build}
%{__python3} setup.py build_sphinx
%endif

%install
%if 0%{?with_python3} == 0
%{py2_install}
%else
%{py3_install}
%endif

%files
%doc README.rst
%doc LICENSE
%doc doc/build/html
%{_bindir}/os-net-config
%{_bindir}/os-net-config-sriov
%if 0%{?with_python3} == 0
%{python2_sitelib}/os_net_config*
%else
%{python3_sitelib}/os_net_config*
%endif



%changelog
