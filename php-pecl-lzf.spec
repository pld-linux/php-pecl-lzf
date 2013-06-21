# TODO
# - use system liblzf
%define		php_name	php%{?php_suffix}
%define		modname	lzf
%define		modname_c	LZF
%define		status		stable
Summary:	%{modname} - (de)compression
Summary(pl.UTF-8):	%{modname} - (de)kompresja
Name:		%{php_name}-pecl-%{modname}
Version:	1.5.2
Release:	5
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	d0313d93783cd11c8e038abfcf1b4f91
URL:		http://pecl.php.net/package/LZF/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package handles LZF de/compression.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
Ten pakiet dostarczaj obsługę (de)kompresji archiwów LZF.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -q -c

%build
cd %{modname_c}-%{version}
phpize
%configure \
	--enable-lzf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{modname_c}-%{version}/modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
