%include	/usr/lib/rpm/macros.perl
Summary:	Foomatic database
Summary(pl.UTF-8):	Baza danych dla foomatic
Name:		foomatic-db
Version:	20110615
Release:	1
License:	GPL v2+
Group:		Applications/System
# foomatic db engine version
%define		fdbeng_ver	4.0
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-%{fdbeng_ver}-%{version}.tar.gz
# Source0-md5:	f01fb27f96d3ec1e3b59dc860c64c52b
URL:		http://www.linuxprinting.org/foomatic.html
BuildRequires:	bash
Requires:	foomatic-db-engine >= 4.0.20110615
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The collected knowledge about printers, drivers, and driver options in
XML files, used by foomatic-db-engine to generate PPD files.

%description -l pl.UTF-8
Całościowa informacja o drukarkach, sterownikach i opcjach sterowników
w postaci plików XML, używanych przez foomatic-db-engine do
generowania plików PPD.

%prep
%setup -q

%build
/bin/bash %configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need PPD files in this package
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/foomatic/db/source/PPD

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README USAGE
%{_datadir}/foomatic/db/source/driver/*.xml
%{_datadir}/foomatic/db/source/opt/*.xml
%{_datadir}/foomatic/db/source/printer/*.xml
%{_datadir}/foomatic/db/oldprinterids
