%include	/usr/lib/rpm/macros.perl
Summary:	Foomatic database
Summary(pl):	Baza danych dla foomatic
Name:		foomatic-db
Version:	20060810
Release:	1
License:	GPL
Group:		Applications/System
# foomatic db engine version
%define		_fev	3.0
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-%{_fev}-%{version}.tar.gz
# Source0-md5:	93b032893df6ee3556e70ef23e015d2c
URL:		http://www.linuxprinting.org/foomatic.html
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	foomatic-db-engine >= 3.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The collected knowledge about printers, drivers, and driver options in
XML files, used by foomatic-db-engine to generate PPD files.

%description -l pl
Ca³o¶ciowa informacja o drukarkach, sterownikach i opcjach sterowników
w postaci plików XML, u¿ywanych przez foomatic-db-engine do generowania
plików PPD.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
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
