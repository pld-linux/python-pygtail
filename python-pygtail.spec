# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		pygtail
%define		egg_name	pygtail
%define		pypi_name	pygtail
Summary:	Reads log file lines that have not been read
Name:		python-%{pypi_name}
Version:	0.8.0
Release:	0.1
License:	GPL v2
Group:		Libraries/Python
Source0:	https://github.com/bgreenlee/pygtail/archive/%{version}.tar.gz
# Source0-md5:	504ffc804e83a4dd09e20546990b1d43
URL:		https://github.com/bgreenlee/pygtail
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pygtail reads log file lines that have not been read. It will even
handle log files that have been rotated.

%package -n python3-%{pypi_name}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{pypi_name}
Pygtail reads log file lines that have not been read. It will even
handle log files that have been rotated.

%prep
%setup -q -n %{pypi_name}-%{version}
sed -i -e 's#0\.7\.0#0\.8\.0#g' pygtail/core.py

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/pygtail
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
