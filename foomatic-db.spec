%include	/usr/lib/rpm/macros.perl
Summary:	Foomatic database
Summary(pl.UTF-8):	Baza danych dla foomatic
Name:		foomatic-db
Version:	20080317
Release:	4
License:	GPL
Group:		Applications/System
# foomatic db engine version
%define		_fev	3.0
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-%{_fev}-%{version}.tar.gz
# Source0-md5:	ff65282a646a6242efd74219b11b0ff1
URL:		http://www.linuxprinting.org/foomatic.html
Requires:	foomatic-db-engine >= 3.0.20080317
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need PPD files in this package
rm $RPM_BUILD_ROOT%{_datadir}/foomatic/db/source/PPD/ -frd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README USAGE
%{_datadir}/foomatic/db/source/driver/*
%{_datadir}/foomatic/db/source/opt/*
%{_datadir}/foomatic/db/source/printer/*
%{_datadir}/foomatic/db/oldprinterids
