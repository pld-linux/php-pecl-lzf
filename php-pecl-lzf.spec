# TODO
# - use system liblzf
%define		_modname	lzf
%define		_modname_c	LZF
%define		_status		stable
Summary:	%{_modname} - (de)compression
Summary(pl):	%{_modname} - (de)kompresja
Name:		php-pecl-%{_modname}
Version:	1.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname_c}-%{version}.tgz
# Source0-md5:	f35d75b70bee9741946c4cb9275a74ab
URL:		http://pecl.php.net/package/LZF/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package handles LZF de/compression.

In PECL status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarczaj obs³ugê (de)kompresji archiwów LZF.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname_c}-%{version}
phpize
%configure \
	--enable-lzf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_smodname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
