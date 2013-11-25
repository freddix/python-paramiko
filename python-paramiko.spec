Summary:	SSH2 protocol for Python
Name:		python-paramiko
Version:	1.12.0
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	https://github.com/paramiko/paramiko/archive/v%{version}.tar.gz
# Source0-md5:	2e6b1782e19fd223689e2d4a3cc426ca
URL:		http://www.lag.net/paramiko/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-Crypto
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A module for python 2.3 (or higher) that implements the SSH2 protocol
for secure (encrypted and authenticated) connections to remote
machines.

%prep
%setup -qn paramiko-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.* NEWS NOTES README TODO
%{py_sitescriptdir}/paramiko
%{py_sitescriptdir}/*.egg-info

