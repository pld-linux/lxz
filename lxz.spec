Summary:	lxz - Parallel xz-like compressor utility
Name:		lxz
Version:	0.01
Release:	1
License:	GPL v3+
Group:		Applications/Archiving
# Source0:	http://lacos.hu/dump2.php?name=lxz.tar.gz&hash=bf7b69f2f9b287c6a209d8b55ffa822a4debcdae
Source0:	%{name}.tar.gz
# Source0-md5:	9b05209ce0347a7dca8605c0e9e06456
URL:		http://lacos.hu/
BuildRequires:	automake
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parallel xz-like compressor utility.

%prep
%setup -q -n %{name}

sed -i -e 's#-O2#%{rpmcflags} %{rpmcppflags}#g' Makefile

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install lxz $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/lxz
