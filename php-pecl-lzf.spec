%define		_modname	lzf
%define		_modname_c	LZF
%define		_status		status
Summary:	%{_modname} - (de)compression
Summary(pl):	%{_modname} - (de)kompresja
Name:		php-pecl-%{_modname}
Version:	1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname_c}-%{version}.tgz
# Source0-md5:	865f1f40326a55ade4ebf7b7568ecf43
URL:		http://pecl.php.net/package/LZF/
BuildRequires:	libtool
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
This package handles LZF de/compression.

This extension has in PEAR status: %{_status}.

%description -l pl
Ten pakiet dostarczaj obs³ugê (de)kompresji archiwów LZF.

To rozszerzenie ma w PEAR status: %{_status}.

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
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname_c}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
