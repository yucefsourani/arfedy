Name:           arfedy
Version:        0.1
Release:        1%{?dist}
Summary:        Python Script to install multimedia codecs and additional software
Group:		Applications/System
BuildArch:	noarch
License:        GPLv3
URL:            https://github.com/yucefsourani/arfedy
Source0:        https://github.com/yucefsourani/arfedy/tree/master/%{version}/arfedy
Source1:  	https://github.com/yucefsourani/arfedy/tree/master/%{version}/talwin.py
BuildRequires:  python3-rpm-macros
Requires:	arfedy-lib

%description
Python Script to install multimedia codecs and additional software


%package -n arfedy-lib
Summary:	Talwin lib for arfedy script
BuildArch:	noarch

%description -n arfedy-lib
Talwin lib for arfedy script

%prep



%build



%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{python3_sitelib}
install -pDm0755 %{SOURCE0} %{buildroot}%{_bindir}
install -pDm0644 %{SOURCE1} %{buildroot}%{python3_sitelib}


%files
%{_bindir}/arfedy

%files -n  arfedy-lib
%{python3_sitelib}/talwin.py


%changelog
* Thu Sep 15 2016 youcef sourani youssef.m.sourani@gmail.com - 0.1-1
- Initial package for Fedora


